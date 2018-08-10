import os
import sys

def pdf2txt(path):
	'''
	This functions takes multiple PDFs as input and it will output plain 
	text files with the text contained within the PDFs. One only needs to
	provide the directory where the PDFs are located

	This is very useful when PDFs are scanned copies, and one needs to be
	able to copy and edit the text.

	Computer needs Tesseract-OCR and Imagemagick installed
	This will (probably) not work in windows
	'''

    #Looping over every file inside the given path
    for root, dirs, files in os.walk(path):
        for file in files:
            #Making sure it is a pdf file
            if file.endswith('.pdf'):
                #Getting filepath
                filepath = os.path.join(root, file)
                filename = filepath[:-4]
                #Useful if you want to know which file is being processed
                print(filename)
                #Escapin spaces and parenthesis
                filename = filename.replace(" ","\ ")
                filename = filename.replace("(","\(")
                filename = filename.replace(")","\)")
        
                #Transforming PDF to plain text
                os.system("convert -density 300 "+filename+".pdf -depth 8 -strip -background grey -alpha off "+filename+".tiff")
                os.system("tesseract "+filename+".tiff -l spa+eng "+filename)

                os.system("rm "+filename+".tiff")

                return "Finshed process"
