import mysql.connector
import itertools

class resp:
    def __init__(self):
        self.con = mysql.connector.connect(host="localhost",user="root",port="3307",passwd="",database="tokolaptop",)
        self.cur = self.con.cursor()
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
            self.cur.execute("select * from promo order by idpromo DESC limit 3")
            return self.cur.fetchall()
        else:
            self.cur.execute("select * from promo where namapromo = '"+nama+"'")
if __name__=="__main__":
    resp()