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

    # default condition: apply SAME padding, and keep stride at 1
    stride_x = 1
    stride_y = 1
    padding_y = int(len(kernel - 1) / 2)
    padding_x = int(len((kernel[0]) - 1) / 2)
    # create the return array with with the same dimensions as <image>,
    # and then create a padded image
    convolved_image = np.zeros((len(image), len(image[0])))
    padded_image = np.zeros((len(image) + 2 * padding_y,
                             len(image[0]) + 2 * padding_x))
    padded_image[padding_x: -padding_x, padding_y: -padding_y] = image

    for py in range(0, len(padded_image) - len(kernel), stride_y):
        for px in range(0, len(padded_image[0]) - len(kernel[0]), stride_x):
            # scan the matrix over columns in image array, then shift the matrix
            # down, and repeat
            padded_image_section = padded_image[py: py + len(kernel[0]),
                                                px: px + len(kernel)]
            # print(padded_image_section)
            convolved_image[py, px] = int(np.tensordot(padded_image_section,
                                                       kernel))

    return convolved_image


if __name__ == '__main__':
    print('Please run the vizualizer.py.')
