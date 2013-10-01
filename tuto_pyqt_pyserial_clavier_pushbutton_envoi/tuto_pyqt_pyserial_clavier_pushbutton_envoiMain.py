#!/usr/bin/python
# -*- coding: utf-8 -*-

# par X. HINAULT - Janv 2013 - Tous droits réservés
# GPLv3 - www.mon-club-elec.fr

# modules a importer 
from PyQt4.QtGui import *
from PyQt4.QtCore import *  # inclut QTimer..
import os,sys

import serial # communication serie

from tuto_pyqt_pyserial_clavier_pushbutton_envoi import * # fichier obtenu à partir QtDesigner et pyuic4

class myApp(QWidget, Ui_Form): # la classe reçoit le Qwidget principal ET la classe définie dans test.py obtenu avec pyuic4
	def __init__(self, parent=None):
		QWidget.__init__(self) # initialise le Qwidget principal 
		self.setupUi(parent) # Obligatoire 

		#Ici, personnalisez vos widgets si nécessaire

		#Réalisez les connexions supplémentaires entre signaux et slots
		# connecte le signal Clicked de l'objet bouton à l'appel de la fonction voulue 
		
		# -- les boutons du clavier numérique --
		self.connect(self.pushButton_0, SIGNAL("clicked()"), self.pushButton_0Clicked) 
		self.connect(self.pushButton_1, SIGNAL("clicked()"), self.pushButton_1Clicked) 
		self.connect(self.pushButton_2, SIGNAL("clicked()"), self.pushButton_2Clicked) 
		self.connect(self.pushButton_3, SIGNAL("clicked()"), self.pushButton_3Clicked) 
		self.connect(self.pushButton_4, SIGNAL("clicked()"), self.pushButton_4Clicked) 
		self.connect(self.pushButton_5, SIGNAL("clicked()"), self.pushButton_5Clicked) 
		self.connect(self.pushButton_6, SIGNAL("clicked()"), self.pushButton_6Clicked) 
		self.connect(self.pushButton_7, SIGNAL("clicked()"), self.pushButton_7Clicked) 
		self.connect(self.pushButton_8, SIGNAL("clicked()"), self.pushButton_8Clicked) 
		self.connect(self.pushButton_9, SIGNAL("clicked()"), self.pushButton_9Clicked) 
		self.connect(self.pushButton_point, SIGNAL("clicked()"), self.pushButton_pointClicked) 
		self.connect(self.pushButton_Clear, SIGNAL("clicked()"), self.pushButton_ClearClicked) 
		
		# -- les boutons du terminal série --
		self.connect(self.pushButtonInitSerial, SIGNAL("clicked()"), self.pushButtonInitSerialClicked) 
		self.connect(self.pushButtonEnvoi, SIGNAL("clicked()"), self.pushButtonEnvoiClicked) 

		# -- les boutons d'envoi série --
		self.connect(self.pushButtonEnvoiValeur_1, SIGNAL("clicked()"), self.pushButtonEnvoiValeur_1Clicked) 		
		self.connect(self.pushButtonEnvoiValeur_2, SIGNAL("clicked()"), self.pushButtonEnvoiValeur_2Clicked) 		
		self.connect(self.pushButtonEnvoiValeur_3, SIGNAL("clicked()"), self.pushButtonEnvoiValeur_3Clicked) 		
		self.connect(self.pushButtonEnvoiValeur_4, SIGNAL("clicked()"), self.pushButtonEnvoiValeur_4Clicked) 		
		self.connect(self.pushButtonEnvoiValeur_5, SIGNAL("clicked()"), self.pushButtonEnvoiValeur_5Clicked) 		

		#-- variables utiles --
		self.flagPoint=False # témoin point déjà utilisé pour éviter 2 fois... 		
		self.serialPort=None # déclaration initiale

		#initialisation Timer
		self.timer=QTimer() # déclare un timer Qt
		self.connect(self.timer, SIGNAL("timeout()"), self.timerEvent) # connecte le signal timeOut de l'objet timer à l'appel de la fonction voulue 
		
	# les fonctions appelées, utilisées par les signaux 
	
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

		self.timer.start(10) # lance le timer avec délai en ms - 10 pour réception rapide 

	def pushButtonEnvoiClicked(self): # lors appui bouton envoi série du champ du Terminal Série
		print("Bouton ENVOI appuyé")
		self.envoiChaineSerie(str(self.lineEditChaineEnvoi.text())) # envoi le contenu du champ texte sur le port série 

	#--------- fonctions des boutons d'envoi des valeurs numériques à partir valeur clavier ---------
	def pushButtonEnvoiValeur_1Clicked(self): # lors appui bouton envoi série du champ du Terminal Série
		print("Bouton ENVOI Valeur 1 appuyé")
		if self.lineEditChaineEnvoiValeur_1.text()=="": # si champ racine vide
			self.envoiChaineSerie(str(self.lineEdit.text())) # envoi le contenu du champ numérique seul sur le port série 
		else: # sinon, = si champ racine pas vide
			self.envoiChaineSerie(str(self.lineEditChaineEnvoiValeur_1.text())+str(self.lineEdit.text())+")") # envoi le contenu du champ racine + champ numérique + ")" sur le port série
		
	def pushButtonEnvoiValeur_2Clicked(self): # lors appui bouton envoi série du champ du Terminal Série
		print("Bouton ENVOI Valeur 2 appuyé")
		if self.lineEditChaineEnvoiValeur_2.text()=="": # si champ racine vide
			self.envoiChaineSerie(str(self.lineEdit.text())) # envoi le contenu du champ numérique seul sur le port série 
		else: # sinon, = si champ racine pas vide
			self.envoiChaineSerie(str(self.lineEditChaineEnvoiValeur_2.text())+str(self.lineEdit.text())+")") # envoi le contenu du champ racine + champ numérique + ")" sur le port série

	def pushButtonEnvoiValeur_3Clicked(self): # lors appui bouton envoi série du champ du Terminal Série
		print("Bouton ENVOI Valeur 3 appuyé")
		if self.lineEditChaineEnvoiValeur_3.text()=="": # si champ racine vide
			self.envoiChaineSerie(str(self.lineEdit.text())) # envoi le contenu du champ numérique seul sur le port série 
		else: # sinon, = si champ racine pas vide
			self.envoiChaineSerie(str(self.lineEditChaineEnvoiValeur_3.text())+str(self.lineEdit.text())+")") # envoi le contenu du champ racine + champ numérique + ")" sur le port série

	def pushButtonEnvoiValeur_4Clicked(self): # lors appui bouton envoi série du champ du Terminal Série
		print("Bouton ENVOI Valeur 4 appuyé")
		if self.lineEditChaineEnvoiValeur_4.text()=="": # si champ racine vide
			self.envoiChaineSerie(str(self.lineEdit.text())) # envoi le contenu du champ numérique seul sur le port série 
		else: # sinon, = si champ racine pas vide
			self.envoiChaineSerie(str(self.lineEditChaineEnvoiValeur_4.text())+str(self.lineEdit.text())+")") # envoi le contenu du champ racine + champ numérique + ")" sur le port série

	def pushButtonEnvoiValeur_5Clicked(self): # lors appui bouton envoi série du champ du Terminal Série
		print("Bouton ENVOI Valeur 5 appuyé")
		if self.lineEditChaineEnvoiValeur_5.text()=="": # si champ racine vide
			self.envoiChaineSerie(str(self.lineEdit.text())) # envoi le contenu du champ numérique seul sur le port série 
		else: # sinon, = si champ racine pas vide
			self.envoiChaineSerie(str(self.lineEditChaineEnvoiValeur_5.text())+str(self.lineEdit.text())+")") # envoi le contenu du champ racine + champ numérique + ")" sur le port série

	
	#-------- fonctions des boutons du clavier -------------- 
	def pushButton_0Clicked(self):
		print("Bouton " + str(self.pushButton_0.text())+ " cliqué")
		self.setLineEdit("0") # appelle fonction locale 

	def pushButton_1Clicked(self):
		print("Bouton " + str(self.pushButton_1.text())+ " cliqué")
		self.setLineEdit("1") # appelle fonction locale 
		
	def pushButton_2Clicked(self):
		print("Bouton " + str(self.pushButton_2.text())+ " cliqué")
		self.setLineEdit("2") # appelle fonction locale 
		
	def pushButton_3Clicked(self):
		print("Bouton " + str(self.pushButton_3.text())+ " cliqué")
		self.setLineEdit("3") # appelle fonction locale 
		
	def pushButton_4Clicked(self):
		print("Bouton " + str(self.pushButton_4.text())+ " cliqué")
		self.setLineEdit("4") # appelle fonction locale 
		
	def pushButton_5Clicked(self):
		print("Bouton " + str(self.pushButton_5.text())+ " cliqué")
		self.setLineEdit("5") # appelle fonction locale 
		
	def pushButton_6Clicked(self):
		print("Bouton " + str(self.pushButton_6.text())+ " cliqué")
		self.setLineEdit("6") # appelle fonction locale 
		
	def pushButton_7Clicked(self):
		print("Bouton " + str(self.pushButton_7.text())+ " cliqué")
		self.setLineEdit("7") # appelle fonction locale 
		
	def pushButton_8Clicked(self):
		print("Bouton " + str(self.pushButton_8.text())+ " cliqué")
		self.setLineEdit("8") # appelle fonction locale 

	def pushButton_9Clicked(self):
		print("Bouton " + str(self.pushButton_9.text())+ " cliqué")
		self.setLineEdit("9") # appelle fonction locale 
		
	def pushButton_pointClicked(self):
		print("Bouton " + str(self.pushButton_point.text())+ " cliqué")
		if not self.flagPoint: # si drapeau point à False (not à True...) 
			self.lineEdit.setText(self.lineEdit.text()+".") # ajoute le caractère au champ
			self.flagPoint=True # met le drapeau d'utilisation du point à True pour éviter réutilisation
		else:print("Point déjà utilisé") # affiche message

	def pushButton_ClearClicked(self):
		print("Bouton " + str(self.pushButton_Clear.text())+ " cliqué")
		self.lineEdit.setText("0") # défini le contenu du champ
		self.flagPoint=False # met le drapeau d'utilisation du point à False pour permettre réutilisation

	#-- fonctions de la classe 
	#-- gestion du champ texte saisie valeur clavier
	def setLineEdit(self, charIn): # fonction reçoit le caractère (str)à ajouter au champ
		if self.lineEdit.text()=="0":self.lineEdit.setText(charIn) # efface contenu si vaut "0"
		else:self.lineEdit.setText(self.lineEdit.text()+charIn) # ajoute le caractère au champ

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
				if self.char=='\n': # si saut de ligne, on sort du while
					print("saut ligne reçu") # debug
					break # sort du while
				else: #tant que c'est pas le saut de ligne, on l'ajoute à la chaine 
					self.chaineIn=self.chaineIn+self.char					
			
			if len(self.chaineIn)>0: # ... pour ne pas avoir d'affichage si ""	
				print(self.chaineIn) # affiche la chaîne 
				self.textEditReception.append(self.chaineIn[:-1]) # ajoute le texte au textEdit en enlevant le dernier caractère 
				
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

