from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        self.set_font("Helvetica", "B", 40)
        self.cell(0, 25, "CS50 Shirtificate", align="C")


def main():
    name = input("Name: ")

    pdf = PDF(orientation="P", unit="mm", format="A4")
    pdf.set_auto_page_break(False)
    pdf.add_page()

    pdf.image("shirtificate.png", x=10, y=70, w=190)

    pdf.set_xy(0, 115)
    pdf.set_font("Helvetica", "B", 24)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(0, 10, f"{name} took CS50", align="C")

    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
