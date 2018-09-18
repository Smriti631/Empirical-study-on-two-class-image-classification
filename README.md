# Empirical-study-on-two-class-image-classification
Aim of this research is to study the two-class
classifiers. A series of experiments were carried out using the
three basic colour models - RGB (red, green, blue), HSV (hue,
saturation, value), and the image temperature based model
CCT (Correlated color Temperature); and feed forward artificial
neural network model, CNN (Convolutional neural network).
Combinations of these models were also tested to check which
combination or the individuals prove to be relevant for indoor
and outdoor scene classification, which has two distinct classes.
Among colour models based experiments, the model with the
combination of average RGB and average HSV achieved the
highest accuracy of 80.95% and the model with the combination
of average RGB and average CCT achieved the lowest accuracy
of 52.38%. CNN with Adam and Stochastic gradient descent
optimizers showed the best performance among the considered
eight optimizers.


Important informations and instructions :

1. This repository contains the dataset named "dataset.tar", which was originally used for performing all the experiments. The dataset contains images for training and testing, in seperate folders. Moreover, indoor and outdoor images also have seperate folders.
2. While using any of the models, there are two files for one particular model, example, 
   a. CCT_ARRAY.py 
   b. CCT_ARRAY_Pred.py 
where the first one is used for generating the training data and the later is used for training the model with data generated        from the first program and perform classification on test data using KNN Clasiifier.

For using any of the codes, one needs to change the path of the dataset.

