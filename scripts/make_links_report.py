from pathlib import Path
import pandas as pd
import ast

results_dir = Path("data/results")
df = pd.read_csv(results_dir / "papers_metadata.csv")

out_file = results_dir / "links_per_paper.md"

with open(out_file, "w", encoding="utf-8") as f:
    f.write("# Links found in each paper\n\n")

    for _, row in df.iterrows():
        f.write(f"## {row['paper']}\n\n")
        f.write(f"**Title:** {row['title']}\n\n")

        links = row["links"]
        if isinstance(links, str):
            try:
                links = ast.literal_eval(links)
            except Exception:
                links = []

        if links:
            for link in links:
                f.write(f"- {link}\n")
        else:
            f.write("- No links found\n")

        f.write("\n")

print(f"Saved: {out_file}")