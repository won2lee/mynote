import pymysql
from datetime import datetime
from tokeep import pswd

open_db = pymysql.connect(
    user='root',
    password=pswd,
    host='127.0.0.1',
    db='new_schema',
    charset='utf8'
)
cursor = open_db.cursor(pymysql.cursors.DictCursor)

def get_notelist(clist,class1):
    if clist:    # to list records in clicked class
        sql = "SELECT id,note,created,class1,class2 FROM mynote WHERE class1='"+class1+"' ORDER BY id DESC LIMIT 20;"
    else:
        sql = "SELECT id,note,created,class1,class2 FROM mynote ORDER BY id DESC LIMIT 20;"
    cursor.execute(sql)
    result = cursor.fetchall()

    listStr = ''
    for i,item in enumerate(result):
        alink="index.py?class1={c}&class2={c2}&created={dt}&id={id}".format(
                c=item['class1'],c2=item['class2'],dt=item['created'],id=item['id'])
        listStr = listStr + "<li><a href='" + alink +"&clist=1'>[{c}]</a>".format(c=item['class1'])
        listStr = listStr + "<a href='" + alink + "'>"
        listStr = listStr + "({}) {}</a></li>".format(item['created'].strftime('%m-%d'),item['note'][:25])
    return listStr

def get_note(id=None,update=False):
    if id:
        sql = "SELECT id,note,created,class1,class2 FROM mynote WHERE id="+str(id)+";"

    else:
        id=''
        sql = "SELECT id,note,created,class1,class2 FROM mynote ORDER BY id DESC LIMIT 1;"
    cursor.execute(sql)
    result = cursor.fetchall()
    if update:
        result = result[0]['note']
    else:
        result = '''
                <form action="process_update.py" method="get">
                  <p><input type="hidden" name="id" value={id}>
                     <input type="text" name="class1" placeholder='{class1}'>
                     <input type="text" name="class2" placeholder='{class2}'>
                     <input type="text" name="class2" placeholder='{created}'>
                  </p>
                  <p><textarea class="autosize" row="10" type="text" style="width:80%;" name="note" placeholder='{note}'></textarea></p>
                </form>'''.format(id=id,class1=result[0]['class1'],class2=result[0]['class2'],created=result[0]['created'],note=result[0]['note'])
    return result

def insertd(inlist):
    if len(inlist)==2:
        class_added="class1,"
    elif len(inlist)==3:
        class_added="class1,class2,"
    else:
        class_added=""

    inlist.append(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    sql="INSERT INTO mynote (note,"+class_added+"created) VALUES ('"
    sql=sql+"','".join(inlist)+"');"
    cursor.execute(sql)
    open_db.commit()

def updated(inlist):
    if len(inlist)>3:
        class_added=",class1='{}'".format(inlist[3])
        if len(inlist)>4:
            class_added=class_added+",class2='{}'".format(inlist[4])
    else:
        class_added=""

    sql="UPDATE mynote SET note='{}', created='{}' {} WHERE id='{}';".format(inlist[1],inlist[2],class_added,inlist[0])
    cursor.execute(sql)
    open_db.commit()
    return sql

def deleted(inlist):
    sql="DELETE FROM mynote WHERE id='{}';".format(inlist[0])
    cursor.execute(sql)
    open_db.commit()
