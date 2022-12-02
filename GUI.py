import tkinter as tk
import random
from create_song import generate_song
import melodies

class Window():
    def __init__(self, width, height, title):
        self.width = width
        self.height = height
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(f"{self.width}x{self.height}")


        self.entered_phrase = tk.StringVar()
        self.selected_melody = tk.IntVar(value=random.randint(0,5))
    

        self.l1 = tk.Label(self.root, text="Hur ska sången börja?")
        self.l1.grid(row = 0, column = 0, sticky = "E")
        self.e1 = tk.Entry(self.root, textvariable=self.entered_phrase, justify="center")
        self.e1.grid(row = 0, column = 1, sticky = "W")
        self.e1.bind("<Return>", self.display_song)


        self.l2 = tk.Label(self.root, text="Vilken melodi vill du ha?")
        self.l2.grid(row = 1, column = 0, sticky = "E")


        self.b1 = tk.Radiobutton(self.root, text="Katyuscha", variable=self.selected_melody, value=0, command=self.display_song)
        self.b1.grid(row = 1, column = 1)
        self.b2 = tk.Radiobutton(self.root, text="Helan går", variable=self.selected_melody, value=1, command=self.display_song)
        self.b2.grid(row = 1, column = 2)
        self.b3 = tk.Radiobutton(self.root, text="Studentsången", variable=self.selected_melody, value=2, command=self.display_song)
        self.b3.grid(row = 1, column = 3)
        self.b4 = tk.Radiobutton(self.root, text="Åh, hur saligt att få vandra", variable=self.selected_melody, value=3, command=self.display_song)
        self.b4.grid(row = 1, column = 4)
        self.b5 = tk.Radiobutton(self.root, text="Rule Britannia", variable=self.selected_melody, value=4, command=self.display_song)
        self.b5.grid(row = 1, column = 5)
        self.b6 = tk.Radiobutton(self.root, text="Du gamla, du fria", variable=self.selected_melody, value=5, command=self.display_song)
        self.b6.grid(row = 1, column = 6)

    
        self.t1 = tk.Text(self.root, font=("Old English Text MT", 16))
        self.t1.tag_configure("tag_name", justify="center")
        self.t1.grid(row = 3, column = 0, columnspan = 7)

    def display_song(self, _=0):
        self.t1.delete("1.0","end")
        self.t1.insert(tk.INSERT, generate_song(self.entered_phrase.get(), melodies.pick_melody(self.selected_melody.get())))
        self.t1.tag_add("tag_name", "1.0", "end")


def main():
    w1 = Window(1000, 600, "sångskapare")
    tk.mainloop()


if __name__ == "__main__":
    main()
