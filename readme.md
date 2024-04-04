# Save paper and save your eyes. Print multiple pages per sheet with cropped margins

This is a really simple  tool to print multiple pages per sheet with cropped margins, so you can save paper and maximize the readable area when printing multiple pages per sheet.

Super handy for printing academic papers, financial reports, or any other documents that you need to read without wasting too much paper.

Unlike the normal pages per sheet feature in your system print dialog, this tool lets you crop the margins of the document that you're printing so you can fit maximal content into a physical piece of paper.

Especially handy for printing PDFs that have built-in margins.

# Usage

1. Clone the git repo
2. Install poppler. This is required for PDF handling by the pdf2image python library, which this tool uses. Look up the instructions for your platform. 
On a mac:
```brew install poppler```
On Ubuntu:
```sudo apt install poppler-utils```
3. In a virtual env, run ```pip install -r requirements.txt```
4. Run ```flask --app app run``` to start the local web server
5. Navigate to http://localhost:5000 in your web browser, upload your PDF, adjust the cropping on the padding, and print in landscape mode!
