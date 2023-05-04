import customtkinter as ctk
from PIL import Image
from Classifier_in_functions import classifyAlpha
from Numerical_Classifier_in_functions import classifyNumerical


class MainWindow:
    def __init__(self, master):

        # Creating window
        master.geometry("520x480")
        master.resizable(False, False)
        master.wm_title("Sign Language Convertor")

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
            width=140,
            height=30,
            command=lambda: start(),
        )
        master.exit = ctk.CTkButton(
            master,
            text="Exit",
            font=my_font,
            width=140,
            height=30,
            command=lambda: close(),
        )

        # setting radio btn values
        master.var = ctk.IntVar()
        master.var.set(1)

        master.alphabets = ctk.CTkRadioButton(
            master,
            text="Alphabets",
            font=my_font,
            variable=master.var,
            value=1,
        )
        master.numbers = ctk.CTkRadioButton(
            master,
            text="Numbers",
            font=my_font,
            variable=master.var,
            value=2,
        )

        # add buttons to the grid
        master.image.grid(
            row=0, column=0, columnspan=4, padx=10, pady=(10,5), sticky="nsew"
        )
        master.alphabets.grid(
            row=1, column=0, columnspan=1, padx=(15,5), pady=(5,10), sticky="nsew"
        )
        master.numbers.grid(
            row=1, column=1, columnspan=1, padx=(5,5), pady=(5,10), sticky="nsew"
        )
        master.start.grid(
            row=1, column=2, columnspan=1, padx=(5,5), pady=(5,10), sticky="nsew"
        )
        master.exit.grid(
            row=1, column=3, columnspan=1, padx=(5,10), pady=(5,10), sticky="nsew"
        )

        def start():
            if master.var.get() == 1:
                classifyAlpha()
            elif master.var.get() == 2:
                classifyNumerical()

        def close():
            master.quit()


def main():
    root = ctk.CTk()
    window = MainWindow(root)
    root.mainloop()


if __name__ == "__main__":
    main()
