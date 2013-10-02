#!/usr/bin/python
# -*- coding: utf-8 -*-

# par X. HINAULT - Mars 2013 - Tous droits réservés
# GPLv3 - www.mon-club-elec.fr

# modules a importer 
from PyQt4.QtGui import *
from PyQt4.QtCore import *  # inclut QTimer..
import os,sys

import serial # communication serie

from tuto_pyqt_pyserial_timer_widget_lcd_dial import * # fichier obtenu à partir QtDesigner et pyuic4

class myApp(QWidget, Ui_Form): # la classe reçoit le Qwidget principal ET la classe définie dans test.py obtenu avec pyuic4
	def __init__(self, parent=None):
		QWidget.__init__(self) # initialise le Qwidget principal 
		self.setupUi(parent) # Obligatoire 

		#Ici, personnalisez vos widgets si nécessaire

		#Réalisez les connexions supplémentaires entre signaux et slots
		self.connect(self.pushButtonGO, SIGNAL("clicked()"), self.pushButtonGOClicked) 
		self.connect(self.pushButtonSTOP, SIGNAL("clicked()"), self.pushButtonSTOPClicked) 

		self.connect(self.pushButtonInitSerial, SIGNAL("clicked()"), self.pushButtonInitSerialClicked) 
		self.connect(self.pushButtonEnvoi, SIGNAL("clicked()"), self.pushButtonEnvoiClicked) 
		self.connect(self.pushButtonStop, SIGNAL("clicked()"), self.pushButtonStopClicked) 

		# connecte le signal Clicked de l'objet bouton à l'appel de la fonction voulue 
		
		# code initial 
		
		#-- initialisation du Timer Horloge
		self.timerClock=QTimer() # déclare un timer Qt
		self.connect(self.timerClock, SIGNAL("timeout()"), self.timerClockEvent) # connecte le signal timeOut de l'objet timer à l'appel de la fonction voulue 
		# NB : le nom de la fonction appelée est ici timerEvent : ce nom est arbitraire et peut être ce que l'on veut...

		#initialisation Timer
		self.timer=QTimer() # déclare un timer Qt
		self.connect(self.timer, SIGNAL("timeout()"), self.timerEvent) # connecte le signal timeOut de l'objet timer à l'appel de la fonction voulue 

		#--- déclaration utiles --- 
		self.serialPort=None # déclaration initiale

		#-- initialisation du widget LCD 
		self.lcdNumber.display(0000) # affiche la valeur dans le LCD
		
	# les fonctions appelées, utilisées par les signaux 
	def pushButtonGOClicked(self):
		print("Bouton < GO > cliqué")
		if self.lcdNumber.value()>0: 
			self.timerClock.start(1000) # lance le timer - durée en ms
			#self.envoiChaineSerie("LED=ON"); # chaîne de déclenchement à envoyer sur le port série
			self.envoiChaineSerie(str(self.lineEditChaineEnvoiGO.text())); # chaîne de déclenchement à envoyer sur le port série

	def pushButtonSTOPClicked(self):
		print("Bouton < STOP > cliqué")
		self.timerClock.stop() # stoppe le timer - durée en ms
		#self.envoiChaineSerie("LED=OFF"); # chaîne d'arret à envoyer sur le port série
		self.envoiChaineSerie(str(self.lineEditChaineEnvoiSTOP.text())); # chaîne d'arret à envoyer sur le port série
		
	#-- fonction gestion survenue évènement Timer
	def timerClockEvent(self): # fonction appelée lors de la survenue d'un évènement Timer - nom de la fonction indiférrent 
		print("Timer") # debug

		self.lcdNumber.display(self.lcdNumber.value()-1) # affiche la valeur de décomptage dans le LCD
		self.dial.setValue(self.lcdNumber.value()) # cale la valeur du Dial sur celle du LCD
		if self.lcdNumber.value()==0 : 
			self.timerClock.stop() # arrête le Timer
			self.envoiChaineSerie("LED=OFF"); # chaîne d'arret à envoyer sur le port série

		
	#----- les fonctions des signaux des boutons du Terminal série ---- 				
	def pushButtonInitSerialClicked(self): # lors appui bouton initialisation série 
		print("Bouton Init cliqué")
		if self.serialPort: # si le port existe déjà 
			self.serialPort.close() # ferme le port si existe

		# -- initialise paramètres initialisation
		if self.comboBoxPort.currentText()=="" : # si le champ d'initialisation Port est vide = initialisation par défaut 
			strPortInit="/dev/ttyACM0" # port par défaut
		else :
			strPortInit=str(self.comboBoxPort.currentText()) #sinon utilise paramètre champ texte pour le port
		
		strDebitInit=str(self.comboBoxDebit.currentText()) # paramètre champ texte pour debit 
		
		#--- initialisation série avec gestion erreur --- 			
		try: # essaie d'exécuter les instructions 
			# initialise port serie avec délai attente en réception en ms
			self.serialPort=serial.Serial(strPortInit, strDebitInit, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE, 0.100) 			
			#self.serialPort=serial.Serial(strPortInit, strDebitInit) # initialise port serie forme réduite 
			self.serialPort.flushInput() # vide la file d'attente série
			print("Initialisation Port Série : " + strPortInit +" @ " + strDebitInit +" = OK ") # affiche debug
			
			#-- change aspect bouton init
			self.pushButtonInitSerial.setStyleSheet(QString.fromUtf8("background-color: rgb(0, 255, 0);")) # bouton en vert
			self.pushButtonInitSerial.setText("OK")  # change titre bouton 
			
		except: # si erreur initialisation 
			print("Erreur initialisation Série")		
				
			#-- change aspect bouton init
			self.pushButtonInitSerial.setStyleSheet(QString.fromUtf8("background-color: rgb(255, 127, 0);")) # bouton en orange
			self.pushButtonInitSerial.setText(QString.fromUtf8("PB"))  # change titre bouton 

		self.timer.start(100) # lance le timer avec délai en ms - 10 pour réception rapide 

	def pushButtonEnvoiClicked(self): # lors appui bouton envoi série du champ du Terminal Série
		print("Bouton ENVOI appuyé")
		self.envoiChaineSerie(str(self.lineEditChaineEnvoi.text())) # envoi le contenu du champ texte sur le port série 
	
	#----- fonction de classe commune d'envoi d'une chaîne sur le port série ---- 
	def envoiChaineSerie(self, chaineIn): # la fonction reçoit un objet chaîne Str
		
		if self.serialPort: # seulement si le port série existe - n'existe pas (=None) tant que pas initialisé 

			self.timer.stop() # stoppe le timer le temps d'envoyer message sur le port série		
			
			# combobox avec index 0 = rien, 1=saut de ligne (LF), 2=retour chariot (CR), 3= les 2 LF+CR
			if self.comboBoxFinLigne.currentIndex()==0: # si rien sélectionné
				# self.serialPort.write(str(self.lineEditChaineEnvoi.text())+'\n'  ) # envoie la chaine sur le port serie		
				self.serialPort.write(chaineIn)  # envoie la chaine sur le port serie	- variante ascii	
				print("Envoi Série : " + chaineIn )
				self.textEditTraceEnvoiSerie.append(chaineIn) # ajoute texteEdit de visualisation 

			if self.comboBoxFinLigne.currentIndex()==1: # si saut de ligne sélectionné
				self.serialPort.write(chaineIn +chr(10) ) # envoie la chaine sur le port serie	- variante ascii	
				print("Envoi Série : " + chaineIn + '\n')
				self.textEditTraceEnvoiSerie.append(chaineIn) # ajoute texteEdit de visualisation 
				
			if self.comboBoxFinLigne.currentIndex()==2: # si retour chariot sélectionné
				self.serialPort.write(chaineIn+chr(13)  ) # envoie la chaine sur le port serie	- variante ascii	
				print("Envoi Série : " + chaineIn + '\r')
				self.textEditTraceEnvoiSerie.append(chaineIn) # ajoute texteEdit de visualisation 
				
			if self.comboBoxFinLigne.currentIndex()==3: # si saut de ligne + retour chariot sélectionné
				self.serialPort.write(chaineIn+chr(10)+chr(13)  ) # envoie la chaine sur le port serie	- variante ascii
				print("Envoi Série : " + chaineIn + '\n'+'\r')
				self.textEditTraceEnvoiSerie.append(chaineIn) # ajoute texteEdit de visualisation 
				
			self.timer.start() # redémarre le timer - laisse délai pour réception en réinitialisation Timer à 0
			# car sinon l'appui survient n'importe quand et si survient peu de temps avant fin délai
			# la réception est hachée
	
	#--- fin envoiChaineSerie

	#-- fonction gestion clicked pushButton Stop 
	def pushButtonStopClicked(self):
		print("Bouton Stop cliqué")

		#-- stoppe la réception série -- 
		if self.serialPort: # si le port existe déjà 
			self.serialPort.close() # ferme le port si existe
			self.timer.stop() # stoppe le timer
		
		#-- change aspect bouton init
		self.pushButtonInitSerial.setStyleSheet(QString.fromUtf8("background-color: rgb(255, 127, 0);")) # bouton en orange
		self.pushButtonInitSerial.setText(QString.fromUtf8("Off"))  # change titre bouton 
	
	#-- fin fonction gestion clicked pushButton Stop 	
	
		#----- fonction de gestion du signal timeout du QTimer
	def timerEvent(self): # fonction appelée lors de la survenue d'un évènement Timer - nom fonction indiférrent 
		#-- variables de réception -- 
		self.chaineIn="";
		self.char="";
		
		# lecture des données reçues		
		if self.serialPort: # seulement si le port série existe 
			self.timer.stop() # stoppe le timer le temps de lire les caractères et éviter "réentrée"
			
			while (self.serialPort.inWaiting()): # tant que au moins un caractère en réception
				self.char=self.serialPort.read() # on lit le caractère
				#self.chaineIn=self.chaineIn+self.char		# forme minimale...
				
				if self.char=='\n': # si saut de ligne, on sort du while
					print("saut ligne reçu") # debug
					break # sort du while
				else: #tant que c'est pas le saut de ligne, on l'ajoute à la chaine 
					self.chaineIn=self.chaineIn+self.char					
				
			if len(self.chaineIn)>0: # ... pour ne pas avoir d'affichage si ""	
				print(self.chaineIn) # affiche la chaîne 
				self.textEditReception.append(self.chaineIn[:-1]) # ajoute le texte au textEdit en enlevant le dernier caractère (saut de ligne)
										
			self.timer.start() # redémarre le timer
			
	#---- fin timerEvent 

def main(args):
	a=QApplication(args) # crée l'objet application 
	f=QWidget() # crée le QWidget racine
	c=myApp(f) # appelle la classe contenant le code de l'application 
	f.show() # affiche la fenêtre QWidget
	r=a.exec_() # lance l'exécution de l'application 
	return r

if __name__=="__main__": # pour rendre le code exécutable 
	main(sys.argv) # appelle la fonction main

