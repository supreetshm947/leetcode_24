from PyPDF2 import PdfMerger

def merge_pdfs(pdf_list, output_path):
    """
    Merges multiple PDF files into a single PDF.

    Args:
        pdf_list (list): List of PDF file paths to merge.
        output_path (str): Path to save the merged PDF.
    """
    merger = PdfMerger()

    try:
        for pdf in pdf_list:
            merger.append(pdf)
        merger.write(output_path)
        print(f"Merged PDF saved to {output_path}")
    except Exception as e:
        print(f"Error merging PDFs: {e}")
    finally:
        merger.close()

if __name__ == "__main__":
    # Example usage
    pdf_files = ["C:\\Users\\supre\\Downloads\\fiktionsbecheinigung-1.pdf", "C:\\Users\\supre\\Downloads\\residence_permit.pdf"]  # Replace with your PDF file paths
    output_file = "merged_output.pdf"  # Replace with your desired output file name
    merge_pdfs(pdf_files, output_file)
