import pygame 
from pygame import Surface
import random
import os

pygame.init()
igrač1ime = input("Unesi ime: ")
while len(igrač1ime)>7 or len(igrač1ime)==0:
    igrač1ime = input("Unesi ime koje ima manje od 7 znakova i više od 0: ")
igrač2ime = input("Unesi ime: ")
while len(igrač2ime)>7 or len(igrač2ime)==0:
    igrač2ime = input("Unesi ime koje ima manje od 7 znakova i više od 0: ")

zelena = (0,100,0)
screen = pygame.display.set_mode((1024,768))
pygame.display.set_caption("ŠNAPS")
FPS = 60
font = pygame.font.Font(None, 60)
font2 = pygame.font.Font(None, 40)
text_color = (255,255,255)
ciji_red = 1
sedam_bodova_slika = pygame.image.load("Desktop\projekt\start_btn.png").convert_alpha()
devet_bodova_slika = pygame.image.load("Desktop\projekt\exit_btn.png").convert_alpha()
povratak_btn_slika = pygame.image.load("Desktop\projekt\povratak_btn.png").convert_alpha()
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

def dijeljenje_karata():#podijeli random karte igračima
	for i in range(3):
		p1inv.append(random.choice(dek))
		dek.remove(p1inv[i])
	for i in range(3): 
		p2inv.append(random.choice(dek))
		dek.remove(p2inv[i])
	adut.append(random.choice(dek))
	dek.remove(adut[0])
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
btn_sedam_bodova = Button(400,180,sedam_bodova_slika,1)		
btn_devet_bodova = Button(600,180,devet_bodova_slika,1)
btn_povratak = Button(10,10,povratak_btn_slika,1)
btn_pravila = Button(450,480,sedam_bodova_slika,1)
btn_podijeli_karte = Button(800,350,sedam_bodova_slika,1)
btn_zavrsi_bacanje = Button(512,70,sedam_bodova_slika,1)


menu_state ="main" #pomaže za mijenjanje prozora
karte_state ="ne_prikaz"
sakri_kartu ="ne"
sakri_kartu2 ="keks"
promjena_reda = 0
prekri_kartu = pygame.Surface((200,500))
prekri_kartu2 = pygame.Surface((200,500))

def kliknut_sedam():#window za igru od 7 bodova
	run = True
	while run:
		clock = pygame.time.Clock()
		clock.tick(FPS)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
		global ciji_red
		global karte_state
		global promjena_reda
		global prekri_kartu
		global sakri_kartu
		global sakri_kartu2
		global p1bodovi_runda
		global p2bodovi_runda
		screen.fill(zelena)
		p1bodovi = 7
		p2bodovi = 7
		draw_text(f"{igrač1ime}:{p1bodovi}",font2,text_color,880,10)
		draw_text(f"{igrač2ime}:{p2bodovi}",font2,text_color,880,50)

		if btn_podijeli_karte.draw() == True:#ako se klikne taj gumb onda se podijeli karte s pomocu funkcije dijeljenje_karata
			dijeljenje_karata()
			karte_state = "prikaz"

		if karte_state == "prikaz":#pomaze mi samo da prikazujem ili ne prikazujem kartu
			#prikaz karata
			if btn_zavrsi_bacanje.draw() == True:#ako se klikne gumb zavrsi bacanje promijeni se graficki prikaz inventorya igraca
				promjena_reda += 1

			if len(usporedba) != 2:
				if promjena_reda %2 == 0:
					p1karta_1 = Button(50,500,pygame.image.load("Desktop\projekt\slike\\"+ slike_karata[p1inv[0]]).convert_alpha(),0.2).draw()
					if p1karta_1 == True:
						usporedba.append(p1inv[0])
						prekri_kartu.fill(zelena)
						sakri_kartu = "da"
					if sakri_kartu == "da":
						screen.blit(prekri_kartu, (50,500))
					p1karta_2 = Button(250,500,pygame.image.load("Desktop\projekt\slike\\"+ slike_karata[p1inv[1]]).convert_alpha(),0.2).draw()
					if p1karta_2 == True:
						usporedba.append(p1inv[1])
						prekri_kartu.fill(zelena)
						sakri_kartu = "da1"
					if sakri_kartu == "da1":
						screen.blit(prekri_kartu, (250,500))
					p1karta_3 = Button(450,500,pygame.image.load("Desktop\projekt\slike\\"+ slike_karata[p1inv[2]]).convert_alpha(),0.2).draw()
					if p1karta_3 == True:
						usporedba.append(p1inv[2])
						prekri_kartu.fill(zelena)
						sakri_kartu = "daa"
					if sakri_kartu == "daa":
						screen.blit(prekri_kartu, (450,500))
					p1karta_4 = Button(650,500,pygame.image.load("Desktop\projekt\slike\\"+ slike_karata[p1inv[3]]).convert_alpha(),0.2).draw()
					if p1karta_4 == True:
						usporedba.append(p1inv[3])
						prekri_kartu.fill(zelena)
						sakri_kartu = "nee"
					if sakri_kartu == "nee":
						screen.blit(prekri_kartu, (650,500))
					p1karta_5 = Button(850,500,pygame.image.load("Desktop\projekt\slike\\"+ slike_karata[p1inv[4]]).convert_alpha(),0.2).draw()
					if p1karta_5 == True:
						usporedba.append(p1inv[4])
						prekri_kartu.fill(zelena)
						sakri_kartu = "daaa"
					if sakri_kartu == "daaa":
						screen.blit(prekri_kartu, (850,500))
				else:
					p2karta_1 = Button(50,500,pygame.image.load("Desktop\projekt\slike\\"+ slike_karata[p2inv[0]]).convert_alpha(),0.2).draw()
					if p2karta_1 == True:
						usporedba.append(p2inv[0])
						prekri_kartu2.fill(zelena)
						sakri_kartu2 = "b"
					if sakri_kartu2 == "b":
						screen.blit(prekri_kartu2, (50,500))
					p2karta_2 = Button(250,500,pygame.image.load("Desktop\projekt\slike\\"+ slike_karata[p2inv[1]]).convert_alpha(),0.2).draw()
					if p2karta_2 == True:
						usporedba.append(p2inv[1])
						prekri_kartu2.fill(zelena)
						sakri_kartu2 = "bb"
					if sakri_kartu2 == "bb":
						screen.blit(prekri_kartu2, (250,500))
					p2karta_3 = Button(450,500,pygame.image.load("Desktop\projekt\slike\\"+ slike_karata[p2inv[2]]).convert_alpha(),0.2).draw()
					if p2karta_3 == True:
						usporedba.append(p2inv[2])
						prekri_kartu2.fill(zelena)
						sakri_kartu2 = "bbb"
					if sakri_kartu2 == "bbb":
						screen.blit(prekri_kartu2, (450,500))
					p2karta_4 = Button(650,500,pygame.image.load("Desktop\projekt\slike\\"+ slike_karata[p2inv[3]]).convert_alpha(),0.2).draw()
					if p2karta_4 == True:
						usporedba.append(p2inv[3])
						prekri_kartu2.fill(zelena)
						sakri_kartu2 = "bbbb"
					if sakri_kartu2 == "bbbb":
						screen.blit(prekri_kartu2, (650,500))
					p2karta_5 = Button(850,500,pygame.image.load("Desktop\projekt\slike\\"+ slike_karata[p2inv[4]]).convert_alpha(),0.2).draw()
					if p2karta_5 == True:
						usporedba.append(p2inv[4])
						prekri_kartu2.fill(zelena)
						sakri_kartu2 = "b1"
					if sakri_kartu2 == "b1":
						screen.blit(prekri_kartu2, (850,500))
			elif len(usporedba) == 2:
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
					usporedba.clear()
					print(p1bodovi_runda,p2bodovi_runda)

		pygame.display.update()
	pygame.quit()

def kliknut_devet():#window za igru od 9 bodova
	novi_prozor = pygame.display.set_mode((1024,768))
	novi_prozor.fill(zelena)
	p1bodovi = 9
	p2bodovi = 9
	draw_text(f"{igrač1ime}:{p1bodovi}",font2,text_color,880,10)
	draw_text(f"{igrač2ime}:{p2bodovi}",font2,text_color,880,50)
	if btn_podijeli_karte.draw() == True:
		dijeljenje_karata()

def pravila():#window za popis pravila igre
	novi_prozor = pygame.display.set_mode((1024,768))
	novi_prozor.fill(zelena)

def main():#loop koji pokrece igru
	global menu_state
	clock = pygame.time.Clock()
	run = True
	while run:
		clock.tick(FPS)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		screen.fill(zelena)
		draw_text("Odaberi početan broj bodova.",font,text_color,220,100)
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
			kliknut_sedam()
			if btn_povratak.draw() == True:
				menu_state = "main"

		if menu_state == "povratak_devet":
			kliknut_devet()
			if btn_povratak.draw() == True:
				menu_state = "main"

		pygame.display.update()
	pygame.quit()

main()
