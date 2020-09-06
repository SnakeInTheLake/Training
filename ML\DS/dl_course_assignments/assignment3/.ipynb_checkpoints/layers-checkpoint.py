import numpy as np


def l2_regularization(W, reg_strength):
    '''
    Computes L2 regularization loss on weights and its gradient

    Arguments:
      W, np array - weights
      reg_strength - float value

    Returns:
      loss, single value - l2 regularization loss
      gradient, np.array same shape as W - gradient of weight by l2 loss
    '''
    # TODO: Copy from previous assignment
    loss = reg_strength * np.sum(W ** 2)
    grad = reg_strength * (W * 2)

    return loss, grad

def softmax(predictions):
    '''
    Computes probabilities from scores

    Arguments:
      predictions, np array, shape is either (N) or (batch_size, N) -
        classifier output

    Returns:
      probs, np array of the same shape as predictions - 
        probability for every class, 0..1
    '''
    # TODO implement softmax
    # Your final implementation shouldn't have any loops
    if predictions.ndim > 1:
        preds = predictions - np.max(predictions, axis=1, keepdims=True)
        probs = np.exp(preds) / np.sum(np.exp(preds), axis=1, keepdims=True)
    else:
        preds = predictions - np.max(predictions)
        probs = np.exp(preds) / np.sum(np.exp(preds))
    return probs

def cross_entropy_loss(probs, target_index):
    '''
    Computes cross-entropy loss

    Arguments:
      probs, np array, shape is either (N) or (batch_size, N) -
        probabilities for every class
      target_index: np array of int, shape is (1) or (batch_size) -
        index of the true class for given sample(s)

    Returns:
      loss: single value
    '''
    # TODO implement cross-entropy
    # Your final implementation shouldn't have any loops
    if probs.ndim > 1:
        loss = -np.mean(np.log(np.take_along_axis(probs, target_index.reshape(-1, 1), axis=1)))
    else:
        loss = -np.mean(np.log(probs[target_index]))
    return loss

def softmax_with_cross_entropy(predictions, target_index):
    '''
    Computes softmax and cross-entropy loss for model predictions,
    including the gradient

    Arguments:
      predictions, np array, shape is either (N) or (batch_size, N) -
        classifier output
      target_index: np array of int, shape is (1) or (batch_size) -
        index of the true class for given sample(s)

    Returns:
      loss, single value - cross-entropy loss
      dprediction, np array same shape as predictions - gradient of predictions by loss value
    '''
    # TODO copy from the previous assignment
    probs = softmax(predictions)
    loss = cross_entropy_loss(probs, target_index)

    sub = np.zeros_like(probs)
    if probs.ndim > 1:
        np.put_along_axis(sub, target_index.reshape(-1, 1), 1, axis=1)
        dprediction = (probs - sub) / len(probs)
    else:
        sub[target_index] = 1
        dprediction = (probs - sub)
    return loss, dprediction


class Param:
    '''
    Trainable parameter of the model
    Captures both parameter value and the gradient
    '''
    def __init__(self, value):
        self.value = value
        self.grad = np.zeros_like(value)

        
class ReLULayer:
    def __init__(self):
        pass

    def forward(self, X):
        # TODO: Implement forward pass
        # Hint: you'll need to save some information about X
        # to use it later in the backward pass
        self.X = X
        return np.maximum(0, X)

    def backward(self, d_out):
        """
        Backward pass

        Arguments:
        d_out, np array (batch_size, num_features) - gradient
           of loss function with respect to output

        Returns:
        d_result: np array (batch_size, num_features) - gradient
          with respect to input
        """
        # TODO: Implement backward pass
        # Your final implementation shouldn't have any loops
        d_result = d_out * (self.X > 0).astype(float)
        return d_result

    def params(self):
        # ReLU Doesn't have any parameters
        return {}


class FullyConnectedLayer:
    def __init__(self, n_input, n_output):
        self.W = Param(0.001 * np.random.randn(n_input, n_output))
        self.B = Param(0.001 * np.random.randn(1, n_output))
        self.X = None

    def forward(self, X):
        # TODO: Implement forward pass
        # Your final implementation shouldn't have any loops
        self.X = X
        return X @ self.W.value + self.B.value

    def backward(self, d_out):
        """
        Backward pass
        Computes gradient with respect to input and
        accumulates gradients within self.W and self.B

        Arguments:
        d_out, np array (batch_size, n_output) - gradient
           of loss function with respect to output

        Returns:
        d_result: np array (batch_size, n_input) - gradient
          with respect to input
        """
        # TODO: Implement backward pass
        # Compute both gradient with respect to input
        # and gradients with respect to W and B
        # Add gradients of W and B to their `grad` attribute

        # It should be pretty similar to linear classifier from
        # the previous assignment
        d_input = d_out @ self.W.value.T
        self.W.grad += self.X.T @ d_out
        self.B.grad += np.sum(d_out, axis=0, keepdims=True)

        return d_input

    def params(self):
        return { 'W': self.W, 'B': self.B }

    
class ConvolutionalLayer:
    def __init__(self, in_channels, out_channels,
                 filter_size, padding):
        '''
        Initializes the layer
        
        Arguments:
        in_channels, int - number of input channels
        out_channels, int - number of output channels
        filter_size, int - size of the conv filter
        padding, int - number of 'pixels' to pad on each side
        '''

        self.filter_size = filter_size
        self.in_channels = in_channels
        self.out_channels = out_channels
        self.W = Param(
            np.random.randn(filter_size, filter_size,
                            in_channels, out_channels)
        )

        self.B = Param(np.zeros(out_channels))

        self.padding = padding


    def forward(self, X):
        batch_size, height, width, channels = X.shape
        self.X = X
        out_height = height - self.filter_size + 2 * self.padding + 1
        out_width = width - self.filter_size + 2 * self.padding + 1 
        
        # TODO: Implement forward pass
        # Hint: setup variables that hold the result
        # and one x/y location at a time in the loop below
        
        # It's ok to use loops for going over width and height
        # but try to avoid having any other loops
        X_pad = np.pad(X, pad_width=([0], [self.padding], [self.padding], [0]))
        W_row = self.W.value.transpose(3, 2, 0, 1).reshape(self.out_channels, -1)
        self.W_row = W_row
        cols = []
        for y in range(out_height):
            for x in range(out_width):
                # TODO: Implement forward pass for specific location
                cols.append(X_pad[:, y:y+self.filter_size, x:x+self.filter_size, :] \
                    .transpose(0, 3, 1, 2).reshape(batch_size, -1, 1))
        X_col = np.concatenate(cols, axis=-1)
        self.X_col = X_col
        out = W_row @ X_col
        self.out = out
        return out.transpose(0, 2, 1) \
                   .reshape(batch_size, out_height, out_width, self.out_channels) \
                   + self.B.value

    def backward(self, d_out):
        # Hint: Forward pass was reduced to matrix multiply
        # You already know how to backprop through that
        # when you implemented FullyConnectedLayer
        # Just do it the same number of times and accumulate gradients

        batch_size, height, width, channels = self.X.shape
        _, out_height, out_width, out_channels = d_out.shape

        # TODO: Implement backward pass
        # Same as forward, setup variables of the right shape that
        # aggregate input gradient and fill them for every location
        # of the output

        # Try to avoid having any other loops here too
        d_input = np.zeros([batch_size, height+2*self.padding,
                            width+2*self.padding, channels])

        stacked_W = np.vstack([self.W.value[np.newaxis, :].copy() \
                               for _ in range(batch_size)])
        #Compute input grad
        for y in range(out_height):
            for x in range(out_width):
                # TODO: Implement backward pass for specific location
                # Aggregate gradients for both the input and
                # the parameters (W and B)
                c = np.expand_dims(d_out[:, y, x, :], axis=(1, 2, 3))
                cgrad = (stacked_W * c).sum(axis=-1)
                temp = np.zeros_like(d_input)
                temp[:, y:y+self.filter_size, x:x+self.filter_size, :] = cgrad
                d_input += temp

        d_input = d_input[:, self.padding:height+self.padding,
                          self.padding:width+self.padding, :]

        # Compute weights grad
        reshaped_d_out = d_out.transpose(0,3,1,2).reshape(self.out.shape)
        reshaped_W_grad = (reshaped_d_out @ self.X_col.transpose(0, 2, 1)).sum(axis=0)
        W_grad = reshaped_W_grad.reshape(-1, self.filter_size, self.filter_size) \
                       .transpose(1,2,0) \
                       .reshape(self.filter_size, self.filter_size, out_channels, channels) \
                       .transpose(0,1,3,2)
        self.W.grad += W_grad

        #Compute bias grad
        B_grad = d_out.sum(axis=(0,1,2))
        self.B.grad += B_grad
        return d_input

    def params(self):
        return { 'W': self.W, 'B': self.B }


class MaxPoolingLayer:
    def __init__(self, pool_size, stride):
        '''
        Initializes the max pool

        Arguments:
        pool_size, int - area to pool
        stride, int - step size between pooling windows
        '''
        self.pool_size = pool_size
        self.stride = stride
        self.X = None

    def forward(self, X):
        batch_size, height, width, channels = X.shape
        # TODO: Implement maxpool forward pass
        # Hint: Similarly to Conv layer, loop on
        # output x/y dimension
        self.X = X
        out_height = ((height - self.pool_size) // self.stride) + 1
        out_width = ((width - self.pool_size) // self.stride) + 1
        indices = []
        reshaped = []
        for y in range(out_height):
            for x in range(out_width):
                square = X[:,
                           y * self.stride:y * self.stride + self.pool_size,
                           x * self.stride:x * self.stride + self.pool_size,
                           :] \
                         .transpose(0,3,1,2).reshape(-1, self.pool_size**2)
                ind = square.argmax(axis=-1)
                indices.append(ind)
                reshaped.append(square)

        indices = np.array(indices)
        self.indices = indices
        reshaped = np.array(reshaped)
        self.reshaped = reshaped

        result = np.take_along_axis(reshaped, indices[:, :, np.newaxis], axis=-1) \
                 .transpose(1,0,2) \
                 .reshape(batch_size, channels, out_height, out_width, 1, 1) \
                 .transpose(0,2,4,3,5,1) \
                 .reshape(batch_size, out_height, out_width, channels)  
        self.result = result
        return result

    def backward(self, d_out):
        # TODO: Implement maxpool backward pass
        batch_size, height, width, channels = self.X.shape
        #print(self.reshaped, self.reshaped.shape)
        d_zeros = np.zeros_like(self.reshaped)
        np.put_along_axis(d_zeros, self.indices[:,:, np.newaxis], 1, axis=-1)
        d_input = d_zeros.transpose(1,0,2) * d_out \
                  .transpose(0,3,1,2) \
                  .reshape(batch_size * channels, d_out.shape[1] * d_out.shape[2], 1)
        d_input = d_input.reshape(batch_size, channels, d_out.shape[1], d_out.shape[2], self.pool_size, self.pool_size)\
                  .transpose(0,2,4,3,5,1).reshape(batch_size, height, width, channels)
        return d_input

    def params(self):
        return {}


class Flattener:
    def __init__(self):
        self.X_shape = None

    def forward(self, X):
        batch_size, height, width, channels = X.shape
        self.X = X
        # TODO: Implement forward pass
        # Layer should return array with dimensions
        # [batch_size, hight*width*channels]
        return X.reshape(batch_size, -1)

    def backward(self, d_out):
        # TODO: Implement backward pass
        return d_out.reshape(self.X.shape)

    def params(self):
        # No params!
        return {}
