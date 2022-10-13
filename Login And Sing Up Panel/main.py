from pickle import ADDITEMS
import kayit
from giris import Uii_MainWindow
from bilgi import xUi_MainWindow
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow
from adminpanel import aUi_MainWindow
tc = ""
parola = ""
parola_tekrar = ""
ad = ""
soyad = ""
kullaniciadi = ""
ulke = ""
class admin(QMainWindow):
    def __init__(self):
        super(admin,self).__init__()
        self.adminui = aUi_MainWindow()
        self.adminui.setupUi(self)
        self.setWindowTitle("Admin Paneli")
        self.load()
        self.adminui.goruntule_buton.clicked.connect(self.goruntule)
        self.adminui.sil_buton.clicked.connect(self.sil)
        self.adminui.ekle_buton.clicked.connect(self.ek)
        self.adminui.cikis_buton.clicked.connect(self.cikis)
    def load(self):
        with open("users.txt","r",encoding="utf-8") as dosya:
            liste = dosya.readlines()
            sayi = 0
            for i in range(0,len(liste)):
                if i %7==3:
                    self.adminui.listearaci.addItem(liste[i])
                    item = self.adminui.listearaci.item(1)             
            self.adminui.listearaci.setCurrentRow(0)
    def goruntule(self):
        indis = self.adminui.listearaci.currentRow()
        ad = indis*7+3
        print(ad)
        sistem.bilgiyazdir(sayi=ad)
        sistem.show()
    def sil(self):
        indis = self.adminui.listearaci.currentRow()
        ad = indis*7
        print(ad)
        with open("users.txt","r+",encoding="utf-8") as dosya:
            liste = dosya.readlines()   
            for i in range(0,7):
                liste.pop(ad)
        self.silad2(ab=liste)
    def silad2(self,ab=[]):
        with open("users.txt","w",encoding="utf-8") as dosya:    
            print(ab)
            for a in ab:
                dosya.write(a)
            ind = self.adminui.listearaci.currentRow()
            it = self.adminui.listearaci.takeItem(ind)
            del it
    def ek(self):
       uyeolucu.show()     
    def ek2(self,ad ="str"):
        self.adminui.listearaci.addItem(ad)
    def cikis(self):
        self.close()
        girisyapici.show()
class bilgiislem(QMainWindow):
    def __init__(self):
        super(bilgiislem,self).__init__()
        self.bilgiui = xUi_MainWindow()
        self.bilgiui.setupUi(self)
    def bilgiyazdir(self,sayi = 0):
        with open("users.txt","r",encoding="utf-8") as dosya:
            liste = dosya.readlines()
            print(liste)
            sayi -= 3
            self.setWindowTitle(liste[sayi + 3])
            self.bilgiui.tc.setText("Tc: "+liste[sayi])
            self.bilgiui.ad.setText("Ad: "+liste[sayi + 1])
            self.bilgiui.soyad.setText("Soyad: "+liste[sayi + 2])
            self.bilgiui.kullaniciadi.setText("Kullanıcı Adı: "+liste[sayi + 3])
            self.bilgiui.sifre.setText("Şifre: "+liste[sayi + 4])
            self.bilgiui.ulke.setText("Ülke: "+liste[sayi + 5])
class uygulama(QMainWindow):
    def __init__(self):
        super(uygulama,self).__init__()
        self.ui = kayit.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Üyelik Sistemi")
        self.ui.uyeol_buton.clicked.connect(self.uye_ol)
        self.ui.girisyap_buton.clicked.connect(self.giris_yap)
    def giris_yap(self):
        self.temizle()
        uyeolucu.close()
        girisyapici.show()
    def uye_ol(self):
        self.atama()
    def atama(self):
        global tc,parola,parola_tekrar,ad,soyad,kullaniciadi,ulke
        tc = self.ui.tc_text.text()
        parola = self.ui.parola_text.text()
        parola_tekrar =self.ui.parolatekrar_text.text()
        ad = self.ui.ad_text.text()
        soyad = self.ui.soyad_text.text()
        kullaniciadi = self.ui.kullanici_text.text()
        ulke = self.ui.ulkesec.currentText()
        self.yildizkontrol()
    def yildizkontrol(self):
        if len(tc)>0 and len(parola)>0 and len(parola_tekrar)>0 and len(kullaniciadi)>0 and len(ad)>0 and len(soyad)>0 and self.ui.kurallar.isChecked() == True and self.ui.sozlesme.isChecked()== True:
            self.sifrekontrol()
        else:
            self.ui.durum_label.setText("DURUM: YILDIZLI ALANLARIN DOLDURULMASI GEREKMEKTEDİR!") 
    def sifrekontrol(self):
        if parola == parola_tekrar:
            print("parolalar aynı")
            import re
            if len(parola) < 8:
                self.ui.durum_label.setText("parola en az 8 karakter olmalıdır.")
            elif not re.search("[a-z]", parola):
                self.ui.durum_label.setText("parola küçük harf içermelidir.") 
            elif not re.search("[A-Z]", parola):
                self.ui.durum_label.setText("parola büyük harf içermelidir.")
            elif not re.search("[0-9]", parola):
                self.ui.durum_label.setText("parola rakam içermelidir.")
            elif re.search("\s",parola):
                self.ui.durum_label.setText("parola boşluk içermemelidir.")
            else:
                print("geçerli parola")
                self.tckontrol()
        else:
            self.ui.durum_label.setText("DURUM: PAROLALAR AYNI DEĞİL!")
    def tckontrol(self):
        try:
            sayi_tc = int(tc)
            if len(tc) == 11:
                self.ui.durum_label.setText("DURUM: ÜYE OLUNDU!")
                adminpanel.ek2(kullaniciadi)
                self.uyeekle()
            else:
                self.ui.durum_label.setText("DURUM: TC KİMLİK 11 HANELİ OLMALI!")
        except Exception as hata :
            self.ui.durum_label.setText("DURUM: TC KİMLİK SAYILARDAN OLUŞMALI")
            print(hata)
    def uyeekle(self):
        with open("users.txt","a",encoding="utf-8") as dosya:
            dosya.write(tc+"\n")
            dosya.write(ad+"\n")
            dosya.write(soyad+"\n")
            dosya.write(kullaniciadi+"\n")
            dosya.write(parola+"\n")
            dosya.write(ulke+"\n")
            dosya.write("per_level_0\n")
            self.guncele()
    def guncele(self):
        global tc,parola,parola_tekrar,ad,soyad,kullaniciadi,ulke
        tc = ""
        parola = ""
        parola_tekrar = ""
        ad = ""
        soyad = ""
        kullaniciadi = ""
        ulke = ""
    def temizle(self):
        self.ui.tc_text.setText("")
        self.ui.parola_text.setText("")
        self.ui.parolatekrar_text.setText("")
        self.ui.ad_text.setText("")
        self.ui.soyad_text.setText("")
        self.ui.kullanici_text.setText("")
class giris(QMainWindow):
    def __init__(self):
        super(giris,self).__init__()
        self.girisui = Uii_MainWindow()
        self.girisui.setupUi(self)
        self.girisui.kayitol_buton.clicked.connect(self.cikis)
        self.girisui.girisyap_buton.clicked.connect(self.gir)
    def gir(self):
        username = self.girisui.kullaniciadigiri_text.text()
        password = self.girisui.sifregiris_text.text()
        ind = 0
        
        with open("users.txt","r",encoding="utf-8") as dosya:
            a = True
            try:
                liste = dosya.readlines()
                print(liste)
                for i in liste:   
                    if liste.index(i)%7==3:
                        if i == username+"\n":
                            ind = liste.index(i)
                            if password+"\n" == liste[ind+1]:
                                print("girildi!")
                                if liste[ind+3]=="per_level_0\n":
                                    sistem.show()
                                    sistem.setWindowTitle(username)
                                    self.close()
                                    print("per level 0")
                                    sistem.bilgiyazdir(sayi=ind)
                                elif liste[ind+3]=="per_level_1\n":
                                    adminpanel.show()
                                    self.close()
                                    sistem.bilgiyazdir(sayi=ind)
                                    print("per level 1")
                                a = False
                                break
                            else:
                                a = False
                                result = QtWidgets.QMessageBox.warning(self,"UYARI!","GİRİLEN KULLANICI ADI VEYA ŞİFRE HATALI!",QtWidgets.QMessageBox.Ok)
                                break
                        else:
                            pass
                if a == True:                              
                    result = QtWidgets.QMessageBox.warning(self,"UYARI!","GİRİLEN KULLANICI ADI VEYA ŞİFRE HATALI!",QtWidgets.QMessageBox.Ok)
                    print("girilen kullanıcı adı bulunamadı")
                                
            except Exception as hata:
                print(hata)
    def cikis(self):
        girisyapici.close()
        uyeolucu.show()
app = QApplication(sys.argv)
girisyapici = giris()
uyeolucu = uygulama()
sistem = bilgiislem()
adminpanel = admin()
girisyapici.show()
app.exit(app.exec_())
