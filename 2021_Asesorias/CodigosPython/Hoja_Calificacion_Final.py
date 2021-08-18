# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.platypus import Paragraph, Frame, Image, PageBreak
#from reportlab.platypus.tables import Table, TableStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
import csv
from numpy import array

pdfmetrics.registerFont(TTFont('Courier', 'cour.ttf'))
pdfmetrics.registerFont(TTFont('Roboto', 'Roboto-Light.ttf'))
pdfmetrics.registerFont(TTFont('Roboto2', 'Roboto-Bold.ttf'))

#Creamos objeto Canvas.

#fichero_pdf = 'ejemplo2.pdf'

def elaboraConstancia(gafete, asistente, nombreNormalizado, cadenahashAsistencia, libroregistro):

    objeto_canvas = Canvas('Constancia_Gafete_' + gafete.strip() + '.pdf', pagesize=landscape(letter))
    
    #Estilo de la hoja.
    
    styles=getSampleStyleSheet()
    
    story = []
    
    #Añadimos algunos flowables.
    
    fichero_imagen = 'banner_constancia.png'
    imagen_logo = Image(fichero_imagen, 3*inch, 8.5*inch)
    story.append(imagen_logo)
    
    #Definimos un frame.
    
    frame = Frame(-17.5 , -30, 3.5*inch, 9*inch, showBoundary=0)
    frame.addFromList(story,objeto_canvas)
    
    #Inicializamos platypus story.
    
    story2 = []
    
    
    ptextoencabezado = 'La Facultad de Medicina Región Veracruz de la Universidad Veracruzana \
                 en conjunto con la Asociación Mexicana de Facultades y Escuelas de Medicina A.C.\
                 otorgan la presente constancia a'
    
    
    styles.add(ParagraphStyle(name='Centrado', alignment=TA_CENTER, fontSize = 16, leading = 20))
    story2.append(Paragraph(ptextoencabezado, styles['Centrado']))
    
    #Definimos otro frame.
    frame2 = Frame(230, 450, 7.5*inch, 1*inch,showBoundary=0)
    frame2.addFromList(story2,objeto_canvas)
    
    story3 = []
    
    ptextoasistente = '<b>%s</b>' % asistente
    styles.add(ParagraphStyle(name='nombreCentrado', alignment=TA_CENTER, fontSize = 22, textColor = colors.blue))
    story3.append(Paragraph(ptextoasistente, styles['nombreCentrado']))
    
    frame3 = Frame(230, 380, 7.5*inch, 0.5*inch,showBoundary=0)
    frame3.addFromList(story3,objeto_canvas)
    
    
    story4 = []
    
    ptextoinfo = 'por su asistencia a la <b><font color="blue">LX Reunión Nacional Ordinaria <em>El reto de evaluar \
                 para mejorar</em></font></b>, llevada a cabo del 26 al 29 de abril del 2017, con un valor curricular \
                 de 15 horas. Se extiende la presente en la ciudad de Boca del Río, Veracruz el día 29 de abril del 2017.'
    
    story4.append(Paragraph(ptextoinfo, styles['Centrado']))
    
    frame4 = Frame(230, 250, 7.5*inch, 1.45*inch,showBoundary=0)
    frame4.addFromList(story4,objeto_canvas)
    
    story5 = []
    
    ptextosello = 'Sello digital: ASISTENCIA|' + nombreNormalizado + '|' + cadenahashAsistencia + ' <br/> | 29-04-2017 | LX-RNO-AMFEM'
    styles.add(ParagraphStyle(name='selloDigital', alignment = TA_LEFT, fontName = "Courier", fontSize = 11, leading = 16))
    story5.append(Paragraph(ptextosello, styles['selloDigital']))
    
    frame5 = Frame(230, 175, 7.5*inch, 1*inch,showBoundary=0)
    frame5.addFromList(story5,objeto_canvas)
    
    #Firmas para la constancia
    
    Firma_Dr_RLB = 'Firma_Dr_RLB.jpg'
    Firma_Dr_PGA = 'Firma_Dr_PGA.jpg'
    Firma_Dr_JCGF = 'Firma_Dr_JCGF.jpg'
    
    #Firma Dr. Ricardo León Bórquez
    story6 = []
    
    imagen_RLB = Image(Firma_Dr_RLB)
    story6.append(imagen_RLB)
    
    ptextofirmaRLB = 'Dr. Ricardo León Bórquez <br/>Presidente de la AMFEM'
    styles.add(ParagraphStyle(name='firmaCentrado', alignment=TA_CENTER, fontSize = 12, leading = 14))
    story6.append(Paragraph(ptextofirmaRLB, styles['firmaCentrado']))
    
    frame6 = Frame(218, 22, 2.5*inch, 1.5*inch, showBoundary = 0)
    frame6.addFromList(story6, objeto_canvas)
    
    #Firma Dr. Pedro Gutiérrez Aguilar
    story7 = []
    
    imagen_PGA = Image(Firma_Dr_PGA, 2*inch, inch)
    story7.append(imagen_PGA)
    
    ptextofirmaPGA = 'Dr. Pedro Gutiérrez Aguilar <br/>Director de la Facultad de Medicina <br/> \
                    Universidad Veracruzana <br/> Región Veracruz'
    
    story7.append(Paragraph(ptextofirmaPGA, styles['firmaCentrado']))
    
    frame7 = Frame(390, -15, 2.8*inch, 2.3*inch, showBoundary = 0)
    frame7.addFromList(story7, objeto_canvas)
    
    #Firma Dr. Julio César Gómez Fernández
    story8 = []
    
    imagen_JCGF = Image(Firma_Dr_JCGF, 2*inch, inch)
    story8.append(imagen_JCGF)
    
    ptextofirmaJCGF = 'Dr. Julio César Gómez Fernández <br/>Vicepresidente de la AMFEM'
    
    story8.append(Paragraph(ptextofirmaJCGF, styles['firmaCentrado']))
    
    frame8 = Frame(585, -15, 2.8*inch, 2.3*inch, showBoundary = 0)
    frame8.addFromList(story8, objeto_canvas)
    
    objeto_canvas.showPage()
    
    
    story9 = []
    story9.append(PageBreak())
    
    #objeto_canvas.line(200, 500, 600, 500)
    #objeto_canvas.line(200, 500, 200, 300)
    #objeto_canvas.line(600, 500, 600, 300)
    #objeto_canvas.line(200, 425, 600, 425)
    #objeto_canvas.line(200, 300, 600, 300)
    
    story10 = []
    
    styles.add(ParagraphStyle(name='textoRegistro', alignment=TA_CENTER, fontName= 'Roboto', fontSize = 12, leading = 18))
    styles.add(ParagraphStyle(name='textoRegistroL', alignment=TA_LEFT, fontName= 'Roboto2', fontSize = 12, leading = 18))
    
    ptextoregistro='La Asociación Mexicana de Facultades y Escuelas de Medicina A.C. <br/> \
                    AMFEM A.C. <br/> \
                    Registró la presente constancia: <br/> <br/> '
    ptextoregistro2 = 'Fecha: 29 de abril del 2017.<br/> \
                    Libro: 1 <br/> \
                    No. de registro: ' +  libroregistro + ' <br/> \
                    Nombre de quien registra: M. en C. Gustavo Contreras Mayén.'
    story10.append(Paragraph(ptextoregistro,styles['textoRegistro']))
    story10.append(Paragraph(ptextoregistro2,styles['textoRegistroL']))
    
    #data=[('Fecha: 29 de abril del 2017','Libro: 1'),('No. de registro:','Nombre de quien registra: M. en C. Gustavo Contreras Mayén')]
    #table = Table(data, colWidths=150, rowHeights=50)
    #
    #table.setStyle(TableStyle([ 
    #        ('GRID', (0,0), (-1, -1), 1, colors.black),
    #        ('FONTSIZE', (0, 0), (-1, -1), 12), 
    #        ('TEXTFONT', (0, 0), (-1, -1), 'Roboto')]))
    #
    #
    #story10.append(table)
    
    frame9 = Frame(170, 210, 7*inch, 2.5*inch, showBoundary = 1)
    frame9.addFromList(story10, objeto_canvas)
    
    
    #Salvamos el PDF.
    objeto_canvas.save()

#os.startfile(fichero_pdf)

def readinputdata(filename): 
    fichero=open(filename,'r') 
    f=[] 
    line='0' 
    with open(filename) as tsv:
        for line in csv.reader(tsv, dialect="excel-tab"): #
            if len(line)>0 : 
                f.append(line) 
    fichero.close() 
    return array(f)

data=readinputdata(r'C:\Users\Master Chief\Documents\AMFEM 2017_01 Reunion Veracruz\Codigos python\asistentesConstancias_2017_05_06.dat') 

print (range(1, len(data)))
#print(data[7])

for i in range(len(data) + 1):
#for i in range(4):
    gafete = data[i][1]
    asistente =  data[i][2]
    nombreNormalizado = data[i][3]
    cadenahashAsistencia = data[i][5]
    libroregistro = data[i][7]
