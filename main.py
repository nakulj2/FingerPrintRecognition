# FingerPrint Recognition using Neural Network Binary Classifier

from PIL import Image
import numpy as np
import os
from sklearn.utils import shuffle

# Using MNIST data set for Labelled Fingerprint Dataset
# Using https://www.imageprocessingplace.com/DIP-3E/dip3e_book_images_downloads.htm for random images
# rows = 480
# columns = 640
# index 0 means fingerprint
# index 1 means not a fingerprint

number_of_input_nodes = 480 * 640
number_of_output_nodes = 2
number_of_hidden_nodes = 50

epochs = 100
lr = 0.01

total_dataset = 173


# --------------------------------------

def main():
    L1weights = np.random.randn(number_of_input_nodes, number_of_hidden_nodes)
    L2weights = np.random.randn(number_of_hidden_nodes, number_of_output_nodes)

    L1biases = np.random.randn(1, number_of_hidden_nodes)
    L2biases = np.random.randn(1, number_of_output_nodes)
    # --------------------------------------
    x_train, y_train, file_names = preProcess()

    x_train = x_train.reshape(total_dataset, 480 * 640, 1) / 255
    y_train = y_train.reshape(total_dataset, 1, 1)
    file_names = file_names.reshape(total_dataset, 1, 1)

    # pre-testing with single input data
    initial_total = 0.0
    initial_sum = 0.0

    for i in range(130, 173):
        initial_total += 1
        if np.argmax(forwardPropagation(x_train[i], L1weights, L2weights, L1biases, L2biases)[0]).reshape(1, 1) == \
                y_train[i]:
            initial_sum += 1

    print str((initial_sum * 100) / initial_total) + "%"

    # training model
    for j in range(epochs):
        print j
        for i in range(0, 130):
            prediction, hidden_layer = forwardPropagation(x_train[i], L1weights, L2weights, L1biases, L2biases)

            X = x_train[i]
            output = np.array([0, 0])
            output[int(y_train[i])] = 1

            L1weights, L2weights, L1biases, L2biases = backwardPropagation(X, output, prediction,
                                                                           L1weights, L2weights, L1biases, L2biases,
                                                                           hidden_layer)

    # testing
    total = 0.0
    sum = 0.0

    for i in range(130, 173):
        total += 1
        prediction = np.argmax(forwardPropagation(x_train[i], L1weights, L2weights, L1biases, L2biases)[0]).reshape(1,
                                                                                                                    1)
        if prediction == y_train[i]:
            sum += 1
        else:
            print file_names[i][0]

        print str(prediction[0]), str(y_train[i][0])

    print str((sum * 100) / total) + "%"

    # example of single fingerprint

    # -------
    file_path = "fingerprint_tryout.jpeg"
    photo = Image.open(file_path)
    photo = photo.resize((480, 640))
    photo = photo.convert("L")
    data = np.array(photo)
    data = data.reshape(480 * 640, 1) / 255
    prediction = np.argmax(forwardPropagation(data, L1weights, L2weights, L1biases, L2biases)[0])
    print prediction
    # --------


# to randomize the data for better training
def arrayShuffle(X, y, z):
    X, y, z = shuffle(X, y, z, random_state=3)
    print y
    return X, y, z


def preProcess():
    arrayofpictures = []
    arrayoflabels = []
    arrayofnames = []

    counter = 0

    # processes all the fingerprint images
    folder_dir = "DB1_B"

    for images in os.listdir(folder_dir):

        if images.endswith(".tif"):
            counter += 1
            file_path = "DB1_B/" + str(images)
            photo = Image.open(file_path)
            data = np.array(photo)
            data = data.reshape(480 * 640)

            arrayofpictures.append(data)
            arrayoflabels.append(0)
            arrayofnames.append(file_path)

    # processes all the non fingerprint images
    folder_dir = "DIP3E_Original_Images_CH01"

    for images in os.listdir(folder_dir):

        if images.endswith(".tif"):
            counter += 1
            file_path = folder_dir + "/" + str(images)
            photo = Image.open(file_path)
            photo = photo.resize((480, 640))
            photo = photo.convert("L")
            data = np.array(photo)
            data = data.reshape(480 * 640)

            arrayofpictures.append(data)
            arrayoflabels.append(1)
            arrayofnames.append(file_path)

    print counter
    return arrayShuffle(np.asarray(arrayofpictures), np.asarray(arrayoflabels), np.asarray(arrayofnames))

# Activation function
def sigmoid(x):
    x = 1 / (1 + np.exp(-x))
    return x


def forwardPropagation(X, W1, W2, B1, B2):
    hidden_layer_change = sigmoid(np.dot(X.T, W1) + B1)
    output = sigmoid(np.dot(hidden_layer_change, W2) + B2)
    return output.reshape(number_of_output_nodes), hidden_layer_change


def backwardPropagation(X, Y, output, W1, W2, B1, B2, hidden_layer):
    output_delta = (Y - output) * output * (1 - output)  # error in (output layer) * derivative of the sigmoid
    output_delta = output_delta.reshape(1, number_of_output_nodes)

    hidden_layer_error = output_delta.dot(W2.T)  # error in hidden layer
    hidden_layer_error_delta = hidden_layer_error * hidden_layer * (1 - hidden_layer)  # error in (hidden layer) *
    # derivative of the sigmoid

    W1 += X.dot(hidden_layer_error_delta)
    W2 += hidden_layer.T.dot(output_delta)

    B1 += hidden_layer_error_delta
    B2 += output_delta

    return W1, W2, B1, B2


main()
