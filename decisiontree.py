import sys, csv, random

def main():
	# input = inputFileName, trainingSetSize, numberOfTrials, verbose

	if len(sys.argv) < 5:
		print "ERR: Missing parameters! Make sure to include inputFileName, trainingSetSize, numberOfTrials, and verbose."
	else: 
		inputFileName = sys.argv[1]
		trainingSetSize = int(sys.argv[2])
		numberOfTrials = sys.argv[3]
		verbose = sys.argv[4]
	
		# 1. read in inputFileName containing examples
		# 2. divide exampes into training set (n = trainingSetSize, chosen randomly) and testing set
		trainingSet, testingSet = sortExamples(inputFileName, trainingSetSize)
		print "Training set: ", len(trainingSet)
		print "Testing set: ", len(testingSet)
		
		# 3. estimate expected prior probability of True or False classifications based on distribution of examples in training set
		truePriorProbability, falsePriorProbability = estimatePriorProb(trainingSet, trainingSetSize)


		# 4. construct decision tree based on training set
		decisionTree = makeID3Tree(trainingSet)

		# 5. classify examples in testing set using the tree
		# 6. classify examples in testing set using most likely class determined by prior probabilities
		# 7. determine proportion of correct classifications in each ^ by comparing classifications to correct answers
		# 8. repeat 2-7 (a trial) until numberOfTrials == the number of trials run
		# 9. print results for each trial (review output format)


def makeID3Tree(trainingSet, targetAttribute, attributes): 
	root = []


def estimatePriorProb(trainingSet, trainingSetSize):
	trueCount = 0.0
	for example in trainingSet: 
		print example
		if example["CLASS"] == True:
			trueCount += 1.0

	print "trueCount", trueCount

	truePriorProb = float(trueCount/len(trainingSet))
	falsePriorProb = float((len(trainingSet) - trueCount)/len(trainingSet))

	print "truePriorProb", truePriorProb
	print "falsePriorProb", falsePriorProb

	return truePriorProb, falsePriorProb



def sortExamples(fileName, trainingSetSize):
	examplesFile = open(fileName, "r")
	examplesDict = csv.DictReader(examplesFile, delimiter='\t')
	trainingSet = []
	testingSet = []

	for example in examplesDict:

		# swap bool strings with Bools
		for attribute in example:
			if example[attribute] == "true":
				example[attribute] = True
			else: 
				example[attribute] = False

		# sort into training and testing sets
		sorter = random.randint(0,1)
		if (sorter == 0 and len(trainingSet) < trainingSetSize):
			trainingSet.append(example)
		else: 
			testingSet.append(example)

	return trainingSet, testingSet



if __name__ == "__main__":
	main()