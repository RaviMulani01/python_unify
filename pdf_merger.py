import PyPDF2


def merge_pdfs(input_pdfs, output_pdf):
    merger = PyPDF2.PdfMerger()

    for pdf in input_pdfs:
        merger.append(pdf)

    with open(output_pdf, 'wb') as output:
        merger.write(output)


# List of input PDF files to merge
input_pdfs = ['1.pdf',
              '2.pdf']

# Output PDF file name
output_pdf = 'merged.pdf'

merge_pdfs(input_pdfs, output_pdf)
