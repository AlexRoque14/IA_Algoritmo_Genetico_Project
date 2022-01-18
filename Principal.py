from Dieta import Dieta
import sys
import math
from PyQt5 import uic 
from PyQt5.QtWidgets import QMainWindow, QApplication, QRadioButton
from PyQt5.QtGui import QPainter, QColor, QPen
from Dieta import main

class View_GUI(QMainWindow):

    Peso = 0
    Altura = 0
    Edad = 0
    Actividad = ""
    Sexo = ""

    def __init__(self):
        super().__init__()
        uic.loadUi("Diseño.ui", self)
        self.btn_IMC.clicked.connect(self.validAttributes)
        self.rbtn1.toggled.connect(self.onClicked)
        self.rbtn2.toggled.connect(self.onClicked)
        self.rbtn3.toggled.connect(self.onClicked)
        self.rbtn4.toggled.connect(self.onClicked)
        self.rbtn5.toggled.connect(self.onClicked)


    def validAttributes(self):
        self.Altura = self.txt_altura.text()
        self.Peso = self.txt_peso.text()
        self.Edad = self.txt_edad.text()
        self.Sexo = self.txt_sexo.text()

        if not self.Altura:
            print("Ingresa la altura")
        elif not self.Peso:
            print("Ingresa el peso")
        elif not self.Edad:
            print("Ingresa la edad")
        elif not self.Sexo:
            print("Ingresa el sexo")
        else: 
            self.run()


    def onClicked(self):
        radioBtn_1 = self.sender()
        if radioBtn_1.isChecked():
            self.Actividad = radioBtn_1.text()
            print(self.Actividad)

    def run(self):
        #Se calcula la Tasa Metabolica Basal (calorias que se comen por día)
        if self.Sexo == "Masculino" or self.Sexo == "M":
            TMB = (6.25 * int(self.Altura)) + (10 * int(self.Peso)) - (5 * int(self.Edad)) + 5
          
        if self.Sexo == "Femenino" or self.Sexo == "F":
            TMB = (6.25 * int(self.Altura)) + (10 * int(self.Peso)) - (5 * int(self.Edad)) - 161

        #calorias que se comen por día cuando existe actividad fisica
        print("Tasa Metabolica Basal (TMB): " , TMB)
        #Se calcula el TMB por actividad fisica
        if self.Actividad == "Sedentario":
            TMBA = TMB * 1.2
        if self.Actividad == "Actividad Ligera":
            TMBA = TMB *  1.375
        if self.Actividad == "Actividad Moderada":
            TMBA = TMB *  1.55
        if self.Actividad == "Muy intensa":
            TMBA = TMB *  1.725
        if self.Actividad == "Intensa":
            TMBA = TMB * 1.9
        
        print("Tasa Metabolica Basal Activa (TMBA) es: " , TMBA)
        self.lab_tmb_1.setText(str(TMB))
        self.lab_tmb_2.setText(str(TMBA))
        main(TMBA)
    
    def listView(self):
        self.Qlist.addItems("Hola")



#Main
if __name__ == "__main__":
    app = QApplication(sys.argv)
    GUI = View_GUI()
    GUI.show()
    app.exec_()