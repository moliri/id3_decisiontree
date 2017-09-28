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
		trainingSet, testingSet = getExamples(inputFileName, trainingSetSize)

		
		# 3. estimate expected prior probability of True or False classifications based on distribution of examples in training set
		# 4. construct decision tree based on training set
		# 5. classify examples in testing set using the tree
		# 6. classify examples in testing set using most likely class determined by prior probabilities
		# 7. determine proportion of correct classifications in each ^ by comparing classifications to correct answers
		# 8. repeat 2-7 (a trial) until numberOfTrials == the number of trials run
		# 9. print results for each trial (review output format)

def getExamples(fileName, trainingSetSize):
	examplesFile = open(fileName, "r")
	examplesDict = csv.DictReader(examplesFile, delimiter='\t')
	trainingSet = []
	testingSet = []
	# i = 0

	# examples = [r for r in examplesDict]
	# while len(trainingSet) < 10:
	# 	trainingSet.append(random.choice(examples))

	for example in examplesDict:
		# i += 1
		sorter = random.randint(0,1)
		examplesNeeded = trainingSetSize - len(trainingSet)
		# examplesLeft = len(list(examplesDict)) - i+1

		# print "need, left: ", examplesNeeded, examplesLeft
		# if (examplesNeeded == examplesLeft): 
			# trainingSet.append(example)
		if (sorter == 0 and len(trainingSet) < trainingSetSize):
			trainingSet.append(example)
		else: 
			testingSet.append(example)

	print "Training set: ", len(trainingSet)
	print "Testing set: ", len(testingSet)

	return trainingSet, testingSet



if __name__ == "__main__":
	main()