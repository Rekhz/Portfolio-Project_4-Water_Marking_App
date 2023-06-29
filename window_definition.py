from tkinter import *
from matplotlib import font_manager
from tkinter import ttk



class ImageWatermarkingApp:
    def __init__(self,window):
        self.window = window
        self.window.title("Image Watermarking App")
        self.window.minsize(width=800, height=800)

        # self.watermarked_image = None
        # self.path = None
        # self.img_name = None
        # self.image = None
        # self.logo_path = None
        # self.logo_image = None
        # self.rImg = None
        # self.logo_re_sizeimg = None
        # self.choice = 1

        self.create_widgets()

    def create_widgets(self):

        self.window.option_add('*font', 'Arial 12 ', )
        self.window.option_add('*foreground', 'black')

        self.window.config(background="#f6f2f2", padx=50, pady=50, )
        self.window.tk_setPalette(background='#f6f2f2')

        self.title_label = Label(self.window, text="Image Watermarking Tool", font=("Helvetica", 24, "bold"))
        self.title_label.grid(row=0, column=0, columnspan=6, padx=200, pady=10, sticky="ew")

        self.image_name_label = Label(self.window, text="Image Name")
        self.image_name_label.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="ew")

        self.canvas = Canvas(self.window, width=600, height=600, border=1, relief=SUNKEN, borderwidth=1, highlightthickness=2,
                        selectforeground="white")
        self.canvas.grid(row=2, column=0, columnspan=3, rowspan=12, padx=10, pady=10)

        self.file_open_label = Label(self.window, text="Upload the Image in which watermark needs to be added", justify="left",
                                anchor="w")
        self.file_open_label.grid(row=2, column=4, sticky="ew", padx=10, pady=10)
        # self.file_button = Button(self.window, text="Open", command=OpenImage().openFile)
        self.file_button = Button(self.window, text="Open")

        self.file_button.grid(row=2, column=5, padx=10, pady=10, sticky="ew")

        self.choice_label = Label(self.window, text="Please select whether you would like to watermark with a logo or with text:",
                             justify="left", anchor="w")
        self.choice_label.grid(row=3, column=4, columnspan=3, sticky="ew", padx=10, pady=10)

        self.radio_state = IntVar()
        # self.radiobutton1 = Radiobutton(self.window, text="Text", value=1, variable=self.radio_state, command=text_watermark,
        #                            justify="center", )
        self.radiobutton1 = Radiobutton(self.window, text="Text", value=1, variable=self.radio_state,justify="center")
        # self.radiobutton2 = Radiobutton(self.window, text="Logo", value=2, variable=self.radio_state, command=logo_watermark,justify="center")
        self.radiobutton2 = Radiobutton(self.window, text="Logo", value=2, variable=self.radio_state,justify="center", )

        # radiobutton3 = Radiobutton(window, text="Show Both", value=3, variable=radio_state, command=show_both,justify="center",)
        self.radiobutton1.grid(row=4, column=4, pady=10, sticky="nw")
        self.radiobutton2.grid(row=5, column=4, pady=10, sticky="nw")
        # radiobutton2.select()
        self.radio_state.set(1)
        # radiobutton3.grid(row=6, column=4,pady=10,sticky="nw")

        self.logo_frame = Frame(self.window, width=50, background='#f6f2f2', relief=RAISED, border=3, borderwidth=1,
                           highlightbackground="#f6f2f2", highlightcolor="#f6f2f2")
        self.text_frame = Frame(self.window, width=50, background='#f6f2f2', relief=RAISED, border=3, borderwidth=1,
                           highlightbackground="#f6f2f2", highlightcolor="#f6f2f2")
        self.text_frame.grid(row=6, column=4, columnspan=3, sticky="ew", padx=10, pady=10, )
        self.logo_frame.grid(row=14, column=4, columnspan=3, sticky="ew", padx=10, pady=10, )
        self.text_frame.rowconfigure(0, weight=1)
        self.logo_frame.rowconfigure(0, weight=1)

        self.text_details_label = Label(self.text_frame, text="Text Details")
        self.text_details_label.grid(row=7, column=4, columnspan=3, sticky="ew", padx=10, pady=10)

        self.watermark_label = Label(self.text_frame, text="Enter the text that needs to be added", anchor="w")
        self.watermark_label.grid(row=8, column=4, sticky="ew", padx=10, pady=10)
        self.watermark_text_entry = Entry(self.text_frame, width=30, bg="white", )
        self.watermark_text_entry.grid(row=8, column=5, sticky="ew", padx=10, pady=10)

        self.orientation_label = Label(self.text_frame, text="Choose orientation for text", anchor="w")
        self.orientation_label.grid(row=9, column=4, sticky="ew", padx=10, pady=10)
        self.orientation_list = ["0", "30", "320", "90"]
        self.orientation_combo = ttk.Combobox(self.text_frame, values=self.orientation_list)
        self.orientation_combo.set("Pick a Text Orientation")
        self.orientation_combo.grid(row=9, column=5, sticky="ew", padx=10, pady=10)

        self.transparency_label = Label(self.text_frame, text="Scale of transparency", anchor="w")
        self.transparency_label.grid(row=10, column=4, sticky="ew", padx=10, pady=10)
        self.Scala2 = Scale(self.text_frame, from_=0, to=10, orient=HORIZONTAL, fg="white", )
        self.Scala2.set(8)
        self.Scala2.grid(row=10, column=5, sticky="ew", padx=10, pady=10)

        self.color_list = ["red", "green", "white", "blue", "black", "yellow", "purple"]
        self.font_combo_list = []
        self.ttf_fonts = [f.fname for f in font_manager.fontManager.ttflist if ".ttf" in f.fname]
        for f in self.ttf_fonts:
            if not "matplotlib" in f:
                self.font_combo_list.append((f.split('\\')[-1]).split(".")[0])

        self.font_size_list = ["10", "20", "30", "40", "50", "60", "80", "90"]
        self.color_combo = ttk.Combobox(self.text_frame, values=self.color_list)
        self.color_combo.set("Pick a Color")

        self.font_characteristics_label = Label(self.text_frame, text="Choose the Font Details")
        self.font_characteristics_label.grid(row=11, column=4, columnspan=3, sticky="ew", padx=10, pady=10)

        self.color_combo.grid(row=12, column=4, sticky="ew", padx=10, pady=10)
        self.font_combo = ttk.Combobox(self.text_frame, values=self.font_combo_list, )
        self.font_combo.set("Pick a Font")
        self.font_combo.grid(row=12, column=5, sticky="ew", padx=10, pady=10)
        self.font_size_combo = ttk.Combobox(self.text_frame, values=self.font_size_list)
        self.font_size_combo.set("Pick a Font Size")
        self.font_size_combo.grid(row=12, column=6, sticky="ew", padx=10, pady=10)

        self.watermark_text_line_choice = Label(self.text_frame, text="Enter the type of watermark and position", anchor="w")
        self.watermark_text_line_choice.grid(row=13, column=4, sticky="ew", padx=10, pady=10)
        self.line_list = ["Multiple Lines", "Single Line - Center of the Image", "Single Line - Top Left",
                     "Single Line - Top Right", "Single Line - Bottom Left", "Single Line - Bottom Right"]
        self.line_list_combo = ttk.Combobox(self.text_frame, values=self.line_list)
        self.line_list_combo.set("Pick a Position for Printing")
        self.line_list_combo.grid(row=13, column=5, sticky="ew", padx=10, pady=10)

        self.logo_frame_label = Label(self.logo_frame, text="Logo Details", )
        self.logo_frame_label.grid(row=15, column=4, columnspan=3, padx=10, pady=10, sticky="ew")

        self.logo_label = Label(self.logo_frame, text="Upload the logo", width=30, anchor="w")
        self.logo_label.grid(row=16, column=4, sticky="ew", padx=10, pady=10)
        # self.logo_upload_button = Button(self.logo_frame, text="Open Logo Image", command=logo_open, width=30)
        self.logo_upload_button = Button(self.logo_frame, text="Open Logo Image",width=30)

        self.logo_upload_button.grid(row=16, column=5, sticky="ew", padx=10, pady=10)

        self.canvas1 = Canvas(self.logo_frame, width=100, height=100, border=1, relief=SUNKEN)
        self.canvas1.grid(row=16, column=6, rowspan=2, padx=50, pady=10, )

        self.logo_line_list = ["Center", "Top Left", "Top Right", "Bottom Left", "Bottom Right"]
        self.logo_line_list_combo = ttk.Combobox(self.logo_frame, values=self.logo_line_list)
        self.logo_position_label = Label(self.logo_frame, text="Enter the position:", anchor="w")
        self.logo_position_label.grid(row=17, column=4, sticky="ew", padx=10, pady=10)
        self.logo_line_list_combo.set("Pick a Position for Printing")
        self.logo_line_list_combo.grid(row=17, column=5, sticky="ew", padx=10, pady=10)
        self.logo_size_label = Label(self.logo_frame, text="Enter the size of the logo to be printed", anchor="w")
        self.logo_size_label.grid(row=18, column=4, sticky="ew", padx=10, pady=10)
        self.logo_size_list = ["Small", "Medium", "Large"]
        self.logo_size_list_combo = ttk.Combobox(self.logo_frame, values=self.logo_size_list)
        self.logo_size_list_combo.set("Pick a Size")
        self.logo_size_list_combo.grid(row=18, column=5, sticky="ew", padx=10, pady=10)

        # self.preview_button = Button(self.window, text="Preview Image", command=preveiw_image, width=10)
        self.preview_button = Button(self.window, text="Preview Image",width=10)

        self.preview_button.grid(row=13, column=0, sticky="ew", padx=10, pady=5)
        # self.save_button = Button(self.window, text="Save Image", command=save_image, width=10)
        self.save_button = Button(self.window, text="Save Image",width=10)

        self.save_button.grid(row=13, column=1, sticky="ew", padx=10, pady=5)
        # self.clear_button = Button(self.window, text="Clear", command=clear_image, width=10)
        self.clear_button = Button(self.window, text="Clear",width=10)

        self.clear_button.grid(row=13, column=2, sticky="ew", padx=10, pady=5)
        self.close_button = Button(self.window, text="Close Window", command=self.window.destroy, width=10)
        self.close_button.grid(column=1, row=14, sticky="ew", padx=10, pady=2)

        self.logo_frame.grid_forget()




















        # self.title_label = Label(self.window, text="Image Watermarking Tool", font=("Helvetica", 24, "bold"))
        # self.title_label.grid(row=0, column=0, columnspan=7, padx=10, pady=10)
        #
        # self.text_frame = Frame(self.window)
        # self.text_frame.grid(row=6, column=4, columnspan=3, sticky="ew", padx=10, pady=10)
        #
        # self.logo_frame = Frame(self.window)
        # self.logo_frame.grid(row=6, column=4, columnspan=3, sticky="ew", padx=10, pady=10)
        #
        # self.canvas = Canvas(self.window)
        # self.canvas.grid(row=7, column=0, columnspan=7, padx=10, pady=10)
        #
        # self.watermark_text_label = Label(self.text_frame, text="Watermark Text:")
        # self.watermark_text_label.grid(row=0, column=0, padx=10, pady=10)
        #
        # self.watermark_text_entry = Entry(self.text_frame)
        # self.watermark_text_entry.grid(row=0, column=1, padx=10, pady=10)
        #
        # self.color_label = Label(self.text_frame, text="Color:")
        # self.color_label.grid(row=1, column=0, padx=10, pady=10)
        #
        # self.color_combo = ttk.Combobox(self.text_frame, values=["Pick a Color", "red", "green", "white", "blue", "black", "yellow", "purple"])
        # self.color_combo.current(0)
        # self.color_combo.grid(row=1, column=1, padx=10, pady=10)
        #
        # self.font_label = Label(self.text_frame, text="Font:")
        # self.font_label.grid(row=2, column=0, padx=10, pady=10)
        #
        # self.font_combo = ttk.Combobox(self.text_frame, values=["Pick a Font"] + [f.name for f in font_manager.fontManager.ttflist])
        # self.font_combo.current(0)
        # self.font_combo.grid(row=2, column=1, padx=10, pady=10)
        #
        # self.font_size_label = Label(self.text_frame, text="Font Size:")
        # self.font_size_label.grid(row=3, column=0, padx=10, pady=10)
        #
        # self.font_size_combo = ttk.Combobox(self.text_frame, values=["Pick a Font Size"] + [str(i) for i in range(1, 101)])
        # self.font_size_combo.current(0)
        # self.font_size_combo.grid(row=3, column=1, padx=10, pady=10)
        #
        # self.orientation_label = Label(self.text_frame, text="Orientation:")
        # self.orientation_label.grid(row=4, column=0.