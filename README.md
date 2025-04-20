# 🔍 Target Keywords Analyzer

**Version:** 1.2.5  
**Author:** Arash Yoosefdoost

## 📘 Overview

This tool processes a `.bib` BibTeX file to detect specific keywords within the `title`, `abstract`, and `keywords` fields of each entry. It helps researchers identify relevant themes across their reference collections. Ideal for systematic reviews, thematic analyses, and science mapping.

---

## 🎯 Purpose

- Automate the thematic review of academic papers.
- Identify how frequently specific research terms appear.
- Prepare structured input for keyword visualization tools.

---

## 📥 Input

A `.bib` file named `INPUT.bib` that contains bibliographic entries with `title`, `abstract`, and `keywords`.

---

## 🧠 Keywords Tracked

Predefined keywords (modifiable in the script):
```python
['Keyword 1','Keyword 2','...','Keyword n']
```

---

## 📤 Output

1. `Target-Keywords_Analysis_[Full-Report].csv`  
   - APA-style reference
   - Title, abstract, and original keywords
   - Occurrence of each target keyword

2. `Target-Keywords_Analysis_[Sankey_Diagram_Data].csv`  
   - Matrix view with references as rows and keywords as columns
   - Useful for visual tools like Sankey diagrams

---

## ⚙️ How It Works

- Loads `.bib` file using `bibtexparser`
- Checks each entry’s title, abstract, and keyword fields for target keywords
- Counts occurrences and stores results
- Outputs two CSV files: a detailed report and a Sankey-friendly matrix

---

## 💻 Usage

1. Install `bibtexparser`:
   ```bash
   pip install bibtexparser
   ```

2. Place your BibTeX file as `INPUT.bib` in the working directory.

3. Run the script:
   ```bash
   python "Target Keywords Analyzer.py"
   ```

---

## 📦 Dependencies

- `bibtexparser`
- Python standard `csv` module

---

## 📈 Example Output

**Full Report (CSV):**
| Reference | Title | Abstract | Keywords | geochemistry | spectroscopy | ... |
|-----------|-------|----------|----------|--------------|--------------|-----|

**Sankey Input (CSV):**
| Reference | geochemistry | spectroscopy | ... |
|-----------|--------------|--------------|-----|



