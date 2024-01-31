import cv2 as cv
import numpy as np
import streamlit as st


def main():

    # local_operations()

    gui_operations()


def gui_operations():
    st.header("Image Converter!")
    st.divider()
    img = st.file_uploader("Upload an image", type=['png', 'jpg'], help="Please upload a png or jpg")
    if img is not None:
        st.image(white_to_transparent(thresh_img(cv.cvtColor(img, cv.COLOR_BGR2GRAY))))

def local_operations():
    # Part 1
    # Reads in the image as img and grayscales it
    # An image is a 3D array - X, Y, {Color Format as Array}
    img = read_img('img.png')

    # Part 2
    # Thresholds the image such that pixels of intensity 127-255 are set to white else black
    ret, img = thresh_img(img)

    # Part 3
    # Writes to file
    write_img(img, 'gsthresh.png')

    # Part 4
    # Makes the background transparent

    bgra = white_to_transparent(img)

    write_img(bgra, 'transparent.png')


def read_img(path:str):
    return cv.imread(path, cv.IMREAD_GRAYSCALE)

def thresh_img(img):
    return cv.threshold(img, 127, 255, cv.THRESH_BINARY)

def write_img(img, name:str):
    cv.imwrite(name, img)

def white_to_transparent(img):
    # Converts default BGR colorspace to BGRA to allow for transparency
    bgra = cv.cvtColor(img, cv.COLOR_BGR2BGRA)

    # Generates a mask that is 255 for black pixels and 0 for white pixels
    mask = cv.inRange(bgra, np.array([0, 0, 0, 0]), np.array([0, 0, 0, 255]))

    # Assigns the alpha column of a BGRA pixel to the value from the mask
    bgra[:, :, 3] = mask

    return bgra


if __name__ == '__main__':
    main()
