import numpy as np
from PIL import Image, ImageTk
import os

import tkinter as tk
from convolution import convolution


def generate_new_image():
    a = np.zeros((300,300))
    a.fill(255)

    frame = Image.fromarray(a)
    frame = frame.convert('L')
    frame.save('Image.gif')
    print('Saved.')


class Vizualizer(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.images = os.listdir(os.getcwd())

    def create_widgets(self):
        self.load_images = tk.Button(self, text='Load Images',
                                     command=self.load_image_dir)
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
    try:
        os.chdir(self_path + '/images/')
    except OSError:
        print('Could not change directory')
    else:
        # generate_new_image()
        root = tk.Tk()

        # create app
        app = Vizualizer(master=root)

        # load the unprocessed image into the canvas
        _image = Image.open(app.images[0]).convert(mode='L')
        unprocessed_img = ImageTk.PhotoImage(_image)
        app.canvas.create_image(50, 100, anchor='nw', image=unprocessed_img)

        # create the kernel
        kernel = np.array([[1, 0, 0], [1, 0, 0], [1, 0, 0]])
        # the unprocessed_img as an array
        _image_array = np.array(_image)

        # convolve the image with the kernel and then create on the canvas
        convolved_img = Image.fromarray(convolution(image=_image_array,
                                                    kernel=kernel))
        convolved_img = ImageTk.PhotoImage(convolved_img)
        app.canvas.create_image(400, 100, anchor='nw', image=convolved_img)

        # run the mainloop
        app.mainloop()
