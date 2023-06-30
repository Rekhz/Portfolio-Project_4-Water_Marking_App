from tkinter import messagebox
from PIL import Image,ImageFont, ImageDraw


class WaterMarking:



   def transparency_check(self,transparency):

      if transparency == 0:
         transparency = 0
      elif transparency == 10:
         transparency = 255
      elif transparency == 5:
         transparency = 128
      elif transparency == 1:
         transparency = 25
      elif transparency == 2:
         transparency = 50
      elif transparency == 3:
         transparency = 75
      elif transparency == 4:
         transparency = 100
      elif transparency == 6:
         transparency = 150
      elif transparency == 7:
         transparency = 175
      elif transparency == 8:
         transparency = 200
      elif transparency == 9:
         transparency = 225
      return transparency


   def color_check(self,color,transparency):
      if color == "red":
         fill = (255, 0, 0, transparency)
      elif color == "green":
         fill = (0, 255, 0, transparency)
      elif color == "white":
         fill = (255, 255, 255, transparency)
      elif color == "blue":
         fill = (0, 0, 255, transparency)
      elif color == "black":
         fill = (0, 0, 0, transparency)
      elif color == "yellow":
         fill = (255, 255, 0, transparency)
      elif color == "purple":
         fill = (191, 64, 191, transparency)
      return fill

   def watermark_line_check_for_text(self,o_size,text_to_be_added,fill):

      font = self.app.font_combo.get() + ".ttf"
      font_size = self.app.font_size_combo.get()
      # print(int(font_size))
      orientation = self.app.orientation_combo.get()
      watermark_line_option = self.app.line_list_combo.get()
      # print(watermark_line_option)

      ft = ImageFont.truetype(font=font, size=int(font_size))
      tim = Image.new('RGBA', (o_size[0] + 100, o_size[1] + 100), (0, 0, 0, 0))
      dr = ImageDraw.Draw(tim)
      text_width, text_height = dr.textsize(text_to_be_added, font=ft)

      if watermark_line_option == "Multiple Lines":

         for i in range(50, o_size[0] - 10, text_width + 100):
            for j in range(50, o_size[1] - 10, 400):
               dr.text((i, j), text=text_to_be_added, font=ft, fill=fill)
         tim = tim.rotate(int(orientation))
         self.watermarked_image.paste(tim, (0, 0), tim)

      elif watermark_line_option == "Single Line - Center of the Image":

         dr.text((o_size[0] / 2 - text_width / 2, o_size[1] / 2 - text_height / 2), text=text_to_be_added, font=ft,
                 fill=fill)
         tim = tim.rotate(int(orientation))
         self.watermarked_image.paste(tim, (0, 0), tim)

      elif watermark_line_option == "Single Line - Top Left":
         # print("Single line -left")
         if int(orientation) != 0:
            messagebox.showinfo(title="Choose Orientation", message="Please choose orientatios as 0")
         else:
            dr.text((50, 50), text=text_to_be_added, font=ft, fill=fill)
            tim = tim.rotate(int(orientation))
            self.watermarked_image.paste(tim, (0, 0), tim)

      elif watermark_line_option == "Single Line - Top Right":
         if int(orientation) != 0:
            messagebox.showinfo(title="Choose Orientation", message="Please choose orientatios as 0")
         else:
            dr.text((o_size[0] - 50 - text_width, 50), text=text_to_be_added, font=ft, fill=fill)
            tim = tim.rotate(int(orientation))
            self.watermarked_image.paste(tim, (0, 0), tim)

      elif watermark_line_option == "Single Line - Bottom Left":
         if int(orientation) != 0:
            messagebox.showinfo(title="Choose Orientation", message="Please choose orientatios as 0")
         else:
            dr.text((50, o_size[1] - 50 - text_height), text=text_to_be_added, font=ft, fill=fill)
            tim = tim.rotate(int(orientation))
            self.watermarked_image.paste(tim, (0, 0), tim)

      elif watermark_line_option == "Single Line - Bottom Right":
         if int(orientation) != 0:
            messagebox.showinfo(title="Choose Orientation", message="Please choose orientatios as 0")
         else:
            dr.text((o_size[0] - 50 - text_width, o_size[1] - 50 - text_height), text=text_to_be_added, font=ft,
                    fill=fill)
            tim = tim.rotate(int(orientation))
            self.watermarked_image.paste(tim, (0, 0), tim)


   def water_marking(self,app,open,choice):
      self.app = app
      self.open = open
      self.choice = choice
      if self.choice==None:
         self.choice=1


      o_size = self.open.image.size
      self.watermarked_image=self.open.image.copy()


      if self.choice==1:
         text_to_be_added = self.app.watermark_text_entry.get().title()

         if len(text_to_be_added) == 0 or self.app.orientation_combo.get()=="Pick a Text Orientation" or self.app.color_combo.get() == "Pick a Color" or self.app.font_combo.get() == "Pick a Font" or self.app.font_size_combo.get() == "Pick a Font Size" or self.app.line_list_combo.get()=="Pick a Position for Printing":
            print("error")
            messagebox.showinfo(title="Empty", message="Please choose all the fields")
         transparency_value=int(self.app.Scala2.get())
         color_string = self.app.color_combo.get()
         transparency = self.transparency_check(transparency_value)
         fill = self.color_check(color_string, transparency)

         self.watermark_line_check_for_text(o_size,text_to_be_added,fill)

      elif self.choice==2:
         if self.app.logo_line_list_combo.get() == "Pick a Position for Printing" or self.app.logo_size_list_combo.get() == "Pick a Size":
            messagebox.showinfo(title="Empty", message="Please choose all the fields")


         logo_size = self.open.logo_image.size
         if logo_size==(0,0):
            messagebox.showinfo(title="Upload Logo", message="Please upload Logo")

         user_logo_size=self.app.logo_size_list_combo.get()
         if logo_size<(100,100):
            messagebox.showinfo(title="Small",message="Logo is dispalyed in its original size..")
            self.logo = self.open.logo_image
         if user_logo_size=="Small":
            # if logo_size[0] > 100 or logo_size[1] > 100:
            logo_factor = min(float(100) / logo_size[1], float(100) / logo_size[0])
            width = int(logo_size[0] * logo_factor)
            height = int(logo_size[1] * logo_factor)
            self.logo = self.open.logo_image.resize((width, height), Image.LANCZOS)
         elif user_logo_size=="Medium":
            logo_factor = min(float(300) / logo_size[1], float(300) / logo_size[0])
            width = int(logo_size[0] * logo_factor)
            height = int(logo_size[1] * logo_factor)
            self.logo = self.open.logo_image.resize((width, height), Image.LANCZOS)
         elif user_logo_size=="Large":
            logo_factor = min(float(500) / logo_size[1], float(500) / logo_size[0])
            width = int(logo_size[0] * logo_factor)
            height = int(logo_size[1] * logo_factor)
            self.logo = self.open.logo_image.resize((width, height), Image.LANCZOS)

         logo_position_entry = self.app.logo_line_list_combo.get()

         if logo_position_entry == "Center":
            position_x = o_size[0] / 2-(self.logo.size[0])/2
            position_y = o_size[1] / 2-(self.logo.size[1])/2

         elif logo_position_entry == "Top Left":
            position_x = 50
            position_y = 50
         elif logo_position_entry == "Top Right":
            position_x = o_size[0] - self.logo.size[0] - 50
            position_y = 50
         elif logo_position_entry == "Bottom Left":
            position_x = 50
            position_y = o_size[1] - self.logo.size[1] - 50

         elif logo_position_entry == "Bottom Right":
            position_x = o_size[0] - self.logo.size[0] - 50
            position_y = o_size[1] - self.logo.size[1] - 50

         self.watermarked_image.paste(self.logo, (int(position_x), int(position_y)), mask=None)
      return self.watermarked_image