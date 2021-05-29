import modal
data = modal.resp()
db= {'halo':'hai hai',
    'menu': '<button class="menu">menu1</button><button class="menu">menu2</button><button class="menu">menu3</button><button class="menu">promo</button> ',
    # "Menu toko: \n silahkan pilih sistem bot \n 1.tentang toko =ketik menu1 \n 2.stock laptop = ketik menu2 nama laptop\
        #  \n 3.spek laptop = ketik menu3 nama laptop \n 4.newest promo =ketik promo",
    'menu1':"selamat datang di toko",
}
def msgFilterHandle(msg):
    response = ""
    msg = msg.split(' ')
    for i in msg:
        for j in db.keys():
            if i ==j:
                response+= db[j]
        else:
            if i =="menu2":
                if len(msg)>1:
                    response = str(data.response2(str(msg[1]))[0])
                else:
                    response = "masukan nama barang"
            elif i =="menu3":
                if len(msg)>1:
                    text = data.response3(str(msg[1]))
                    headtext  = "Detail product"
                    for i in text:
                        headtext+="\n %s : %s" % (str(i),str(text[i]))
            
                    response =headtext
                else:
                    response = "masukan nama barang"
            elif i=="promo":
                response = str(data.promo())
    return response