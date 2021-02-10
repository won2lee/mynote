#!/home/john/anaconda3/bin/python3

import cgi, linkdb

form = cgi.FieldStorage()
if 'id' in form:
    linkdb.deleted([form["id"].value])
    # opened_file=open("data/"+title,'w')
    # opened_file.write(description)
    # opened_file.close()
    #Redirection
print("Location: index.py")
print()
