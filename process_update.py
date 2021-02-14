#!/home/john/anaconda3/bin/python3
# print("Content-Type: text/html")
# print()

import cgi, linkdb

form = cgi.FieldStorage()
if 'note' not in form:
    print("Location: index.py")
else:
    inlist=[form["id"].value, form["note"].value,form["created"].value]
    if 'class1' in form and form["class1"].value!='None':
        inlist.append(form["class1"].value)
        if 'class2' in form and form["class2"].value!='None':
            inlist.append(form["class2"].value)
    linkdb.updated(inlist)
    # print(linkdb.updated(inlist))
    # print(inlist)
    print("Location: index.py")
print()
