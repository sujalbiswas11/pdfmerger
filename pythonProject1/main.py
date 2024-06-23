import PyPDF2 #pip3 install pypdf2
pdffiles = ["1.pdf","2.pdf"]
merger = PyPDF2.PdfMerger()
for filename in pdffiles:
    pdfFiles = open(filename,'rb') #readbinary mode
    pdfReader = PyPDF2.PdfReader(pdfFiles)
    merger.append(pdfReader)
pdfFiles.close()
merger.write("merged.pdf")

