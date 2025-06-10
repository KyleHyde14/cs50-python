from fpdf import FPDF

def main():
    name = input('Student name: ').capitalize()
    create_pdf(name)

class custom_pdf(FPDF):
    def header(self):
        self.image('./shirtificate.png', 12, 75, 180)
        self.set_font('helvetica', style='', size=50)
        self.cell(0, 57, 'CS50 Shirtificate', align='C')
        self.ln(20)

def create_pdf(name):
    pdf = custom_pdf()
    pdf.set_auto_page_break(False)
    pdf.add_page()
    pdf.set_font('Courier', style='B', size=30)
    pdf.set_text_color(212, 175, 55)
    pdf.cell(0, 213, f'{name} took CS50', align='C')
    pdf.output('shirtificate.pdf')


if __name__ == '__main__':
    main()
