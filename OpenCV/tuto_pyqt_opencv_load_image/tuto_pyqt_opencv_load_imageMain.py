#!/usr/bin/python
# -*- coding: utf-8 -*-

# Par X. HINAULT - Tous droits réservés - GPLv3
# Déc 2012 - www.mon-club-elec.fr

# --- importation des modules utiles ---
from PyQt4.QtGui import *
from PyQt4.QtCore import * # inclut QTimer..

import os,sys
from cv2 import * # importe module OpenCV - cv est un sous module de cv2

sys.path.insert(0,'/home/xavier') # si pas path système 
from pyqtcv import * # importe librairie perso comportant fonctions utiles pour utiliser opencv avec pyqt

# --- importation du fichier de description GUI --- 
from tuto_pyqt_opencv_load_image import *

# --- classe principale du programme pyQt contenant le code actif ---
class myApp(QWidget, Ui_Form): 
# la classe reçoit le Qwidget principal ET la classe Ui_Form définie dans *.py obtenu avec pyuic4

	# Note : ici self représente la classe 

	def __init__(self, parent=None):
		QWidget.__init__(self) # initialise le Qwidget principal 
		self.setupUi(parent) # Obligatoire 

		#-- variables utiles --

		#--- code actif initial 
		self.iplImage=cv.LoadImage("test.jpg", cv.CV_LOAD_IMAGE_COLOR) # charge l'image sous forme d'une iplImage 3 canaux
		self.qImage=IplToQImage(self.iplImage) # récupère l'IplImage dans un QImage - fonction pyqtcv
		self.qPixmap=QPixmap.fromImage(self.qImage) # récupère le QImage dans un QPixmap
		self.labelImage.setPixmap(self.qPixmap) # affiche l'image dans le label 
		# NB : pour éviter les problèmes, les objets de manipulation d'image doivent être "self"
	
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
