import fpdf
import Tkinter as tk

class PDFConverter:
    def __init__(self, master):
        self.master = master
        master.title("Convertidor de PDF")

        self.label = tk.Label(master, text="Ingrese el texto para convertir a PDF:")
        self.label.pack()

        self.text_entry = tk.Text(master, height=10, width=50)
        self.text_entry.pack()

        self.convert_button = tk.Button(master, text="Convertir a PDF", command=self.convert_to_pdf)
        self.convert_button.pack()

    def convert_to_pdf(self):
        text = self.text_entry.get("1.0", tk.END)
        pdf = fpdf.FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, text)
        pdf.output("output.pdf")
        tk.messagebox.showinfo("Éxito", "El PDF ha sido creado exitosamente.")