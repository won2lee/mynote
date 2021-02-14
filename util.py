
from linkdb import get_note

def form_maker(clss,id=None,class1=None,class2=None,created=None,note=''):
    if clss=="delete":
        clfunct="confirm"
    elif clss=="create":
        clfunct="update"
    elif clss=="modify":
        clfunct="process_update"
    elif clss=="generate":
        clfunct="process_create"
    else:
        clfunct=clss
    # action = "modify" if action=="update" else clss
    #gen = clss # if (clss=="update" or clss=="create") else None
    hiddenTxt = "text" if (clss=="modify" or clss=="generate") else "hidden"
    # clfunc="confirm" if clss=="delete" else clss
    scrpt = '''
            <form action="{clfunct}.py" method="get">
                <p><input type="hidden" name="id" value="{id}">
                <input type="hidden" name="mod" value="{clss}">
                <input type="{h_t}" name="class1" value="{class1}">
                <input type="{h_t}" name="class2" value="{class2}">
                <input type="{h_t}" name="created" value="{created}"></p>
                <p>{note}</p>
                <p><input type="submit" value="{clss}"></p>
            </form>
        '''.format(clss=clss,id=id,h_t=hiddenTxt,class1=class1,
            class2=class2,created=created,clfunct=clfunct,note=note)
    return scrpt

def js_css():
    scrpt ='''
        <link type="text/css" rel="stylesheet" href="mystyle9.css">
        <script src="colors.js"></script>
        '''
    return scrpt

def gen_action(form):
    clist = form["clist"].value if 'clist' in form else 0
    class1 = form["class1"].value if 'class1' in form else None
    class2 = form["class2"].value if 'class2' in form else None
    created = form["created"].value if 'created' in form else None
    action = form["mod"].value  if 'mod' in form else None

    if action=="update":
        noteId = form["id"].value
        note = get_note(noteId,update=True)
        note2 ='''
            <textarea class="autosize" row="10" type="text"
            style="width:80%;" name="note">{note}</textarea>
            '''.format(note=note)
        return noteId,clist,class1,class2,note,form_maker('modify',noteId,class1,class2,created,note2)

    if action=="create":
        note2 ='''
            <textarea class="autosize" row="10" type="text"
            style="width:80%;" name="note"></textarea>
            '''
        return '','','','','',form_maker('generate',note=note2)

    if 'id' in form:
        noteId = form["id"].value
        description = get_note(noteId)
        update_link = form_maker('update',noteId,class1,class2,created)
        #'<a href="update.py?id={}&class1={}">update</a>'.format(pageId,class1)
        delete_action = form_maker('delete',noteId)
    else:
        noteId = ''
        description = get_note()
        update_link = ''
        delete_action = ''
    create_link=form_maker('create')
    return noteId,clist,class1,class2,description,"{}{}{}".format(create_link,update_link,delete_action)
