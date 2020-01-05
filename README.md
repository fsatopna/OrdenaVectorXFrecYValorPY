
***
# Ordenar un vector por frecuencia y valor
***
## Problema: 
Se tiene un vector de enteros, y se desea ordenar el mismo por la frecuencia de cada elemento y para la misma frecuencia por el valor del elemento:

* entrada:  {5, 1, 5, 4, 3, 5, 5, 3}    
* salida :  {1, 4, 3, 3, 5, 5, 5, 5} 

### Entrada
<Table>
  <tr>
      <td>Elementos</td>
      <td>5</td>
      <td>1</td>
      <td>5</td>
      <td>4</td>
      <td>3</td>
      <td>5</td>
      <td>5</td>
      <td>3</td>
   </tr>
   <tr>
</Table>

### Frecuencias
<Table>
  <tr>
      <td>Elemento</td>
      <td>1</td>
      <td>3</td>
      <td>4</td>
      <td>5</td>
   </tr>
   <tr>
    <td>Frecuencia</td>
      <td>1</td>
      <td>2</td>
      <td>1</td>
      <td>4</td>
  </tr>
</Table>

## Objetivo
Comprender y utilizar distintos tipos de colecciones para resolución de problemas de conjunto.

***


## Estrategia: 
* Obtener elementos únicos, anum.           `[1,3,4,5]` 
* Obtener las frecuencias de anum, afrec.   `{1,2,1,4]`
* Obtener un vector de pares ordenados con (afrec,anum). `{frecuencia,valor}`{(1,1),(2,3)(1,4)(4,5)}`
* Ordenar el vector de pares por frecuencia y valor. `{1,3,3,4,5,5,5,5}`frecuencia,valor}

## Implementación: 
* ### Obtener elementos unicos, anum.
```
anum = list(set(arr))

```

* ### Obtener las frecuencias, afrec.
```
afrec = []
for n in anum:
    afrec.append(arr.count(n))
```
Notar que el vector anum no necesariamente debe estar ordenado, si debe tener valores únicos(set).

* ### Obtener un vector de pares ordenados con  valor y frecuencia (afrec,anum), anf.
```
anf= list(zip(afrec,anum))
```

* ### Ordenar el vector, anfs.
```
anfs = sorted(anf)
```


### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Alternativa de Ordenar el vector de pares.
```
sorted(anf, cmp=cmp_tuplas)  

anf= list(zip(af def cmp_tuplas(a, b):
   if a[0]>b[0]:
      return 1
   elif a[0]<b[0]:
      return -1
   else:
       if a[1]<b[1]:
          return 1
       elif a[1]>b[1]:
          return -1
       else:
          return 0
rec,anum))
```

* ### Generar el vector resultado desde anfs, res.
```
res =  []
for fila in anfs:
#    print(fila[1],'->',fila[0])
    for i in range(fila[0]):
        res.append(fila[1])

```

***
# App Grafica usando PyQt5
***
## Interfaz

Se utilizo la siguiente interfaz desarrollada con Qt Designer


![Ventana Principal](https://github.com/fsatopna/OrdenaVectorXFrecYValorPY/blob/master/ordenaVecFrecValuePyQt5.jpg)


## ordenaVecFrecValuePyQt5.ui


```
<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>694</width>
    <height>305</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Ordena Vector Enteros por Frec y Value</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="pb_ordenar">
    <property name="geometry">
     <rect>
      <x>330</x>
      <y>240</y>
      <width>89</width>
      <height>25</height>
     </rect>
    </property>
    <property name="text">
     <string>Ordenar</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pb_salir">
    <property name="geometry">
     <rect>
      <x>470</x>
      <y>240</y>
      <width>89</width>
      <height>25</height>
     </rect>
    </property>
    <property name="text">
     <string>Salir</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="le_entrada">
    <property name="geometry">
     <rect>
      <x>140</x>
      <y>150</y>
      <width>301</width>
      <height>25</height>
     </rect>
    </property>
   </widget>
   <widget class="QLabel" name="lab_salida">
    <property name="geometry">
     <rect>
      <x>140</x>
      <y>200</y>
      <width>361</width>
      <height>17</height>
     </rect>
    </property>
    <property name="text">
     <string> </string>
    </property>
   </widget>
   <widget class="QLabel" name="label_2">
    <property name="geometry">
     <rect>
      <x>70</x>
      <y>150</y>
      <width>67</width>
      <height>17</height>
     </rect>
    </property>
    <property name="text">
     <string>Entrada:</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_3">
    <property name="geometry">
     <rect>
      <x>70</x>
      <y>200</y>
      <width>67</width>
      <height>17</height>
     </rect>
    </property>
    <property name="text">
     <string>Salida:</string>
    </property>
   </widget>
   <widget class="QTextEdit" name="textEdit">
    <property name="geometry">
     <rect>
      <x>63</x>
      <y>10</y>
      <width>561</width>
      <height>111</height>
     </rect>
    </property>
    <property name="html">
     <string>&lt;!DOCTYPE HTML PUBLIC &quot;-//W3C//DTD HTML 4.0//EN&quot; &quot;http://www.w3.org/TR/REC-html40/strict.dtd&quot;&gt;
&lt;html&gt;&lt;head&gt;&lt;meta name=&quot;qrichtext&quot; content=&quot;1&quot; /&gt;&lt;style type=&quot;text/css&quot;&gt;
p, li { white-space: pre-wrap; }
&lt;/style&gt;&lt;/head&gt;&lt;body style=&quot; font-family:'Ubuntu'; font-size:11pt; font-weight:400; font-style:normal;&quot;&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;Aplicacion ejemplo de uso de función ordenaFrecYValor(), con interface gráficausando PyQt5. &lt;/p&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;Uso:&lt;/p&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;* Entrada: debe ingresar un conjunto de enteros separado por coma. Ej: [1,3,2]. &lt;/p&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;* Salida: [1,2,3]&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>694</width>
     <height>22</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>

```

## ordenaVecFrecValuePyQt5.py

```
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
 
```






