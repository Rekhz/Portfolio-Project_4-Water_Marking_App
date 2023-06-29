
from PIL import Image, ImageTk
from tkinter import filedialog


class OpenImage:
    def __init__(self):
        self.image=None
        self.rImg=None
        self.canvas=None




    def logo_open(self,canvas1):


        self.logo_path = filedialog.askopenfilename(filetypes=(("JPEG files", "*.jpg"), ("PNG files", "*.png")))
        self.logo_image = Image.open(self.logo_path)
        self.logo_size = self.logo_image.size
        if self.logo_size[0] > 100 or self.logo_size[1] > 100:
            self.logo_factor = min(float(100) / self.logo_size[1], float(100) / self.logo_size[0])
            self.width = int(self.logo_size[0] * self.logo_factor)
            self.height = int(self.logo_size[1] * self.logo_factor)
            self.logo_re_sizeimg = self.logo_image.resize((self.width, self.height), Image.LANCZOS)
            self.logo_re_sizeimg = ImageTk.PhotoImage(self.logo_re_sizeimg)
            logo_on_canvas =canvas1.create_image(50, 50, image=self.logo_re_sizeimg)
        else:
            self.logo_re_sizeimg = ImageTk.PhotoImage(self.logo_image)
            logo_on_canvas =canvas1.create_image(50, 50, image=self.logo_re_sizeimg)
    def openFile(self,canvas,image_name_label):
        self.canvas=canvas
        self.path = filedialog.askopenfilename(filetypes=(("JPEG files", "*.jpg"), ("PNG files", "*.png")))
        self.img_name = self.path.split("/")[-1].split(".")[0]
        image_name_label.config(text=self.img_name)
        self.image = Image.open(self.path)
        self.o_size = self.image.size
        self.f_size = (600, 600)
        self.factor = min(float(self.f_size[1]) / self.o_size[1], float(self.f_size[0]) / self.o_size[0])
        self.width = int(self.o_size[0] * self.factor)
        self.height = int(self.o_size[1] * self.factor)
        self.rImg = self.image.resize((self.width, self.height), Image.LANCZOS)
        self.rImg = ImageTk.PhotoImage(self.rImg)
        image_on_canvas = self.canvas.create_image(300, 300, image=self.rImg)

    def clear_image(self):
        # canvas.delete("all")
        image_on_canvas = self.canvas.create_image(300, 300, image=self.rImg)
