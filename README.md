# \# Individual Assessment 1

# 

# \## Overview

# This repository contains an analysis of 10 open-access articles about Large Language Models using GROBID and Python-based text processing tools.

# 

# The project generates:

# 1\. A keyword cloud based on the abstracts of the selected papers.

# 2\. A visualization showing the number of figures per article.

# 3\. A list of the links found in each paper.

# 

# \## Repository structure

# 

# ```text

# individual-assessment-1/

# &#x20;- data/:

# &#x20;	 - raw\_pdfs/          # Input PDF articles

# &#x09; - tei\_xml/           # TEI XML files generated with GROBID 

# &#x09; - results/           # Final outputs

# &#x20;- scripts/:

# &#x09; - run\_grobid.py

# &#x09; - extract\_data.py

# &#x09; - make\_keyword\_cloud.py

# &#x09; - make\_figures\_plot.py

# &#x09; - make\_links\_report.py

# &#x20;- papers.csv

# &#x20;- requirements.txt

# &#x20;- README.md

