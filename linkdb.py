import pymysql
from datetime import datetime

open_db = pymysql.connect(
    user='root',
    password='314159',
    host='127.0.0.1',
    db='new_schema',
    charset='utf8'
)
cursor = open_db.cursor(pymysql.cursors.DictCursor)

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

def get_notelist(clist,class1):
    if clist:    # to list records in clicked class
        sql = "SELECT id,note,created,class1 FROM mynote WHERE class1='"+class1+"' ORDER BY id DESC LIMIT 20;"
    else:
        sql = "SELECT id,note,created,class1 FROM mynote ORDER BY id DESC LIMIT 20;"
    cursor.execute(sql)
    result = cursor.fetchall()

    listStr = ''
    for i,item in enumerate(result):
        listStr = listStr + "<li><a href='index.py?clist=1&class1={c}&id={id}'>[{c}]</a>".format(c=item['class1'],id=item['id'])
        listStr = listStr + "<a href='index.py?class1={c}&id={id}'>".format(c=item['class1'],id=item['id'])
        listStr = listStr + "({}) {}</a></li>".format(item['created'].strftime('%m-%d'),item['note'][:25])
    return listStr

def get_note(id=None,update=False):
    if id:
        sql = "SELECT id,note,created,class1 FROM mynote WHERE id="+str(id)+";"
        #sql = "SELECT id,note,created FROM mynote WHERE id='"+tl+"';"
    else:
        id=''
        sql = "SELECT id,note,created,class1 FROM mynote ORDER BY id DESC LIMIT 1;"
    cursor.execute(sql)
    result = cursor.fetchall()
    if update:
        result = result[0]['note']
    else:
        result = '''
                <form action="process_update.py" method="get">
                  <p><input type="hidden" name="id" value={id}>
                     <input type="text" name="class1" value='{class1}'>
                     <input type="text" name="class2" placeholder='{class2}'>
                  </p>
                  <p><textarea class="autosize" row="10" type="text" style="width:80%;" name="note">{note}</textarea></p>
                </form>'''.format(id=id,class1=result[0]['class1'],class2='',note=result[0]['note'])
    return result   #result[0]['note']

def insertd(inlist):
    if len(inlist)==2:
        class_added="class1,"
    elif len(inlist)==3:
        class_added="class1,class2,"
    else:
        class_added=""
    #inlist.insert(2,datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    inlist.append(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    sql="INSERT INTO mynote (note,"+class_added+"created) VALUES ('"
    sql=sql+"','".join(inlist)+"');"
    cursor.execute(sql)
    open_db.commit()

def updated(inlist):
    if len(inlist)==3:
        class_added=",class1='{}'".format(inlist[2])
        if len(inlist)==4:
            class_added=class_added+",class2='{}'".format(inlist[3])
    else:
        class_added=""
    #inlist.insert(2,datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    #inlist.append(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    sql="UPDATE mynote SET note='{}'{} WHERE id='{}';".format(inlist[1],class_added,inlist[0])
    cursor.execute(sql)
    open_db.commit()

def deleted(inlist):
    sql="DELETE FROM mynote WHERE id='{}';".format(inlist[0])
    cursor.execute(sql)
    open_db.commit()


# print(readSQL('MySQL'))
#
#
# import pandas as pd
#
# result = pd.DataFrame(result)
# print(result)
#
# sql = "INSERT INTO topic (title,description,created,author_id) VALUES('Python','Python is ..',NOW(),1);"
# cursor.execute(sql)
# open_db.commit()
#
# cursor = open_db.cursor(pymysql.cursors.DictCursor)
#
# sql = "SELECT * FROM topic;"
# cursor.execute(sql)
# result = cursor.fetchall()
# print(result[0]['title'])
# print(result[1]['title'])
# print('\n\n')
# print()
