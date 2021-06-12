import modal
data = modal.resp()
db= {'halo':'hai hai',
    'menu': '\
        <div class="outer-box">\
        <button class="menu" onclick="info()">info Toko</button>\
            <p class="info -hidden">segala tentang toko</p>\
            <button class="menu" onclick="stocks()">stock</button>\
                <p class="stocks -hidden">kirim nama barang yang ingin dicek persediannya</p>\
            <button class="menu" onclick="details()">details</button>\
                <p class="detail -hidden">kirim nama barang untuk mengetahui spesifikasi</p>\
        <button class="menu" onclick="promo()">promo</button> \
            <p class="promo -hidden">promo terbaru dari kami :)</p>\
            <button class="menu" onclick="sarans()">Saran</button>\
                <p class="saran -hidden">masukan saran anda ketik cancel untuk cancel</p>\
            <button class="menu" onclick="admin()">chat admin</button></div>'
}
def menu1():
    text = data.info()
    headtext  = "selamat datang ditoko"
    for i in text:
        headtext+="<br> %s : %s" % (str(i),str(text[i]))
    return headtext
def putroom(rooms):
    data.room(rooms)
def promo():
    text = data.promo()
    headtext  = "Promo terbaru "
    for j in text:
        for i in j:
            headtext+="<br> %s : %s" % (str(i),str(j[i]))
    return headtext
def detil(msg):
    try:
        text = data.response3(str(msg))
        headtext  = "Detail product"
        for i in text:
            headtext+="<br> %s : %s" % (str(i),str(text[i]))
    except:
        headtext = "data tidak ada atau terjadi kesalahan"    
    return headtext
def stock(msg):
    try:    
        response = str(data.response2(str(msg))[0])+" buah"
    except:
        response = "data tidak ada atau terjadi kesalahan"
    return (response)
def getrm():
    roomlist = []
    for i in (data.getRoom()):
        roomlist.append(i[0])
    return roomlist
def dcroom(room):
    try:
        data.dltroom(room)
    except:
        print("error")
def srn(pesan):
    data.saran(pesan)
def msgFilterHandle(msg):
    response = ""
    msg = msg.split(' ')
    for i in msg:
        for j in db.keys():
            if i ==j:
                response+= db[j]
    return response
getrm()