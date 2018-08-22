import os
import datetime
import pandas as pd
from SQLhelpers import * 
from bottle import Bottle, request, abort, response

'''
This is an API implemented in Bottle it takes a file saves it and loads it into an existing DB.

To send file to API use the following curl command:

curl -F "datafile=@[FILEPATH]" -X POST "http://[IP-ADDRESS]:[PORT]/api/books?pw=[PASSWORD]"

'''

#Defining API
apiTest = Bottle()

@apiTest.route('/api/books', method=['POST'])
def read_csv():

    #datafile is the file being sent
    #pw is just here in case you ask for a pw to be able to load a file to DB
    datafile = request.files.get('datafile')
    pw = request.query.pw
    
    if pw is None:
        raise ValueError('pw is invalid')
        
    #Getting filename and extension
    name, ext = os.path.splitext(datafile.filename)
    
    #Making sure we are working with a valid file format
    if ext not in ('.txt'):
        raise ValueError('{} is and invalid extension'.format(ext))
        
    #Place where you want to save the file
    save_path = "/tmp/apiTest"

    #If the path doesnt exist, create it
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    #Saving the file
    file_path = "{path}/{file}".format(path=save_path, file=datafile.filename)
    datafile.save(file_path)

    #Connecting to DB see SQLhelpers
    con = create_connection()

    #Loading CSV to a dataframe
    df = pd.read_csv(file_path, encoding="utf-8", sep="|", header=None)
    
    #Naming columns
    df.columns = ["year","title","author"]
    
    #Checking if a column is empty
    if df['year'].isnull().all():
        raise ValueError('some error')
        
    #Checking column type
    if df['num_cliente'].dtypes != 'object':
        pass
        
    #Loading info to DB
    df.to_sql('Mybooks',
              con,
              if_exists='append',
              index=False)

if __name__ == '__main__':
    apiTest.run( host='0.0.0.0', port=3000, reloader=True)

