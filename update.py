#!/home/john/anaconda3/bin/python3
print("Content-Type: text/html")
print()
import cgi
from linkdb import get_notelist, get_note
from util import form_maker, js_css, gen_action

form = cgi.FieldStorage()

noteId,clist,class1,class2,description,bts = gen_action(form)

print('''<!doctype html>
<html>
<head>
  <title>WEB1 - Welcome</title>
  <meta charset="utf-8">
  {js_css}
</head>
<body>
  <h1><a href="index.py">My Note</a></h1>
  <input id="niteButton" type="button" value='day' onclick="
  nightDayHandler(this);">

  <div id="grid">
      <ol reversed>
        {listStr}
      </ol>
      <div id="article">
        {to_modify}
      </div>
  </div>
</body>
</html>
'''.format(title=str(noteId),
            js_css = js_css(),
            desc=description,
            listStr=get_notelist(clist,class1),
            to_modify=bts))
