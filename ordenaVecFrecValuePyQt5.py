import sys
from PyQt5 import uic, QtWidgets
import re


from ordenarArrayFrecuenciaYValor import ordenaFrecYValor


qtCreatorFile = "ordenaVecFrecValuePyQt5.ui" 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
           
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)    
        self.pb_ordenar.clicked.connect(self.pb_ordenar_click)
        self.pb_salir.clicked.connect(app.quit)

    def pb_ordenar_click(self):    
        sent = self.le_entrada.text()
        
        patronValidaLisEnt.search(sent)

        sarr = sent.split(',')
        if len(sarr) <= 1 and sarr[0] == '':
            self.lab_salida.setText("empty")
        elif patronValidaLisEnt.match(sent) is not None:
            arr = [int(si) for si in sarr]
        
            res = ordenaFrecYValor(arr)
            
            self.lab_salida.setText(str(res))
        else:
            self.lab_salida.setText("Error de Entrada")
            

        

    def pb_salir_click(self):
        self.le_entrada.setText("salir")
 
if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    
    patronValidaLisEnt = re.compile('^(\d+\,?)+$')

    
    sys.exit(app.exec())   
 