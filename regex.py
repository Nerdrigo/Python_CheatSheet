import re

def read_text(file):
    '''
    This program has no real only purpose.

    I am only wrinting this so that I don't have to remember the little
    details of opening and preprocessing text before using regex
    '''

    #Opening file
    with codecs.open(file, "rb", encoding = 'utf8') as txt_file:
            #Reading file
            text = txt_file.read()
            #Replacing special characters
            text = text.replace('“','"')
            text = text.replace('”','"')
            text = text.replace('’',"'")
            text = text.replace("á","a")
            text = text.replace("é","e")
            text = text.replace("í","i")
            text = text.replace("ó","o")
            text = text.replace("ú","u")
            text = text.replace("ñ","n")
            text = text.replace("Ñ","N")
            text = text.replace("Á","A")
            text = text.replace("É","E")
            text = text.replace("Í","I")
            text = text.replace("Ó","O")
            text = text.replace("Ú","U")
            
            ##############LOOKING FOR SOMETHING#######################

            search_pattern = re.search(r'[regex]',text)
            
            try:
                #If there was a match replace linebreaks with spaces
                search_pattern = search_pattern.group(0)
                search_pattern = search_pattern.replace("\n"," ")

            except AttributeError:
                #If no match was found do something
                pass

