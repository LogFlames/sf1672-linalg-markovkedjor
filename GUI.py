import tkinter as tk
import random
import create_song

class Window():
    def __init__(self, width, height, title):
        self.width = width
        self.height = height
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(f"{self.width}x{self.height}")


        self.entered_phrase = tk.StringVar()
        self.selected_melody = tk.IntVar()
        self.selected_melody.set(random.randint(1,6))
    

        self.l1 = tk.Label(self.root, text="Hur ska sången börja?")
        self.l1.grid(row = 0, column = 0, sticky = "E")
        self.e1 = tk.Entry(self.root, textvariable=self.entered_phrase, justify="center")
        self.e1.grid(row = 0, column = 1, sticky = "W")
        self.e1.bind("<Return>", self.return_pressed)


        self.l2 = tk.Label(self.root, text="Val av melodi")
        self.l2.grid(row = 1, column = 0)


        self.b1 = tk.Radiobutton(self.root, text="Helan går", variable=self.selected_melody, value=1,)
        self.b1.grid(row = 1, column = 1)
        self.b2 = tk.Radiobutton(self.root, text="Studentsången", variable=self.selected_melody, value=2)
        self.b2.grid(row = 1, column = 2)
        self.b3 = tk.Radiobutton(self.root, text="Katyuscha", variable=self.selected_melody, value=3)
        self.b3.grid(row = 1, column = 3)
        self.b4 = tk.Radiobutton(self.root, text="Åh, hur saligt att få vandra", variable=self.selected_melody, value=4)
        self.b4.grid(row = 1, column = 4)
        self.b5 = tk.Radiobutton(self.root, text="Rule Britannia", variable=self.selected_melody, value=5)
        self.b5.grid(row = 1, column = 5)
        self.b6 = tk.Radiobutton(self.root, text="Du gamla, du fria", variable=self.selected_melody, value=6)
        self.b5.grid(row = 1, column = 6)

    
        self.t1 = tk.Text(self.root)
        self.t1.grid(row = 3, column = 0, columnspan = 7, sticky = "N")

    def return_pressed(self, _):
        lyrics = create_song.generate_song(self.entered_phrase.get(), self.selected_melody.get())
        self.t1.insert(tk.INSERT, lyrics)


def main():
    w1 = Window(800, 600, "sångskapare")
    tk.mainloop()


if __name__ == "__main__":
    main()
