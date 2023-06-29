class UserOption:

    def __init__(self):
        self.choice=None

    def text_watermark(self,logo_frame,text_frame):
       self.choice=1
       logo_frame.grid_forget()
       text_frame.grid(row=6, column=4, columnspan=3, sticky="ew", padx=10, pady=10, )


    def logo_watermark(self,logo_frame,text_frame):

       self.choice=2
       text_frame.grid_forget()
       logo_frame.grid(row=6, column=4, columnspan=3, sticky="ew", padx=10, pady=10, )

