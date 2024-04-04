# Pages per sheet: Print PDFs with multiple pages per sheet while maximizing content area

Save paper and maximize the viewable area when printing multiple pages per sheet.

Using the traditional pages per sheet feature in your browser or system print dialog won't get rid of margins in the original file, so you end up with lots of blank space:
![With blank space](static/img/before.jpg)

Pages per sheet is a handy tool to adjust the zoom level on individual pages before printing, so you end up with something that looks like this instead:
![Without blank space](static/img/after.jpg)

Setting it up is easy and takes ~5 min to deploy locally on a mac or linux computer.

# Usage

1. Clone the git repo
2. Install poppler. This is required for PDF handling by the pdf2image python library.
On a mac:
```brew install poppler```
On Ubuntu:
```sudo apt install poppler-utils```
3. In a virtual env, run ```pip install -r requirements.txt```
4. Run ```flask --app app run``` to start the local web server
5. Navigate to http://localhost:5000 in your web browser, upload your PDF, adjust the cropping on the padding, and print in landscape mode!
