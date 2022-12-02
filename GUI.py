import tkinter as tk
import create_song


class Window():
    def __init__(self, width, height, title):
        self.width = width
        self.height = height
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(f"{self.width}x{self.height}")

        self.entered_phrase = tk.StringVar()

<<<<<<< HEAD
        self.l1 = tk.Label( self.root, text="Skriv hur du vill att sången ska börja")
=======
        self.l1 = tk.Label(self.root, text="Skriv hur du vill att sången ska börja")
>>>>>>> 966866e7afb0bf31584723910f433c33cfdac64f
        self.l1.pack(side="top", pady=(15, 0))
        self.e1 = tk.Entry(self.root, textvariable=self.entered_phrase, justify="center")
        self.e1.pack(side="top", pady=(15, 20))
        self.t1 = tk.Text(self.root)
        self.t1.pack(side="top", pady=(15, 20))

        self.e1.bind("<Return>", self.return_pressed)

    def return_pressed(self, _):
<<<<<<< HEAD
        lyrics = generate_song(self.entered_phrase)
=======
        # Funkar inte eftersom create_song inte funkar så här :)
        #lyrics = create_song(self.entered_phrase)
>>>>>>> 966866e7afb0bf31584723910f433c33cfdac64f
        self.t1.insert(tk.INSERT, "lyrics")


def main():
    w1 = Window(800, 600, "sångskapare")
    tk.mainloop()


if __name__ == "__main__":
    main()
