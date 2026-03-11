from pathlib import Path
import requests
import time

input_dir = Path("data/raw_pdfs")
output_dir = Path("data/tei_xml")
output_dir.mkdir(parents=True, exist_ok=True)

pdf_files = sorted(input_dir.glob("*.pdf"))
url = "http://localhost:8070/api/processFulltextDocument"

print(f"Found {len(pdf_files)} PDF(s)")

for pdf_path in pdf_files:
    print(f"\nProcessing {pdf_path.name}...")
    try:
        with open(pdf_path, "rb") as f:
            files = {"input": (pdf_path.name, f, "application/pdf")}
            data = {
                "consolidateHeader": "1",
                "consolidateCitations": "0",
                "segmentSentences": "0",
            }

            response = requests.post(url, files=files, data=data, timeout=600)

        print("Status code:", response.status_code)

        if response.status_code == 200:
            out_file = output_dir / f"{pdf_path.stem}.tei.xml"
            out_file.write_text(response.text, encoding="utf-8")
            print(f"Saved: {out_file}")
        else:
            err_file = output_dir / f"{pdf_path.stem}_{response.status_code}.txt"
            err_file.write_text(response.text, encoding="utf-8")
            print(f"Error saved: {err_file}")

        time.sleep(2)

    except Exception as e:
        err_file = output_dir / f"{pdf_path.stem}_exception.txt"
        err_file.write_text(str(e), encoding="utf-8")
        print(f"Exception in {pdf_path.name}: {e}")

print("\nFinished.")