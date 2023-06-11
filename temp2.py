import numpy as np
from PIL import Image
import os

def main():
    # identity kernel is     kernel = np.array([[0, 0, 0],
    #                    [0, -1, 0],
    #                    [0, 0, 0]])

    # kernel_2 = np.array([[1, 0, 1],
    #                      [-1, 1, -1],
    #                      [1, 0, 1]])

    # kernel_1 = np.array([[1, 1, 1],
    #                     [1, -4, 1],
    #                     [1, 1, 1]])
    #
    kernel_1 = np.array([[0, 0, 0, 0, 0],
                        [0, 0, -1, 0, 0],
                        [0, -1, 5, -1, 0],
                        [0, 0, -1, 0, 0],
                        [0, 0, 0, 0, 0]])

    ##  best detection till now
    # kernel_1 = np.array([[0, 0, 0],
    #                     [1, -1, 0],
    #                     [0, 0, 0]])

    # kernel_1 = np.array([[0, -1, 0],
    #                      [-1, 4, -1],
    #                      [0, -1, 0]])

    # file_path = "DB1_B/110_4.tif"
    # photo = Image.open(file_path)
    # photo = photo.resize((480, 640))
    # photo = photo.convert("L")
    # photo.show()
    # data = np.array(photo)
    # data = image_convolution(data, kernel_1)
    # data = Image.fromarray((data * 255).astype(np.uint8))
    # data.show()
    #
    # file_path = 'DIP3E_Original_Images_CH01/Fig0109(f)(organic superconductor).tif'
    # photo = Image.open(file_path)
    # photo = photo.resize((480, 640))
    # photo = photo.convert("L")
    # photo.show()
    # data = np.array(photo)
    # data = image_convolution(data, kernel_1)
    # data = Image.fromarray((data * 255).astype(np.uint8))
    # data.show()
    #
    # file_path = "n01440764/sketch_36.JPEG"
    # photo = Image.open(file_path)
    # photo = photo.resize((480, 640))
    # photo = photo.convert("L")
    # photo.show()
    # data = np.array(photo)
    # data = image_convolution(data, kernel_1)
    # data = Image.fromarray((data * 255).astype(np.uint8))
    # data.show()

    # data = data.reshape(480 * 640) / 255


# used https://stackoverflow.com/questions/43373521/how-to-do-convolution-matrix-operation-in-numpy
def image_convolution(matrix, kernel):
    # assuming kernel is symmetric and odd
    k_size = len(kernel)
    m_height, m_width = matrix.shape
    padded = np.pad(matrix, (k_size - 1, k_size - 1), 'minimum')

    # iterates through matrix, applies kernel, and sums
    output = []
    for i in range(m_height):
        for j in range(m_width):
            output.append(np.sum(padded[i:k_size + i, j:k_size + j] * kernel))

    output = np.array(output).reshape((m_height, m_width))
    return output


main()

# import os
# from PIL import Image
# import numpy as np
#
# file_path = "n01440764/sketch_36.JPEG"
# photo = Image.open(file_path)
# photo.show()
# photo = photo.resize((480, 640))
# photo = photo.convert("L")
# photo.show()
# data = np.array(photo)
# print np.shape(data)
# data = data.reshape(480 * 640) / 255
# print data

# 'DIP3E_Original_Images_CH01/Fig0112(1)(top-canada).tif'
# 'DB1_B/107_7.tif'
# 'DB1_B/105_3.tif'

# folder_dir = "DIP3E_Original_Images_CH01"
#
# count = 0
# for images in os.listdir(folder_dir):
#
#     if images.endswith(".tif"):
#         count += 1
#         file_path = folder_dir + "/" + str(images)
#         print file_path
#         photo = Image.open(file_path)
#         photo = photo.resize((480, 640))
#         photo = photo.convert("L")
#         data = np.array(photo)
#         data = data.reshape(480 * 640)
#         print count
# print count


# folder_dir = "DB1_B"
# for images in os.listdir(folder_dir):
#
#     # check if the image ends with png
#     if images.endswith(".tif"):
#         file_path = "DB1_B/" + str(images)
#         # print file_path
#         photo = Image.open(file_path)
#         data = np.array(photo)

# folder_dir = "n01440764"
# for images in os.listdir(folder_dir):
#
#
#
#     if images.endswith(".JPEG"):
#         file_path = "n01440764/" + str(images)
#         print file_path
#         photo = Image.open(file_path)
#         data = np.array(photo)
#         print data.reshape(480, 640)
# Past coded model for handwritten recognition

# Opens a image in RGB mode

# Size of the image in pixels (size of original image)
# (This is not mandatory)
# width, height = im.size

# Setting the points for cropped image
# left = 6
# top = height / 4
# right = 174
# bottom = 3 * height / 4

# Cropped image of above dimension
# (It will not change original image)
# im1 = im.crop((left, top, right, bottom))
# newsize = (480, 640)
# image = im.resize(newsize)
# image = image.convert("1")
# data = np.array(image)
# print np.shape(data)


## Copy of main.py

# example of fingerprint from net
#
# # -------
# file_path = "fingerprint_tryout.jpeg"
# photo = Image.open(file_path)
# photo = photo.resize((480, 640))
# photo = photo.convert("L")
# data = np.array(photo)
# data = data.reshape(480 * 640, 1) / 255
# prediction = np.argmax(forwardPropagation(data, L1weights, L2weights, L1biases, L2biases)[0])
# print prediction
# # --------


# def tempPreProcess():
#
#     arrayofpictures = []
#     arrayoflabels = []
#     arrayofnames = []
#
#     counter = 0
#
#     # processes all the non fingerprint images
#     folder_dir = "Kernel_images/Fingerprints"
#
#     for images in os.listdir(folder_dir):
#
#         if images.endswith(".tif") or images.endswith(".JPEG"):
#             counter += 1
#             file_path = folder_dir + "/" + str(images)
#             photo = Image.open(file_path)
#             # photo = photo.resize((480, 640))
#             # photo = photo.convert("L")
#             data = np.array(photo).reshape(480 * 640)
#             arrayofpictures.append(data)
#             arrayoflabels.append(0)
#             arrayofnames.append(file_path)
#             print counter, str(images), str(0)
#
#     folder_dir = "Kernel_images/Non-Fingerprints"
#
#     for images in os.listdir(folder_dir):
#
#         if images.endswith(".tif") or images.endswith(".JPEG"):
#             counter += 1
#             file_path = folder_dir + "/" + str(images)
#             photo = Image.open(file_path)
#             # photo = photo.resize((480, 640))
#             # photo = photo.convert("L")
#             data = np.array(photo).reshape(480 * 640)
#             arrayofpictures.append(data)
#             arrayoflabels.append(1)
#             arrayofnames.append(file_path)
#             print counter, str(images), str(1)
#
#     # print counter
#     return arrayShuffle(np.asarray(arrayofpictures), np.asarray(arrayoflabels), np.asarray(arrayofnames))

#
# new_folder = "Kernel_images/"
# counter = 0
#
# # processes all the fingerprint images
# folder_dir = "DB1_B"
#
# for images in os.listdir(folder_dir):
#
#     if images.endswith(".tif"):
#         counter += 1
#         print counter
#         file_path = "DB1_B/" + str(images)
#         photo = Image.open(file_path)
#         data = np.array(photo)
#         data = image_convolution(data, kernel_1)
#         data = Image.fromarray((data * 255).astype(np.uint8))
#         data.save(new_folder + str(images))
#
# # processes all the fish images
# folder_dir = "n01440764"
#
# for images in os.listdir(folder_dir):
#
#     if images.endswith(".JPEG"):
#         counter += 1
#         print counter
#         file_path = "n01440764/" + str(images)
#         photo = Image.open(file_path)
#         photo = photo.resize((480, 640))
#         photo = photo.convert("L")
#         data = np.array(photo)
#         data = image_convolution(data, kernel_1)
#         data = Image.fromarray((data * 255).astype(np.uint8))
#         data.save(new_folder + str(images))
#
# # processes all the non fingerprint images
# folder_dir = "DIP3E_Original_Images_CH01"
#
# for images in os.listdir(folder_dir):
#
#     if images.endswith(".tif"):
#         counter += 1
#         print counter
#         file_path = folder_dir + "/" + str(images)
#         photo = Image.open(file_path)
#         photo = photo.resize((480, 640))
#         photo = photo.convert("L")
#         data = np.array(photo)
#         data = image_convolution(data, kernel_1)
#         data = Image.fromarray((data * 255).astype(np.uint8))
#         data.save(new_folder + str(images))

