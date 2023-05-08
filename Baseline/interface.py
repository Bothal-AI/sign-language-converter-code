import customtkinter as ctk
from PIL import Image
from AtoE_Classifier import classifyAtoE
from FtoI_Classifier import classifyFtoI
from KtoO_Classifier import classifyKtoO
from PtoT_Classifier import classifyPtoT
from UtoY_Classifier import classifyUtoY
from Numerical_Classifier_in_functions import classifyNumerical

class MainWindow:
    def __init__(self, master):

        # Creating window
        master.geometry("520x485")
        master.resizable(True, True)
        master.wm_title("SignPal ASL Convertor")

        # Creating grid
        master.grid_rowconfigure(0, weight=1)
        master.grid_columnconfigure(0, weight=1)

        # Fonts
        my_font = ("Helvetica", 14)

        # Image
        master.pic = ctk.CTkImage(dark_image=Image.open("letters_.png"), size=(500, 400))

        # create buttons
        master.image = ctk.CTkButton(
            master,
            text=None,
            fg_color="black",
            hover_color="black",
            height=400,
            corner_radius=0,
            border_spacing=8,
            image=master.pic,
        )
        master.start = ctk.CTkButton(
            master,
            text="Start",
            font=my_font,
            width=120,
            height=30,
            command=lambda: start(),
        )
        master.exit = ctk.CTkButton(
            master,
            text="Exit",
            font=my_font,
            width=120,
            height=30,
            command=lambda: close(),
        )


        master.current_var = ctk.StringVar(value='A to E')
        master.combobox = ctk.CTkComboBox(
            master, 
            values=['A to E', 'F to I', 'K to O', 'P to T', 'U to Y', 'Numbers'],
            state='readonly',
            variable=master.current_var,
        )


        # add buttons to the grid
        master.image.grid(
            row=0, column=0, columnspan=3, padx=10, pady=(10,5), sticky="nsew"
        )
        master.combobox.grid(
            row=1, column=0, columnspan=1, padx=(10,5), pady=(5,10), sticky="nsew"
        )
        master.start.grid(
            row=1, column=1, columnspan=1, padx=(5,5), pady=(5,10), sticky="nsew"
        )
        master.exit.grid(
            row=1, column=2, columnspan=1, padx=(5,10), pady=(5,10), sticky="nsew"
        )
        

        def start():
            master.value = master.combobox.get()
            if master.value == 'A to E':
                classifyAtoE()
            elif master.value == 'F to I':
                classifyFtoI()
            elif master.value == 'K to O':
                classifyKtoO()
            elif master.value == 'P to T':
                classifyPtoT()
            elif master.value == 'U to Y':
                classifyUtoY()
            else:
                classifyNumerical()

        def close():
            master.quit()


def main():
    root = ctk.CTk()
    window = MainWindow(root)
    root.mainloop()


if __name__ == "__main__":
    main()
