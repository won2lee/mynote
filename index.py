#!/home/john/anaconda3/bin/python3
print("Content-Type: text/html")
print()
import cgi
from linkdb import get_notelist, get_note
from util import form_maker, js_css, gen_action

# files = os.listdir('data')
# listStr = ''
# for item in files:
#     listStr = listStr + '<li><a href="index.py?id={name}">{name}</a></li>'.format(name=item)

# def form_maker(clss,id,class1=None):
#     clfunc = "confirm" if clss=="delete" else clss
#     scrpt = '''
#             <form action="{clfunc}.py" method="post">
#                 <input type="hidden" name="id" value="{id}">
#                 <input type="hidden" name="class1" value="{class1}">
#                 <input type="submit" value="{clss}">
#             </form>
#         '''.format(clss=clss,id=id,class1=class1,clfunc=clfunc)
#     return scrpt

form = cgi.FieldStorage()
# def gen_action(form):
#     clist = form["clist"].value if 'clist' in form else 0
#     class1 = form["class1"].value if 'class1' in form else None
#     class2 = form["class2"].value if 'class2' in form else None
#
#     if 'id' in form:
#         noteId = form["id"].value
#         description = get_note(noteId)
#         update_link = form_maker('update',noteId,class1,class2)
#         #'<a href="update.py?id={}&class1={}">update</a>'.format(pageId,class1)
#         delete_action = form_maker('delete',noteId)
#     else:
#         noteId = ''
#         description = get_note()
#         update_link = ''
#         delete_action = ''
#     create_link=form_maker('create',1)
#
#     return noteId,clist,class1,description,"{}{}{}".format(create_link,update_link,delete_action)

noteId,clist,class1,class2,description,bts = gen_action(form)
#tl = '"'+pageId+'"'
# descDB = readSQL(pageId)[0]['description'] if pageId!="Welcome" else ''
print('''<!doctype html>
<html>
<head>
  <title>WEB1 - Welcome</title>
  <meta charset="utf-8">
  {js_css}
  # <link type="text/css" rel="stylesheet" href="mystyle9.css">
  # <script src="colors.js"></script>
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
          <p>{desc}</p>
          <div id="to_action">
            {buttons}
          </div>
      </div>
  </div>
</body>
</html>
'''.format(title=str(noteId),
            js_css = js_css(),
            desc=description,
            listStr=get_notelist(clist,class1),
            buttons=bts))
            # {create_link}{update_link}{delete_action}
            # create_link=form_maker('create',1),
            # update_link=update_link,
            # delete_action=delete_action
            # ))
