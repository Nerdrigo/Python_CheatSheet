from PyPDF2 import PdfFileReader

def pdf_reader():
    '''
    This function has no purpose, it it only intended to remind me of how
    to manipulate a PDF file 
    '''

    #Downloading the PDF file
    url = "'http://www.zelda.com/navi.pdf'"
    curl = "curl -o /tmp/my_pdf_copy.pdf "
    os.system(curl + url)

    #Checking if file was succesfully downloaded
    if not os.path.exists('/tmp/my_pdf_copy.pdf'):
        return False

    #Reading the PDF file
    pdf = PdfFileReader('/tmp/my_pdf_copy.pdf')

    #Getting the PDF Outline
    outline = pdf.getOutlines()

    #If there are subsections
    #Getting first section
    first_sec = outline[1]

    #Getting the subsections of the first section
    subsec = []
    for p in first_sec:
        if type(p) is PyPDF2.generic.Destination:
            subsec.append(p)

    #Looking for specific sub_section section
    ganondorf = None
    for sub in subsec:
        if sub['/Title'] == 'Ganondorf':
            ganondorf = sub
            break

    #Getting the text from the desired page
    page_num = ganondorf['/Page']['/StructParents']
    page = pdf.getPage(page_num)
    text = page.extractText()
