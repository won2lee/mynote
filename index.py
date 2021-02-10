#!/home/john/anaconda3/bin/python3
print("Content-Type: text/html")
print()
import cgi
from linkdb import get_notelist, get_note

# files = os.listdir('data')
# listStr = ''
# for item in files:
#     listStr = listStr + '<li><a href="index.py?id={name}">{name}</a></li>'.format(name=item)

def form_maker(clss,id,class1=None):
    scrpt = '''
            <form action="{clss}.py" method="post">
                <input type="hidden" name="id" value="{id}">
                <input type="hidden" name="class1" value="{class1}">
                <input type="submit" value="{clss}">
            </form>
        '''.format(clss=clss,id=id,class1=class1)
    return scrpt

form = cgi.FieldStorage()
clist = form["clist"].value if 'clist' in form else 0
class1 = form["class1"].value if 'class1' in form else None

if 'id' in form:
    pageId = form["id"].value
    description = get_note(pageId)
    update_link = form_maker('update',pageId,class1)
    #'<a href="update.py?id={}&class1={}">update</a>'.format(pageId,class1)
    delete_action = form_maker('delete',pageId)
else:
    pageId = ''
    description = get_note()
    update_link = ''
    delete_action = ''
#tl = '"'+pageId+'"'
# descDB = readSQL(pageId)[0]['description'] if pageId!="Welcome" else ''
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
          <p>{desc}</p>
          <div id="to_action">
            {create_link}{update_link}{delete_action}
          </div>
      </div>
  </div>
</body>
</html>
'''.format(title=str(pageId),
            desc=description,
            listStr=get_notelist(clist,class1),
            create_link=form_maker('create',1),
            update_link=update_link,
            delete_action=delete_action
            ))
