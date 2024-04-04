
# Pages per sheet: Print PDFs with multiple pages per sheet while maximizing content area

Save paper and maximize the viewable area when printing multiple pages per sheet.

**Problem**: Using the traditional *pages per sheet* feature in your browser or print dialog won't get rid of margins in the original file, so you end up with lots of blank space like in this example:
![With blank space](https://github.com/theak/pagespersheet/raw/main/static/img/before.jpg)
**Solution**: Pages per sheet is a handy tool to adjust the zoom level on individual pages before printing, so you end up with something that looks like this instead:
![Without blank space](https://github.com/theak/pagespersheet/raw/main/static/img/after.jpg)
Setting it up is easy and takes ~5 min to deploy locally on a mac or linux computer. At some point I'd love to deploy a hosted version of this.

# Option 1: Run as docker image

1. Clone the repo: ```git clone https://github.com/theak/pagespersheet```
2. Run ```docker build -t pagespersheet -f Dockerfile .``` to build the docker container
3. Run ```docker run -it -p 5000:5000 pagespersheet``` to make sure it works, then ctrl+C to stop it.
4. Run ```docker run -d -p 5000:5000 --restart unless-stopped pagespersheet```

# Option 2: Run directly

1. Clone the repo: ```git clone https://github.com/theak/pagespersheet```
2. Install poppler. This is required for PDF handling by the pdf2image python library.
On a mac:
```brew install poppler```
On Ubuntu:
```sudo apt install poppler-utils```
3. In a virtual env, run ```pip install -r requirements.txt```
4. Run ```flask --app app run``` to start the local web server
5. Navigate to http://localhost:5000 in your web browser, upload your PDF, adjust the cropping on the padding, and print in landscape mode!