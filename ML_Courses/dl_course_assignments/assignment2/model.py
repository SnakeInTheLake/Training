import numpy as np

from layers import FullyConnectedLayer, ReLULayer, softmax_with_cross_entropy, \
                   l2_regularization, softmax


class TwoLayerNet:
    """ Neural network with two fully connected layers """

    def __init__(self, n_input, n_output, hidden_layer_size, reg):
        """
        Initializes the neural network

        Arguments:
        n_input, int - dimension of the model input
        n_output, int - number of classes to predict
        hidden_layer_size, int - number of neurons in the hidden layer
        reg, float - L2 regularization strength
        """
        self.reg = reg
        # TODO Create necessary layers
        self.layer_1 = FullyConnectedLayer(n_input, hidden_layer_size)
        self.relu = ReLULayer()
        self.layer_2 = FullyConnectedLayer(hidden_layer_size, n_output)
        self.layers = [self.layer_1, self.relu, self.layer_2]

    def compute_loss_and_gradients(self, X, y):
        """
        Computes total loss and updates parameter gradients
        on a batch of training examples

        Arguments:
        X, np array (batch_size, input_features) - input data
        y, np array of int (batch_size) - classes
        """
        # Before running forward and backward pass through the model,
        # clear parameter gradients aggregated from the previous pass
        # TODO Set parameter gradient to zeros
        # Hint: using self.params() might be useful!
        for param in self.params():
            self.params()[param].grad *= 0
            
        # TODO Compute loss and fill param gradients
        # by running forward and backward passes through the model
        inp = X.copy()
        for layer in self.layers:
            inp = layer.forward(inp)

        loss, out_grad = softmax_with_cross_entropy(inp, y)

        for layer in reversed(self.layers):
            out_grad = layer.backward(out_grad)   
        
        # After that, implement l2 regularization on all params
        # Hint: self.params() is useful again!
        for layer in self.layers:
            if isinstance(layer, ReLULayer):
                continue
            reg_loss, reg_grad = l2_regularization(layer.W.value, self.reg)
            loss += reg_loss
            layer.W.grad += reg_grad

        return loss

    def predict(self, X):
        """
        Produces classifier predictions on the set

        Arguments:
          X, np array (test_samples, num_features)

        Returns:
          y_pred, np.array of int (test_samples)
        """
        # TODO: Implement predict
        # Hint: some of the code of the compute_loss_and_gradients
        # can be reused
        pred = np.zeros(X.shape[0], np.int)
        inp = X.copy()
        for layer in self.layers:
            inp = layer.forward(inp)
        
        probs = softmax(inp)
        pred = np.argmax(probs, axis=1)
        return pred

    def params(self):
        result = {'W1': self.layer_1.W, 'B1': self.layer_1.B,
                  'W2': self.layer_2.W, 'B2': self.layer_2.B}

        # TODO Implement aggregating all of the params

        return result
