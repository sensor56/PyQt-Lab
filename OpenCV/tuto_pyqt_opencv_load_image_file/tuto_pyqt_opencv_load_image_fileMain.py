#!/usr/bin/python
# -*- coding: utf-8 -*-

# Par X. HINAULT - Tous droits réservés - GPLv3
# Déc 2012 - www.mon-club-elec.fr

# --- importation des modules utiles ---
from PyQt4.QtGui import *
from PyQt4.QtCore import * # inclut QTimer..

import os,sys
from cv2 import * # importe module OpenCV

sys.path.insert(0,'/home/xavier') # si pas path système 
from pyqtcv import * # importe librairie perso comportant fonctions utiles pour utiliser opencv avec pyqt

# --- importation du fichier de description GUI --- 
from tuto_pyqt_opencv_load_image_file import *

# --- classe principale du programme pyQt contenant le code actif ---
class myApp(QWidget, Ui_Form): 
# la classe reçoit le Qwidget principal ET la classe Ui_Form définie dans *.py obtenu avec pyuic4

	# Note : ici self représente la classe 

	def __init__(self, parent=None):
		QWidget.__init__(self) # initialise le Qwidget principal 
		self.setupUi(parent) # Obligatoire 

		#-- variables utiles --

		#Ici, personnalisez vos widgets si nécessaire en utilisant les noms définis dans QtDesigner
		
		#Réalisez les connexions supplémentaires entre signaux et slots
		# les widgets sont désignés sous la forme self.nom en utilisant les noms définis dans QtDesigner
		self.connect(self.pushButtonOuvrir, SIGNAL("clicked()"), self.pushButtonOuvrirClicked) # connecte le signal Clicked de l'objet bouton à l'appel de la fonction voulue 
		
		#--- code actif initial 
	
	# les fonctions appelées, utilisées par les signaux 
	def pushButtonOuvrirClicked(self):
		print("Bouton OUVRIR appuyé") # debug
		
		#self.filename=QFileDialog.getOpenFileName(self, 'Ouvrir fichier', os.getenv('HOME')) # ouvre l'interface fichier
		self.filename=QFileDialog.getOpenFileName(self, 'Ouvrir fichier', QDir.currentPath()) # ouvre l'interface fichier
		# getOpenFileName ouvre le fichier sans l'effacer et getSaveFileName l'efface si il existe 
		
		
		print(self.filename) # debug
		self.lineEditChemin.setText(self.filename) # affiche le chemin du fichier dans le champ texte		
		
		# charge de l'image
		self.cvImageSrc=cv.LoadImage(str(self.filename), cv.CV_LOAD_IMAGE_COLOR) # charge l'image sous forme d'une iplImage 3 canaux
		
		# crée une image OpenCV de la taille du label d'affichage
		self.cvImage=cv.CreateImage((self.labelImage.width(), self.labelImage.height()), cv.IPL_DEPTH_8U, 3)

		# redimensionne image source aux dimensions du label d'affichage
		cv.Resize(self.cvImageSrc,self.cvImage, cv.CV_INTER_LINEAR) 
		
		# affiche l'image dans Qt 
		self.qImage=IplToQImage(self.cvImage) # récupère l'IplImage dans un QImage
		self.qPixmap=QPixmap.fromImage(self.qImage) # récupère le QImage dans un QPixmap
		self.labelImage.setPixmap(self.qPixmap) # affiche l'image dans le label 
		# NB : pour éviter les problèmes, les objets de manipulation d'image doivent être "self"

	
	# autres fonctions actives
	# ... 

# fonction principale exécutant l'application Qt			
def main(args):
	a=QApplication(args) # crée l'objet application 
	f=QWidget() # crée le QWidget racine
	c=myApp(f) # appelle la classe contenant le code de l'application 
	f.show() # affiche la fenêtre QWidget
	r=a.exec_() # lance l'exécution de l'application 
	return r

# pour rendre le fichier *.py exécutable
if __name__=="__main__": # pour rendre le code exécutable 
	main(sys.argv) # appelle la fonction main
