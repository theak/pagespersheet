
# Pages per sheet: Print PDFs with multiple pages per sheet while maximizing content area

Save paper and maximize the viewable area when printing multiple pages per sheet.

***Problem**: The pages per sheet feature in your print dialog keeps margins in the original file, so you're stuck up with lots of blank space:*
<div><center><kbd><img src="https://github.com/theak/pagespersheet/raw/main/static/img/before.jpg" alt="drawing" width="400"/></kbd></center></div>

***Solution**: Pages per sheet zooms in on individual pages before printing to minimize whitespace and get the most use out of each page:*
<div><center><kbd><img src="https://github.com/theak/pagespersheet/raw/main/static/img/after.jpg" alt="drawing" width="400"/></kbd></center></div>

### Option 1: Run as docker image

1. Clone the repo: ```git clone https://github.com/theak/pagespersheet```
2. Run ```cd pagespersheet```
3. Run ```docker build -t pagespersheet -f Dockerfile .``` to build the docker container
4. Run ```docker run -it -p 5000:5000 pagespersheet``` to make sure everything works, then ctrl+C to stop
5. Run ```docker run -d -p 5000:5000 --restart unless-stopped pagespersheet```

### Option 2: Run directly

1. Clone the repo: ```git clone https://github.com/theak/pagespersheet```
2. Install poppler. This is required for PDF handling by the pdf2image python library.
On a mac:
```brew install poppler```
On Ubuntu:
```sudo apt install poppler-utils```
3. In a virtual env, run ```pip install -r requirements.txt```
4. Run ```flask --app app run``` to start the local web server

### Usage

Navigate to http://localhost:5000 in your web browser, upload your PDF, adjust the pages per sheet and zoom to your desired level, then hit ctrl+P (or cmd+P on a mac) to print it!
