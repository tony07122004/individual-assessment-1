from pathlib import Path
import pandas as pd
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

results_dir = Path("data/results")
df = pd.read_csv(results_dir / "papers_metadata.csv")

text = " ".join(df["abstract"].fillna("").astype(str))

extra_stopwords = {
    "paper", "study", "results", "method", "methods", "conclusion",
    "conclusions", "using", "based", "show", "shows", "used",
    "approach", "approaches", "model", "models", "large", "language"
}

stopwords = STOPWORDS.union(extra_stopwords)

wc = WordCloud(
    width=1400,
    height=700,
    background_color="white",
    stopwords=stopwords
).generate(text)

plt.figure(figsize=(14, 7))
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.tight_layout()

out_file = results_dir / "keyword_cloud.png"
plt.savefig(out_file, dpi=300, bbox_inches="tight")
print(f"Saved: {out_file}")