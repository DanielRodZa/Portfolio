import webbrowser
import os

from fpdf import FPDF


class PDFReport:
    """

    """
    def __init__(self, filename):
        self.filename = filename
        self.border = 0

    def generate(self, flatmate1, flatmate2, bill):
        flatmate1_pay = f"$ {flatmate1.pays(bill=bill, flatmate2=flatmate2):.2f}"
        flatmate2_pay = f"$ {flatmate2.pays(bill=bill, flatmate2=flatmate1):.2f}"

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        pdf.image("files/house.png", w=30, h=30)

        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt='Flatmates Bill', border=self.border, align='C', ln=1)


        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=100, h=40, txt="Period: ", border=self.border)
        pdf.cell(w=200, h=40, txt=bill.period, border=self.border, ln=1)

        pdf.cell(w=100, h=40, txt=flatmate1.name, border=self.border)
        pdf.cell(w=200, h=40, txt=flatmate1_pay, border=self.border, ln=1)

        pdf.cell(w=100, h=40, txt=flatmate2.name, border=self.border)
        pdf.cell(w=200, h=40, txt=flatmate2_pay, border=self.border, ln=1)

        pdf.output(f"files/{self.filename}")

        os.chdir("files")

        webbrowser.open(self.filename)
