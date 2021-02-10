#!/home/john/anaconda3/bin/python3


import cgi, linkdb

form = cgi.FieldStorage()
if 'note' not in form:
    print("Location: create.py")
else:
    inlist=[form["note"].value]
    if 'class1' in form:
        inlist.append(form["class1"].value)
        if 'class2' in form:
            inlist.append(form["class2"].value)
    linkdb.insertd(inlist)
    # opened_file=open("data/"+title,'w')
    # opened_file.write(description)
    # opened_file.close()

    #Redirection
    print("Location: index.py")
print()
