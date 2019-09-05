# Implement-Research-paper-VERY-DEEP-CONVOLUTIONAL-NETWORKS-FOR-LARGE-SCALE-IMAGE-RECOGNITION
Contribution : Evaluation of deep neural network with depth of 16-19 weight layers and very small (3 * 3) convolution filters.
# Architecture :
Pre-processing : Substracting RGB mean value from each value.<br />
Convolution filters : (3 * 3 ) and (1 * 1). <br />
Describes why we need to chooses smaller sized filter : https://towardsdatascience.com/deciding-optimal-filter-size-for-cnns-d6f7b56f9363 <br />
Why do we need (1 * 1) convolution layer : https://machinelearningmastery.com/introduction-to-1x1-convolutions-to-reduce-the-complexity-of-convolutional-neural-networks/. Author explains how (1 * 1) convolution filter can help us to match the number of filters of input to the ouput of residual modules.
