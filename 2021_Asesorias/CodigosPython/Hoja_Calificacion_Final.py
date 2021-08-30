# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, Frame
from reportlab.lib.enums import TA_LEFT, TA_JUSTIFY
import csv
from numpy import array



def concatenaNombre(nombres, apellido1, apellido2):
    return nombres + " " + apellido1 + " " + apellido2

def defineSaludo(entrada):
    if entrada == "1":
        return "Alumno"
    else:
        return "Alumna"

def elaboraConstancia(numeroCuenta, nombreCompleto, saludo, ejerciciosEntregados, puntajeObtenido,
                      promedioCalculado, ajustePromedio, calificacionFinal, calificacionLetra):
    
    objetoCanvas = Canvas('Calificacion_Final_MAF_' + nombreCompleto.strip() + '.pdf', pagesize=letter)
    
    objetoCanvas.drawString(275, 700, 'Ciudad de México a 19 de agosto del 2021.')
    
    #Estilo de la hoja.
    
    styles=getSampleStyleSheet()
    
    story1= []
    
    ptextoencabezado = saludo + ': ' + nombreCompleto + '. <br/><br/>'\
                        'Número de cuenta: ' + numeroCuenta
    styles.add(ParagraphStyle(name='Izquierda', alignment=TA_LEFT, fontSize = 14, leading = 20))
    story1.append(Paragraph(ptextoencabezado, styles['Izquierda']))
    
    frame = Frame(50, 600, 6.5*inch, 1*inch, showBoundary=0)
    frame.addFromList(story1, objetoCanvas)
    
    story2 = []
    
    ptextomensaje = 'A continuación se presenta el resumen de la evaluación para el curso de Matemáticas ' +\
                    'de la Física que cursaste durante el semestre 2021-2.  <br/><br/>' +\
                    'Ejercicios entregados: ' + ejerciciosEntregados + ' de 20 <br/>' +\
                    'Puntaje obtenido: ' + puntajeObtenido + '<br/><br/>'+\
                    'De acuerdo al esquema de evaluación presentado, para el puntaje obtenido ' +\
                    'por los ejercicios que resolviste y enviaste,<br/><br/>' +\
                    'Tu <strong>calificación final es </strong> : ' + calificacionFinal + ' ( ' + calificacionLetra +' ) <br/><br/>' +\
                    'Esta calificación se asentará en el acta oficial del curso, una vez que se haya realizado la captura y ' +\
                    'y la firma electrónica, se les notificará vía correo electrónico, por lo que en un par de días ' +\
                    'ya podrán ver reflejada la calificación en su historial académico. <br/<br/>'
    
    if calificacionFinal != '5':
        ptextomensaje = ptextomensaje + 'Te deseamos el mayor de los éxitos y confiamos en que continues con el mismo esfuerzo ' +\
                        'y compromiso en lo que resta de la carrera de Física.<br/><br/>M. en C. Ramón Gustavo Contreras Mayén.'
    else:
        ptextomensaje = ptextomensaje + '<br/><br/>M. en C. Ramón Gustavo Contreras Mayén.'
            
                    
                    
    styles.add(ParagraphStyle(name='Justificado', alignment=TA_JUSTIFY, fontSize = 12, leading = 18))
    story2.append(Paragraph(ptextomensaje, styles['Justificado']))
    
    #Definimos otro frame.
    frame2 = Frame(50, 50, 6.5*inch, 7.5*inch, showBoundary=0)
    frame2.addFromList(story2, objetoCanvas)
    
    
    objetoCanvas.showPage()
    
    #Salvamos el PDF.
    objetoCanvas.save()

def readinputdata(filename): 
    fichero=open(filename,'r') 
    f=[] 
    line='0' 
    with open(filename) as csv_file:
        for line in csv.reader(csv_file, delimiter=','): #
            if len(line)>0 : 
                f.append(line) 
    fichero.close() 
    return array(f)


data=readinputdata(r'CalificacionesFinalesMAF2021_2.csv') 
# print (range(1, len(data))) #range(1,26)

for i in range(1, len(data)):
    numeroCuenta = data[i][0]
    nombreCompleto = concatenaNombre(data[i][3], data[i][1], data[i][2])
    print(nombreCompleto)
    saludo = defineSaludo(data[i][5])
    ejerciciosEntregados = data[i][26]
    puntajeObtenido = data[i][28]
    promedioCalculado = data[i][29]
    ajustePromedio = data[i][30]
    calificacionFinal = data[i][31]
    calificacionLetra = data[i][32]
    elaboraConstancia(numeroCuenta, nombreCompleto, saludo, ejerciciosEntregados, puntajeObtenido,
                      promedioCalculado, ajustePromedio, calificacionFinal, calificacionLetra)
