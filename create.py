#!/home/john/anaconda3/bin/python3
print("Content-Type: text/html")
print()
import cgi
from linkdb import get_notelist, get_note

# files = os.listdir('data')
# listStr = ''
# for item in files:
#     listStr = listStr + '<li><a href="index.py?id={name}">{name}</a></li>'.format(name=item)

form = cgi.FieldStorage()
clist = form["clist"].value if 'clist' in form else 0
class1 = form["class1"].value if 'class1' in form else None
if 'id' in form:
    pageId = form["id"].value
    description = get_note(pageId)
    #description = open('data/'+pageId, 'r').read()
else:
    pageId = 'Welcome'
    description = get_note()
print('''<!doctype html>
<html>
<head>
  <title>WEB1 - Welcome</title>
  <meta charset="utf-8">
  <link type="text/css" rel="stylesheet" href="mystyle7.css">
</head>
<body>
  <h1><a href="index.py">My Note</a></h1>

  <div id="grid">
    <ol reversed>
    {listStr}
    </ol>
    <div id="article">
        <form action="process_create.py" method="get">
          <p><input type="text" name="class1" placeholder="basis">
             <input type="text" name="class2" placeholder="">
          </p>
          <p><textarea class="autosize" row=10 style="width:80%;" name="note" placeholder="note"></textarea></p>
          <p><input type="submit"></p>
        </form>
    </div>

  </div>
</body>
</html>
'''.format( listStr=get_notelist(clist,class1)))
