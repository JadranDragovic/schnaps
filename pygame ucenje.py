from turtle import Screen
import pygame 
import random
import time
from pygame import Surface
from pyvidplayer import Video

pygame.init()
igrač1ime = input("Unesi ime: ").upper()
while len(igrač1ime)>7 or len(igrač1ime)==0:
    igrač1ime = input("Unesi ime koje ima manje od 7 znakova i više od 0: ").upper()
igrač2ime = input("Unesi ime: ").upper()
while len(igrač2ime)>7 or len(igrač2ime)==0:
    igrač2ime = input("Unesi ime koje ima manje od 7 znakova i više od 0: ").upper()

#velicine
screen = pygame.display.set_mode((1024,768))
pygame.display.set_caption("ŠNAPS")
FPS = 60
font = pygame.font.Font(None, 60)
font2 = pygame.font.Font(None, 40)
font3 = pygame.font.Font(None, 100)
font4 = pygame.font.Font(None, 80)
text_color = (255,255,255)

#video
video = Video("Desktop\projekt\slike\cards1.mp4")
video.set_size((1024, 768))
#slike za buttone
sedam_bodova_slika = pygame.image.load("Desktop\projekt\slike\sedam.png").convert_alpha()
devet_bodova_slika = pygame.image.load("Desktop\projekt\slike\devet.png").convert_alpha()
povratak_btn_slika = pygame.image.load("Desktop\projekt\slike\povratak_btn.png").convert_alpha()
promijeni_red_btn_slika = pygame.image.load("Desktop\projekt\slike\promijeni_btn.png").convert_alpha()
pravila_slika = pygame.image.load("Desktop\projekt\slike\pravila_btn.png").convert_alpha()
igra_slika = pygame.image.load("Desktop\projekt\slike\igra_btn.png").convert_alpha()
izlaz_slika = pygame.image.load("Desktop\projekt\slike\izlaz_btn.png").convert_alpha()
kraj_runde_slika = pygame.image.load("Desktop\projekt\slike\kraj_runde_table.png").convert_alpha()
kraj_igre_tablica = pygame.image.load("Desktop\projekt\slike\kraj_igre_table.png").convert_alpha()
background_slika = pygame.image.load("Desktop\projekt\slike\pozadina.png").convert_alpha()
pozadina2_slika = pygame.image.load("Desktop\projekt\slike\pozadina2.png").convert_alpha()
mainMenu_slika = pygame.image.load("Desktop\projekt\slike\mainScreen.png").convert_alpha()
zatvaranje_slika = pygame.image.load("Desktop\projekt\slike\zatvaranje_btn.png").convert_alpha()
zvanje_slika = pygame.image.load("Desktop\projekt\slike\zvanje_btn.png").convert_alpha()
kraj_slika = pygame.image.load("Desktop\projekt\slike\kraj_btn.png").convert_alpha()
nastavi_slika = pygame.image.load("Desktop\projekt\slike\continue_btn.png").convert_alpha()
vrati_se_slika = pygame.image.load("Desktop\projekt\slike\leave_btn.png").convert_alpha()
podijeli_karte_slika = pygame.image.load("Desktop\projekt\slike\podijeli_btn.png").convert_alpha()
nastavi_slika = pygame.image.load("Desktop\projekt\slike\continue_btn.png").convert_alpha()
waiting_slika1 = pygame.image.load("Desktop\projekt\slike\waiting1.png").convert_alpha()
waiting_slika2 = pygame.image.load("Desktop\projekt\slike\waiting2.png").convert_alpha()
waiting_slika3 = pygame.image.load("Desktop\projekt\slike\waiting3.png").convert_alpha()

#liste
vrijednosti_karata = {"JC":2, "QC":3, "KC":4, "10C":10, "AC":11,"JS":2, "QS":3, "KS":4, "10S":10, "AS":11,"JD":2, "QD":3, "KD":4, "10D":10, "AD":11,"JH":2, "QH":3, "KH":4, "10H":10, "AH":11}
dek = ["JC", "QC", "KC", "10C", "AC","JS", "QS", "KS", "10S", "AS","JD", "QD", "KD", "10D", "AD","JH", "QH", "KH", "10H", "AH"]
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
usporedba = []
karte_crtanje = []
usporedba2 = []
usporedba_red_bacanja1 = []
usporedba_red_bacanja2 = []
bacena_kartap1 = []
bacena_kartap2 = []
zvanje_baceno = []
zadnja_karta = []
moguca_zvanja = []

def dijeljenje_karata():#podijeli random karte igračima
	for i in range(3):
		p1inv.append(random.choice(dek))
		dek.remove(p1inv[i])
	for i in range(3): 
		p2inv.append(random.choice(dek))
		dek.remove(p2inv[i])
	adut.append(random.choice(dek))
	for i in range(3,5):
		p1inv.append(random.choice(dek))
		dek.remove(p1inv[i])
	for i in range(3,5): 
		p2inv.append(random.choice(dek))
		dek.remove(p2inv[i])

def draw_text(text,font,text_col,x,y):#služi za prikazivanje bilo kakavog teksta na ekranu
	img = font.render(text,True,text_col)
	screen.blit(img,(x,y))

class Button():#proizvodim vlastitu klasu za gumb 
	hovered = False
	def __init__(self, x, y, image,scale):
		
		self.image = image
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def draw(self,):		
		action = False
			#dobivamo mouse position
		pos = pygame.mouse.get_pos()
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True
		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False
			
		screen.blit(self.image,(self.rect.x,self.rect.y))
		return action
	
#buttoni
btn_zavrsi_bacanje = Button(460,80,promijeni_red_btn_slika,0.5)
btn_izvuci_kartu = Button(800,250,sedam_bodova_slika,0.5)

#varijable
menu_state ="main" #pomaže za mijenjanje prozora
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
p1pobjeda = 0
p2pobjeda = 0
brojac_vrsteP1 = 0
brojac_vrsteP2 = 0
zatvara = "0"
zatvaranje_tekst = ""
stih = 0
brojac_ibera = 0
brojac_ibera2 = 0
ogranici_zavrsi = 1
ciji_red = 0
zvanje_provjera = 0
prihvati_zvanje = 0
prikazi_video = 0
ogranici_bodovanje = 0
keks = pygame.Surface((150,150))


def igra():#window za igru od 7 bodova
	run = True
	while run:
		clock = pygame.time.Clock()
		clock.tick(FPS)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
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
		global menu_state
		global p1bodovi
		global p2bodovi
		global stari_bodovi1
		global stari_bodovi2
		global brojac_vrsteP1
		global brojac_vrsteP2
		global zatvara
		global zatvaranje_tekst
		global zadnja_karta
		global brojac_ibera
		global brojac_ibera2
		global stih
		global ogranici_zavrsi
		global ciji_red
		global moguca_zvanja
		global zvanje_provjera
		global prihvati_zvanje
		global zvanje_baceno
		screen.blit(background_slika, (0,0))
		draw_text(f"{igrač1ime}:{p1bodovi}",font2,text_color,880,10)
		draw_text(f"{igrač2ime}:{p2bodovi}",font2,text_color,880,50)

		#dijeljenje karti
		if len(p1inv) == 0 and len(dek) != 0:
			btn_podijeli_karte = Button(448,245,podijeli_karte_slika,0.7)
			if btn_podijeli_karte.draw() == True:#ako se klikne taj gumb onda se podijeli karte s pomocu funkcije dijeljenje_karata
				while btn_podijeli_karte_crtaj % 2 == 0:
					dijeljenje_karata()
					karte_state = "prikaz"
					btn_podijeli_karte_crtaj += 1


		if karte_state == "prikaz":#pomaze mi samo da prikazujem ili ne prikazujem kartu
			#prikaz karata
			if len(adut) != 0:
				if adut[0][-1] == "H":
					draw_text(f"ADUT: HERC",font2,(255,255,255),50,40)
				if adut[0][-1] == "S":
					draw_text(f"ADUT: PIK",font2,(255,255,255),50,40)
				if adut[0][-1] == "D":
					draw_text(f"ADUT: KARO",font2,(255,255,255),50,40)
				if adut[0][-1] == "C":
					draw_text(f"ADUT: TREF",font2,(255,255,255),50,40)
				
			
			if len(usporedba) != 2:
				if promjena_reda == 0:
					draw_text(f"{igrač1ime} JE NA REDU",font2,(255,255,255),50,10)
					xos = 95
					for i in p1inv:
						karta = Button(xos,500,pygame.image.load("Desktop\projekt\karte\\"+ slike_karata[i]).convert_alpha(),0.18).draw()
						xos += 180
						if karta == True:
							if len(dek) != 0:	
								while ogranici_bacanje1 == 0:
									karte_crtanje.append(i)
									bacena_kartap1.append(i)
									bacena_karta_state ="da"
									usporedba.append(i)
									p1inv.remove(i)
									ogranici_bacanje1 =1
									ogranici_bacanje2 =1
									ogranici_zavrsi = 0					
							if len(dek) == 0:
								if len(usporedba) != 0:
									for m in p1inv:
										if m[-1] == bacena_kartap2[-1][-1]:
											brojac_vrsteP1 = 1
										if brojac_vrsteP1 == 0:
											if m[-1] == adut[0][-1]:
												brojac_vrsteP1 = 2
									if brojac_vrsteP1 == 0:
										for k in p1inv:
											if k[-1] != bacena_kartap2[-1][-1] and k[-1] != adut[0][-1]:
												brojac_vrsteP1 = 3
									for h in p1inv:
										if h[-1] == bacena_kartap2[-1][-1] and vrijednosti_karata[h]>vrijednosti_karata[bacena_kartap2[-1]]:
											brojac_ibera = 1
									print(brojac_vrsteP1)
									if brojac_vrsteP1 == 1:
										brojac_vrsteP1 = 0
										if i[-1] == bacena_kartap2[-1][-1]:
											if brojac_ibera == 1:
												brojac_ibera = 0
												if i[-1] == bacena_kartap2[-1][-1] and vrijednosti_karata[i]>vrijednosti_karata[bacena_kartap2[-1]]:
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
													draw_text("MORAŠ PRATITI PRAVILO IBEROVANJA",font2,(255,255,255),250,150)
													pygame.display.update()
													time.sleep(2)
											else:
												if i[-1] == bacena_kartap2[-1][-1]:
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
													draw_text("MORAŠ PRATITI PRAVILO POŠTOVANJA",font2,(255,255,255),250,150)
													pygame.display.update()
													time.sleep(2)
										else:
											draw_text("MORAŠ PRATITI PRAVILO POŠTOVANJA",font2,(255,255,255),250,150)
											pygame.display.update()
											time.sleep(2)
									if brojac_vrsteP1 == 2:
										brojac_vrsteP1 = 0
										if i[-1] == adut[0][-1]:
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
											draw_text("MORAŠ PRATITI PRAVILO POŠTOVANJA",font2,(255,255,255),250,150)
											pygame.display.update()
											time.sleep(2)
									if brojac_vrsteP1 == 3:
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
								if len(usporedba)  == 0:
									while ogranici_bacanje1 == 0:
										karte_crtanje.append(i)
										bacena_kartap1.append(i)
										bacena_karta_state ="da"
										usporedba.append(i)
										p1inv.remove(i)
										ogranici_bacanje1 =1
										ogranici_bacanje2 =1
										ogranici_zavrsi = 0
									
				if len(karte_crtanje) == 1 or len(karte_crtanje) == 2:
					if bacena_karta_state =="da":
						bacena_karta = Button(455,250,pygame.image.load("Desktop\projekt\karte\\"+ slike_karata[karte_crtanje[-1]]).convert_alpha(),0.18).draw()
				
				if promjena_reda == 1:
					draw_text(f"{igrač2ime} JE NA REDU",font2,(255,255,255),50,10)
					xos = 95
					for t in p2inv:
						karta = Button(xos,500,pygame.image.load("Desktop\projekt\karte\\"+ slike_karata[t]).convert_alpha(),0.18).draw()
						xos += 180
						if karta == True:
							if len(dek) != 0:
								while ogranici_bacanje2 == 1:
									karte_crtanje.append(t)
									bacena_kartap2.append(t)
									bacena_karta_state2 ="da"
									usporedba.append(t)
									p2inv.remove(t)
									ogranici_bacanje2 = 0
									ogranici_bacanje1 = 0
									ogranici_zavrsi = 0					
							if len(dek) == 0:
								if len(usporedba) != 0:
									for l in p2inv:
										if l[-1] == bacena_kartap1[-1][-1]:
											brojac_vrsteP2 = 1
										if brojac_vrsteP2 == 0:
											if l[-1] == adut[0][-1]:
												brojac_vrsteP2 = 2
									if brojac_vrsteP2 == 0:
										for s in p2inv:
											if s[-1] != bacena_kartap1[-1][-1] and s[-1] != adut[0][-1]:
												brojac_vrsteP2 = 3
									for z in p2inv:
										if z[-1] == bacena_kartap1[-1][-1] and vrijednosti_karata[z]>vrijednosti_karata[bacena_kartap1[-1]]:
											brojac_ibera2 = 1
									print(brojac_vrsteP2)
									if brojac_vrsteP2 == 1:
										brojac_vrsteP2 = 0
										if t[-1] == bacena_kartap1[-1][-1]:
											if brojac_ibera2 == 1:
												brojac_ibera2 = 0
												if t[-1] == bacena_kartap1[-1][-1] and vrijednosti_karata[t]>vrijednosti_karata[bacena_kartap1[-1]]:
													while ogranici_bacanje2 == 1:
														bacena_kartap2.append(t)
														karte_crtanje.append(t)
														bacena_karta_state2 ="da"
														usporedba.append(t)
														p2inv.remove(t)
														ogranici_bacanje2 = 0
														ogranici_bacanje1 = 0
														ogranici_zavrsi = 0
														
												else:
													draw_text("MORAŠ PRATITI PRAVILO IBEROVANJA",font2,(255,255,255),250,150)
													pygame.display.update()
													time.sleep(2)
											else:
												if t[-1] == bacena_kartap1[-1][-1]:
													while ogranici_bacanje2 == 1:
														bacena_kartap2.append(t)
														karte_crtanje.append(t)
														bacena_karta_state2 ="da"
														usporedba.append(t)
														p2inv.remove(t)
														ogranici_bacanje2 = 0
														ogranici_bacanje1 = 0
														ogranici_zavrsi = 0
															
												else:
													draw_text("MORAŠ PRATITI PRAVILO POŠTOVANJA",font2,(255,255,255),250,150)
													screen.display.update()
													time.sleep(2)
										else:
											draw_text("MORAŠ PRATITI PRAVILO POŠTOVANJA",font2,(255,255,255),250,150)
											pygame.display.update()
											time.sleep(2)
									if brojac_vrsteP2 == 2:
										brojac_vrsteP2 = 0
										if t[-1] == adut[0][-1]:
											while ogranici_bacanje2 == 1:
												bacena_kartap2.append(t)
												karte_crtanje.append(t)
												bacena_karta_state2 ="da"
												usporedba.append(t)
												p2inv.remove(t)
												ogranici_bacanje2 = 0
												ogranici_bacanje1 = 0
												ogranici_zavrsi = 0
												
										else:
											draw_text("MORAŠ PRATITI PRAVILO POŠTOVANJA",font2,(255,255,255),250,150)
											pygame.display.update()
											time.sleep(2)

									if brojac_vrsteP2 == 3:
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
								if len(usporedba)  == 0:
									while ogranici_bacanje2 == 1:
										bacena_kartap2.append(t)
										karte_crtanje.append(t)
										bacena_karta_state2 ="da"
										usporedba.append(t)
										p2inv.remove(t)
										ogranici_bacanje2 = 0
										ogranici_bacanje1 = 0
										ogranici_zavrsi = 0
								
				if len(karte_crtanje) == 1 or len(karte_crtanje) == 2:
					if bacena_karta_state2 =="da":
						bacena_karta = Button(455,250,pygame.image.load("Desktop\projekt\karte\\"+ slike_karata[karte_crtanje[-1]]).convert_alpha(),0.18).draw()
			
				if ogranici_zavrsi == 0:
					if btn_zavrsi_bacanje.draw() == True:#ako se klikne gumb zavrsi bacanje promijeni se graficki prikaz inventorya igraca
						ogranici_zavrsi = 1
						ciji_red +=1
						zvanje_provjera = 0
						prihvati_zvanje = 0
						moguca_zvanja.clear()

						if len(karte_crtanje) == 2:
							karte_crtanje.clear()
						else:
							pass
						if stih == 1:
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

						if zavrsi_bacanje_kliknut == 0:
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
						if zavrsi_bacanje_kliknut == 2:
							if usporedba_red_bacanja1[-1] == "0":
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
								ogranici_bacanje1 = 0
								ogranici_bacanje2 = 1
								usporedba_red_bacanja1.append("1")
								usporedba_red_bacanja2.append("1")
							elif usporedba_red_bacanja2[-1] == "1":
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
								ogranici_bacanje1 = 0
								ogranici_bacanje2 = 1
								usporedba_red_bacanja2.append("0")
								usporedba_red_bacanja1.append("0")

			elif len(usporedba) == 2:
				if karte_crtanje[-2] ==  bacena_kartap1[-1] and karte_crtanje[-1] == bacena_kartap2[-1]:
					if usporedba[0][-1] == usporedba[1][-1]:
						if vrijednosti_karata[usporedba[0]]>vrijednosti_karata[usporedba[1]]:
							p1bodovi_runda.append(vrijednosti_karata[usporedba[0]]+vrijednosti_karata[usporedba[1]])
							stih = 1
							zavrsi_bacanje_kliknut = 2
							usporedba_red_bacanja1.append("0")
							usporedba_red_bacanja2.append("0")
							usporedba.clear()
							print(p1bodovi_runda,p2bodovi_runda)
						elif vrijednosti_karata[usporedba[0]]<vrijednosti_karata[usporedba[1]]:
							p2bodovi_runda.append(vrijednosti_karata[usporedba[0]]+vrijednosti_karata[usporedba[1]])
							stih = 1
							zavrsi_bacanje_kliknut = 2
							usporedba_red_bacanja2.append("1")
							usporedba_red_bacanja1.append("1")
							usporedba.clear()
							print(p1bodovi_runda,p2bodovi_runda)
						else:
							p1bodovi_runda.append(vrijednosti_karata[usporedba[0]]+vrijednosti_karata[usporedba[1]])
							stih = 1
							zavrsi_bacanje_kliknut = 2
							usporedba_red_bacanja1.append("0")
							usporedba_red_bacanja2.append("0")
							usporedba.clear()
							print(p1bodovi_runda,p2bodovi_runda)
					elif usporedba[0][-1] != usporedba[1][-1]:
						if usporedba[1][-1] == adut[0][-1] and usporedba[0][-1] != adut[0][-1]:
							p2bodovi_runda.append(vrijednosti_karata[usporedba[0]]+vrijednosti_karata[usporedba[1]])
							stih = 1
							zavrsi_bacanje_kliknut = 2
							usporedba_red_bacanja2.append("1")
							usporedba_red_bacanja1.append("1")
							usporedba.clear()
							print(p1bodovi_runda,p2bodovi_runda)
						elif usporedba[1][-1] == adut[0][-1] and usporedba[0][-1] == adut[0][-1]:
							if vrijednosti_karata[usporedba[0]]>vrijednosti_karata[usporedba[1]]:
								p1bodovi_runda.append(vrijednosti_karata[usporedba[0]]+vrijednosti_karata[usporedba[1]])
								stih = 1
								zavrsi_bacanje_kliknut = 2
								usporedba_red_bacanja1.append("0")
								usporedba_red_bacanja2.append("0")
								usporedba.clear()
								print(p1bodovi_runda,p2bodovi_runda)
							elif vrijednosti_karata[usporedba[0]]<vrijednosti_karata[usporedba[1]]:
								p2bodovi_runda.append(vrijednosti_karata[usporedba[0]]+vrijednosti_karata[usporedba[1]])
								stih = 1
								zavrsi_bacanje_kliknut = 2
								usporedba_red_bacanja2.append("1")
								usporedba_red_bacanja1.append("1")
								usporedba.clear()
								print(p1bodovi_runda,p2bodovi_runda)
						else:
							p1bodovi_runda.append(vrijednosti_karata[usporedba[0]]+vrijednosti_karata[usporedba[1]])
							stih = 1
							zavrsi_bacanje_kliknut = 2
							usporedba_red_bacanja1.append("0")
							usporedba_red_bacanja2.append("0")
							usporedba.clear()
							print(p1bodovi_runda,p2bodovi_runda)

				if karte_crtanje[-1] == bacena_kartap1[-1] and karte_crtanje[-2] == bacena_kartap2[-1]:
					if usporedba[0][-1] == usporedba[1][-1]:
						if vrijednosti_karata[usporedba[0]]>vrijednosti_karata[usporedba[1]]:
							p2bodovi_runda.append(vrijednosti_karata[usporedba[0]]+vrijednosti_karata[usporedba[1]])
							stih = 1
							zavrsi_bacanje_kliknut = 2
							usporedba_red_bacanja2.append("1")
							usporedba_red_bacanja1.append("1")
							usporedba.clear()
							print(p1bodovi_runda,p2bodovi_runda)
						elif vrijednosti_karata[usporedba[0]]<vrijednosti_karata[usporedba[1]]:
							p1bodovi_runda.append(vrijednosti_karata[usporedba[0]]+vrijednosti_karata[usporedba[1]])
							stih = 1
							zavrsi_bacanje_kliknut = 2
							usporedba_red_bacanja1.append("0")
							usporedba_red_bacanja2.append("0")
							usporedba.clear()
							print(p1bodovi_runda,p2bodovi_runda)
						else:
							p2bodovi_runda.append(vrijednosti_karata[usporedba[0]]+vrijednosti_karata[usporedba[1]])
							stih = 1
							zavrsi_bacanje_kliknut = 2
							usporedba_red_bacanja1.append("1")
							usporedba_red_bacanja2.append("1")
							usporedba.clear()
							print(p1bodovi_runda,p2bodovi_runda)
					elif usporedba[0][-1] != usporedba[1][-1]:
						if usporedba[1][-1] == adut[0][-1] and usporedba[0][-1] != adut[0][-1]:
							p1bodovi_runda.append(vrijednosti_karata[usporedba[0]]+vrijednosti_karata[usporedba[1]])
							stih = 1
							zavrsi_bacanje_kliknut = 2
							usporedba_red_bacanja2.append("0")
							usporedba_red_bacanja1.append("0")
							usporedba.clear()
							print(p1bodovi_runda,p2bodovi_runda)
						elif usporedba[1][-1] == adut[0][-1] and usporedba[0][-1] == adut[0][-1]:
							if vrijednosti_karata[usporedba[0]]>vrijednosti_karata[usporedba[1]]:
								p2bodovi_runda.append(vrijednosti_karata[usporedba[0]]+vrijednosti_karata[usporedba[1]])
								stih = 1
								zavrsi_bacanje_kliknut = 2
								usporedba_red_bacanja1.append("1")
								usporedba_red_bacanja2.append("1")
								usporedba.clear()
								print(p1bodovi_runda,p2bodovi_runda)
							elif vrijednosti_karata[usporedba[0]]<vrijednosti_karata[usporedba[1]]:
								p1bodovi_runda.append(vrijednosti_karata[usporedba[0]]+vrijednosti_karata[usporedba[1]])
								stih = 1
								zavrsi_bacanje_kliknut = 2
								usporedba_red_bacanja2.append("0")
								usporedba_red_bacanja1.append("0")
								usporedba.clear()
								print(p1bodovi_runda,p2bodovi_runda)
						else:
							p2bodovi_runda.append(vrijednosti_karata[usporedba[0]]+vrijednosti_karata[usporedba[1]])
							stih = 1
							zavrsi_bacanje_kliknut = 2
							usporedba_red_bacanja1.append("1")
							usporedba_red_bacanja2.append("1")
							usporedba.clear()
							print(p1bodovi_runda,p2bodovi_runda)
		
		#tipka za zvanje
		if ciji_red % 2 == 0:
			if promjena_reda == 0:
				for zvanje_moguce in p1inv:
					if zvanje_provjera < 6:
						zvanje_provjera +=1
						if zvanje_moguce[0] == "K" or zvanje_moguce[0] == "Q":
							if len(moguca_zvanja) > 0:
								for z in moguca_zvanja:
									if zvanje_moguce not in moguca_zvanja and zvanje_moguce[1] == z[1] and zvanje_moguce not in zvanje_baceno:
										prihvati_zvanje = 1
							moguca_zvanja.append(zvanje_moguce)
			elif promjena_reda == 1:
				for zvanje_moguce in p2inv:
					if zvanje_provjera < 6:
						zvanje_provjera +=1
						if zvanje_moguce[0] == "K" or zvanje_moguce[0] == "Q":
							if len(moguca_zvanja) > 0:
								for z in moguca_zvanja:
									if zvanje_moguce not in moguca_zvanja and zvanje_moguce[1] == z[1] and zvanje_moguce not in zvanje_baceno:
										prihvati_zvanje = 1
							moguca_zvanja.append(zvanje_moguce)
                            
		if prihvati_zvanje == 1:
			btn_zvanje = Button(100,265,zvanje_slika, 0.5)
			if btn_zvanje.draw() == True:
				menu_state ="zvanje"
			#drzi menu zvanje otvorenim
			if menu_state == "zvanje":
				zvanje()	

		#ZATVARANJE
		if len(dek) > 2 and len(p1inv) > 0:
			if ciji_red % 2 == 0:	
				zatvaranje_btn = Button(50,430,zatvaranje_slika, 0.5)
				if zatvaranje_btn.draw() == True:
					zatvaranje_tekst = "da"
					if promjena_reda == 0:
						zatvara = "1"
					if promjena_reda == 1:
						zatvara = "2"
					dek.clear()

		if zatvaranje_tekst == "da":
			draw_text(f"ZATVARANJE!",font3,(255,255,255),300,20)

		#KRAJ RUNDE	
		if (sum(p1bodovi_runda) >= 66 or sum(p2bodovi_runda) >= 66) or ((zatvara == "1" or zatvara == "2") and len(p1inv) == 0 and len(p2inv) == 0 and sum(p1bodovi_runda) < 66 and sum(p2bodovi_runda) < 66):
			kraj_runde_btn = Button(800,250,kraj_slika, 0.5)
			if kraj_runde_btn.draw() == True:
				menu_state = "kraj_runde"
				if menu_state == "kraj_runde":
					stari_bodovi1 = p1bodovi
					stari_bodovi2 = p2bodovi
					kraj_runde()
		
		pygame.display.update()
	pygame.quit()


def pravila():#window za popis pravila igre
	global menu_state
	novi_prozor = pygame.display.set_mode((1024,768))
	novi_prozor.blit(pozadina2_slika, (0,0))

	btn_povratak = Button(0,30,povratak_btn_slika,0.5)
	if btn_povratak.draw() == True:
		menu_state = "main"
	if menu_state =="main":
		main()

def zvanje():
	ogranici_zvanje = 0
	ogranici_zbroj = 0
	zvanje_state = "0"
	global p1bodovi_runda
	global p2bodovi_runda
	global promjena_reda
	global menu_state
	global zvanje_baceno
	global prihvati_zvanje
	global zvanje_provjera
	global moguca_zvanja
	clock = pygame.time.Clock()
	run = True
	while run:
		clock.tick(FPS)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
		novi_prozor = pygame.display.set_mode((1024,768))
		novi_prozor.blit(background_slika, (0,0))
		draw_text(f"ZVANJE",font3,(255,255,255),400,80)
		xos = 95
		if promjena_reda == 0:
			for i in p1inv:
				karta = Button(xos,500,pygame.image.load("Desktop\projekt\karte\\"+ slike_karata[i]).convert_alpha(),0.18).draw()
				xos += 180
				if karta == True:
					if ogranici_zvanje < 2:
						if i not in zvanje_baceno:
							if i[0] == "K" or i[0] == "Q":
								zvanje_baceno.append(i)
								ogranici_zvanje += 1


		else:
			for t in p2inv:
				karta = Button(xos,500,pygame.image.load("Desktop\projekt\karte\\"+ slike_karata[t]).convert_alpha(),0.18).draw()
				xos += 180
				if karta == True:
					if ogranici_zvanje < 2:
						if t not in zvanje_baceno:
							if t[0] == "K" or t[0] == "Q":
								zvanje_baceno.append(t)
								ogranici_zvanje += 1

		if ogranici_zvanje == 0 and len(zvanje_baceno) % 2 == 1:
			zvanje_baceno.remove(zvanje_baceno[-1])

		if ogranici_zvanje == 2:
			if zvanje_baceno[-2][0] != zvanje_baceno[-1][0]:
				print(zvanje_baceno[-2])
				print(zvanje_baceno[-1])
				if zvanje_baceno[-2][1] == zvanje_baceno[-1][1] and zvanje_baceno[-1][1] == adut[0][-1]:
					zvanje_state = "1"
					if ogranici_zbroj == 0:
						if promjena_reda == 0:
							p1bodovi_runda.append(40)
							ogranici_zbroj +=1
							print(p1bodovi_runda)
						else:
							p2bodovi_runda.append(40)
							ogranici_zbroj +=1
							print(p2bodovi_runda)
				elif zvanje_baceno[-2][1] == zvanje_baceno[-1][1] and zvanje_baceno[-1][1] != adut[0][-1]:
					zvanje_state = "2"
					if ogranici_zbroj == 0:
						if promjena_reda == 0:
							p1bodovi_runda.append(20)
							ogranici_zbroj +=1
							print(p1bodovi_runda)
						else:
							p2bodovi_runda.append(20)
							ogranici_zbroj +=1
							print(p2bodovi_runda)
				else:
					zvanje_baceno.remove(zvanje_baceno[-1])
					zvanje_baceno.remove(zvanje_baceno[-1])
			else:
				zvanje_baceno.remove(zvanje_baceno[-1])
				zvanje_baceno.remove(zvanje_baceno[-1])
			ogranici_zvanje = 3

		if zvanje_state == "1":
			draw_text(f"Zvanje je uspješno! Dobivaš 40",font2,(255,255,255),400,150)
		if zvanje_state == "2":
			draw_text(f"Zvanje je uspješno! Dobivaš 20",font2,(255,255,255),400,150)
		
		iz_zvanje_u_igru_btn = Button(280,300,vrati_se_slika, 1)
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
	global zadnja_karta
	global brojac_ibera
	global brojac_ibera2
	global stih
	global ogranici_zavrsi

	clock = pygame.time.Clock()
	run = True
	while run:
		clock.tick(FPS)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
		novi_prozor = pygame.display.set_mode((1024,768))
		novi_prozor.blit(pozadina2_slika, (0,0))
		if zatvara == "1" and p2bodovi == stari_bodovi2:
			if sum(p1bodovi_runda) < 66:
				if sum(p2bodovi_runda) == 0:
					p2bodovi = stari_bodovi2 - 3
				if sum(p2bodovi_runda) > 0 and sum(p2bodovi_runda) < 33:
					p2bodovi = stari_bodovi2 - 2
				if sum(p2bodovi_runda) > 33:
					p2bodovi = stari_bodovi2 - 1
				if sum(p2bodovi_runda) == 33:
					if zadnja_karta[0][0] > zadnja_karta[0][1]:
						p1bodovi = stari_bodovi1 - 1
					else:
						p2bodovi = stari_bodovi2 - 1
			else:
				zatvara = "0"
		elif zatvara == "2" and p1bodovi == stari_bodovi1:
			if sum(p2bodovi_runda) < 66:
				if sum(p1bodovi_runda) == 0:
					p1bodovi = stari_bodovi1 - 3
				if sum(p1bodovi_runda) > 0 and sum(p2bodovi_runda) < 33:
					p1bodovi = stari_bodovi1 - 2
				if sum(p1bodovi_runda) > 33:
					p1bodovi = stari_bodovi1 - 1
				if sum(p2bodovi_runda) == 33:
					if zadnja_karta[0][0] > zadnja_karta[0][1]:
						p1bodovi = stari_bodovi1 - 1
					else:
						p2bodovi = stari_bodovi2 - 1
			else:
				zatvara = "0"
		elif zatvara == "0":
			if sum(p1bodovi_runda) > sum(p2bodovi_runda) and stari_bodovi1 == p1bodovi:
				if sum(p2bodovi_runda) == 0:
					p1bodovi = stari_bodovi1 - 3
				if sum(p2bodovi_runda) > 0 and sum(p2bodovi_runda) < 33:
					p1bodovi = stari_bodovi1 - 2
				if sum(p2bodovi_runda) > 33:
					p1bodovi = stari_bodovi1 - 1
			if sum(p2bodovi_runda) > sum(p1bodovi_runda) and stari_bodovi2 == p2bodovi:
				if sum(p1bodovi_runda) == 0:
					p2bodovi = stari_bodovi2 - 3
				if sum(p1bodovi_runda) > 0 and sum(p1bodovi_runda) < 33:
					p2bodovi = stari_bodovi2 - 2
				if sum(p1bodovi_runda) > 33:
					p2bodovi = stari_bodovi2 - 1
		novi_prozor.blit(kraj_runde_slika, (0,0))

		draw_text(f"{igrač1ime}",font4,(250,250,250),500,252)
		draw_text(f"{igrač2ime}",font4,(250,250,250),820,252)
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
		usporedba2.clear()
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

		if p1bodovi <= 0 or p2bodovi <= 0: #gleda je li runda gotova
			draw_text(f"KRAJ IGRE",font3,(255,255,255),300,80)
			nastavi_rundu_btn = Button(280,600,nastavi_slika, 1)
			if p1bodovi < 0:
				p1bodovi = 0
			if p2bodovi < 0:
				p2bodovi = 0
			if nastavi_rundu_btn.draw() == True:
				menu_state = "pobjeda"
			if menu_state == "pobjeda":
				#reseta bodove runde
				p1bodovi_runda.clear()
				p2bodovi_runda.clear()
				zatvara = "0"
				zadnja_karta = []
				pobjeda()
		else: #nastavlja rundu ako nije gotova runda
			draw_text(f"KRAJ RUNDE",font3,(255,255,255),300,80)
			nastavi_rundu_btn = Button(280,600,nastavi_slika, 1)
			if nastavi_rundu_btn.draw() == True:
				menu_state = "nastavi_sedam"
			if menu_state == "nastavi_sedam":
				#reseta bodove runde
				p1bodovi_runda.clear()
				p2bodovi_runda.clear()
				zatvara = "0"
				zadnja_karta = []
				igra()
		pygame.display.update()
	pygame.quit()

def pobjeda():
	global p1pobjeda
	global p2pobjeda
	global p1bodovi
	global p2bodovi
	global ogranici_bodovanje
	clock = pygame.time.Clock()
	run = True
	while run:
		clock.tick(FPS)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
		screen.blit(pozadina2_slika, (0,0))
		if p1bodovi <= 0:
			draw_text(f"Pobijedio je {igrač1ime}!",font3,(255,255,255),280,150)
			if ogranici_bodovanje == 0:
				p1bodovi = 0
				p1pobjeda += 1
				ogranici_bodovanje +=1
		elif p2bodovi <= 0:
			draw_text(f"Pobijedio je {igrač2ime}!",font3,(255,255,255),280,150)
			if ogranici_bodovanje == 0:
				p2bodovi = 0
				p2pobjeda += 1
				ogranici_bodovanje += 1
		draw_text(f"STATISTIKA",font4,(255,255,255),400,40)
		screen.blit(kraj_igre_tablica, (0,0))
		draw_text(f"{igrač1ime}",font4,(250,250,250),500,252)
		draw_text(f"{igrač2ime}",font4,(250,250,250),820,252)
		draw_text(f"{p1pobjeda}",font4,(250,250,250),550,340)
		draw_text(f"{p2pobjeda}",font4,(250,250,250),870,340)
		zavrsi_rundu_btn = Button(280,700,vrati_se_slika, 0.5)
		if zavrsi_rundu_btn.draw() == True:
			ogranici_bodovanje = 0
			main()
		pygame.display.update()
	pygame.quit()

def main():#loop koji pokrece igru
	global menu_state
	global p1bodovi
	global p2bodovi
	global prikazi_video
	clock = pygame.time.Clock()
	run = True
	while run:
		clock.tick(FPS)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
		
		video.draw(screen, (0, 0))
		igraj_btn = Button(290,330,igra_slika, 1)
		pravila_btn = Button(290,450,pravila_slika, 1)
		if igraj_btn.draw() == True:
			menu_state = "opcije"
		if menu_state == "opcije":
			opcije()
		if pravila_btn.draw() == True:
			menu_state = "pravila"
		if menu_state =="pravila":
			pravila()

		pygame.display.update()
	pygame.quit()

def opcije():
	global menu_state
	global p1bodovi
	global p2bodovi
	clock = pygame.time.Clock()
	run = True
	while run:
		clock.tick(FPS)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
		screen.blit(pozadina2_slika, (0,0))
		sedam_bodova_btn = Button(350,400,sedam_bodova_slika,1.2)		
		devet_bodova_btn = Button(580,400,devet_bodova_slika,1.2)
		btn_povratak = Button(0,30,povratak_btn_slika,0.5)
		draw_text(f"ODABERI BROJ BODOVA",font3,(255,255,255),100,200)
		if btn_povratak.draw() == True:
			menu_state = "main"
		if menu_state =="main":
			main()
		if sedam_bodova_btn.draw() == True:
			menu_state = "igra"
			p1bodovi = 7
			p2bodovi = 7
		if menu_state == "igra":
			igra()
		if devet_bodova_btn.draw() == True:
			menu_state = "igra"
			p1bodovi = 9
			p2bodovi = 9
		pygame.display.update()
	pygame.quit()

main()
