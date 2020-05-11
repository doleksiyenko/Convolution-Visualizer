import numpy as np
from PIL import Image, ImageTk
import os
import tkinter as tk


class Vizualizer(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.images = os.listdir(os.getcwd())
        
    def create_widgets(self):
        self.load_images = tk.Button(self, text='Load Images', command=self.load_image_dir)
        self.load_images.pack(side="top")
        
        # load the images 
        self.canvas = tk.Canvas(self, width=1000, height=600)
        self.canvas.pack(side='bottom')

    def load_image_dir(self):
        print(self.images)
        self.load_image()

    def load_image(self):
        print(self.images[0])
        

if __name__ == '__main__':
    self_path = os.getcwd()
    a = np.zeros((300,300))
    a.fill(255)
    try:
        os.chdir(self_path + '/images/')
    except OSError:
        print('Could not change directory')
    else:
       frame = Image.fromarray(a)
       frame = frame.convert('L')
       frame.save('Image.gif')
       print('Saved.')
        
       root = tk.Tk()
        
       app = Vizualizer(master=root)
       unprocessed_img = ImageTk.PhotoImage(Image.open(app.images[0]))
       app.canvas.create_image(0,100, anchor='nw', image=unprocessed_img)
       app.mainloop()

