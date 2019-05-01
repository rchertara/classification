# kNearest.py
# ---------------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

import util
import classificationMethod
import math


def guessFromKNearest(AllNeighbors,k):
  sorted_neighbors= sorted(AllNeighbors, key=lambda x: x.distance)
  classVotes=util.Counter()
  for i in range(int(k)):
    neighbor=sorted_neighbors[i]
    classVotes[neighbor.label]+=1

  return classVotes.argMax()


class KNearestClassifier(classificationMethod.ClassificationMethod):
  """
  The  is a very simple classifier: for
  every test instance presented to it, the classifier returns
  the label that was seen most often in the training data.
  """
  def __init__(self, legalLabels):
    self.guess = None
    self.type = "kmeans"
    self.legalLabels=legalLabels

  
  def train(self, data, labels, validationData, validationLabels,options):
    """
    Find the most common label in the training data.
    """
    # counter = util.Counter()
    # counter.incrementAll(labels, 1)
    # self.guess = counter.argMax()
    self.trainData=data
    self.trainLabels=labels
    if(options=="faces"):
      self.k=.25*len(data) #k amount of neighbors to compare similarity! THIS IS CRUCIAL idk why a bigger k for faces works better
    else:
      self.k=3 #for digits a smaller k works the best! basically finding the most similar thing it looks like is best choice lol
    #i think i can skip train?
  def classify(self, testData,options):
    """
    Classify all test data as the most common label.
    """
    #guesses[]
    #voteTally [] or counter use argMAX and append to guesses
    # [self.guess for i in testData]
    #an object to hold the vector?(dont think i need this),label, its distance to feature vector
    #finally iterate thru collection and tally up the amount of votes for each label
    xRange=0
    yRange=0
    if(options=="faces"):
      xRange=10
      yRange=10
    else:
      xRange=7
      yRange=7

    guesses=[]
    for i in range(len(testData)):
      testImage=testData[i]#for each test image loop thru all train images to see which is closet to determine class
      AllNeighbors = []
      for j in range(len(self.trainData)):
        trainImage=self.trainData[j]
        trainLabel=self.trainLabels[j]
        distance=0
        for x in range(xRange):#For each feature (x,y) coordinate pixel
          for y in range(yRange):
            featTrainVal=trainImage.get((x,y))
            featTestVal =testImage.get((x, y))
            distance+=(featTrainVal-featTestVal)**2
        distance=math.sqrt(distance)
        neighbor=Neighbor(trainLabel,distance)
        AllNeighbors.append(neighbor)

      guessLabel=guessFromKNearest(AllNeighbors,self.k)
      guesses.append(guessLabel)

    return guesses

class Neighbor:
  def __init__(self,label,distance):
    self.label=label
    self.distance=distance

