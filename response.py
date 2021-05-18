db= {'halo':'hai hai',
    'menu': "Menu toko: \n silahkan pilih sistem bot \n 1.tentang toko =ketik menu1 \n 2.stock laptop = ketik menu2 nama laptop\
         \n 3.spek laptop = ketik menu3 nama laptop \n 4.newest promo =ketik promo",
    'menu1':"selamat datang di toko",
    'promo':'promo hari ini habis'
}
def msgFilterHandle(msg):
    response = ""
    msg = msg.split(' ')
    for i in msg:
        for j in db.keys():
            if i ==j:
                response+= db[j]
        else:
            #will changed to proper mysql bridge 
            if i =="menu2":
                response ="select stock from laptop l join stock s on l.id_laptop =s.id_laptop where name=?,"+str(msg[1:])
            elif i =="menu3":
                response = "select * from laptop where name=?"+str(msg[1:])
    return response