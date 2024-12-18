**Gene ID and Species Extractor**
This Python script extracts gene IDs and species names from a phylogenetic tree data file, which uses a specific format of __ as a separator between the gene ID and species. The species names may be enclosed in single quotes (') or not.

**Features**
Extracts gene IDs and species names from a provided input file.
Handles species names with or without single quotes.
Outputs the data in a tab-separated format (.tsv) for easy use in further analysis.
**Requirements**
Python 3.x
No additional libraries required (uses built-in re library).
Input Format
The script expects the input data in the following format:

Gene ID and species are separated by __.
Species names may or may not be enclosed in single quotes (').
