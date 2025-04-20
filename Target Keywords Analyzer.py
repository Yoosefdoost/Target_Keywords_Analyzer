# Target Keywords Analyzer
# Version: 1.2.5  
# Author: Arash Yoosefdoost

# Description:
# This tool processes a `.bib` BibTeX file to detect specific keywords within the `title`, `abstract`, and `keywords` fields of each entry. It helps researchers identify relevant themes across their reference collections. Ideal for systematic reviews, thematic analyses, and science mapping.

# - Automate the thematic review of academic papers.
# - Identify how frequently specific research terms appear.
# - Prepare structured input for keyword visualization tools.


import bibtexparser
import csv

# Define the desired keywords
Kewords_Desired = ['Keyword 1','Keyword 2','...','Keyword n']

# Read the BibTeX.bib file
with open('INPUT.bib') as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)

# Create a list to store the results
results = []

# Function to format authors in APA style
def format_authors(authors):
    if len(authors) > 1:
        return f"{authors[0]} et al."
    return authors[0]

# Iterate over each study in the BibTeX database
for entry in bib_database.entries:

    # Initialize the count for each keyword to zero
    keyword_counts = {keyword: 0 for keyword in Kewords_Desired}

    # Check the title, abstract, and keywords of the study for the desired keywords
    for keyword in Kewords_Desired:
        if keyword in entry.get('title', '').lower():
            keyword_counts[keyword] += 1
        if keyword in entry.get('abstract', '').lower():
            keyword_counts[keyword] += 1
        if 'keywords' in entry:
            if keyword in entry['keywords'].lower():
                keyword_counts[keyword] += 1

    # Format authors and year in APA style
    authors = entry.get('author', '').split(" and ")
    year = entry.get('year', '')
    Reference = f"{format_authors(authors)}, {year}"

    # Add the results to the list
    results.append({'Reference': Reference,
                    'title': entry.get('title', ''),
                    'abstract': entry.get('abstract', ''),
                    'keywords': entry.get('keywords', ''),
                    **keyword_counts})

# Write the results to a CSV file
with open('Target-Keywords_Analysis_[Full-Report].csv', mode='w') as csv_file:
    fieldnames = ['Reference', 'title', 'abstract', 'keywords'] + Kewords_Desired
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    for result in results:
        writer.writerow(result)

# Write the Sankey Diagram data to a CSV file
with open('Target-Keywords_Analysis_[Sankey_Diagram_Data].csv', mode='w') as sankey_csv_file:
    sankey_fieldnames = ['Reference'] + Kewords_Desired
    sankey_writer = csv.DictWriter(sankey_csv_file, fieldnames=sankey_fieldnames)

    sankey_writer.writeheader()
    for result in results:
        sankey_writer.writerow({key: result[key] for key in sankey_fieldnames})

