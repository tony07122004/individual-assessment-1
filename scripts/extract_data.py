from pathlib import Path
from bs4 import BeautifulSoup
import pandas as pd

tei_dir = Path("data/tei_xml")
output_dir = Path("data/results")
output_dir.mkdir(parents=True, exist_ok=True)

rows = []

for tei_file in sorted(tei_dir.glob("*.tei.xml")):
    with open(tei_file, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "xml")

    title_tag = soup.find("title", attrs={"type": "main"})
    if title_tag is None:
        title_tag = soup.find("title")
    title = title_tag.get_text(" ", strip=True) if title_tag else tei_file.stem

    abstract_tag = soup.find("abstract")
    abstract = abstract_tag.get_text(" ", strip=True) if abstract_tag else ""

    figures = soup.find_all("figure")
    n_figures = len(figures)

    links = set()

    for ptr in soup.find_all("ptr"):
        target = ptr.get("target")
        if target and target.startswith(("http://", "https://")):
            links.add(target)

    for ref in soup.find_all("ref"):
        target = ref.get("target")
        if target and target.startswith(("http://", "https://")):
            links.add(target)

    rows.append({
        "paper": tei_file.stem.replace(".tei", ""),
        "title": title,
        "abstract": abstract,
        "n_figures": n_figures,
        "n_links": len(links),
        "links": sorted(links),
    })

df = pd.DataFrame(rows)
df.to_csv(output_dir / "papers_metadata.csv", index=False, encoding="utf-8")
df.to_json(output_dir / "papers_metadata.json", orient="records", indent=2, force_ascii=False)

print(df[["paper", "n_figures", "n_links"]])
print("\nSaved:")
print(output_dir / "papers_metadata.csv")
print(output_dir / "papers_metadata.json")