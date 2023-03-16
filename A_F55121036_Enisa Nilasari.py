import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
import cv2

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Perbaikan Citra")
        self.geometry("600x400")

        self.original_image_label = tk.Label(self)
        self.original_image_label.pack(side=tk.TOP)

        self.result_image_label = tk.Label(self)
        self.result_image_label.pack(side=tk.TOP)

        self.open_button = tk.Button(self, text="Buka Gambar", command=self.open_image)
        self.open_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.method1_button = tk.Button(self, text="Metode 1", command=self.method1)
        self.method1_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.method2_button = tk.Button(self, text="Metode 2", command=self.method2)
        self.method2_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.image = None

    def open_image(self):
        filename = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.jpeg")])

        if filename:
            # membaca gambar menggunakan OpenCV
            self.image = cv2.imread(filename)
            self.image = cv2.resize(self.image, (300,200))
            # mengubah mode warna dari BGR ke RGB
            self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
            self.image = cv2.resize(self.image, (300, 200))
            # menampilkan gambar asli di label
            self.show_image(self.original_image_label, self.image)
            self.image = cv2.resize(self.image, (300, 200))

    def method1(self):
        if self.image is not None:
            # melakukan operasi perbaikan citra dengan metode 1
            result = cv2.GaussianBlur(self.image, (5, 5), 0)
            # menampilkan gambar hasil di label
            self.show_image(self.result_image_label, result)

    def method2(self):
        if self.image is not None:
            # melakukan operasi perbaikan citra dengan metode 2
            result = cv2.medianBlur(self.image, 5)
            # menampilkan gambar hasil di label
            self.show_image(self.result_image_label, result)

    def show_image(self, label, image):
        image_tk = ImageTk.PhotoImage(Image.fromarray(image))
        label.configure(image=image_tk)
        label.image = image_tk

if __name__ == '__main__':
    window = MainWindow()
    window.mainloop()



