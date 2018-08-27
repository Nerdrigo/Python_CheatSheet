import os
import pandas as pd
import SQLhelpers
from bottle import Bottle, request, abort, response

'''
Code snippet to take an SQL query result, and returning a JSON with that information.
'''

#Declaring API
apiTest = Bottle()

#Defining API route and funciont
@apiTest.route('/api/test', method=['GET'])
def get_info():
    
    #Making query
    query = "SELECT * from [TABLE NAME];"
    
    #Connecting with DB, function def in SQLhelpers.py
    con = create_connection()
    
    #Carrying out the query
    try:
        cur = con.cursor()
        cur.execute(query)
        query_result = cur.fetchall()
        cur.close()
    except psycopg2.ProgrammingError: #IF DB doesn't exist
        con.rollback()
        pass
        
    #There are two ways to get the results
    #First: 
    df = pd.DataFrame(query_result)
    df.columns = ["year","title","author"]
    #Second: (it's ok if you need to process query result before creating the JSON
    #year = [x[0] for x in query_result]
    #title = [x[1] for x in query_result]
    #author = [x[2] for x in query_result]
    
    #process info...
    
    #If you chose second way to store query results
    df = pd.DataFrame({'year': year,
                       'title': title,
                       'author': author})
    
    #If you need to round up something
    df[COL_NAME] = ['%.2f' % x for x in df[COL_NAME]]
    
    #Making JSON
    json_result = df.to_json(orient = 'records')
    
    return json result
    
if __name__ == '__main__':
    apiRepEnt.run(host='0.0.0.0', port=3017, reloader=True)
    
    
    
    
