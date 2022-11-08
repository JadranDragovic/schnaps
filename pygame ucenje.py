from turtle import Screen
import pygame 
import random
import time
from pygame import Surface
from pyvidplayer import Video

pygame.init()

#velicine
screen = pygame.display.set_mode((1024,768))
pygame.display.set_caption("ŠNAPS")
FPS = 60
font = pygame.font.Font(None, 60)
font2 = pygame.font.Font(None, 40)
font3 = pygame.font.Font(None, 100)
font4 = pygame.font.Font(None, 80)
font5 = pygame.font.Font(None, 30)
font6 = pygame.font.Font(None, 35)
font7 = pygame.font.Font(None, 25)
text_color = (255,255,255)
#video
video = Video("Desktop\projekt\slike\cards1.mp4")
video.set_size((1024, 768))
#slike za buttone
sedam_bodova_slika = pygame.image.load("Desktop\projekt\slike\sedam.png").convert_alpha()
sedam_kliknut_slika = pygame.image.load("Desktop\projekt\slike\sedam_kliknut.png").convert_alpha()
devet_bodova_slika = pygame.image.load("Desktop\projekt\slike\devet.png").convert_alpha()
devet_kliknut_slika = pygame.image.load("Desktop\projekt\slike\devet_kliknut.png").convert_alpha()
povratak_btn_slika = pygame.image.load("Desktop\projekt\slike\povratak_btn.png").convert_alpha()
promijeni_red_btn_slika = pygame.image.load("Desktop\projekt\slike\promijeni_btn.png").convert_alpha()
statistika_slika = pygame.image.load("Desktop\projekt\slike\statistika_slika.png").convert_alpha()
igra_slika = pygame.image.load("Desktop\projekt\slike\igra_btn.png").convert_alpha()
izlaz_slika = pygame.image.load("Desktop\projekt\slike\izlaz_btn.png").convert_alpha()
kraj_runde_slika = pygame.image.load("Desktop\projekt\slike\kraj_runde_table.png").convert_alpha()
kraj_igre_tablica = pygame.image.load("Desktop\projekt\slike\kraj_igre_table.png").convert_alpha()
background_slika = pygame.image.load("Desktop\projekt\slike\pozadina.png").convert_alpha()
pozadina2_slika = pygame.image.load("Desktop\projekt\slike\pozadina2.png").convert_alpha()
mainMenu_slika = pygame.image.load("Desktop\projekt\slike\mainScreen.png").convert_alpha()
opcije1_slika = pygame.image.load("Desktop\projekt\slike\opcije1.png").convert_alpha()
opcije2_slika = pygame.image.load("Desktop\projekt\slike\opcije2.png").convert_alpha()
podijeli_karte_slika = pygame.image.load("Desktop\projekt\slike\podijeli_btn.png").convert_alpha()
kraj_slika = pygame.image.load("Desktop\projekt\slike\kraj_btn.png").convert_alpha()
zatvaranje_slika = pygame.image.load("Desktop\projekt\slike\zatvaranje_btn.png").convert_alpha()
zvanje_slika = pygame.image.load("Desktop\projekt\slike\zvanje_btn.png").convert_alpha()
nastavi_slika = pygame.image.load("Desktop\projekt\slike\continue_btn.png").convert_alpha()
vrati_se_slika = pygame.image.load("Desktop\projekt\slike\leave_btn.png").convert_alpha()
waiting_slika1 = pygame.image.load("Desktop\projekt\slike\waiting1.png").convert_alpha()
waiting_slika2 = pygame.image.load("Desktop\projekt\slike\waiting2.png").convert_alpha()
waiting_slika3 = pygame.image.load("Desktop\projekt\slike\waiting3.png").convert_alpha()
adut_tref_slika = pygame.image.load("Desktop\projekt\slike\_tref_adut.png").convert_alpha()
adut_pik_slika = pygame.image.load("Desktop\projekt\slike\_pik_adut.png").convert_alpha()
adut_herc_slika = pygame.image.load("Desktop\projekt\slike\_herc_adut.png").convert_alpha()
adut_karo_slika = pygame.image.load("Desktop\projekt\slike\_karo_adut.png").convert_alpha()
scoreboard_prvi_slika = pygame.image.load("Desktop\projekt\slike\scoreboard1.png").convert_alpha()
scoreboard_drugi_slika = pygame.image.load("Desktop\projekt\slike\scoreboard2.png").convert_alpha()

#liste
vrijednosti_karata = {"JC":2, "QC":3, "KC":4, "10C":10, "AC":11,"JS":2, "QS":3, "KS":4, "10S":10, "AS":11,"JD":2, "QD":3, "KD":4, "10D":10, "AD":11,"JH":2, "QH":3, "KH":4, "10H":10, "AH":11}
dek = ["JC", "QC", "KC", "10C", "AC","JS","QS","KS","10S","AS","JD", "QD", "KD", "10D", "AD","JH", "QH", "KH", "10H", "AH"]
slike_karata = {"10C":"10C.png",
				"10D":"10D.png",
				"10H":"10H.png",
				"10S":"10S.png",
				"AC":"AC.png",
				"AD":"AD.png",
				"AH":"AH.png",
				"AS":"AS.png",
				"JC":"JC.png",
				"JD":"JD.png",
				"JH":"JH.png",
				"JS":"JS.png",
				"KC":"KC.png",
				"KD":"KD.png",
				"KH":"KH.png",
				"KS":"KS.png",
				"QC":"QC.png",
				"QD":"QD.png",
				"QH":"QH.png",
				"QS":"QS.png"}
p1inv=[]
p2inv = []
adut = []
p1bodovi_runda = []
p2bodovi_runda = []
usporedba = [] #unutar ove liste se usporeduju dvije bacene karte od igraca 1 i 2
karte_crtanje = [] #unutar ove liste se nalaza bacene karte
usporedba_red_bacanja1 = []
usporedba_red_bacanja2 = []
bacena_kartap1 = []
bacena_kartap2 = []
zvanje_baceno = []
moguca_zvanja = []
bodoviPoRundi_stat1 = []
bodoviPoRundi_stat2 = []

def dijeljenje_karata():#podijeli random karte igračima
	for i in range(3): 
		p1inv.append(random.choice(dek)) #dodaju se 3 random karte u inv od igraca 1 i iste karte se brisu iz deka
		dek.remove(p1inv[i])
	for i in range(3): 
		p2inv.append(random.choice(dek)) #dodaju se 3 random karte u inv od igraca 2 i iste karte se brisu iz deka
		dek.remove(p2inv[i])
	adut.append(random.choice(dek))
	for i in range(3,5): 
		p1inv.append(random.choice(dek)) #dodaju se 2 random karte u inv od igraca 1 i iste karte se brisu iz deka
		dek.remove(p1inv[i])
	for i in range(3,5): 
		p2inv.append(random.choice(dek)) #dodaju se 2 random karte u inv od igraca 2 i iste karte se brisu iz deka
		dek.remove(p2inv[i])

def draw_text(text,font,text_col,x,y):#služi za prikazivanje bilo kakavog teksta na ekranu, funkcija za argumente prima text, font i velicinu texta, boju teksta i koordinate gdje ce se text prikazivati
	img = font.render(text,True,text_col)
	screen.blit(img,(x,y))

class Button():#proizvodim vlastitu klasu za gumb 
	hovered = False
	def __init__(self, x, y, image,scale):
		
		self.image = image
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale))) #originalna sirina i visina slike se mnoze sa scaleom i tako se postavljaju nova sirina i visina slike 
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y) #postavlja sliku na upisane koordinate
		self.clicked = False

	def draw(self,):#sluzi za prikazivanje gumba na ekranu i provjeru je li gumb kliknut	
		action = False #varijabla koja sluzi za provjeru je li gumb kliknut
			#dobivamo mouse position
		pos = pygame.mouse.get_pos()
		if self.rect.collidepoint(pos): #provjerava prolazi li kursor misa preko gumba
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:#provjerava je li pritisnut lijevi klik misa na gumbu
				self.clicked = True
				action = True
		if pygame.mouse.get_pressed()[0] == 0:#prikazuje gumb na glavni window (sliku gumba na zadane koordinate)
			self.clicked = False
			
		screen.blit(self.image,(self.rect.x,self.rect.y))
		return action

#buttoni
btn_zavrsi_bacanje = Button(460,80,promijeni_red_btn_slika,0.5)

#varijable
menu_state ="main" #pomaže za mijenjanje prozora
karte_state ="ne_prikaz" #sluzi za prikaz karata na ekranu
bacena_karta_state ="ne" #varijabla koja se mijenja ovisno o tome je li karta bacena za igraca 1
bacena_karta_state2 ="ne" #varijabla koja se mijenja ovisno o tome je li karta bacena za igraca 2
promjena_reda = 0 #varijabla koja sluzi za pracenje promjene reda bacanja 
btn_podijeli_karte_crtaj = 0 #provjerava je li kliknuta karta tj. gumb koji dijeli karte
ogranici_bacanje1 = 0 #varijabla koja sluzi za ogranicavanje bacanja karata tj. da igrac ne moze baciti vise od jedne karte odjednom za igraca 1
ogranici_bacanje2 = 1 #varijabla koja sluzi za ogranicavanje bacanja karata tj. da igrac ne moze baciti vise od jedne karte odjednom za igraca 2
zavrsi_bacanje_kliknut = 0 #sluzi za provjeru je li kliknut gumb zavrsi bacanje
p1pobjeda = 0 #ukupne pobjede igraca 1 od kad se upali igra
p2pobjeda = 0 #ukupne pobjede igraca 2 od kad se upali igra
brojac_vrsteP1 = 0 #broji koliko karata ima igrac 1 koje su iste vrste kao bacena karta igraca 2
brojac_vrsteP2 = 0 #broji koliko karata ima igrac 2 koje su iste vrste kao bacena karta igraca 1
zatvara = "0" #provjerava koji je igrac odlucio pozvati zatvaranje igre (1 prvi igrac, 2 drugi)
zatvaranje_tekst = "" #prikaz teksta "zatvaranje"
stih = 0 #sluzi za brojanje odigranih stihova
brojac_ibera = 0 #provjerava je li u inventoriju igrača 1 ima karta koja je iste vrste i je li veća od bačene karte 2. igrača 
brojac_ibera2 = 0 #provjerava je li u inventoriju igrača 2 ima karta koja je iste vrste i je li veća od bačene karte 1. igrača 
ogranici_zavrsi = 1 #broji koliko je puta kliknuto "zavrsi bacanje" kako se ne bi moglo stalno klikati bez da je igrac odigrao potez
ciji_red = 0 #sluzi za zvanje i zatvaranje tj. broji tko je pobijedio stih 
zvanje_provjera = 0 #za svaku kartu u inv provjerava moze li se zvati
prihvati_zvanje = 0 #prikazuje gumb za zvanje ako je zvanje moguće (ako je varijabla 1)
ogranici_bodovanje = 0 #ogranicuje bodovanje za igrača nakon završene runde (ako je 1 onda ne da bodovati)
p1runda_stat = 0 #broji pobijeđene runde 1. igrača za statistiku
p2runda_stat = 0 #broji pobijeđene runde 2. igrača za statistiku
p1stih_stat = 0 #broji nošene štihove 1. igrača za statistiku
p2stih_stat = 0	#broji nošene štihove 2. igrača za statistiku
p1bodProsjek_stat = 0 #računa prosječan broj bodova 1. igrača
p2bodProsjek_stat = 0 #računa prosječan broj bodova 2. igrača
makni_sedam = 0 #makne sliku 7 i zamijeni s kliknutom slikom 7
makni_devet = 0 #makne sliku 9 i zamijeni s kliknutom slikom 9
ogranici_scoreboard = "ne" #ogranaicuje prikaz znacenja brojeva u scoreboardu 
prvi_nosi = 0 #pomaže da se isprinta tekst da 1. igrac nosi stih
drugi_nosi = 0 #pomaže da se isprinta tekst da 2. igrac nosi stih
kraj_state = "ne" #provjerava je li runda gotova, ako je, ne dopušta mijenjanje reda i stvara gumb za kraj
brojac = 0

def igra():#window u kojemu se igra snaps
	run = True
	while run:
		clock = pygame.time.Clock()
		clock.tick(FPS) #odreduje u koliko fps igra radi
		for event in pygame.event.get():
			if event.type == pygame.QUIT: #sluzi za gasenje prozora
				run = False
		global karte_state #global sluzi kako bi se varijable koje postoje od prije mogle prepoznati unutar novog defa/
		global promjena_reda
		global p1bodovi_runda
		global p2bodovi_runda
		global ogranici_izvlacenje1
		global ogranici_izvlacenje2
		global bacena_karta_state
		global bacena_karta_state2
		global btn_podijeli_karte_crtaj
		global ogranici_bacanje1
		global ogranici_bacanje2
		global zavrsi_bacanje_kliknut
		global menu_state
		global p1bodovi
		global p2bodovi
		global stari_bodovi1
		global stari_bodovi2
		global brojac_vrsteP1
		global brojac_vrsteP2
		global zatvara
		global zatvaranje_tekst
		global brojac_ibera
		global brojac_ibera2
		global stih
		global ogranici_zavrsi
		global ciji_red
		global moguca_zvanja
		global zvanje_provjera
		global prihvati_zvanje
		global zvanje_baceno
		global p1stih_stat
		global p2stih_stat
		global ogranici_scoreboard
		global prvi_nosi
		global drugi_nosi
		global kraj_state
		global ogranici_zbroj
		global brojac
		screen.blit(background_slika, (0,0))

		#dijeljenje karti
		if len(p1inv) == 0 and len(dek) != 0:
			btn_podijeli_karte = Button(448,245,podijeli_karte_slika,0.7)
			if btn_podijeli_karte.draw() == True:#ako se klikne taj gumb onda se podijeli karte s pomocu funkcije dijeljenje_karata
				while btn_podijeli_karte_crtaj % 2 == 0:
					dijeljenje_karata()
					karte_state = "prikaz" #mijenja varijablu kako bi se podijeljene karte prikazivale na ekranu
					btn_podijeli_karte_crtaj += 1


		if karte_state == "prikaz":
			#prikaz karata
			if len(adut) != 0: #prikaz boje aduta na ekranu
				if adut[0][-1] == "H":
					adut_slika = Button(25,-15,adut_herc_slika, 0.7).draw()
				if adut[0][-1] == "S":
					adut_slika = Button(25,-15,adut_pik_slika, 0.7).draw()
				if adut[0][-1] == "D":
					adut_slika = Button(25,-15,adut_karo_slika, 0.7).draw()
				if adut[0][-1] == "C":
					adut_slika = Button(25,-15,adut_tref_slika, 0.7).draw()
			#prikaz informacija u scoreboardu
			draw_text(f"{igrač1ime}",font6,text_color,814,22)
			draw_text(f"{igrač2ime}",font6,text_color,920,22)
			draw_text(f"{p1bodovi}",font,text_color,865,72)
			draw_text(f"{p2bodovi}",font,text_color,940,72)
			if sum(p1bodovi_runda) < 10: #ako je jednoznamenkasti broj, stavi ga u sredinu
				draw_text(f"{sum(p1bodovi_runda)}",font,text_color,865,128)
			else: #ako nije, stavi ga u lijevo da izgleda ljepše
				draw_text(f"{sum(p1bodovi_runda)}",font,text_color,855,128)
			if sum(p2bodovi_runda) < 10:
				draw_text(f"{sum(p2bodovi_runda)}",font,text_color,940,128)
			else:
				draw_text(f"{sum(p2bodovi_runda)}",font,text_color,930,128)
				
			if ciji_red == 0:
				draw_text(f"Klikni na tablicu za vrijednosti",font7,text_color,770,235)

			if len(usporedba) != 2: #ako je istina oba igraca nisu bacila kartu i stih se nastavlja
				if promjena_reda == 0: #ako je promjena reda 0 onda je 1. igrac na redu
					scoreboard_btn = Button(805,0,scoreboard_prvi_slika, 1.1)
					if scoreboard_btn.draw() == True:
						if ogranici_scoreboard == "ne":
							ogranici_scoreboard = "da"
						else:
							ogranici_scoreboard = "ne"
					if ogranici_scoreboard == "da":
						draw_text(f"Ukupni bodovi ->",font6,text_color,630,72)
						draw_text(f"Bodovi runde  ->",font6,text_color,630,128)
						draw_text(f"Tko je na redu->",font6,text_color,630,185)
					xos = 95
					for i in p1inv:#prolazi kroz p1inv i crta sve karte na stol
						karta = Button(xos,500,pygame.image.load("Desktop\projekt\karte\\"+ slike_karata[i]).convert_alpha(),0.18).draw()
						xos += 180
						if karta == True:#provjerava je li karta kliknuta
							if brojac == 1:
								if i == zvanje_baceno[-1] or i == zvanje_baceno[-2]:
									while ogranici_bacanje1 == 0:#karta se moze baciti,prikazuje se na sredini stola, dodaje se u usporedbu kako bi se kasnije mogla usporediti s kartom od 2. igraca, bacena karta se izbacuje iz p1inv, i zabranjuje bacanje jos jedna karte
										karte_crtanje.append(i)
										bacena_kartap1.append(i)
										bacena_karta_state ="da"
										usporedba.append(i)
										p1inv.remove(i)
										ogranici_bacanje1 =1
										ogranici_bacanje2 =1
										ogranici_zavrsi = 0
										brojac = 0
								else:
									draw_text(f"MORAŠ BACITI JEDNU OD ZVANIH KARATA",font2,text_color,250,120)
									pygame.display.update()
									time.sleep(2)
	
							if len(dek) != 0 and brojac == 0: #ako u deku ima karata onda ne vrijede pravila poštovanja i iberovanja
								while ogranici_bacanje1 == 0:#karta se moze baciti,prikazuje se na sredini stola, dodaje se u usporedbu kako bi se kasnije mogla usporediti s kartom od 2. igraca, bacena karta se izbacuje iz p1inv, i zabranjuje bacanje jos jedna karte
									karte_crtanje.append(i)
									bacena_kartap1.append(i)
									bacena_karta_state ="da"
									usporedba.append(i)
									p1inv.remove(i)
									ogranici_bacanje1 =1
									ogranici_bacanje2 =1
									ogranici_zavrsi = 0					
							if len(dek) == 0 and brojac == 0: #ako je dek prazan onda se moraju pratiti pravila poštovanja i iberovanja
								if len(usporedba) != 0: #ako je 1. igrač drugi na redu onda mora pratiti pravila
									for m in p1inv: #prolazi kroz inventori prvog igrača 
										if m[-1] == bacena_kartap2[-1][-1]: #provjerava je li vrsta bačene karte drugog igrača jednaka vrsti karti u njegovom inventoriju
											brojac_vrsteP1 = 1
										if brojac_vrsteP1 == 0: #ako se brojač nije promijenio
											if m[-1] == adut[0][-1]: #provjerava je li ima adut ako nema iste vrste
												brojac_vrsteP1 = 2 
									if brojac_vrsteP1 == 0:
										for k in p1inv:
											if k[-1] != bacena_kartap2[-1][-1] and k[-1] != adut[0][-1]: #ako nema adut ni vrstu
												brojac_vrsteP1 = 3
									for h in p1inv: #prolazi kroz inventori prvog igrača
										if h[-1] == bacena_kartap2[-1][-1] and vrijednosti_karata[h]>vrijednosti_karata[bacena_kartap2[-1]]: #provjerava je li u inventoriju ima karta koja je iste vrste i veća od bačene karte drugog igrača
											brojac_ibera = 1 
									if brojac_vrsteP1 == 1: #ako ima iste vrste
										brojac_vrsteP1 = 0
										if i[-1] == bacena_kartap2[-1][-1]: #ako je bačena karta prvog igrača jednaka vrsti bačene karte drugog igrača
											if brojac_ibera == 1: #ako ima kartu koja je veće vrijednosti
												brojac_ibera = 0
												if i[-1] == bacena_kartap2[-1][-1] and vrijednosti_karata[i]>vrijednosti_karata[bacena_kartap2[-1]]: #provjerava je li bačena karta iste vrste i je li veća ako ju ima
													while ogranici_bacanje1 == 0:
														karte_crtanje.append(i)
														bacena_kartap1.append(i)
														bacena_karta_state ="da"
														usporedba.append(i)
														p1inv.remove(i)
														ogranici_bacanje1 =1
														ogranici_bacanje2 =1
														ogranici_zavrsi = 0
												else:
													draw_text("MORAŠ PRATITI PRAVILO IBEROVANJA",font2,(255,255,255),250,150) #sve dok se ne klikne točna karta će se printat ovaj tekst
													pygame.display.update()
													time.sleep(2)
											else: #ako nema kartu koja je veća
												if i[-1] == bacena_kartap2[-1][-1]: #je li bačena karta igrača jedna iste vrste kao bačena karta drugog igrača
													while ogranici_bacanje1 == 0: 
														karte_crtanje.append(i)
														bacena_kartap1.append(i)
														bacena_karta_state ="da"
														usporedba.append(i)
														p1inv.remove(i)
														ogranici_bacanje1 =1
														ogranici_bacanje2 =1
														ogranici_zavrsi = 0
															
												else: #sve dok se ne klikne točna karta će se printat ovaj tekst
													draw_text("MORAŠ PRATITI PRAVILO POŠTOVANJA",font2,(255,255,255),250,150)
													pygame.display.update()
													time.sleep(2)
										else: #sve dok se ne klikne točna karta će se printat ovaj tekst
											draw_text("MORAŠ PRATITI PRAVILO POŠTOVANJA",font2,(255,255,255),250,150)
											pygame.display.update()
											time.sleep(2)
									if brojac_vrsteP1 == 2: #ako nema kartu iste vrste onda provjerava za adut
										brojac_vrsteP1 = 0
										if i[-1] == adut[0][-1]: #ako je vrsta bačene karte jednaka vrsti aduta
											while ogranici_bacanje1 == 0:
												karte_crtanje.append(i)
												bacena_kartap1.append(i)
												bacena_karta_state ="da"
												usporedba.append(i)
												p1inv.remove(i)
												ogranici_bacanje1 =1
												ogranici_bacanje2 =1
												ogranici_zavrsi = 0
												
										else: #sve dok se ne klikne točna karta će se printat ovaj tekst
											draw_text("MORAŠ PRATITI PRAVILO POŠTOVANJA",font2,(255,255,255),250,150)
											pygame.display.update()
											time.sleep(2)
									if brojac_vrsteP1 == 3: #ako nema ni vrstu ni adut
										brojac_vrsteP1 = 0
										while ogranici_bacanje1 == 0:
											karte_crtanje.append(i)
											bacena_kartap1.append(i)
											bacena_karta_state ="da"
											usporedba.append(i)
											p1inv.remove(i)
											ogranici_bacanje1 =1
											ogranici_bacanje2 =1
											ogranici_zavrsi = 0
								if len(usporedba)  == 0: #ako je 1. igrač prvi na redu onda ne mora pratiti pravila 
									while ogranici_bacanje1 == 0:
										karte_crtanje.append(i)
										bacena_kartap1.append(i)
										bacena_karta_state ="da"
										usporedba.append(i)
										p1inv.remove(i)
										ogranici_bacanje1 =1
										ogranici_bacanje2 =1
										ogranici_zavrsi = 0
									
				if len(karte_crtanje) == 1 or len(karte_crtanje) == 2:#sluzi za prikaz bacene karte na sredini stola
					if bacena_karta_state =="da":
						bacena_karta = Button(455,250,pygame.image.load("Desktop\projekt\karte\\"+ slike_karata[karte_crtanje[-1]]).convert_alpha(),0.18).draw()
				
				if promjena_reda == 1:#ako je promjena reda 1 onda je 2. igrac na redu
					scoreboard_btn = Button(805,0,scoreboard_drugi_slika, 1.1)
					if scoreboard_btn.draw() == True:
						if ogranici_scoreboard == "ne":
							ogranici_scoreboard = "da"
						else:
							ogranici_scoreboard = "ne"
					if ogranici_scoreboard == "da":
						draw_text(f"Ukupni bodovi ->",font6,text_color,630,72)
						draw_text(f"Bodovi runde  ->",font6,text_color,630,128)
						draw_text(f"Tko je na redu->",font6,text_color,630,185)
					xos = 95
					for t in p2inv:#prolazi kroz p2inv i crta sve karte na stol
						karta = Button(xos,500,pygame.image.load("Desktop\projekt\karte\\"+ slike_karata[t]).convert_alpha(),0.18).draw()
						xos += 180
						if karta == True:#provjerava je li karta kliknuta
							if brojac == 1:
								if t == zvanje_baceno[-1] or t == zvanje_baceno[-2]:
									while ogranici_bacanje2 == 1:#karta se moze baciti,prikazuje se na sredini stola, dodaje se u usporedbu kako bi se kasnije mogla usporediti s kartom od 2. igraca, bacena karta se izbacuje iz p1inv, i zabranjuje bacanje jos jedna karte
										karte_crtanje.append(t)
										bacena_kartap2.append(t)
										bacena_karta_state2 ="da"
										usporedba.append(t)
										p2inv.remove(t)
										ogranici_bacanje2 = 0
										ogranici_bacanje1 = 0
										ogranici_zavrsi = 0	
										brojac = 0
								else:
									draw_text(f"MORAŠ BACITI JEDNU OD ZVANIH KARATA",font2,text_color,250,120)
									pygame.display.update()
									time.sleep(2)

							if len(dek) != 0 and brojac == 0: #ako u deku ima karata onda ne vrijede pravila poštovanja i iberovanja
								while ogranici_bacanje2 == 1:#karta se moze baciti,prikazuje se na sredini stola, dodaje se u usporedbu kako bi se kasnije mogla usporediti s kartom od 1. igraca, bacena karta se izbacuje iz p2inv, i zabranjuje bacanje jos jedna karte
									karte_crtanje.append(t)
									bacena_kartap2.append(t)
									bacena_karta_state2 ="da"
									usporedba.append(t)
									p2inv.remove(t)
									ogranici_bacanje2 = 0
									ogranici_bacanje1 = 0
									ogranici_zavrsi = 0					
							if len(dek) == 0 and brojac == 0: #ako je dek prazan moraju se pratiti pravilo poštovanja i iberovanja
								if len(usporedba) != 0: #ako je drugi igrač drugi na redu
									for l in p2inv: #prolazi kroz inventori drugog igrača
										if l[-1] == bacena_kartap1[-1][-1]: #ako u inventoriju ima kartu iste vrste kao bačena karta prvog igrača
											brojac_vrsteP2 = 1
										if brojac_vrsteP2 == 0: #ako nema iste vrste
											if l[-1] == adut[0][-1]: #provjerava je li ima adut
												brojac_vrsteP2 = 2
									if brojac_vrsteP2 == 0: #ako nema ni jedno ni drugi
										for s in p2inv: #prolazi kroz inventori drugog igrača
											if s[-1] != bacena_kartap1[-1][-1] and s[-1] != adut[0][-1]:#radi provjeru
												brojac_vrsteP2 = 3
									for z in p2inv:#prolazi kroz inventory
										if z[-1] == bacena_kartap1[-1][-1] and vrijednosti_karata[z]>vrijednosti_karata[bacena_kartap1[-1]]:#provjerava je li u inventoriju drugog igrača ima karta koja je iste vrste i veća od bačene karte prvog igrača
											brojac_ibera2 = 1
									if brojac_vrsteP2 == 1: #provjera je li iste vrste
										brojac_vrsteP2 = 0
										if t[-1] == bacena_kartap1[-1][-1]: #ako je bačena karta drugog igrača iste vrste kao bačena karta prvog
											if brojac_ibera2 == 1: #ako ima kartu koja je veće vrijednosti
												brojac_ibera2 = 0
												if t[-1] == bacena_kartap1[-1][-1] and vrijednosti_karata[t]>vrijednosti_karata[bacena_kartap1[-1]]: #provjerava je li bačena karta iste vrste i je li veća ako ju ima
													while ogranici_bacanje2 == 1:
														bacena_kartap2.append(t)
														karte_crtanje.append(t)
														bacena_karta_state2 ="da"
														usporedba.append(t)
														p2inv.remove(t)
														ogranici_bacanje2 = 0
														ogranici_bacanje1 = 0
														ogranici_zavrsi = 0
														
												else: #sve dok se ne klikne točna karta će se printat ovaj tekst
													draw_text("MORAŠ PRATITI PRAVILO IBEROVANJA",font2,(255,255,255),250,150)
													pygame.display.update()
													time.sleep(2)
											else: #ako nema kartu veće vrijednosti
												if t[-1] == bacena_kartap1[-1][-1]: #provjerava je li bačena karta iste vrste kao od prvog igrača
													while ogranici_bacanje2 == 1:
														bacena_kartap2.append(t)
														karte_crtanje.append(t)
														bacena_karta_state2 ="da"
														usporedba.append(t)
														p2inv.remove(t)
														ogranici_bacanje2 = 0
														ogranici_bacanje1 = 0
														ogranici_zavrsi = 0
															
												else:#sve dok se ne klikne točna karta će se printat ovaj tekst
													draw_text("MORAŠ PRATITI PRAVILO POŠTOVANJA",font2,(255,255,255),250,150)
													screen.display.update()
													time.sleep(2)
										else: #sve dok se ne klikne točna karta će se printat ovaj tekst
											draw_text("MORAŠ PRATITI PRAVILO POŠTOVANJA",font2,(255,255,255),250,150)
											pygame.display.update()
											time.sleep(2)
									if brojac_vrsteP2 == 2: #ako nema iste vrste a ima adut
										brojac_vrsteP2 = 0
										if t[-1] == adut[0][-1]: #je li bačena karta jednaka adutu
											while ogranici_bacanje2 == 1:
												bacena_kartap2.append(t)
												karte_crtanje.append(t)
												bacena_karta_state2 ="da"
												usporedba.append(t)
												p2inv.remove(t)
												ogranici_bacanje2 = 0
												ogranici_bacanje1 = 0
												ogranici_zavrsi = 0
												
										else: #sve dok se ne klikne točna karta će se printat ovaj tekst
											draw_text("MORAŠ PRATITI PRAVILO POŠTOVANJA",font2,(255,255,255),250,150)
											pygame.display.update()
											time.sleep(2)

									if brojac_vrsteP2 == 3: #ako nema ni vrstu ni adut
										brojac_vrsteP2 = 0
										while ogranici_bacanje2 == 1:
											bacena_kartap2.append(t)
											karte_crtanje.append(t)
											bacena_karta_state2 ="da"
											usporedba.append(t)
											p2inv.remove(t)
											ogranici_bacanje2 = 0
											ogranici_bacanje1 = 0
											ogranici_zavrsi = 0
								if len(usporedba)  == 0: #ako je drugi igrač prvi na redu
									while ogranici_bacanje2 == 1:
										bacena_kartap2.append(t)
										karte_crtanje.append(t)
										bacena_karta_state2 ="da"
										usporedba.append(t)
										p2inv.remove(t)
										ogranici_bacanje2 = 0
										ogranici_bacanje1 = 0
										ogranici_zavrsi = 0
								
				if len(karte_crtanje) == 1 or len(karte_crtanje) == 2:#sluzi za prikaz bacene karte na sredini stola
					if bacena_karta_state2 =="da":
						bacena_karta = Button(455,250,pygame.image.load("Desktop\projekt\karte\\"+ slike_karata[karte_crtanje[-1]]).convert_alpha(),0.18).draw()
				
				if kraj_state == "da":
					ogranici_zavrsi = 1
					kraj_btn = Button(460,80,kraj_slika,0.5)
					if kraj_btn.draw() == True:
						kraj_runde()
				
				if ogranici_zavrsi == 0:
					if btn_zavrsi_bacanje.draw() == True:#ako se klikne gumb zavrsi bacanje promijeni se graficki prikaz inventorya igraca
						ogranici_zavrsi = 1
						ciji_red +=1
						zvanje_provjera = 0
						prihvati_zvanje = 0
						moguca_zvanja.clear()
						prvi_nosi = 0
						drugi_nosi = 0

						if len(karte_crtanje) == 2:
							karte_crtanje.clear()
						else:
							pass
						if stih == 1:#automatsko dijeljenje karata nakon svakog stiha tj. broji je li stih gotov i ako je svakom igracu se doda jedna karta iz deka
							if len(dek) > 0:
								p1inv.append(random.choice(dek))
								dek.remove(p1inv[-1])
								p2inv.append(random.choice(dek))
								dek.remove(p2inv[-1])
								stih = 0
							else:
								pass
						else:
							pass

						if zavrsi_bacanje_kliknut == 0:#samo sluzi za prvu promjenu reda kasnije je nebitan dio koda, prikazuje se waiting screen preko cijelog ekrana kako bi igraci stigli zamijeniti mjesta i kako ne bi vidjeli karte od protivnika
							promjena_reda =1
							screen.blit(waiting_slika1, (0,0))
							draw_text(f"{igrač2ime} MOŽE IGRATI ZA",font2,(0,0,0),370,430)
							pygame.display.update()
							time.sleep(1)
							screen.blit(waiting_slika2, (0,0))
							draw_text(f"{igrač2ime} MOŽE IGRATI ZA",font2,(0,0,0),370,430)
							pygame.display.update()
							time.sleep(1)
							screen.blit(waiting_slika3, (0,0))
							draw_text(f"{igrač2ime} MOŽE IGRATI ZA",font2,(0,0,0),370,430)
							pygame.display.update()
							time.sleep(1)
							zavrsi_bacanje_kliknut = 1
						if zavrsi_bacanje_kliknut == 2:#sluzi za promjenu reda igraca tijekom cijele igre tj. nakon prvog stiha
							if usporedba_red_bacanja1[-1] == "0":#prvi igrac je dobio stih pa on mora biti na redu (ako je 0 prvi igrac je dobio stih)
								promjena_reda = 0
								screen.blit(waiting_slika1, (0,0))
								draw_text(f"{igrač1ime} MOŽE IGRATI ZA",font2,(0,0,0),370,430)
								pygame.display.update()
								time.sleep(1)
								screen.blit(waiting_slika2, (0,0))
								draw_text(f"{igrač1ime} MOŽE IGRATI ZA",font2,(0,0,0),370,430)
								pygame.display.update()
								time.sleep(1)
								screen.blit(waiting_slika3, (0,0))
								draw_text(f"{igrač1ime} MOŽE IGRATI ZA",font2,(0,0,0),370,430)
								pygame.display.update()
								time.sleep(1)
								ogranici_bacanje1 = 0#resetiraju se ogranicenja za bacanje
								ogranici_bacanje2 = 1
								usporedba_red_bacanja1.append("1")#dodaje se 1 na kraj lista kako igrac 1 ne bi vise mogao igrati i da igrac 2 bude na redu
								usporedba_red_bacanja2.append("1")
							elif usporedba_red_bacanja2[-1] == "1":#drugi igrac je dobio stih pa on mora biti na redu (ako je 1 drugi igrac je dobio stih)
								promjena_reda = 1
								screen.blit(waiting_slika1, (0,0))
								draw_text(f"{igrač2ime} MOŽE IGRATI ZA",font2,(0,0,0),370,430)
								pygame.display.update()
								time.sleep(1)
								screen.blit(waiting_slika2, (0,0))
								draw_text(f"{igrač2ime} MOŽE IGRATI ZA",font2,(0,0,0),370,430)
								pygame.display.update()
								time.sleep(1)
								screen.blit(waiting_slika3, (0,0))
								draw_text(f"{igrač2ime} MOŽE IGRATI ZA",font2,(0,0,0),370,430)
								pygame.display.update()
								time.sleep(1)
								ogranici_bacanje1 = 0#resetiraju se ogranicenja za bacanje
								ogranici_bacanje2 = 1
								usporedba_red_bacanja2.append("0")#dodaje se 0 na kraj lista kako igrac 2 ne bi vise mogao igrati i da igrac 1 bude na redu
								usporedba_red_bacanja1.append("0")

			elif len(usporedba) == 2:#ako je istina oba igraca su bacila kartu i stih se mora zavrsiti
				if karte_crtanje[-2] ==  bacena_kartap1[-1] and karte_crtanje[-1] == bacena_kartap2[-1]:#sluzi za to da znamo da je 1. igrac bacao prvi
					if usporedba[0][-1] == usporedba[1][-1]:#provjerava jesu li obje bacene karte iste vrste
						if vrijednosti_karata[usporedba[0]]>vrijednosti_karata[usporedba[1]]:#ako je karta od igraca 1 jaca od karte od igraca 2 onda igrac jedan dobiva bodove
							p1bodovi_runda.append(vrijednosti_karata[usporedba[0]]+vrijednosti_karata[usporedba[1]])
							p1stih_stat += 1
							stih = 1
							zavrsi_bacanje_kliknut = 2
							usporedba_red_bacanja1.append("0")
							usporedba_red_bacanja2.append("0")
							usporedba.clear()
							prvi_nosi = 1
						elif vrijednosti_karata[usporedba[0]]<vrijednosti_karata[usporedba[1]]:#ako je karta od igraca 1 slabija od karte od igraca 2 onda igrac dva dobiva bodove
							p2bodovi_runda.append(vrijednosti_karata[usporedba[0]]+vrijednosti_karata[usporedba[1]])
							p2stih_stat += 1
							stih = 1
							zavrsi_bacanje_kliknut = 2
							usporedba_red_bacanja2.append("1")
							usporedba_red_bacanja1.append("1")
							usporedba.clear()
							drugi_nosi = 1
						else:
							p1bodovi_runda.append(vrijednosti_karata[usporedba[0]]+vrijednosti_karata[usporedba[1]])
							p1stih_stat += 1
							stih = 1
							zavrsi_bacanje_kliknut = 2
							usporedba_red_bacanja1.append("0")
							usporedba_red_bacanja2.append("0")
							usporedba.clear()
							prvi_nosi = 1
					elif usporedba[0][-1] != usporedba[1][-1]:#provjerava jesu li obje bacene karte razlicite vrste
						if usporedba[1][-1] == adut[0][-1] and usporedba[0][-1] != adut[0][-1]:#provjerava je li karta 2. igrac adut, a karta 1. nije adut
							p2bodovi_runda.append(vrijednosti_karata[usporedba[0]]+vrijednosti_karata[usporedba[1]])#ako je 2. igrac imao aduta, a prvi nije onda 2. svejedno nosi stih tj. pisu mu se bodovi
							p2stih_stat += 1
							stih = 1
							zavrsi_bacanje_kliknut = 2
							usporedba_red_bacanja2.append("1")
							usporedba_red_bacanja1.append("1")
							usporedba.clear()
							drugi_nosi = 1
						elif usporedba[1][-1] == adut[0][-1] and usporedba[0][-1] == adut[0][-1]:#provjerava je li karta 2. igrac adut i karta 1. adut
							if vrijednosti_karata[usporedba[0]]>vrijednosti_karata[usporedba[1]]:#ako je adut od igraca 1 veci on dobiva bodove
								p1bodovi_runda.append(vrijednosti_karata[usporedba[0]]+vrijednosti_karata[usporedba[1]])
								p1stih_stat += 1
								stih = 1
								zavrsi_bacanje_kliknut = 2
								usporedba_red_bacanja1.append("0")
								usporedba_red_bacanja2.append("0")
								usporedba.clear()
								prvi_nosi = 1
							elif vrijednosti_karata[usporedba[0]]<vrijednosti_karata[usporedba[1]]:#ako je adut od igraca 2 veci on dobiva bodove
								p2bodovi_runda.append(vrijednosti_karata[usporedba[0]]+vrijednosti_karata[usporedba[1]])
								p2stih_stat += 1
								stih = 1
								zavrsi_bacanje_kliknut = 2
								usporedba_red_bacanja2.append("1")
								usporedba_red_bacanja1.append("1")
								usporedba.clear()
								drugi_nosi = 1
						else:#ako oba igraca imaju u potpunosti razalicite vrste karata onda igrac 1 dobiva bodove jer 2. igrac nije pratio pravilo postovanja
							p1bodovi_runda.append(vrijednosti_karata[usporedba[0]]+vrijednosti_karata[usporedba[1]])
							p1stih_stat += 1
							stih = 1
							zavrsi_bacanje_kliknut = 2
							usporedba_red_bacanja1.append("0")
							usporedba_red_bacanja2.append("0")
							usporedba.clear()
							prvi_nosi = 1

				if karte_crtanje[-1] == bacena_kartap1[-1] and karte_crtanje[-2] == bacena_kartap2[-1]:#sluzi za to da znamo da je 2. igrac bacao prvi
					if usporedba[0][-1] == usporedba[1][-1]:#provjerava jesu li obje bacene karte iste vrste
						if vrijednosti_karata[usporedba[0]]>vrijednosti_karata[usporedba[1]]:#ako je karta od igraca 1 slabija od karte od igraca 2 onda igrac dva dobiva bodove
							p2bodovi_runda.append(vrijednosti_karata[usporedba[0]]+vrijednosti_karata[usporedba[1]])
							p2stih_stat += 1
							stih = 1
							zavrsi_bacanje_kliknut = 2
							usporedba_red_bacanja2.append("1")
							usporedba_red_bacanja1.append("1")
							usporedba.clear()
							drugi_nosi = 1
						elif vrijednosti_karata[usporedba[0]]<vrijednosti_karata[usporedba[1]]:#ako je karta od igraca 1 jaca od karte od igraca 2 onda igrac jedan dobiva bodove
							p1bodovi_runda.append(vrijednosti_karata[usporedba[0]]+vrijednosti_karata[usporedba[1]])
							p1stih_stat += 1
							stih = 1
							zavrsi_bacanje_kliknut = 2
							usporedba_red_bacanja1.append("0")
							usporedba_red_bacanja2.append("0")
							usporedba.clear()
							prvi_nosi = 1
						else:
							p2bodovi_runda.append(vrijednosti_karata[usporedba[0]]+vrijednosti_karata[usporedba[1]])
							p2stih_stat += 1
							stih = 1
							zavrsi_bacanje_kliknut = 2
							usporedba_red_bacanja1.append("1")
							usporedba_red_bacanja2.append("1")
							usporedba.clear()
							drugi_nosi = 1
					elif usporedba[0][-1] != usporedba[1][-1]:#provjerava jesu li obje bacene karte razlicite vrste
						if usporedba[1][-1] == adut[0][-1] and usporedba[0][-1] != adut[0][-1]:#provjerava je li karta od 1. igraca adut, a od drugog nije adut
							p1bodovi_runda.append(vrijednosti_karata[usporedba[0]]+vrijednosti_karata[usporedba[1]])#prvi igrac dobiva bodove jer je imao aduta
							p1stih_stat += 1
							stih = 1
							zavrsi_bacanje_kliknut = 2
							usporedba_red_bacanja2.append("0")
							usporedba_red_bacanja1.append("0")
							usporedba.clear()
							prvi_nosi = 1
						elif usporedba[1][-1] == adut[0][-1] and usporedba[0][-1] == adut[0][-1]:#provjerava jesu li obje karte adut
							if vrijednosti_karata[usporedba[0]]>vrijednosti_karata[usporedba[1]]:#ako je adut od igraca 2 jaci od aduta od igraca 1, igrac 2 dobiva bodove
								p2bodovi_runda.append(vrijednosti_karata[usporedba[0]]+vrijednosti_karata[usporedba[1]])
								p2stih_stat += 1
								stih = 1
								zavrsi_bacanje_kliknut = 2
								usporedba_red_bacanja1.append("1")
								usporedba_red_bacanja2.append("1")
								usporedba.clear()
								drugi_nosi = 1
							elif vrijednosti_karata[usporedba[0]]<vrijednosti_karata[usporedba[1]]:#ako je adut od igraca 1 jaci od aduta od igraca 2, igrac 1 dobiva bodove
								p1bodovi_runda.append(vrijednosti_karata[usporedba[0]]+vrijednosti_karata[usporedba[1]])
								p1stih_stat += 1
								stih = 1
								zavrsi_bacanje_kliknut = 2
								usporedba_red_bacanja2.append("0")
								usporedba_red_bacanja1.append("0")
								usporedba.clear()
								prvi_nosi = 1
						else:#ako oba igraca imaju u potpunosti razalicite vrste karata onda igrac 2 dobiva bodove jer 1. igrac nije pratio pravilo postovanja
							p2bodovi_runda.append(vrijednosti_karata[usporedba[0]]+vrijednosti_karata[usporedba[1]])
							p2stih_stat += 1
							stih = 1
							zavrsi_bacanje_kliknut = 2
							usporedba_red_bacanja1.append("1")
							usporedba_red_bacanja2.append("1")
							usporedba.clear()
							drugi_nosi = 1
		#tekst tko nosi stih
		if prvi_nosi == 1:
			draw_text(f"{igrač1ime} uzima štih!",font,(255,255,255),600,330)
			draw_text(f"Vrijednost: {p1bodovi_runda[-1]}",font2,(255,255,255),600,380)
		if drugi_nosi == 1:
			draw_text(f"{igrač2ime} uzima štih!",font,(255,255,255),600,330)
			draw_text(f"Vrijednost: {p2bodovi_runda[-1]}",font2,(255,255,255),600,380)
		
		#tipka za zvanje
		if ciji_red % 2 == 0: #provjerava je li igrač 1. na redu
			if promjena_reda == 0: #koji je igrač na redu (1.)
				for zvanje_moguce in p1inv:
					if zvanje_provjera < 6: #ogranici da ne gleda beskonačno karte u inventoriju
						zvanje_provjera +=1
						if zvanje_moguce[0] == "K" or zvanje_moguce[0] == "Q": #provjerava je li karta kralj ili baba
							if len(moguca_zvanja) > 0:
								for z in moguca_zvanja:
									if zvanje_moguce not in moguca_zvanja and zvanje_moguce[1] == z[1] and zvanje_moguce not in zvanje_baceno: #provjerava je li karta različita, iste boje i nije zvana. Ako je istinito sve, može se zvati
										prihvati_zvanje = 1
							moguca_zvanja.append(zvanje_moguce) #dodaj u listu karti koje se mogu zvati
			elif promjena_reda == 1: #koji je igrač na redu (2.)
				for zvanje_moguce in p2inv: 
					if zvanje_provjera < 6: #ogranici da ne gleda beskonačno karte u inventoriju
						zvanje_provjera +=1
						if zvanje_moguce[0] == "K" or zvanje_moguce[0] == "Q": #provjerava je li karta kralj ili baba
							if len(moguca_zvanja) > 0:
								for z in moguca_zvanja:
									if zvanje_moguce not in moguca_zvanja and zvanje_moguce[1] == z[1] and zvanje_moguce not in zvanje_baceno: #provjerava je li karta različita, iste boje i nije zvana. Ako je istinito sve, može se zvati
										prihvati_zvanje = 1
							moguca_zvanja.append(zvanje_moguce) #dodaj u listu karti koje se mogu zvati
                            
		if prihvati_zvanje == 1:
			btn_zvanje = Button(100,265,zvanje_slika, 0.5) #gumb za zvanje
			if btn_zvanje.draw() == True: #ako se gumb za zvanje klikne
				menu_state ="zvanje" #menu je sada zvanje
			#drzi menu zvanje otvorenim
			if menu_state == "zvanje": #ako je menu zvanje, izvrsi zvanje funckiju
				zvanje()

		#ZATVARANJE
		if len(dek) > 2 and len(p1inv) > 0: #pravilo zatvaranja je da moraju biti barem 2 karte u deku
			if ciji_red % 2 == 0:#provjerava je li igrač 1. na redu
				if len(p1inv) == 5 and len(p2inv) == 5:
					zatvaranje_btn = Button(50,430,zatvaranje_slika, 0.5) #gumb za zatvaranje
					if zatvaranje_btn.draw() == True:
						zatvaranje_tekst = "da"
						if promjena_reda == 0: #ako je prvi igrac na redu
							zatvara = "1" #zatvara je 1 sto znaci da je 1. igrac htio zatvoriti
						if promjena_reda == 1: #ako je drugi igrac na redu
							zatvara = "2" #zatvara je 2 sto znaci da je 2. igrac htio zatvoriti
						dek.clear() #dek je prazan u zatvaranju po pravilima. ne možeš vući karte iz deka

		if zatvaranje_tekst == "da":
			draw_text(f"ZATVARANJE!",font3,(255,255,255),300,17) #tekst koji signalizira zatvaranje
			if len(p1inv) == 5 and len(p2inv) == 5:
				draw_text(f"U zatvaranju ne dobivaš karte iz deka. Vrijede pravila iberovanja i poštovanja.",font5,(255,255,255),150,130) #tekst koji opisuje što je zatvaranje
				draw_text(f"Ako ne dođeš do 66 bodova do kraja runde, protivnik pobjeđuje.",font5,(255,255,255),190,160) 

		#KRAJ RUNDE	
		if (sum(p1bodovi_runda) >= 66 or sum(p2bodovi_runda) >= 66) or ((zatvara == "1" or zatvara == "2") and len(p1inv) == 0 and len(p2inv) == 0 and sum(p1bodovi_runda) < 66 and sum(p2bodovi_runda) < 66): #provjerava je li runda gotova tako da gleda ima li jedan igrač 66 bodova ili više ili su završili zatvaranje
			stari_bodovi1 = p1bodovi
			stari_bodovi2 = p2bodovi
			kraj_state = "da"
		if len(p1inv) == 0 and len(p2inv) == 0 and len(dek) == 0 and sum(p1bodovi_runda)<66 and sum(p2bodovi_runda)<66:
			zatvara = "4"
			kraj_runde() 
		
		pygame.display.update()
	pygame.quit()

def zvanje():
	ogranici_zvanje = 0 #ogranicuje zvanje na dvije karte
	ogranici_zbroj = 0 #daje da se samo jednom smije zbrajati
	zvanje_state = "0" ##provjerava je li zvanje s ili bez aduta
	global p1bodovi_runda
	global p2bodovi_runda
	global promjena_reda
	global menu_state
	global zvanje_baceno
	global prihvati_zvanje
	global zvanje_provjera
	global moguca_zvanja
	global brojac
	clock = pygame.time.Clock()
	run = True
	while run:
		clock.tick(FPS)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
		novi_prozor = pygame.display.set_mode((1024,768))
		novi_prozor.blit(background_slika, (0,0))
		draw_text("ZVANJE",font3,(255,255,255),390,30) #stavi tekst "zvanje"(tekst,velicina,boja,x,y)
		xos = 95
		if len(zvanje_baceno) == 0:
			draw_text(f"U zvanju moraš baciti kralja i kraljicu iste boje.",font2,(255,255,255),250,150)
		if promjena_reda == 0:  #koji je igrač na redu (1.)
			for i in p1inv:
				karta = Button(xos,500,pygame.image.load("Desktop\projekt\karte\\"+ slike_karata[i]).convert_alpha(),0.18).draw()
				xos += 180
				if karta == True: #ako je karta kliknuta
					if ogranici_zvanje < 2: #daje da se samo dvije karte smiju zvati
						if i not in zvanje_baceno: #provjerava da karta već nije bila kliknuta
							if i[0] == "K" or i[0] == "Q": #provjerava je li karta kralj ili baba
								zvanje_baceno.append(i)
								ogranici_zvanje += 1


		else:  #koji je igrač na redu (2.)
			for t in p2inv:
				karta = Button(xos,500,pygame.image.load("Desktop\projekt\karte\\"+ slike_karata[t]).convert_alpha(),0.18).draw()
				xos += 180
				if karta == True: #ako je karta kliknuta
					if ogranici_zvanje < 2: #daje da se samo dvije karte smiju zvati
						if t not in zvanje_baceno: #provjerava da karta već nije bila kliknuta
							if t[0] == "K" or t[0] == "Q": #provjerava je li karta kralj ili baba
								zvanje_baceno.append(t)
								ogranici_zvanje += 1

		if ogranici_zvanje == 0 and len(zvanje_baceno) % 2 == 1: #ako je igraač zvao samo jednu kartu, a ne dvije, izbriši je iz liste baceno, tj. ne zove se
			zvanje_baceno.remove(zvanje_baceno[-1]) 

		if len(zvanje_baceno) != 0:
			zvana_karta = Button(320,250,pygame.image.load("Desktop\projekt\karte\\"+ slike_karata[zvanje_baceno[-1]]).convert_alpha(),0.18).draw()
			if len(zvanje_baceno) % 2 == 0:
				zvana_karta = Button(580,250,pygame.image.load("Desktop\projekt\karte\\"+ slike_karata[zvanje_baceno[-2]]).convert_alpha(),0.18).draw()

		if ogranici_zvanje == 2: #ako su zvane dvije karte, pogledaj mogu li se zvati
			if zvanje_baceno[-2][0] != zvanje_baceno[-1][0]: #provjerava da te dvije karte nisu ista vrsta (npr. baba-baba ili kralj-kralj)
				if zvanje_baceno[-2][1] == zvanje_baceno[-1][1] and zvanje_baceno[-1][1] == adut[0][-1]: #zvanje je uspješno. imaju iste boje karte i kao adut
					zvanje_state = "1" #varijabla za ispisivanje teksta u slucaju iste boje aduta
					if ogranici_zbroj == 0: #dopušta da se bodovi daju igraču samo jednom
						if promjena_reda == 0: #provjerava je li 1. igrač na redu
							p1bodovi_runda.append(40) #daj 1. igracu 40 bodova
							ogranici_zbroj +=1
							brojac = 1
						else: #provjerava je li 2. igrač na redu
							p2bodovi_runda.append(40) #daj 2. igracu 40 bodova
							ogranici_zbroj +=1
							brojac = 1
				elif zvanje_baceno[-2][1] == zvanje_baceno[-1][1] and zvanje_baceno[-1][1] != adut[0][-1]:
					zvanje_state = "2"  #varijabla za ispisivanje teksta u slucaju razlicite boje aduta
					if ogranici_zbroj == 0: #dopušta da se bodovi daju igraču samo jednom
						if promjena_reda == 0: #provjerava je li 1. igrač na redu
							p1bodovi_runda.append(20) #daj 1. igracu 20 bodova
							ogranici_zbroj +=1
							brojac = 1
						else: #provjerava je li 2. igrač na redu
							p2bodovi_runda.append(20) #daj 2. igracu 20 bodova
							ogranici_zbroj +=1
							brojac = 1
				else:
					zvanje_baceno.remove(zvanje_baceno[-1]) #zvanje nije bilo uspješno, izbaci karte
					zvanje_baceno.remove(zvanje_baceno[-1])
			else:
				zvanje_baceno.remove(zvanje_baceno[-1]) #zvanje nije bilo uspješno, izbaci karte
				zvanje_baceno.remove(zvanje_baceno[-1])
			ogranici_zvanje = 3

		if zvanje_state == "1":
			draw_text(f"ZVANJE JE USPJEŠNO!",font2,(255,255,255),370,150)
			draw_text(f"+40",font3,(255,255,255),450,320)
		if zvanje_state == "2":
			draw_text(f"ZVANJE JE USPJEŠNO!",font2,(255,255,255),370,150)
			draw_text(f"+20",font3,(255,255,255),450,320)
		
		iz_zvanje_u_igru_btn = Button(50,50,povratak_btn_slika, 0.8)
		#resettiranje varijabli
		zvanje_provjera = 0
		moguca_zvanja.clear()
		prihvati_zvanje = 0

		if iz_zvanje_u_igru_btn.draw() == True:
			menu_state = "nastavi_sedam"
		if menu_state == "nastavi_sedam":
			igra()

		pygame.display.update()
	pygame.quit()

def kraj_runde():
	global menu_state
	global karte_state
	global promjena_reda
	global p1bodovi_runda
	global p2bodovi_runda
	global ogranici_izvlacenje1
	global ogranici_izvlacenje2
	global bacena_karta_state
	global bacena_karta_state2
	global btn_podijeli_karte_crtaj
	global ogranici_bacanje1
	global ogranici_bacanje2
	global zavrsi_bacanje_kliknut
	global dek
	global p1bodovi
	global p2bodovi
	global stari_bodovi1
	global stari_bodovi2
	global p1pobjeda
	global p2pobjeda
	global zatvara
	global zatvaranje_tekst
	global ogranici_zvanje 
	global ogranici_zbroj
	global zvanje_state
	global zvanje_baceno
	global prihvati_zvanje
	global zvanje_provjera
	global moguca_zvanja
	global ciji_red
	global brojac_vrsteP1
	global brojac_vrsteP2
	global brojac_ibera
	global brojac_ibera2
	global stih
	global ogranici_zavrsi
	global p1runda_stat
	global p2runda_stat
	global bodoviPoRundi_stat1
	global bodoviPoRundi_stat2
	global prvi_nosi
	global drugi_nosi
	global ogranici_scoreboard
	global kraj_state 
	global brojac

	clock = pygame.time.Clock()
	run = True
	while run:
		clock.tick(FPS)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
		novi_prozor = pygame.display.set_mode((1024,768))
		novi_prozor.blit(pozadina2_slika, (0,0))

		if zatvara == "1" and p2bodovi == stari_bodovi2: #provjerava je li 1. igrač zatvarao
			if sum(p1bodovi_runda) < 66: #provjerava je li igrač uspio ili nije uspio zatvaranje
				p2runda_stat += 1
				if sum(p2bodovi_runda) == 0: #ako je protivnik imao 0 bodova, ide dolje za 3
					p2bodovi = stari_bodovi2 - 3
				if sum(p2bodovi_runda) > 0 and sum(p2bodovi_runda) < 33: #ako je protivnik imao vise od 0, ali manje od 33 bodova, ide dolje za 2
					p2bodovi = stari_bodovi2 - 2
				if sum(p2bodovi_runda) > 33: #ako je protivnik imao 33 bodova ili vise, ide dolje za 1
					p2bodovi = stari_bodovi2 - 1
				if sum(p2bodovi_runda) == 33:
					p1bodovi = stari_bodovi1 - 1
			else:
				zatvara = "0"
		elif zatvara == "2" and p1bodovi == stari_bodovi1: #provjerava je li 2. igrač zatvarao
			if sum(p2bodovi_runda) < 66: #provjerava je li igrač uspio ili nije uspio zatvaranje
				p1runda_stat += 1
				if sum(p1bodovi_runda) == 0: #ako je protivnik imao 0 bodova, ide dolje za 3
					p1bodovi = stari_bodovi1 - 3
				if sum(p1bodovi_runda) > 0 and sum(p2bodovi_runda) < 33: #ako je protivnik imao vise od 0, ali manje od 33 bodova, ide dolje za 2
					p1bodovi = stari_bodovi1 - 2
				if sum(p1bodovi_runda) > 33: #ako je protivnik imao 33 bodova ili vise, ide dolje za 1
					p1bodovi = stari_bodovi1 - 1
				if sum(p2bodovi_runda) == 33:
					p1bodovi = stari_bodovi1 - 1
			else:
				zatvara = "0"
		elif zatvara == "0": #boduje se normalno, ne kao zatvaranje
			if sum(p1bodovi_runda) > sum(p2bodovi_runda) and stari_bodovi1 == p1bodovi: #ako je 1. igrač pobijedio
				p1runda_stat += 1
				if sum(p2bodovi_runda) == 0: #ako protivnik ima 0 boda, ide dolje za 3 pobjednik
					p1bodovi = stari_bodovi1 - 3
				if sum(p2bodovi_runda) > 0 and sum(p2bodovi_runda) < 33: #ako protivnik ima više od 0, ali manje od 33 boda, ide dolje za 2 pobjednik
					p1bodovi = stari_bodovi1 - 2
				if sum(p2bodovi_runda) > 33: #ako protivnik ima vise od 33 boda, ide dolje za 1 pobjednik
					p1bodovi = stari_bodovi1 - 1
			if sum(p2bodovi_runda) > sum(p1bodovi_runda) and stari_bodovi2 == p2bodovi: #ako je 2. igrač pobijedio
				p2runda_stat += 1
				if sum(p1bodovi_runda) == 0: #ako protivnik ima 0 boda, ide dolje za 3 pobjednik
					p2bodovi = stari_bodovi2 - 3
				if sum(p1bodovi_runda) > 0 and sum(p1bodovi_runda) < 33: #ako protivnik ima više od 0, ali manje od 33 boda, ide dolje za 2 pobjednik
					p2bodovi = stari_bodovi2 - 2
				if sum(p1bodovi_runda) > 33: #ako protivnik ima vise od 33 boda, ide dolje za 1 pobjednik
					p2bodovi = stari_bodovi2 - 1
		elif zatvara == "4":
			p1bodovi = p1bodovi
			p2bodovi = p2bodovi
		
		novi_prozor.blit(kraj_runde_slika, (0,0)) #stvori sliku tablice
		#upisi brojeve u tablicu
		draw_text(f"{igrač1ime}",font4,(250,250,250),470,252)
		draw_text(f"{igrač2ime}",font4,(250,250,250),790,252)
		draw_text(f"{sum(p1bodovi_runda)}",font4,(250,250,250),550,340)
		draw_text(f"{sum(p2bodovi_runda)}",font4,(250,250,250),870,340)
		draw_text(f"{p1bodovi}",font4,(250,250,250),550,430)
		draw_text(f"{p2bodovi}",font4,(250,250,250),870,430)

		#reseta sve varijable i liste
		usporedba.clear()
		p1inv.clear()
		p2inv.clear()
		dek = ["JC", "QC", "KC", "10C", "AC","JS", "QS", "KS", "10S", "AS","JD", "QD", "KD", "10D", "AD","JH", "QH", "KH", "10H", "AH"]
		karte_crtanje.clear()
		karte_state ="ne_prikaz"
		bacena_karta_state ="ne"
		bacena_karta_state2 ="ne"
		promjena_reda = 0
		ogranici_izvlacenje1 = 0
		ogranici_izvlacenje2 = 0
		btn_podijeli_karte_crtaj = 0
		ogranici_bacanje1 = 0
		ogranici_bacanje2 = 1
		zavrsi_bacanje_kliknut = 0
		adut.clear()
		usporedba_red_bacanja1.clear()
		usporedba_red_bacanja2.clear()
		bacena_kartap1.clear()
		bacena_kartap2.clear()
		zatvaranje_tekst = ""
		ogranici_zvanje = 0
		ogranici_zbroj = 0
		zvanje_state = "0"
		zvanje_baceno.clear()
		zvanje_provjera = 0
		moguca_zvanja.clear()
		prihvati_zvanje = 0
		ciji_red = 0
		brojac_vrsteP1 = 0
		brojac_vrsteP2 = 0
		brojac_ibera = 0
		brojac_ibera2 = 0
		stih = 0
		ogranici_zavrsi = 1
		prvi_nosi = 0
		drugi_nosi = 0
		ogranici_scoreboard = "ne"
		kraj_state = "ne"
		brojac = 0

		if p1bodovi <= 0 or p2bodovi <= 0: #gleda je li igra gotova
			draw_text(f"KRAJ IGRE",font3,(255,255,255),300,80)
			nastavi_rundu_btn = Button(280,600,nastavi_slika, 1)
			if p1bodovi < 0: #ako igrač ima manje od 0 boda, zapisi kao da ima 0
				p1bodovi = 0
			if p2bodovi < 0:
				p2bodovi = 0
			if nastavi_rundu_btn.draw() == True: #ako se "nastavi" gumb kline, izbaci pobjednika i statistiku
				menu_state = "pobjeda"
			if menu_state == "pobjeda":
				#resetira varijable
				zatvara = "0"
				bodoviPoRundi_stat1.append(sum(p1bodovi_runda))
				bodoviPoRundi_stat2.append(sum(p2bodovi_runda))
				p1bodovi_runda.clear()
				p2bodovi_runda.clear()
				pobjeda()
		else: #nastavlja rundu ako nije gotova igra
			draw_text(f"KRAJ RUNDE",font3,(255,255,255),300,80)
			nastavi_rundu_btn = Button(280,600,nastavi_slika, 1)
			if nastavi_rundu_btn.draw() == True:
				menu_state = "nastavi_sedam"
			if menu_state == "nastavi_sedam": #ako se "nastavi" gumb kline, nastavi igru
				zatvara = "0"
				bodoviPoRundi_stat1.append(sum(p1bodovi_runda))
				bodoviPoRundi_stat2.append(sum(p2bodovi_runda))
				#reseta bodove runde
				p1bodovi_runda.clear()
				p2bodovi_runda.clear()
				igra()
		pygame.display.update()
	pygame.quit()

def pobjeda():
	global p1pobjeda
	global p2pobjeda
	global p1bodovi
	global p2bodovi
	global ogranici_bodovanje
	global p1runda_stat
	global p2runda_stat
	global p1stih_stat
	global p2stih_stat
	global p1bodProsjek_stat
	global p2bodProsjek_stat
	global menu_state
	clock = pygame.time.Clock()
	run = True
	while run:
		clock.tick(FPS)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
		screen.blit(pozadina2_slika, (0,0))
		if p1bodovi <= 0: #provjerava je li 1. igrac pobijedio
			draw_text(f"Pobijedio je {igrač1ime}!",font4,(255,255,255),240,140)
			if ogranici_bodovanje == 0:
				p1bodovi = 0
				p1pobjeda += 1 #dodaje mu pobjedu u varijablu
				ogranici_bodovanje +=1
		elif p2bodovi <= 0: #provjerava je li 2. igrac pobijedio
			draw_text(f"Pobijedio je {igrač2ime}!",font4,(255,255,255),240,140)
			if ogranici_bodovanje == 0:
				p2bodovi = 0
				p2pobjeda += 1 #dodaje mu pobjedu u varijablu
				ogranici_bodovanje += 1
		p1bodProsjek_stat = round(sum(bodoviPoRundi_stat1) / len(bodoviPoRundi_stat1),2) #dijeli bodove u rundi kroz koliko je bilo rundi
		p2bodProsjek_stat = round(sum(bodoviPoRundi_stat2) / len(bodoviPoRundi_stat2),2)
		draw_text(f"STATISTIKA",font3,(255,255,255),350,30)
		screen.blit(kraj_igre_tablica, (0,0))
		draw_text(f"{igrač1ime}",font4,(250,250,250),470,252)
		draw_text(f"{igrač2ime}",font4,(250,250,250),790,252)
		draw_text(f"{p1pobjeda}",font4,(250,250,250),550,340)
		draw_text(f"{p2pobjeda}",font4,(250,250,250),870,340)
		draw_text(f"{p1runda_stat}",font4,(250,250,250),550,430)
		draw_text(f"{p2runda_stat}",font4,(250,250,250),870,430)
		draw_text(f"{p1stih_stat}",font4,(250,250,250),550,520)
		draw_text(f"{p2stih_stat}",font4,(250,250,250),870,520)
		draw_text(f"{p1bodProsjek_stat}",font4,(250,250,250),530,610)
		draw_text(f"{p2bodProsjek_stat}",font4,(250,250,250),850,610)
		zavrsi_rundu_btn = Button(400,700,vrati_se_slika, 0.5)
		if zavrsi_rundu_btn.draw() == True:
			menu_state = "main"
		if menu_state == "main":	
			main()
		pygame.display.update()
	pygame.quit()

def main():#loop koji pokrece igru
	global menu_state
	global p1bodovi
	global p2bodovi
	global p1pobjeda
	global p2pobjeda
	global makni_sedam
	global makni_devet 
	makni_sedam = 0
	makni_devet = 0
	clock = pygame.time.Clock()
	run = True
	while run:
		clock.tick(FPS)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
		
		screen.blit(mainMenu_slika, (0,0))
		video.draw(screen, (0, 0)) #stvori video
		igraj_btn = Button(290,330,igra_slika, 1)
		izlaz_btn = Button(290,570,izlaz_slika,1)
		if izlaz_btn.draw() == True:
			menu_state = "izlaz"
		if menu_state == "izlaz":
			pygame.quit()

		if p1pobjeda > 0 or p2pobjeda > 0:
			statistika_btn = Button(290,450,statistika_slika, 1)
			if statistika_btn.draw() == True:
				menu_state = "statistika"
		
		if igraj_btn.draw() == True:
			menu_state = "opcije"
			video.close()
		if menu_state == "opcije":
			opcije()
		
		if menu_state =="statistika":
			pobjeda()

		pygame.display.update()
	pygame.quit()

def opcije():
	global menu_state
	global p1bodovi
	global p2bodovi
	global ogranici_bodovanje
	global igrač1ime
	global igrač2ime
	global makni_sedam
	global makni_devet
	nastavi_state = ""
	igrač1ime = "" #tekst koji je upisao 1. igrac
	igrač2ime = "" #tekst koji je upisao 2. igrac
	text_box1 = pygame.Rect(150,300,300,50)
	text_box2 = pygame.Rect(755,300,300,50)
	active1 = False
	active2 = False
	color1 = pygame.Color('red')
	color2= pygame.Color('red')
	clock = pygame.time.Clock()
	run = True
	while run:
		clock.tick(FPS)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			if event.type == pygame.MOUSEBUTTONDOWN:
				if text_box1.collidepoint(event.pos):
					active1 = True
				else:
					active1 = False
				if text_box2.collidepoint(event.pos):
					active2 = True
				else:
					active2 = False
			if event.type == pygame.KEYDOWN:
				if active1:
					if event.key == pygame.K_BACKSPACE:
						igrač1ime = igrač1ime[:-1]
					else:
						igrač1ime += event.unicode
				if active2:
					if event.key == pygame.K_BACKSPACE:
						igrač2ime = igrač2ime[:-1]
					else:
						igrač2ime += event.unicode


		if menu_state == "opcije":
			screen.blit(opcije1_slika, (0,0))
		
			if active1:
				color1 = pygame.Color('coral2')
			else:
				color1 = pygame.Color('red')
			if active2:
				color2 = pygame.Color('coral2')
			else:
				color2 = pygame.Color('red')

			pygame.draw.rect(screen,color1, text_box1,4)
			surf1 = font.render(igrač1ime,True,'white')
			screen.blit(surf1, (text_box1.x +5 , text_box1.y +5))
			text_box1.w = max(100, surf1.get_width()+10)

			pygame.draw.rect(screen,color2, text_box2,4)
			surf2 = font.render(igrač2ime,True,'white')
			screen.blit(surf2, (text_box2.x +5 , text_box2.y +5))
			text_box2.w = max(100, surf2.get_width()+10)

			btn_povratak = Button(20,20,povratak_btn_slika,0.8)
			if btn_povratak.draw() == True:
				menu_state = "main"
			if menu_state =="main":
				main()

		if len(igrač2ime)>7 or len(igrač2ime)==0 or len(igrač1ime)>7 or len(igrač1ime)==0: #provjerava je li ime ispravno uspisano
				draw_text(f"Ime se mora upisati. Najveća duljina je 7 slova.",font2,(250,250,250),250,610)
				menu_state = "opcije"
		else:
			if menu_state != "nastavi" and menu_state != "igra":
				menu_state = "bodovi"
		if menu_state == "bodovi":
			screen.blit(opcije2_slika, (0,0))
			
			if active1:
				color1 = pygame.Color('coral2')
			else:
				color1 = pygame.Color('red')
			if active2:
				color2 = pygame.Color('coral2')
			else:
				color2 = pygame.Color('red')

			pygame.draw.rect(screen,color1, text_box1,4)
			surf1 = font.render(igrač1ime,True,'white')
			screen.blit(surf1, (text_box1.x +5 , text_box1.y +5))
			text_box1.w = max(100, surf1.get_width()+10)

			pygame.draw.rect(screen,color2, text_box2,4)
			surf2 = font.render(igrač2ime,True,'white')
			screen.blit(surf2, (text_box2.x +5 , text_box2.y +5))
			text_box2.w = max(100, surf2.get_width()+10)

			btn_povratak = Button(20,20,povratak_btn_slika,0.8)
			if btn_povratak.draw() == True:
				menu_state = "main"
			if menu_state =="main":
				main()

			if makni_sedam == 0:
				sedam_bodova_btn = Button(350,470,sedam_bodova_slika,1)
			else:
				sedam_bodova_btn = Button(350,470,sedam_kliknut_slika,1)
			if makni_devet == 0:
				devet_bodova_btn = Button(580,470,devet_bodova_slika,1)
			else:
				devet_bodova_btn = Button(580,470,devet_kliknut_slika,1)
			if sedam_bodova_btn.draw() == True:
				p1bodovi = 7
				p2bodovi = 7
				makni_sedam = 1
				makni_devet = 0
				nastavi_state = "da" #ako se klikne 7, stvori se "nastavi"
			if devet_bodova_btn.draw() == True:
				p1bodovi = 9
				p2bodovi = 9
				makni_devet = 1
				makni_sedam = 0
				nastavi_state = "da" #ako se klikne 9, stvori se "nastavi"
			
			if nastavi_state == "da":
				nastavi_btn = Button(290,610,nastavi_slika,1)
				if nastavi_btn.draw() == True:
					menu_state = "igra" #ako se klikne "nastavi", krene se igra
			if menu_state == "igra":
				ogranici_bodovanje = 0
				makni_sedam = 0
				makni_devet = 0
				igra()
		

		pygame.display.update()
	pygame.quit()
main()
