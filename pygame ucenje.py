import pygame 
import random
import time
from pygame import Surface

pygame.init()
igrač1ime = input("Unesi ime: ").upper()
while len(igrač1ime)>7 or len(igrač1ime)==0:
    igrač1ime = input("Unesi ime koje ima manje od 7 znakova i više od 0: ").upper()
igrač2ime = input("Unesi ime: ").upper()
while len(igrač2ime)>7 or len(igrač2ime)==0:
    igrač2ime = input("Unesi ime koje ima manje od 7 znakova i više od 0: ").upper()

zelena = (0,100,0)
screen = pygame.display.set_mode((1024,768))
pygame.display.set_caption("ŠNAPS")
FPS = 60
font = pygame.font.Font(None, 60)
font2 = pygame.font.Font(None, 40)
font3 = pygame.font.Font(None, 100)
font4 = pygame.font.Font(None, 80)
text_color = (255,255,255)

#slike za buttone
sedam_bodova_slika = pygame.image.load("Desktop\projekt\sedam.png").convert_alpha()
devet_bodova_slika = pygame.image.load("Desktop\projekt\devet.png").convert_alpha()
povratak_btn_slika = pygame.image.load("Desktop\projekt\povratak_btn.png").convert_alpha()
promijeni_red_btn_slika = pygame.image.load("Desktop\projekt\promijeni_btn.png").convert_alpha()
pravila_slika = pygame.image.load("Desktop\projekt\pravila_btn.png").convert_alpha()
kraj_runde_slika = pygame.image.load("Desktop\projekt\kraj_runde_table.png").convert_alpha()

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
btn_sedam_bodova = Button(300,240,sedam_bodova_slika,1)		
btn_devet_bodova = Button(600,240,devet_bodova_slika,1)
btn_povratak = Button(40,50,povratak_btn_slika,1)
btn_pravila = Button(430,550,pravila_slika,0.7)
btn_podijeli_karte = Button(800,350,sedam_bodova_slika,0.5)
btn_zavrsi_bacanje = Button(460,80,promijeni_red_btn_slika,1)
btn_izvuci_kartu = Button(800,250,sedam_bodova_slika,0.5)
btn_zvanje = Button(200,350,sedam_bodova_slika, 0.5)

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

brojac_ibera = 0
brojac_ibera2 = 0

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

		global brojac_ibera
		global brojac_ibera2
		screen.fill(zelena)
		draw_text(f"{igrač1ime}:{p1bodovi}",font2,text_color,880,10)
		draw_text(f"{igrač2ime}:{p2bodovi}",font2,text_color,880,50)

		if btn_podijeli_karte.draw() == True:#ako se klikne taj gumb onda se podijeli karte s pomocu funkcije dijeljenje_karata
			while btn_podijeli_karte_crtaj % 2 == 0:
				dijeljenje_karata()
				karte_state = "prikaz"
				btn_podijeli_karte_crtaj += 1
		
		#tipka za zvanje
		if btn_zvanje.draw() == True:
			menu_state ="pravila"

		#tipka za zvanje
		if btn_zvanje.draw() == True:
			menu_state ="pravila"

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
					xos = 50
					for i in p1inv:
						karta = Button(xos,500,pygame.image.load("Desktop\projekt\slike\\"+ slike_karata[i]).convert_alpha(),0.2).draw()
						xos += 200
						if karta == True:
							if len(dek) != 0 or (len(p1inv) == 5 or len(p2inv) == 5):		
								while ogranici_bacanje1 == 0:
									karte_crtanje.append(i)
									bacena_kartap1.append(i)
									bacena_karta_state ="da"
									usporedba.append(i)
									p1inv.remove(i)
									ogranici_bacanje1 =1
									ogranici_bacanje2 =1					
							if len(dek) == 0 and len(p1inv) <5 and len(p2inv) <5:
								if len(usporedba) != 0:
									for m in p1inv:
										if m[-1] == usporedba[-1][-1]:
											brojac_vrsteP1 = 1
										if brojac_vrsteP1 == 0:
											if m[-1] == adut[0][-1] and m[-1] != usporedba[-1][-1]:
												brojac_vrsteP1 = 2
											elif m[-1] != usporedba[-1][-1] and m[-1] != adut[0][-1]:
												brojac_vrsteP1 = 3
									for h in p1inv:
										if h[-1] == usporedba[-1][-1] and vrijednosti_karata[h]>vrijednosti_karata[usporedba[0]]:
											brojac_ibera = 1
									if brojac_vrsteP1 == 1:
										brojac_vrsteP1 = 0
										if brojac_ibera == 1:
											brojac_ibera = 0
											if i[-1] == usporedba[-1][-1] and vrijednosti_karata[i]>vrijednosti_karata[usporedba[0]]:
												while ogranici_bacanje1 == 0:
													karte_crtanje.append(i)
													bacena_kartap1.append(i)
													bacena_karta_state ="da"
													usporedba.append(i)
													p1inv.remove(i)
													ogranici_bacanje1 =1
													ogranici_bacanje2 =1
											else:
												print("Moraš pratiti pravilo iberovanja")
										else:
											if i[-1] == usporedba[-1][-1]:
												while ogranici_bacanje1 == 0:
													karte_crtanje.append(i)
													bacena_kartap1.append(i)
													bacena_karta_state ="da"
													usporedba.append(i)
													p1inv.remove(i)
													ogranici_bacanje1 =1
													ogranici_bacanje2 =1
														
											else:
												print("Moraš pratiti pravilo poštovanja")

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
												
										else:
											print("Moraš pratiti pravilo poštovanja")
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
								if len(usporedba)  == 0:
									while ogranici_bacanje1 == 0:
										karte_crtanje.append(i)
										bacena_kartap1.append(i)
										bacena_karta_state ="da"
										usporedba.append(i)
										p1inv.remove(i)
										ogranici_bacanje1 =1
										ogranici_bacanje2 =1
									
						if btn_izvuci_kartu.draw() == True:
							if ogranici_izvlacenje1 == 0:
								if len(dek) != 0:
									p1inv.append(random.choice(dek))
									dek.remove(p1inv[len(p1inv)-1])
									print(p1inv,dek)
									ogranici_izvlacenje1 = 1
									ogranici_izvlacenje2 = 1
								else:
									print("dek je prazan")
				if len(karte_crtanje) == 1 or len(karte_crtanje) == 2:
					if bacena_karta_state =="da":
						bacena_karta = Button(400,250,pygame.image.load("Desktop\projekt\slike\\"+ slike_karata[karte_crtanje[-1]]).convert_alpha(),0.2).draw()
				
				if promjena_reda == 1:
					draw_text(f"{igrač2ime} JE NA REDU",font2,(255,255,255),50,10)
					xos = 50
					for t in p2inv:
						karta = Button(xos,500,pygame.image.load("Desktop\projekt\slike\\"+ slike_karata[t]).convert_alpha(),0.2).draw()
						xos += 200
						if karta == True:
							if len(dek) != 0 or (len(p1inv) == 5 or len(p2inv) == 5):		
								while ogranici_bacanje2 == 1:
									karte_crtanje.append(t)
									bacena_kartap2.append(t)
									bacena_karta_state2 ="da"
									usporedba.append(t)
									p2inv.remove(t)
									ogranici_bacanje2 = 0
									ogranici_bacanje1 = 0					
							if len(dek) == 0 and len(p1inv) <5 and len(p2inv) <5:
								if len(usporedba) != 0:
									for l in p2inv:
										if l[-1] == usporedba[-1][-1]:
											brojac_vrsteP2 = 1
										if brojac_vrsteP2 == 0:
											if l[-1] == adut[0][-1] and l[-1] != usporedba[-1][-1]:
												brojac_vrsteP2 = 2
											elif l[-1] != usporedba[-1][-1] and l[-1] != adut[0][-1]:
												brojac_vrsteP2 = 3
									for z in p2inv:
										if z[-1] == usporedba[-1][-1] and vrijednosti_karata[z]>vrijednosti_karata[usporedba[0]]:
											brojac_ibera2 = 1

									if brojac_vrsteP2 == 1:
										brojac_vrsteP2 = 0
										if brojac_ibera2 == 1:
											brojac_ibera2 = 0
											if t[-1] == usporedba[-1][-1] and vrijednosti_karata[t]>vrijednosti_karata[usporedba[0]]:
												while ogranici_bacanje2 == 1:
													bacena_kartap2.append(t)
													karte_crtanje.append(t)
													bacena_karta_state2 ="da"
													usporedba.append(t)
													p2inv.remove(t)
													ogranici_bacanje2 = 0
													ogranici_bacanje1 = 0
													
											else:
												print("Moraš pratiti pravilo iberovanja")
										else:
											if t[-1] == usporedba[-1][-1]:
												while ogranici_bacanje2 == 1:
													bacena_kartap2.append(t)
													karte_crtanje.append(t)
													bacena_karta_state2 ="da"
													usporedba.append(t)
													p2inv.remove(t)
													ogranici_bacanje2 = 0
													ogranici_bacanje1 = 0
														
											else:
												print("Moraš pratiti pravilo poštovanja")

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
												
										else:
											print("Moraš pratiti pravilo poštovanja")

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
								if len(usporedba)  == 0:
									while ogranici_bacanje2 == 1:
										bacena_kartap2.append(t)
										karte_crtanje.append(t)
										bacena_karta_state2 ="da"
										usporedba.append(t)
										p2inv.remove(t)
										ogranici_bacanje2 = 0
										ogranici_bacanje1 = 0
						if btn_izvuci_kartu.draw() == True:
							if ogranici_izvlacenje2 == 1:
								if len(dek) != 0:
									p2inv.append(random.choice(dek))
									dek.remove(p2inv[len(p2inv)-1])
									print(p2inv,dek)
									ogranici_izvlacenje1 = 0
									ogranici_izvlacenje2 = 0
								else:
									print("dek je prazan")
								
				if len(karte_crtanje) == 1 or len(karte_crtanje) == 2:
					if bacena_karta_state2 =="da":
						bacena_karta = Button(400,250,pygame.image.load("Desktop\projekt\slike\\"+ slike_karata[karte_crtanje[-1]]).convert_alpha(),0.2).draw()
			
				if btn_zavrsi_bacanje.draw() == True:#ako se klikne gumb zavrsi bacanje promijeni se graficki prikaz inventorya igraca
					if len(karte_crtanje) == 2:
						karte_crtanje.clear()
					if zavrsi_bacanje_kliknut == 0:
						promjena_reda =1
						pygame.draw.rect(screen,zelena, pygame.Rect(0,0,1024,768))
						draw_text(f"{igrač2ime} MOŽE IGRATI ZA 5 SEKUNDI",font,(255,255,255),110,330)
						pygame.display.update()
						time.sleep(2)
						zavrsi_bacanje_kliknut = 1
					if zavrsi_bacanje_kliknut == 2:
						if usporedba_red_bacanja1[-1] == "1":
							pygame.draw.rect(screen,zelena, pygame.Rect(0,0,1024,768))
							draw_text(f"{igrač1ime} MOŽE IGRATI ZA 5 SEKUNDI",font,(255,255,255),110,330)
							pygame.display.update()
							time.sleep(2)
							promjena_reda = 0
							ogranici_bacanje1 = 0
							ogranici_bacanje2 = 1
							ogranici_izvlacenje1 = 0
							ogranici_izvlacenje2 = 1
							usporedba_red_bacanja1.append("0")
						else:
							usporedba_red_bacanja2.append("1")
							zavrsi_bacanje_kliknut = 3
					if zavrsi_bacanje_kliknut  == 3:
						if usporedba_red_bacanja2[-1] == "1":
							pygame.draw.rect(screen,zelena, pygame.Rect(0,0,1024,768))
							draw_text(f"{igrač2ime} MOŽE IGRATI ZA 5 SEKUNDI",font,(255,255,255),110,330)
							pygame.display.update()
							time.sleep(2)
							promjena_reda = 1
							ogranici_bacanje1 = 0
							ogranici_bacanje2 = 1
							ogranici_izvlacenje1 = 0
							ogranici_izvlacenje2 = 1
							usporedba_red_bacanja2.append("0")
						else:
							usporedba_red_bacanja1.append("1")
							zavrsi_bacanje_kliknut = 2

			elif len(usporedba) == 2:
				if karte_crtanje[-2] ==  bacena_kartap1[-1] and karte_crtanje[-1] == bacena_kartap2[-1]:
					if vrijednosti_karata[usporedba[0]]>vrijednosti_karata[usporedba[1]]:
						p1bodovi_runda.append(vrijednosti_karata[usporedba[0]]+vrijednosti_karata[usporedba[1]])
						usporedba_red_bacanja1.append("1")
						zavrsi_bacanje_kliknut = 2
						usporedba.clear()
						print(p1bodovi_runda,p2bodovi_runda)
					elif vrijednosti_karata[usporedba[0]]<vrijednosti_karata[usporedba[1]]:
						p2bodovi_runda.append(vrijednosti_karata[usporedba[0]]+vrijednosti_karata[usporedba[1]])
						usporedba_red_bacanja2.append("1")
						zavrsi_bacanje_kliknut = 3
						usporedba.clear()
						print(p1bodovi_runda,p2bodovi_runda)
					else:
						print("Neš ne radi")
						usporedba.clear()
						print(p1bodovi_runda,p2bodovi_runda)
				if karte_crtanje[-1] == bacena_kartap1[-1] and karte_crtanje[-2] == bacena_kartap2[-1]:
					if vrijednosti_karata[usporedba[0]]>vrijednosti_karata[usporedba[1]]:
						p2bodovi_runda.append(vrijednosti_karata[usporedba[0]]+vrijednosti_karata[usporedba[1]])
						usporedba_red_bacanja2.append("1")
						zavrsi_bacanje_kliknut = 2
						usporedba.clear()
						print(p1bodovi_runda,p2bodovi_runda)
					elif vrijednosti_karata[usporedba[0]]<vrijednosti_karata[usporedba[1]]:
						p1bodovi_runda.append(vrijednosti_karata[usporedba[0]]+vrijednosti_karata[usporedba[1]])
						usporedba_red_bacanja1.append("1")
						zavrsi_bacanje_kliknut = 3
						usporedba.clear()
						print(p1bodovi_runda,p2bodovi_runda)
					else:
						print("Neš ne radi")
						usporedba.clear()
						print(p1bodovi_runda,p2bodovi_runda)
				print(len(dek))
		if len(p1inv) == 0 and len(p2inv) == 0 and len(dek) == 0:
			print("gotova runda")
		if sum(p1bodovi_runda) >= 66 or sum(p2bodovi_runda) >= 66:
			kraj_runde_btn = Button(200,250,sedam_bodova_slika, 0.5)
			if kraj_runde_btn.draw() == True:
				menu_state = "kraj_runde"
				if menu_state == "kraj_runde":
					stari_bodovi1 = p1bodovi
					stari_bodovi2 = p2bodovi
					kraj_runde()
		
		pygame.display.update()
	pygame.quit()


def pravila():#window za popis pravila igre
	novi_prozor = pygame.display.set_mode((1024,768))
	novi_prozor.fill(zelena)

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
	clock = pygame.time.Clock()
	run = True
	while run:
		clock.tick(FPS)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
		novi_prozor = pygame.display.set_mode((1024,768))
		novi_prozor.fill(zelena)
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

		draw_text(f"{igrač1ime}",font4,(250,250,250),550,252)
		draw_text(f"{igrač2ime}",font4,(250,250,250),870,252)
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

		
		if p1bodovi <= 0 or p2bodovi <= 0: #gleda je li runda gotova
			draw_text(f"KRAJ IGRE",font3,(255,255,255),300,80)
			if p1bodovi <= 0:
				p1bodovi = 0
				draw_text(f"Pobjedio je {igrač1ime}!",font,(255,255,255),10,30)
				p1pobjeda += 1
			else:
				p2bodovi = 0
				draw_text(f"Pobjedio je {igrač2ime}!",font,(255,255,255),10,30)
				p2pobjeda += 1
			zavrsi_rundu_btn = Button(480,600,devet_bodova_slika, 0.5)
			if zavrsi_rundu_btn.draw() == True:
				menu_state = "main"
			if menu_state == "main":
				#reseta bodove runde
				p1bodovi_runda.clear()
				p2bodovi_runda.clear()
				main()
		else: #nastavlja rundu ako nije gotova runda
			draw_text(f"KRAJ RUNDE",font3,(255,255,255),300,80)
			nastavi_rundu_btn = Button(480,600,sedam_bodova_slika, 0.5)
			if nastavi_rundu_btn.draw() == True:
				menu_state = "nastavi_sedam"
			if menu_state == "nastavi_sedam":
				#reseta bodove runde
				p1bodovi_runda.clear()
				p2bodovi_runda.clear()
				igra()
		pygame.display.update()
	pygame.quit()

def main():#loop koji pokrece igru
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

		screen.fill(zelena)
		draw_text("ODABERI POČETAN BROJ BODOVA",font,text_color,170,100)
		if menu_state == "main":#provjerave jesam li u glavnom menuu ili u jednom od prozora za igru

			if btn_pravila.draw() == True:
				menu_state ="pravila"
			if btn_sedam_bodova.draw() == True:
				menu_state ="povratak_sedam"
			if btn_devet_bodova.draw() == True:
				menu_state ="povratak_devet"

		if menu_state =="pravila":
			pravila()
			if btn_povratak.draw() == True:
				menu_state = "main"

		if menu_state == "povratak_sedam":
			p1bodovi = 7
			p2bodovi = 7
			igra()
			if btn_povratak.draw() == True:
				menu_state = "main"

		if menu_state == "povratak_devet":
			p1bodovi = 9
			p2bodovi = 9
			igra()
			if btn_povratak.draw() == True:
				menu_state = "main"

		pygame.display.update()
	pygame.quit()

main()
