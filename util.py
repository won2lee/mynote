
from linkdb import get_note

def form_maker(clss,id,class1=None,class2=None,note=''):
    if clss=="delete":
        clfunct="confirm"
    elif clss=="modify":
        clfunct="process_update"
    else:
        clfunct=clss
    hiddenTxt = "text" if clss=="modify" else "hidden"
    # clfunc="confirm" if clss=="delete" else clss

    scrpt = '''
            <form action="{clfunct}.py" method="get">
                <input type="hidden" name="id" value="{id}">
                <input type="{h_t}" name="class1" value="{class1}">
                <input type="{h_t}" name="class2" value="{class2}">
                {note}
                <input type="submit" value="{clss}">
            </form>
        '''.format(clss=clss,id=id,h_t=hiddenTxt,class1=class1,
            class2=class2,clfunct=clfunct,note=note)
    return scrpt

def js_css():
    scrpt ='''
        <link type="text/css" rel="stylesheet" href="mystyle9.css">
        <script src="colors.js"></script>
        '''
    return scrpt

def gen_action(form,action=None):
    clist = form["clist"].value if 'clist' in form else 0
    class1 = form["class1"].value if 'class1' in form else None
    class2 = form["class2"].value if 'class2' in form else None

    if action=="update":
        noteId = form["id"].value
        note = get_note(noteId,update=True)
        note ='''
            <p><textarea class="autosize" row="10" type="text"
            style="width:80%;" name="note">{note}</textarea></p>
            '''.format(note=note)
        return noteId,clist,class1,class2,get_note(noteId,update=True),form_maker('modify',noteId,class1,class2,note)

    if 'id' in form:
        noteId = form["id"].value
        description = get_note(noteId)
        update_link = form_maker('update',noteId,class1,class2)
        #'<a href="update.py?id={}&class1={}">update</a>'.format(pageId,class1)
        delete_action = form_maker('delete',noteId)
    else:
        noteId = ''
        description = get_note()
        update_link = ''
        delete_action = ''
    create_link=form_maker('create',1)
    return noteId,clist,class1,class2,description,"{}{}{}".format(create_link,update_link,delete_action)
