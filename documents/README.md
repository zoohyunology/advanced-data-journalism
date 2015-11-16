# Documents as data

Data doesn't always come in rows and columns. Often, it also comes in less structured forms, such as PDF documents or text files, that defy conventional data-crunching techniques. But that doesn't mean we can't figure out a way to analyze those as well.

## Homebrew (OSX)

Most of what we'll be doing here involves using several command-line utilities to turn common documents, in the form of PDFs, into data that we can analyze. To install that software, the first thing you'll want to do (if you're using a Mac) is to get acquainted with [Homebrew](http://brew.sh/) -- a package manager that makes it easy to install command-line tools that are useful for developers and data journalists.

Installation instructions are on the site (you literally copy and paste a line of code into the terminal).

## Windows

Windows doesn't have a Homebrew equivalent, so links to installation instructions for your software will be included below.

## Dealing with text PDFs

For data-processing purposes, PDFs come in two flavors: as documents containing text as part of their metadata, and as images. The first kind is by far the easiest to deal with. You'll just need to install a tool called pdftotext.

### OSX

Pdftotext comes as part of a package called xpdf, which can be installed via Homebrew like this:

```
brew update
brew install Caskroom/cask/xquartz
brew install homebrew/x11/xpdf
```

### Windows

Installation instructions are [here](http://www.foolabs.com/xpdf/download.html). You'll want the x86, Windows, precompiled binary.

### Running the software

Running the pdftotext command is easy. Assuming you're in this directory:

```
pdftotext clinton_email.pdf
```

## Dealing with image PDFs 

PDFs that contain images of text, rather than text itself, are a bit more difficult to deal with. To turn those into analzyable data, you'll need to employ a technique known as Optical Character Recognition, which attempts to read the characters in the image and convert them to text. That requires a couple steps.

### OSX

You'll need three tools -- two of which allow you to covert PDFs to image files, and another that performs the OCR steps. All of these can be installed via Homebrew:

```
brew install tesseract
brew install ghostscript
brew install imagemagick
```

### Windows

Tesseract and its associated libraries don't work as consistently on Windows. Your best bet if you need to convert a document from a Windows machine is to use [DocumentCloud](http://www.documentcloud.org), which performs conversions in the cloud using the same software.

If you'd like to try getting the software running locally, you can find some instructions [here](https://github.com/tesseract-ocr/tesseract/wiki#windows).

Likewise, ImageMagick has installable binaries available [here](http://www.imagemagick.org/script/binary-releases.php).

### Running the software

Tesseract only works on image files, not PDFs themselves. So your first step must be to convert the document to a .tiff file using ImageMagick like this:

```
convert -density 300 -depth 8 -quality 85 -background white +matte rubio_statement.pdf ./pages/file-%04d.tiff
```

Once that's done, Tesseract can be used to convert the resulting pages:

```
tesseract page1.pdf page1.tiff
```

That last part can easily be scripted to execute over every resulting page, so you don't have to run the command multiple times.