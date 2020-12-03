import fpdf

from fpdf import FPDF  # fpdf class

class PDF(FPDF):

     pass # nothing happens when it is executed.

pdf = FPDF()

pdf = PDF(orientation='P', unit='mm', format='A4')

pdf.add_page()

pdf_w=5

pdf_h=5

class PDF(FPDF):

    def lines(self):

        self.set_line_width(0.0)

        self.line(0,pdf_h/2,210,pdf_h/2)

pdf.line(0,0,0,0)

class PDF(FPDF):

    def lines(self):

        self.set_line_width(0.0)

        self.line(5.0,5.0,205.0,5.0) # top one

        self.line(5.0,292.0,205.0,292.0) # bottom one

        self.line(5.0,5.0,5.0,292.0) # left one

        self.line(205.0,5.0,205.0,292.0) # right one

class PDF(FPDF):

    def lines(self):

        self.rect(5.0, 5.0, 200.0,287.0)
pdf.rect( 5.0, 5.0, 200.0,287.0, style='')
pdf.set_font("Arial", size = 16) 

pdf.cell(w = 200.0, h =10.0, align='L', ln = 1, txt="2. Regression sumary", border=0)

f = open(r"D:\S1 - MAG 1\Python\Exercice2.txt" , "r") 
pdf.set_font("Arial", size = 10)
# insert the texts in pdf 
for x in f: 
    pdf.cell(200, 10, txt = x, ln = 2, align = 'L') 

pdf.output('analysis231.pdf','F')
