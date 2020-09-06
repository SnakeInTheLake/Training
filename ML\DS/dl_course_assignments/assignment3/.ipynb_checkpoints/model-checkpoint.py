import numpy as np

from layers import (
    FullyConnectedLayer, ReLULayer,
    ConvolutionalLayer, MaxPoolingLayer, Flattener,
    softmax_with_cross_entropy, l2_regularization, softmax
    )


class ConvNet:
    """
    Implements a very simple conv net

    Input -> Conv[3x3] -> Relu -> Maxpool[4x4] ->
    Conv[3x3] -> Relu -> MaxPool[4x4] ->
    Flatten -> FC -> Softmax
    """
    def __init__(self, input_shape, n_output_classes, conv1_channels, conv2_channels):
        """
        Initializes the neural network

        Arguments:
        input_shape, tuple of 3 ints - image_width, image_height, n_channels
                                         Will be equal to (32, 32, 3)
        n_output_classes, int - number of classes to predict
        conv1_channels, int - number of filters in the 1st conv layer
        conv2_channels, int - number of filters in the 2nd conv layer
        """
        # TODO Create necessary layers
        self.first_conv = ConvolutionalLayer(input_shape[-1], conv1_channels, 3, 1)
        self.first_relu = ReLULayer()
        self.first_maxpool = MaxPoolingLayer(4, 4)
        self.second_conv = ConvolutionalLayer(conv1_channels, conv2_channels, 3, 1)
        self.second_relu = ReLULayer()
        self.second_maxpool = MaxPoolingLayer(4, 4)
        self.flattener = Flattener()
        self.linear = FullyConnectedLayer(8, n_output_classes)

        self.layers = [self.first_conv,self.first_relu, self.first_maxpool,
                       self.second_conv, self.second_relu, self.second_maxpool,
                       self.flattener, self.linear]

    def compute_loss_and_gradients(self, X, y):
        """
        Computes total loss and updates parameter gradients
        on a batch of training examples

        Arguments:
        X, np array (batch_size, height, width, input_features) - input data
        y, np array of int (batch_size) - classes
        """
        # Before running forward and backward pass through the model,
        # clear parameter gradients aggregated from the previous pass
        for param in self.params():
            self.params()[param].grad *= 0
        # TODO Compute loss and fill param gradients
        # Don't worry about implementing L2 regularization, we will not
        # need it in this assignment
        inp = X.copy()
        for layer in self.layers:
            out = layer.forward(inp)
            inp = out
        from layers import cross_entropy_loss
        loss, out_grad = softmax_with_cross_entropy(out, y)

        for layer in reversed(self.layers):
            inp_grad = layer.backward(out_grad)
            out_grad = inp_grad
            #print(f'Input shape: {layer.X.shape}, grad_shape: {out_grad.shape}')
        return loss

    def predict(self, X):
        # You can probably copy the code from previous assignment
        inp = X.copy()
        for layer in self.layers:
            out = layer.forward(inp)
            inp = out

        probs = softmax(out)
        pred = np.argmax(probs, axis=1)
        return pred

    def params(self):
        # TODO: Aggregate all the params from all the layers
        # which have parameters
        result = {'W1': self.first_conv.W, 'B1': self.first_conv.B,
                  'W2': self.second_conv.W, 'B2': self.second_conv.B,
                  'W3': self.linear.W, 'B3': self.linear.B}

        return result
