from tkinter import *
window=Tk()
from window_definition import ImageWatermarkingApp
from open_file import OpenImage
from user_option import UserOption
from watermarking_process import WaterMarking
from preview_image import PreviewImage


choice=1

app=ImageWatermarkingApp(window)
open=OpenImage()
option=UserOption()
watermarking=WaterMarking()
preveiw=PreviewImage()



app.file_button['command']= lambda : open.openFile(app.canvas,app.image_name_label)
app.radiobutton1['command'] = lambda : option.text_watermark(app.logo_frame,app.text_frame)
app.radiobutton2 ['command']= lambda : option.logo_watermark(app.logo_frame,app.text_frame)
app.logo_upload_button['command'] = lambda : open.logo_open(app.canvas1)
app.preview_button['command'] = lambda :preveiw.preveiw_image(watermarking,app.canvas,app,open,option.choice)
app.save_button['command'] =preveiw.save_image
app.clear_button['command'] = open.clear_image



window.mainloop()