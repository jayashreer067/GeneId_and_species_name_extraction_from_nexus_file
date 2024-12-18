import re

# Function to extract gene IDs and species names
def extract_genes_species(data):
    """
    Extracts gene IDs and species names from the given phylogenetic tree data.
    """
    pattern = r"([\w\.]+)__([\w\s\.\-]+)_"
    matches = re.findall(pattern, data)
    return matches


# Main function
def main():
    input_file = "3rd_paralog_gene.txt"
    #.tsv to get the gene_ID and species name in columns
    output_file = "new_paralog.tsv"

    try:
        # Read the input file
        with open(input_file, "r") as file:
            data = file.read()

        # Extract data
        extracted_data = extract_genes_species(data)

        # Save results to output file
        with open(output_file, "w") as file:
            for gene_id, species in extracted_data:
                file.write(f"{gene_id}\t{species}\n")

        print(f"Extraction complete. Results saved to '{output_file}'")
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Entry point
if __name__ == "__main__":
    main()
