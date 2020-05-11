import numpy as np

def convolution(image: np.array, matrix: np.array):
    """ Precondition: len(image[0]) % len(matrix[0]) == 0
                      len(images) % len(matrix) == 0
    """

    # skip every <strafe> pixels. i.e run a 2x2 matrix over an 8x8 grid, you travel from 0, 2, 4, 6
    stride_x = int(len(image[0]) / len(matrix[0]))
    stride_y = int(len(image) / len(matrix))
    for py in range(0, len(image), strafe_y):    
        for px in range(0, len(image[0]), strafe_x):
            # scan the matrix over columns in image array, then shift the matrix down, and repeat

        


if __name__ == '__main__':
    print('Please run the vizualizer.py.')
