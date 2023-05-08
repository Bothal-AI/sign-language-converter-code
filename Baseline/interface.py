import customtkinter as ctk
from PIL import Image
from Classifier_in_functions import classify

class MainWindow:
    def __init__(self, master):  
        
        # Creating window
        master.geometry("320x190")
        master.resizable(False, False)
        master.wm_title("Sign Language Convertor")

        # Creating grid
        master.grid_rowconfigure(0, weight=1)
        master.grid_columnconfigure(0, weight=1)

        my_font = ("Helvetica", 14)

        # create buttons
        master.start = ctk.CTkButton(master, text="Start", font=my_font, width=150, height=30, command=lambda: start())
        master.exit = ctk.CTkButton(master, text="Exit", font=my_font, width=150, height=30, command=lambda: close())

        # add buttons to the grid
        master.start.grid(row=0, column=0, columnspan=1, padx=70, pady=(60,5), sticky="nsew")
        master.exit.grid(row=1, column=0, columnspan=1, padx=70, pady=(5,60), sticky="nsew")
       
       
        def start():
            classify()

        def close():
            master.quit()


def main():
    root = ctk.CTk()
    window = MainWindow(root)
    root.mainloop()


if __name__ == "__main__":
    main()
