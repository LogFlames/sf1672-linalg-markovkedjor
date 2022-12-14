import tkinter as tk
import random
from create_song import generate_song
from parse_data import *
import melodies
#import playsound
#import pyttsx

class Window():
    def __init__(self, width, height, title):
        _, self.unique_sorted_words = get_words()
        self.width = width
        self.height = height
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(f"{self.width}x{self.height}")

        self.entered_phrase = tk.StringVar()
        self.selected_melody = tk.IntVar(value=random.randint(0,5))
        self.random_mode = tk.IntVar(value=0)
        self.markov_mode = tk.IntVar(value=0)

        self.l1 = tk.Label(self.root, font=("Arial", 18), text="Hur ska sången börja?")
        self.l1.grid(row = 0, column = 1, sticky="W", padx=10, pady=0)
        self.e1 = tk.Entry(self.root, textvariable=self.entered_phrase, justify="center")
        self.e1.grid(row = 1, column = 1, sticky="NW", padx=8)
        self.e1.bind("<Return>", self.display_song)
        self.l2 = tk.Label(self.root, font=("Arial", 18), text="Vilken melodi?")
        self.l2.grid(row = 3, column = 1, sticky="NW", padx=10)
        self.b1 = tk.Radiobutton(self.root, text="Katyuscha", borderwidth=0, variable=self.selected_melody, value=0,       command=self.display_song)
        self.b1.grid(row = 4, column = 1, sticky="NW", padx=10)
        self.b2 = tk.Radiobutton(self.root, text="Helan går", borderwidth=0, variable=self.selected_melody, value=1, command=self.display_song)
        self.b2.grid(row = 5, column = 1, sticky="NW", padx=10)
        self.b3 = tk.Radiobutton(self.root, text="Studentsången", borderwidth=0, variable=self.selected_melody, value=2, command=self.display_song)
        self.b3.grid(row = 6, column = 1, sticky="NW", padx=10)
        self.b4 = tk.Radiobutton(self.root, text="Åh, hur saligt att få vandra", borderwidth=0, variable=self.selected_melody, value=3, command=self.display_song)
        self.b4.grid(row = 7, column = 1, sticky="NW", padx=10)
        self.b5 = tk.Radiobutton(self.root, text="Rule Britannia", borderwidth=0, variable=self.selected_melody, value=4, command=self.display_song)
        self.b5.grid(row = 8, column = 1, sticky="NW", padx=10)
        self.b6 = tk.Radiobutton(self.root, text="Du gamla, du fria", borderwidth=0, variable=self.selected_melody, value=5, command=self.display_song)
        self.b6.grid(row = 9, column = 1, sticky="NW", padx=10)
        self.b7 = tk.Radiobutton(self.root, text="Ingen melodi", borderwidth=0, variable=self.selected_melody, value=6, command=self.display_song)
        self.b7.grid(row = 10, column = 1, sticky="NW", padx=10)

        self.c1 = tk.Checkbutton(self.root, text="Random", variable=self.random_mode, onvalue=1, offvalue=0)
        self.c1.grid(row = 11, column = 1, sticky="NW", padx=10)
        self.c2 = tk.Checkbutton(self.root, text="Markov v2", variable=self.markov_mode, onvalue=1, offvalue=0)
        self.c2.grid(row = 11, column = 1, sticky="NE", padx=10)

        self.t1 = tk.Text(self.root, font=("Arial", 16), highlightthickness=0, state="disabled", height=30, width=60, padx=20)
        self.t1.tag_configure("tag_name", justify="center")
        self.t1.grid(row = 0, column = 0, rowspan = 12, pady=20, padx=20)


    def display_song(self, *args):
        self.t1.config(state="normal")
        self.t1.delete("1.0","end")
        if self.entered_phrase.get() in self.unique_sorted_words:
            self.t1.insert(tk.INSERT, 
                generate_song(
                    self.entered_phrase.get(), 
                    melodies.pick_melody(self.selected_melody.get()), 
                    totally_random = self.random_mode.get() == 1,
                    keep_word_probability_vector = self.markov_mode.get())
                    )
        else:
            self.t1.insert(tk.INSERT, f"Ordet {self.entered_phrase.get()} finns ej i ordlistan")
        self.t1.tag_add("tag_name", "1.0", "end")
        self.t1.config(state="disabled")


def main():
    w1 = Window(850, 580, "sångskapare")
    tk.mainloop()


if __name__ == "__main__":
    main()
    
