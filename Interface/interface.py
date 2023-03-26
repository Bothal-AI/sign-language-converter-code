import customtkinter as ctk
from PIL import Image
import json

class MainWindow:
    def __init__(self, master):  
        master.newWindow = None
        
        # Creating window
        master.geometry("340x210")
        master.resizable(False, False)
        master.wm_title("Sign Language Convertor")

        # Creating grid
        master.grid_rowconfigure(0, weight=1)
        master.grid_columnconfigure(0, weight=1)

        my_font = ("Helvetica", 14)

        # create buttons
        master.start = ctk.CTkButton(master, text="Start", font=my_font, width=150, height=30, command=lambda: start())
        master.settings = ctk.CTkButton(master, text="Settings", font=my_font, width=150, height=30, command=lambda: open_settings())
        master.exit = ctk.CTkButton(master, text="Exit", font=my_font, width=150, height=30, command=lambda: close())

        # add buttons to the grid
        master.start.grid(row=1, column=0, columnspan=1, padx=70, pady=(50,5), sticky="nsew")
        master.settings.grid(row=2, column=0, columnspan=1, padx=70, pady=5, sticky="nsew")
        master.exit.grid(row=3, column=0, columnspan=1, padx=70, pady=(5,50), sticky="nsew")
       
       
        def start():
           if master.newWindow is not None:
               master.newWindow.top.destroy()
               master.newWindow = None
           
           
        def open_settings():
            if master.newWindow is None:
                master.newWindow = SettingsWindow(master)
            else:
                master.newWindow.top.lift()

 
        def close():
            master.quit()


class SettingsWindow:
    def __init__(self, master):
        self.master = master
        self.top = ctk.CTkToplevel()

        # Creating window
        self.top.geometry("300x290")
        self.top.resizable(False, False)
        self.top.wm_title("Settings")

        # Creating grid
        self.top.grid_rowconfigure(0, weight=1)
        self.top.grid_columnconfigure(0, weight=1)
        
        # fonts
        my_font = ("Helvetica", 14)
        my_font_label = ("Helvetica", 14, "bold")
        
        # read from settings.json
        with open('settings.json', 'r') as file:
            settings = json.load(file)
        
        # radio btns
        self.var = ctk.IntVar()
        self.var.set(settings["translation_settings"])
        
        # checkbox btns
        if settings["gesture_instruction"] is True:
            self.box1 = ctk.IntVar(value=1)
        else:
            self.box1 = ctk.IntVar(value=0)
        
        if settings["text_to_speech"] is True:
            self.box2 = ctk.IntVar(value=1)
        else:
            self.box2 = ctk.IntVar(value=0)
        
        # create buttons
        trans_label = ctk.CTkLabel(self.top, text="Translation Settings:", font=my_font_label)
        overlay_radio = ctk.CTkRadioButton(self.top, text="On-Screen Overlay", font=my_font, variable=self.var, value=1)
        subtitles_radio = ctk.CTkRadioButton(self.top, text="Subtitles Text", font=my_font, variable=self.var, value=2)
        
        features_label = ctk.CTkLabel(self.top, text="Additonal Features:", font=my_font_label)
        instruction_check = ctk.CTkCheckBox(self.top, text="Gesture Instruction", font=my_font, onvalue=1, offvalue=0, variable=self.box1)
        speech_check = ctk.CTkCheckBox(self.top, text="Text-to-Speech", font=my_font, onvalue=1, offvalue=0, variable=self.box2)
        
        cancel = ctk.CTkButton(self.top, text="Cancel", font=my_font, width=135, height=30, command=lambda: self.go_back())
        save = ctk.CTkButton(self.top, text="Save", font=my_font, width=135, height=30, command=lambda: self.save())
        
        # add buttons to the grid
        trans_label.grid(row=0, column=0, columnspan=4, rowspan=1, padx=10, pady=10, sticky="nsew")
        overlay_radio.grid(row=1, column=0, columnspan=4, rowspan=1, padx=10, pady=5, sticky="w")
        subtitles_radio.grid(row=2, column=0, columnspan=4, rowspan=1, padx=10, pady=5, sticky="w")
        
        features_label.grid(row=3, column=0, columnspan=4, rowspan=1, padx=10, pady=10, sticky="nsew")
        instruction_check.grid(row=4, column=0, columnspan=4, rowspan=1, padx=10, pady=5, sticky="w")
        speech_check.grid(row=5, column=0, columnspan=4, rowspan=1, padx=10, pady=10, sticky="w")
        
        cancel.grid(row=6, column=0, columnspan=2, padx=(10,5), pady=(5,10), sticky="nsew")
        save.grid(row=6, column=2, columnspan=2, padx=(5,10), pady=(5,10), sticky="nsew")
        
        # close window
        self.top.protocol("WM_DELETE_WINDOW", self.go_back)


    def save(self):
        settings = {
        'translation_settings': self.var.get(),
        'on_screen_overlay': self.var.get() == 1,
        'subtitles_text': self.var.get() == 2,
        'gesture_instruction': self.box1.get() == 1,
        'text_to_speech': self.box2.get() == 1,
        }

        # Save settings to a file or a database
        with open('settings.json', 'w') as file:
            json.dump(settings, file)
            
        self.go_back()
        
        
    def go_back(self):
        self.master.newWindow = None
        self.top.destroy()



def main():
    root = ctk.CTk()
    window = MainWindow(root)
    root.mainloop()


if __name__ == "__main__":
    main()
