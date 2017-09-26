import sys, csv

def main():
	# input = inputFileName, trainingSetSize, numberOfTrials, verbose

	if len(sys.argv) < 5:
		print "ERR: Missing parameters! Make sure to include inputFileName, trainingSetSize, numberOfTrials, and verbose."
	else: 
		inputFileName = sys.argv[1]
		trainingSetSize = sys.argv[2]
		numberOfTrials = sys.argv[3]
		verbose = sys.argv[4]
	
		# 1. read in inputFileName containing examples
		getExamples(inputFileName)

		# 2. divide exampes into training set (n = trainingSetSize, chosen randomly) and testing set
		# 3. estimate expected prior probability of True or False classifications based on distribution of examples in training set
		# 4. construct decision tree based on training set
		# 5. classify examples in testing set using the tree
		# 6. classify examples in testing set using most likely class determined by prior probabilities
		# 7. determine proportion of correct classifications in each ^ by comparing classifications to correct answers
		# 8. repeat 2-7 (a trial) until numberOfTrials == the number of trials run
		# 9. print results for each trial (review output format)
	


def getExamples(fileName):
	examplesFile = open(fileName, "r")
	print "got examples yay!"
	# print examplesFile.readline()

	examplesDict = csv.DictReader(examplesFile, delimiter='\t')
	for example in examplesDict:
		print example['GoodGrades']
	print examplesDict



if __name__ == "__main__":
	main()