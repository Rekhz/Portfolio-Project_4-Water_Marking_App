from PIL import Image,ImageTk
from tkinter import messagebox
import os
from tkinter.simpledialog import askstring

class PreviewImage:
    def __init__(self):
        self.rImg = None
        self.watermarked_image=None
        self.path=None

    def preveiw_image(self,watermarking,canvas,app,open,choice):
        self.open=open
        self.path=open.path
        self.watermarking = watermarking
        self.app=app
        # self.canvas = canvas
        self.watermarked_image=self.watermarking.water_marking(self.app,self.open,choice)

        # self.canvas = canvas
        try:



          o_size =self.watermarked_image.size


          f_size = (600, 600)
          factor = min(float(f_size[1]) / o_size[1], float(f_size[0]) / o_size[0])

          width = int(o_size[0] * factor)
          height = int(o_size[1] * factor)


          self.rImg = self.watermarked_image.resize((width, height), Image.LANCZOS)

          self.rImg = ImageTk.PhotoImage(self.rImg)

          image_on_canvas = self.app.canvas.create_image(300, 300, image=self.rImg)
          # self.canvas.image = rImg  # keep reference to the image
          # watermarked_image.show()
        except NameError:
             messagebox.showinfo(title="Empty", message="Please upload an image")
#

    def save_image(self):
        # print(self.path)
        x = self.path.split("/")[:-1]
        img_name = self.path.split("/")[-1].split(".")[0]

        new_path = "/".join(x)
        altered_path = new_path + "/"
        folder_path = new_path + "/" + "water-marked/"
        try:
            final_filepath = os.path.join(folder_path, f"watermarked_image_{img_name}.jpg")
            if os.path.exists(final_filepath):
                messagebox.showwarning(title="Warning",
                                       message=f"Error: 'watermarked_image_{img_name}.jpg' already exists!")
                new_file_name = askstring('Name', 'Enter the new name')
                final_filepath = os.path.join(folder_path, f"{new_file_name}.jpg")
                self.watermarked_image.save(final_filepath)
                messagebox.showinfo(title="Success",
                                    message="Image saved in 'watermarked_images' folder at original location.")
                self.app.canvas.delete("all")
                # print(f"Error: 'watermarked_image_{img_name}.jpg' already exists!")
            else:
                self.watermarked_image.save(final_filepath)
                print("watermark added")
                messagebox.showinfo(title="Success",
                                    message="Image saved in 'watermarked_images' folder at original location.")
        except FileNotFoundError:
            folder = "water-marked"
            path = os.path.join(altered_path, folder)
            os.mkdir(path)
            final_filepath = os.path.join(folder_path, f"watermarked_image_{img_name}.jpg")
            if os.path.exists(final_filepath):
                messagebox.showwarning(title="Warning",
                                       message=f"Error: 'watermarked_image_{img_name}.jpg' already exists!")
                new_file_name = askstring('Name', 'Enter the new name')
                final_filepath = os.path.join(folder_path, f"{new_file_name}.jpg")
                self.watermarked_image.save(final_filepath)
                messagebox.showinfo(title="Success",
                                    message="Image saved in 'watermarked_images' folder at original location.")
                self.app.canvas.delete("all")
                # print(f"Error: 'watermarked_image_{img_name}.jpg' already exists!")
            else:
                self.watermarked_image.save(final_filepath)
                # print("watermark added")
                messagebox.showinfo(title="Success",
                                    message="Image saved in 'watermarked_images' folder at original location.")
    #
