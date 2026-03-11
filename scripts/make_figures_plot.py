from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

results_dir = Path("data/results")
df = pd.read_csv(results_dir / "papers_metadata.csv")
df = df.sort_values("n_figures", ascending=False)

plt.figure(figsize=(12, 6))
plt.bar(df["paper"], df["n_figures"])
plt.xlabel("Paper")
plt.ylabel("Number of figures")
plt.title("Number of figures per article")
plt.xticks(rotation=45)
plt.tight_layout()

out_file = results_dir / "figures_per_article.png"
plt.savefig(out_file, dpi=300, bbox_inches="tight")
print(f"Saved: {out_file}")