from ast import IsNot
from distutils.cmd import Command
from msilib import add_tables
from subprocess import HIGH_PRIORITY_CLASS
import tkinter as tk
from turtle import back
import random

#KASNIJE UBACITI UNOS IMENA BAŠ U PROGRAMU UKOLIKO JE MOGUĆE
igrač1ime = input("Unesi ime: ")
while len(igrač1ime)>7 or len(igrač1ime)==0:
    igrač1ime = input("Unesi ime koje ima manje od 7 znakova i više od 0: ")
igrač2ime = input("Unesi ime: ")
while len(igrač2ime)>7 or len(igrač2ime)==0:
    igrač2ime = input("Unesi ime koje ima manje od 7 znakova i više od 0: ")
ciji_red = 1  
usporedba = []
bacenaKarta = []
def tab1():
    #main window igre
    windowmain = tk.Tk()
    windowmain.configure(background="green")
    windowmain.geometry("500x500")
    windowmain.title("ŠNAPS")
    #funkcija za provjeru kliknutog gumba 7
    def kliknut7():
        novi_prozor = tk.Tk()
        windowmain.destroy()
        novi_prozor.geometry("1300x900")
        novi_prozor.title("ŠNAPS")
        novi_prozor.configure(bg="green")
        p1score = 7
        p2score = 7
        #turn_tekst
        turn_tekst = tk.Label(novi_prozor,text=f"{igrač1ime} je na redu!",font=("Arial bold", 30),bg="green",fg="white").place(x=460,y=50,width=400,height=60)
        #scoreboardovi
        p1scoreboard = tk.Label(novi_prozor, text=f"{igrač1ime}: {p1score}",font=("Arial bold", 20) ).place(x=1110,y=50,width=150,height=60)
        p2scoreboard = tk.Label(novi_prozor, text=f"{igrač2ime}: {p2score}",font=("Arial bold", 20) ).place(x=1110,y=120,width=150,height=60)
        #back button
        def povratak7():
            novi_prozor.destroy()
            tab1()
        nazad = tk.Button(novi_prozor,text="Izlazak iz igre",bg="red",fg="white",font=("Arial bold", 18),command=povratak7).place(x=50,y=50,width=160,height=50)
        #button za dijeljenje karata
        vrsta = ["Tref", "Pik", "Karo", "Srce"]
        vrijednosti_karata = {"Tref Dečko":2, "Tref Dama":3, "Tref Kralj":4, "Tref Deset":10, "Tref As":11,"Pik Dečko":2, "Pik Dama":3, "Pik Kralj":4, "Pik Deset":10, "Pik As":11,"Karo Dečko":2, "Karo Dama":3, "Karo Kralj":4, "Karo Deset":10, "Karo As":11,"Srce Dečko":2, "Srce Dama":3, "Srce Kralj":4, "Srce Deset":10, "Srce As":11}
        dek = ["Tref Dečko", "Tref Dama", "Tref Kralj", "Tref Deset", "Tref As","Pik Dečko", "Pik Dama", "Pik Kralj", "Pik Deset", "Pik As","Karo Dečko", "Karo Dama", "Karo Kralj", "Karo Deset", "Karo As","Srce Dečko", "Srce Dama", "Srce Kralj", "Srce Deset", "Srce As"]
        p1inv=[]
        p2inv = []
        adut = []
        p1bodovi_runda = []
        p2bodovi_runda = []
        def dijeljenje_karata():
            for i in range(3):
                p1inv.append(random.choice(dek))
                dek.remove(p1inv[i])
            for i in range(3): 
                p2inv.append(random.choice(dek))
                dek.remove(p2inv[i])
            adut.append(random.choice(dek))
            dek.remove(adut[0])
            slikaAduta = tk.Label(novi_prozor, text=adut[0],font=("Arial bold", 18) ).place(x=525,y=300,width= 250,height=180)
            for i in range(3,5):
                p1inv.append(random.choice(dek))
                dek.remove(p1inv[i])
            for i in range(3,5): 
                p2inv.append(random.choice(dek))
                dek.remove(p2inv[i])
            print(p1inv, p2inv)
            #karte_prikaz
            p1karta_1 = tk.Button(novi_prozor,text=p1inv[0],font=("Arial bold", 18), command=lambda:[kliknut_gumb1()]).place(x=125,y=550,width= 180,height=250)
            p1karta_2 = tk.Button(novi_prozor,text=p1inv[1],font=("Arial bold", 18), command=lambda:[kliknut_gumb2()]).place(x=325,y=550,width= 180,height=250)
            p1karta_3 = tk.Button(novi_prozor,text=p1inv[2],font=("Arial bold", 18), command=lambda:[kliknut_gumb3()]).place(x=525,y=550,width= 180,height=250)
            p1karta_4 = tk.Button(novi_prozor,text=p1inv[3],font=("Arial bold", 18), command=lambda:[kliknut_gumb4()]).place(x=725,y=550,width= 180,height=250)
            p1karta_5 = tk.Button(novi_prozor,text=p1inv[4],font=("Arial bold", 18), command=lambda:[kliknut_gumb5()]).place(x=925,y=550,width= 180,height=250)

            p2karta_1 = tk.Button(novi_prozor,text=p2inv[0],font=("Arial bold", 18), command=lambda:[kliknut_gumb6()]).place(x=3000,y=550,width= 180,height=250)
            p2karta_2 = tk.Button(novi_prozor,text=p2inv[1],font=("Arial bold", 18), command=lambda:[kliknut_gumb7()]).place(x=3000,y=550,width= 180,height=250)
            p2karta_3 = tk.Button(novi_prozor,text=p2inv[2],font=("Arial bold", 18), command=lambda:[kliknut_gumb8()]).place(x=3000,y=550,width= 180,height=250)
            p2karta_4 = tk.Button(novi_prozor,text=p2inv[3],font=("Arial bold", 18), command=lambda:[kliknut_gumb9()]).place(x=3000,y=550,width= 180,height=250)
            p2karta_5 = tk.Button(novi_prozor,text=p2inv[4],font=("Arial bold", 18), command=lambda:[kliknut_gumb10()]).place(x=3000,y=550,width= 180,height=250)
            #promjena_tura
        def promijeni_red():
            global usporedba
            global ciji_red
            print(f"bacena karta je {bacenaKarta}")
            if ciji_red % 2 != 0:
                turn_tekst = tk.Label(novi_prozor,text=f"{igrač2ime} je na redu!",font=("Arial bold", 30),bg="green",fg="white").place(x=460,y=50,width=400,height=60)
                if p1inv[0] != bacenaKarta[-1]:
                    p1karta_1 = tk.Button(novi_prozor,text=p1inv[0],font=("Arial bold", 18), command=lambda:[kliknut_gumb1()]).place(x=3000,y=550,width= 180,height=250)
                else:
                    pass
                if p1inv[1] != bacenaKarta[-1]:
                    p1karta_2 = tk.Button(novi_prozor,text=p1inv[1],font=("Arial bold", 18), command=lambda:[kliknut_gumb2()]).place(x=3000,y=550,width= 180,height=250)
                else:
                    pass
                if p1inv[2] != bacenaKarta[-1]:
                    p1karta_3 = tk.Button(novi_prozor,text=p1inv[2],font=("Arial bold", 18), command=lambda:[kliknut_gumb3()]).place(x=3000,y=550,width= 180,height=250)
                else:
                    pass
                if p1inv[3] != bacenaKarta[-1]:
                    p1karta_4 = tk.Button(novi_prozor,text=p1inv[3],font=("Arial bold", 18), command=lambda:[kliknut_gumb4()]).place(x=3000,y=550,width= 180,height=250)
                else:
                    pass
                if p1inv[4] != bacenaKarta[-1]:
                    p1karta_5 = tk.Button(novi_prozor,text=p1inv[4],font=("Arial bold", 18), command=lambda:[kliknut_gumb5()]).place(x=3000,y=550,width= 180,height=250) 
                else:
                    pass
                if p2inv[0] != bacenaKarta[-1]:
                    p2karta_1 = tk.Button(novi_prozor,text=p2inv[0],font=("Arial bold", 18), command=lambda:[kliknut_gumb6()]).place(x=125,y=550,width= 180,height=250)
                else:
                    pass
                if p2inv[1] != bacenaKarta[-1]:
                    p2karta_2 = tk.Button(novi_prozor,text=p2inv[1],font=("Arial bold", 18), command=lambda:[kliknut_gumb7()]).place(x=325,y=550,width= 180,height=250)
                else:
                    pass
                if p2inv[2] != bacenaKarta[-1]:
                    p2karta_3 = tk.Button(novi_prozor,text=p2inv[2],font=("Arial bold", 18), command=lambda:[kliknut_gumb8()]).place(x=525,y=550,width= 180,height=250)
                else:
                    pass
                if p2inv[3] != bacenaKarta[-1]:
                    p2karta_4 = tk.Button(novi_prozor,text=p2inv[3],font=("Arial bold", 18), command=lambda:[kliknut_gumb9()]).place(x=725,y=550,width= 180,height=250)
                else:
                    pass
                if p2inv[4] != bacenaKarta[-1]:
                    p2karta_5 = tk.Button(novi_prozor,text=p2inv[4],font=("Arial bold", 18), command=lambda:[kliknut_gumb10()]).place(x=925,y=550,width= 180,height=250)
                else:
                    pass
                ciji_red +=1
            else:
                turn_tekst = tk.Label(novi_prozor,text=f"{igrač1ime} je na redu!",font=("Arial bold", 30),bg="green",fg="white").place(x=460,y=50,width=400,height=60)
                if p1inv[0] != bacenaKarta[-1]:
                    p1karta_1 = tk.Button(novi_prozor,text=p1inv[0],font=("Arial bold", 18), command=lambda:[kliknut_gumb1()]).place(x=125,y=550,width= 180,height=250)
                else:
                    pass
                if p1inv[1] != bacenaKarta[-1]:
                    p1karta_2 = tk.Button(novi_prozor,text=p1inv[1],font=("Arial bold", 18), command=lambda:[kliknut_gumb2()]).place(x=325,y=550,width= 180,height=250)
                else:
                   pass
                if p1inv[2] != bacenaKarta[-1]:
                    p1karta_3 = tk.Button(novi_prozor,text=p1inv[2],font=("Arial bold", 18), command=lambda:[kliknut_gumb3()]).place(x=525,y=550,width= 180,height=250)
                else:
                    pass
                if p1inv[3] != bacenaKarta[-1]:
                    p1karta_4 = tk.Button(novi_prozor,text=p1inv[3],font=("Arial bold", 18), command=lambda:[kliknut_gumb4()]).place(x=725,y=550,width= 180,height=250)
                else:
                    pass
                if p1inv[4] != bacenaKarta[-1]:
                    p1karta_5 = tk.Button(novi_prozor,text=p1inv[4],font=("Arial bold", 18), command=lambda:[kliknut_gumb5()]).place(x=925,y=550,width= 180,height=250)
                else:
                    pass

                if p2inv[0] != bacenaKarta[-1]:
                    p2karta_1 = tk.Button(novi_prozor,text=p2inv[0],font=("Arial bold", 18), command=lambda:[kliknut_gumb6()]).place(x=3000,y=550,width= 180,height=250)
                else:
                    pass
                if p2inv[1] != bacenaKarta[-1]:
                    p2karta_2 = tk.Button(novi_prozor,text=p2inv[1],font=("Arial bold", 18), command=lambda:[kliknut_gumb7()]).place(x=3000,y=550,width= 180,height=250)
                else:
                    pass
                if p2inv[2] != bacenaKarta[-1]:
                    p2karta_3 = tk.Button(novi_prozor,text=p2inv[2],font=("Arial bold", 18), command=lambda:[kliknut_gumb8()]).place(x=3000,y=550,width= 180,height=250)
                else:
                    pass
                if p2inv[3] != bacenaKarta[-1]:
                    p2karta_4 = tk.Button(novi_prozor,text=p2inv[3],font=("Arial bold", 18), command=lambda:[kliknut_gumb9()]).place(x=3000,y=550,width= 180,height=250)
                else:
                    pass
                if p2inv[4] != bacenaKarta[-1]:
                    p2karta_5 = tk.Button(novi_prozor,text=p2inv[4],font=("Arial bold", 18), command=lambda:[kliknut_gumb10()]).place(x=3000,y=550,width= 180,height=250)
                else:
                    pass
                ciji_red +=1
                print(f"usporedba: {usporedba}")
                if vrijednosti_karata[usporedba[0]]>vrijednosti_karata[usporedba[1]]:
                    p1bodovi_runda.append(vrijednosti_karata[usporedba[0]]+vrijednosti_karata[usporedba[1]])
                    usporedba.clear()
                    print(p1bodovi_runda,p2bodovi_runda)
                elif vrijednosti_karata[usporedba[0]]<vrijednosti_karata[usporedba[1]]:
                    p2bodovi_runda.append(vrijednosti_karata[usporedba[0]]+vrijednosti_karata[usporedba[1]])
                    usporedba.clear()
                    print(p1bodovi_runda,p2bodovi_runda)
                else:
                    print("Neš ne radi")
                print(p1bodovi_runda,p2bodovi_runda)
        promjena = tk.Button(novi_prozor,text="Završi bacanje",font=("Arial bold", 18),bg="red",fg="white",command=promijeni_red).place(x=570,y=130,width=170,height=50)
        podijeli = tk.Button(novi_prozor, text="Podijeli karte",font=("Arial bold", 18), bg="red",fg="white",command=dijeljenje_karata).place(x=1100,y=450,width=160,height=50)
         #buttoni za bacanje karte
        def kliknut_gumb1():
            karta_bacena = tk.Label(novi_prozor,text=p1inv[0],font=("Arial bold", 18)).place(x=730,y=250,width= 180,height=250)
            usporedba.append(p1inv[0])
            bacenaKarta.append(p1inv[0])
        def kliknut_gumb2():
            karta_bacena = tk.Label(novi_prozor,text=p1inv[1],font=("Arial bold", 18)).place(x=730,y=250,width= 180,height=250)
            usporedba.append(p1inv[1])
            bacenaKarta.append(p1inv[1])
        def kliknut_gumb3():
            karta_bacena = tk.Label(novi_prozor,text=p1inv[2],font=("Arial bold", 18)).place(x=730,y=250,width= 180,height=250)
            usporedba.append(p1inv[2])
            bacenaKarta.append(p1inv[2])
        def kliknut_gumb4():
            karta_bacena = tk.Label(novi_prozor,text=p1inv[3],font=("Arial bold", 18)).place(x=730,y=250,width= 180,height=250)
            usporedba.append(p1inv[3])
            bacenaKarta.append(p1inv[3])
        def kliknut_gumb5():
            karta_bacena = tk.Label(novi_prozor,text=p1inv[4],font=("Arial bold", 18)).place(x=730,y=250,width= 180,height=250)
            usporedba.append(p1inv[4])
            bacenaKarta.append(p1inv[4])
        def kliknut_gumb6():
            karta_bacena = tk.Label(novi_prozor,text=p2inv[0],font=("Arial bold", 18)).place(x=730,y=250,width= 180,height=250)
            usporedba.append(p2inv[0])
            bacenaKarta.append(p2inv[0])
        def kliknut_gumb7():
            karta_bacena = tk.Label(novi_prozor,text=p2inv[1],font=("Arial bold", 18)).place(x=730,y=250,width= 180,height=250)
            usporedba.append(p2inv[1])
            bacenaKarta.append(p2inv[1])
        def kliknut_gumb8():
            karta_bacena = tk.Label(novi_prozor,text=p2inv[2],font=("Arial bold", 18)).place(x=730,y=250,width= 180,height=250)
            usporedba.append(p2inv[2])
            bacenaKarta.append(p2inv[2])
        def kliknut_gumb9():
            karta_bacena = tk.Label(novi_prozor,text=p2inv[3],font=("Arial bold", 18)).place(x=730,y=250,width= 180,height=250)
            usporedba.append(p2inv[3])
            bacenaKarta.append(p2inv[3])
        def kliknut_gumb10():
            karta_bacena = tk.Label(novi_prozor,text=p2inv[4],font=("Arial bold", 18)).place(x=730,y=250,width= 180,height=250)
            usporedba.append(p2inv[4])
            bacenaKarta.append(p2inv[4])
        
    #funkcija za provjeru kliknutog gumba 9
    def kliknut9():
        novi_prozor = tk.Tk()
        windowmain.destroy()
        novi_prozor.geometry("1300x900")
        novi_prozor.title("ŠNAPS")
        novi_prozor.configure(bg="green")
        p1score = 9
        p2score = 9
        #turn_tekst
        turn_tekst = tk.Label(novi_prozor,text=f"{igrač1ime} je na redu!",font=("Arial bold", 30),bg="green",fg="white").place(x=460,y=50,width=400,height=60)
        #promjena_turna
        promjena = tk.Button(novi_prozor,text="Završi bacanje",font=("Arial bold", 18),bg="red",fg="white").place(x=570,y=130,width=170,height=50)
        #scoreboardovi
        p1scoreboard = tk.Label(novi_prozor, text=f"{igrač1ime}: {p1score}",font=("Arial bold", 20) ).place(x=1100,y=50,width=150,height=60)
        p2scoreboard = tk.Label(novi_prozor, text=f"{igrač2ime}: {p2score}",font=("Arial bold", 20) ).place(x=1100,y=120,width=150,height=60)
        #back button
        def povratak9():
            novi_prozor.destroy()
            tab1()
        nazad = tk.Button(novi_prozor,text="Izlazak iz igre",bg="red",fg="white",font=("Arial bold", 18),command=povratak9).place(x=50,y=50,width=160,height=50)
        #button za dijeljenje karata
        vrsta = ["Tref", "Pik", "Karo", "Srce"]
        vrijednosti_karata = {"Tref Dečko":2, "Tref Dama":3, "Tref Kralj":4, "Tref Deset":10, "Tref As":11,"Pik Dečko":2, "Pik Dama":3, "Pik Kralj":4, "Pik Deset":10, "Pik As":11,"Karo Dečko":2, "Karo Dama":3, "Karo Kralj":4, "Karo Deset":10, "Karo As":11,"Srce Dečko":2, "Srce Dama":3, "Srce Kralj":4, "Srce Deset":10, "Srce As":11}
        dek = ["Tref Dečko", "Tref Dama", "Tref Kralj", "Tref Deset", "Tref As","Pik Dečko", "Pik Dama", "Pik Kralj", "Pik Deset", "Pik As","Karo Dečko", "Karo Dama", "Karo Kralj", "Karo Deset", "Karo As","Srce Dečko", "Srce Dama", "Srce Kralj", "Srce Deset", "Srce As"]
        p1inv=[]
        p2inv = []
        adut = []
        def bačena_karta():
            print("radi")
        def dijeljenje_karata():
            brojac = 0
            xos = 115
            for i in range(3):
                p1inv.append(random.choice(dek))
                dek.remove(p1inv[i])
                if brojac == i:
                    gumbKarte = tk.Button(novi_prozor, text=p1inv[i],font=("Arial bold", 16), command=bačena_karta).place(x=xos,y=600,width= 180,height=250)
                    xos += 220
                    brojac += 1
            for i in range(3): 
                p2inv.append(random.choice(dek))
                dek.remove(p2inv[i])
            adut.append(random.choice(dek))
            dek.remove(adut[0])
            slikaAduta = tk.Label(novi_prozor, text=adut[0],font=("Arial bold", 16) ).place(x=525,y=350,width= 250,height=180)
            for i in range(3,5):
                p1inv.append(random.choice(dek))
                dek.remove(p1inv[i])
                if brojac == i:
                    gumbKarte = tk.Button(novi_prozor, text=p1inv[i],font=("Arial bold", 16), command=bačena_karta).place(x=xos,y=600,width= 180,height=250)
                    xos += 220
                    brojac += 1
            for i in range(3,5): 
                p2inv.append(random.choice(dek))
                dek.remove(p2inv[i])
        podijeli = tk.Button(novi_prozor, text="Podijeli karte",font=("Arial bold", 18), bg="red",fg="white",command=dijeljenje_karata).place(x=1100,y=450,width=160,height=50)
    #prozor za odabir početnih bodova tj. života
    opb = tk.Label(windowmain, text="Odaberite početan broj bodova.", fg="white",font=("Arial bold", 18))
    opb.configure(background="red")
    opb.pack(padx=10,pady=180)
    #pravila button
    def pravila():
        novi_prozor = tk.Tk()
        windowmain.destroy()      
        novi_prozor.geometry("500x500")
        novi_prozor.title("ŠNAPS")
        novi_prozor.configure(bg="green")
        def povratak_pravila():
            novi_prozor.destroy()
            tab1()
        nazad = tk.Button(novi_prozor,text="Povratak",bg="red",fg="white",font=("Arial bold", 18),command=povratak_pravila).place(x=10,y=5,width=200,height=40)
    pravila_igre = tk.Button(windowmain, text="Pravila igre",font=("Arial bold", 18), bg="red",fg="white",command=pravila).place(x=175,y=400,height=40,width=150)
    
    #gumbi s brojevima 7 i 9
    bsedam = tk.Button(windowmain,text="7",fg="white",font=("Arial bold", 30), command=kliknut7)
    bsedam.configure(background="red")
    bsedam.place(x=170,y=240,height=50,width=50)
    bdevet = tk.Button(windowmain, text="9",fg="white",font=("Arial bold", 30),command=kliknut9)
    bdevet.configure(background="red")
    bdevet.place(x=270,y=240,height=50,width=50)
    windowmain.mainloop() 

tab1()
