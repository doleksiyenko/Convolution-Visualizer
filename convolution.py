import numpy as np


def convolution(image: np.array, kernel: np.array) -> np.array:
    """
    Return an array that represents <image> convolved with <kernel>.

    PADDING:
    Given an n * n image, and an f * f kernel, the convolved return image
    will be an (n - f + 1) * (n - f + 1) sized image.

    Given some padding, p, for the image, the resolution then changes to
    (n + 2p - f + 1) * (n + 2p - f + 1). Therefore if we want "same" padding,
    the padding is p = (f - 1) / 2. This means that it is better to keep the
    padding an odd number, to ensure a integer padding.

    STRIDE:
    Given an n * n image, and an f * f kernel, and with a padding of p and
    stride s, the output size is ((n + 2p - f) / s) + 1 * ((n + 2p - f) / s) + 1
    Given a float output, floor the result.

    Precondition:
                len(kernel) == len(kernel[0])
    """
    # apply SAME padding, and keep stride at 1
    stride_x = 1
    stride_y = 1
    padding_y = (len(kernel) - 1) / 2
    padding_x = (len(kernel[0]) - 1) / 2

    # create the return array
    convolved_image = np.zeros((len(image) + int(padding_y),
                                len(image[0]) + int(padding_x)))

    for py in range(0, len(image), stride_y):
        for px in range(0, len(image[0]), stride_x):
            # scan the matrix over columns in image array, then shift the matrix
            # down, and repeat
            pass

    return convolved_image


if __name__ == '__main__':

    print('Please run the vizualizer.py.')
