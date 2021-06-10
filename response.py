import modal
data = modal.resp()
db= {'halo':'hai hai',
    'menu': '\
        <div class="outer-box">\
        <button class="menu" onclick="info()">info</button><button class="menu" onclick="stocks()">stock</button>\
            <button class="menu" onclick="details()">\
        details</button><button class="menu" onclick="promo()">promo</button> \
            <button class="menu" onclick="admin()">chat admin</button></div>',
    'menu1':"selamat datang di toko",
}
def putroom(rooms):
    data.room(rooms)
def promo():
    return str(data.promo())
def detil(msg):
    try:
        text = data.response3(str(msg))
        headtext  = "Detail product"
        for i in text:
            headtext+="\n %s : %s" % (str(i),str(text[i]))
    except:
        headtext = "data tidak ada atau terjadi kesalahan"    
    return headtext
def stock(msg):
    try:    
        response = str(data.response2(str(msg))[0])+" buah"
    except:
        response = "data tidak ada atau terjadi kesalahan"
    return (response)
def msgFilterHandle(msg):
    response = ""
    msg = msg.split(' ')
    for i in msg:
        for j in db.keys():
            if i ==j:
                response+= db[j]
    return response