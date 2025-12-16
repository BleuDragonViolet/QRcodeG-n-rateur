import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
import qrcode

class QRApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Générateur de QR Code")
        self.root.geometry("420x520")
        self.root.resizable(False, False)

        style = ttk.Style()
        style.theme_use("clam")

        ttk.Label(
            root,
            text="Générateur de QR Code",
            font=("Segoe UI", 18, "bold")
        ).pack(pady=20)

        ttk.Label(root, text="URL :", font=("Segoe UI", 11)).pack()
        self.url_entry = ttk.Entry(root, width=45)
        self.url_entry.pack(pady=8)

        ttk.Button(
            root,
            text="Générer",
            command=self.generate_qr
        ).pack(pady=10)

        self.qr_label = ttk.Label(root)
        self.qr_label.pack(pady=20)

        ttk.Button(
            root,
            text="Enregistrer le QR",
            command=self.save_qr
        ).pack()

        self.qr_image = None

    def generate_qr(self):
        url = self.url_entry.get().strip()
        if not url:
            messagebox.show_error("Erreur", "Veuillez entrer une URL")
            return

        qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=4
        )
        qr.add_data(url)
        qr.make(fit=True)

        self.qr_image = qr.make_image(fill_color="black", back_color="white")
        preview = self.qr_image.resize((250, 250))
        self.tk_img = ImageTk.PhotoImage(preview)

        self.qr_label.config(image=self.tk_img)

    def save_qr(self):
        if not self.qr_image:
            messagebox.show_error("Erreur", "Aucun QR généré")
            return

        file = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("Image PNG", "*.png")]
        )

        if file:
            self.qr_image.save(file)
            messagebox.show_info("Succès", "QR code enregistré")

if __name__ == "__main__":
    root = tk.Tk()
    app = QRApp(root)
    root.mainloop()
