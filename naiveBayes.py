# naiveBayes.py
# -------------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

import util
import classificationMethod
import math


class NaiveBayesClassifier(classificationMethod.ClassificationMethod):
    """
  See the project description for the specifications of the Naive Bayes classifier.

  Note that the variable 'datum' in this code refers to a counter of features
  (not to a raw samples.Datum).
  """

    def __init__(self, legalLabels):
        self.legalLabels = legalLabels
        self.type = "naivebayes"
        self.k = 1  # this is the smoothing parameter, ** use it in your train method **
        self.automaticTuning = False  # Look at this flag to decide whether to choose k automatically ** use this in your train method **

    def setSmoothing(self, k):
        """
    This is used by the main method to change the smoothing parameter before training.
    Do not modify this method.
    """
        self.k = k

    def train(self, trainingData, trainingLabels, validationData, validationLabels, options):
        """
    Outside shell to call your method. Do not modify this method.
    """
        # WHAT IS KGRID#

        # might be useful in your code later...
        # this is a list of all features in the training set.
        self.features = list(set([f for datum in trainingData for f in datum.keys()]));

        if (self.automaticTuning):
            kgrid = [0.001, 0.01, 0.05, 0.1, 0.5, 1, 5, 10, 20, 50]
        else:
            kgrid = [self.k]

        self.trainAndTune(trainingData, trainingLabels, validationData, validationLabels, kgrid, options)

    def trainAndTune(self, trainingData, trainingLabels, validationData, validationLabels, kgrid, options):
        """
    Trains the classifier by collecting counts over the training data, and
    stores the Laplace smoothed estimates so that they can be used to classify.
    Evaluate each value of k in kgrid to choose the smoothing parameter
    that gives the best accuracy on the held-out validationData.

    trainingData and validationData are lists of feature Counters.  The corresponding
    label lists contain the correct label for each datum.

    To get the list of all possible features or labels, use self.features and
    self.legalLabels.

    """

        # NEED TO FIX FOR FACES

        self.classProb = {}
        self.classOccurence = {}
        self.allFeaturesProb = {}
        numOfClasses = 0
        pixelWidth = 0
        pixelHeight = 0
        if (options == 'digits'):
            numOfClasses = 10
            pixelHeight = 28
            pixelWidth = 28

        else:
            numOfClasses = 2
            pixelHeight = 70
            pixelWidth = 60

        occur = 0
        for digit in range(numOfClasses):
            for x in range(len(trainingLabels)):
                if (trainingLabels[x] == digit):
                    occur += 1
            self.classOccurence[digit] = occur
            self.classProb[digit] = float(occur) / float(len(trainingLabels))
            occur = 0

        # --------------------------------------------------------------above is prob of a class,below prob of a feature for a class
        occurOfOne = 0
        for digit in range(numOfClasses):  # for each class
            self.allFeaturesProb[digit] = {}
            for x in range(pixelWidth):  # each (x,y) is a feature
                for y in range(pixelHeight):
                    for z in range(len(trainingLabels)):  # check to see if image we are on is in the class
                        if (trainingLabels[z] == digit):
                            image = trainingData[z]  # get that specific image
                            if (image.get((x, y)) == 1):  # check to see if pixel for this image is a 1
                                occurOfOne += 1

                    self.allFeaturesProb[digit][(x, y)] = float(occurOfOne) / float(
                        self.classOccurence[digit])  # idk if i need these denomineters of if this is right denom
                    occurOfOne = 0

    def classify(self, testData, options):
        """
    Classify the data based on the posterior distribution over labels.

    You shouldn't modify this method.
    """
        guesses = []
        self.posteriors = []  # Log posteriors are stored for later data analysis (autograder).
        for datum in testData:
            posterior = self.calculateLogJointProbabilities(datum, options)
            guesses.append(posterior.argMax())
            self.posteriors.append(posterior)
        return guesses

    def calculateLogJointProbabilities(self, datum, options):
        """
    Returns the log-joint distribution over legal labels and the datum.
    Each log-probability should be stored in the log-joint counter, e.g.
    logJoint[3] = <Estimate of log( P(Label = 3, datum) )>

    To get the list of all possible features or labels, use self.features and
    self.legalLabels.
    """
        logJoint = util.Counter()
        numOfClasses = 0
        pixelWidth = 0
        pixelHeight = 0
        if (options == 'digits'):
            numOfClasses = 10
            pixelHeight = 28
            pixelWidth = 28

        else:
            numOfClasses = 2
            pixelHeight = 70
            pixelWidth = 60

        self.k = .01  # this is so far best choice for k idk why

        # NEED HELP WITH THIS NEED TO SET K correctly and confirm math
        for digit in range(numOfClasses):
            probOfClassAndFeature = math.log(self.classProb[digit] + self.k)
            for x in range(pixelWidth):
                for y in range(pixelHeight):
                    if (datum.get((x, y)) == 1):
                        probOfClassAndFeature += math.log(self.allFeaturesProb[digit][(x, y)] + self.k)
                    else:
                        probOfClassAndFeature += math.log(1 - (self.allFeaturesProb[digit][(x, y)]) + self.k)
            logJoint[digit] = probOfClassAndFeature
            probOfClassAndFeature = 0

        return logJoint

    def findHighOddsFeatures(self, label1, label2):
        """
    Returns the 100 best features for the odds ratio:
            P(feature=1 | label1)/P(feature=1 | label2)

    Note: you may find 'self.features' a useful way to loop through all possible features
    """
        featuresOdds = []

        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

        return featuresOdds




