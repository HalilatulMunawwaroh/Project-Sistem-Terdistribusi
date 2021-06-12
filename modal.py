import mysql.connector
import itertools

class resp:
    def __init__(self):
        self.con = mysql.connector.connect(host="localhost",
        #user="root"
        user="istiyadi"
        #,port="3307"
        #,passwd=""
        ,passwd="123456"
        ,database="tokolaptop",)
        self.cur = self.con.cursor()
    def info(self):
        dct = {}
        self.cur.execute("select namaToko,pemilikToko,alamatToko,emailtoko,tlptoko,igtoko from infotoko where idtoko=1")
        column =  [i[0] for i in self.cur.description]
        row = [[i for i in l] for l in self.cur.fetchall()]
        return dict(zip(column, row[0]))        
    def response2(self,nama):
        self.cur.execute("select jumlahbarang from spesifikasi s join detailproduct d on s.idlap = d.idlap where nama='"+nama+"'")
        return [i[0] for i in self.cur.fetchall()]
    def response3(self,name):
        dct = {}
        self.cur.execute("select nama,processor,Ram,Display,SistemOperasi from spesifikasi where nama= '"+name+"'")
        column =  [i[0] for i in self.cur.description]
        row = [[i for i in l] for l in self.cur.fetchall()]
        return dict(zip(column, row[0]))
    def promo(self,nama=None):
        if nama ==None:
            dct={}
            self.cur.execute("select namapromo,potonganharga,durasi from promo order by idpromo DESC limit 3")
            column =  [i[0] for i in self.cur.description]
            rows = [[i for i in l] for l in self.cur.fetchall()]
            return [dict(zip(column, row)) for row in rows]
        else:
            self.cur.execute("select * from promo where namapromo = '"+nama+"'")
    def saran(self,saran):
        self.cur.execute("""insert into saran (saran) values('%s')""" % str(saran))
        self.con.commit()
    def room(self,room):
        self.cur.execute("""insert into room (roomcode) values('%s')""" % str(room))
        self.con.commit()
    def getRoom(self):
        self.cur.execute("select roomcode from room")
        return self.cur.fetchall()
    def dltroom(self,room):
        room = str(room)
        self.cur.execute("DELETE FROM room WHERE roomcode="+room)
        self.con.commit()
if __name__=="__main__":
    resp()
