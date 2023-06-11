# FingerPrintRecognition



# The following libraries are required to run the code:

# PIL: Python Imaging Library for image processing
# numpy: Numerical computing library
# sklearn: Scikit-learn library for data shuffling
# You can install the required libraries using pip:

# Copy code
# pip install pillow numpy scikit-learn

# Dataset
# The code uses the MNIST dataset for labelled fingerprint data. It also utilizes random images from the following source: https://www.imageprocessingplace.com/DIP-3E/dip3e_book_images_downloads.htm. The dataset contains 480x640 grayscale images, where index 0 represents a fingerprint and index 1 represents a non-fingerprint.

# Neural Network Configuration
# The neural network architecture used in this code consists of:

# Input layer: 480x640 nodes (one node for each pixel)
# Hidden layer: 50 nodes
# Output layer: 2 nodes (one for each class: fingerprint or non-fingerprint)
# The hyperparameters used for training the neural network are as follows:

# Number of epochs: 100
# Learning rate: 0.01
# Code Flow
# The preProcess() function loads and preprocesses the fingerprint and non-fingerprint images. It shuffles the data for better training.
# The forwardPropagation() function performs forward propagation through the neural network, calculating the output probabilities.
# The backwardPropagation() function performs backward propagation, updating the weights and biases based on the calculated errors.
# The main() function initializes the weights and biases, preprocesses the data, and trains the neural network using the training set.
# After training, the accuracy is evaluated using the testing set, and the percentage of correct predictions is printed.
# Finally, an example fingerprint image is loaded and classified using the trained neural network.
# Usage
# To run the code, ensure that the required libraries are installed and the dataset images are available in the appropriate directories. Then, execute the code.

# Please note that this code is intended as an educational example and may require modifications or additional steps to adapt it to your specific use case or dataset.
