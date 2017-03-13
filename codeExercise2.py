import csv
import sys

def findTuple(listOfTuples, tupleToFind):
	if(tupleToFind in listOfTuples):
		return listOfTuples.index(tupleToFind)
	else:
		return -1

def findChildrenNodes(listOfTuples, rootPost, repostIdCol):
	children = ()
	for item in listOfTuples:
		if(int(item[repostIdCol]) == rootPost):
			temp = (tuple(item),)
			children = children + temp
	return children


def countFollowersBeneath(socialNetwork, node, postCol, repostCol, followersCol):
	''' This function takes a tuple list of tuples which represents each row of csv without headers labeled Social Network
	function must be given post, repost, and followers column id 
	function is primarly responsible for calling findChildrenNodes to get the childrenNodes of the node that is given.
	function must then iterate through any children nodes and call the findTuple function to return the index of the list of the tuples
	function then returns total of children followers and the node given followers count. this recursively calls this function again. 
	if there are no children function returns
	just the followers count of the given node.'''
	childrenNodes = findChildrenNodes(socialNetwork, int(node[postCol]), repostCol);
	if(childrenNodes):	
		totalChildrenCount = 0
		for child in childrenNodes:
			nextNodeDown = findTuple(socialNetwork, child)
			if(nextNodeDown > -1):
				countBeneath = countFollowersBeneath(socialNetwork, socialNetwork[nextNodeDown], postCol, repostCol, followersCol)
				totalChildrenCount = totalChildrenCount + countBeneath
		return int(node[followersCol]) + totalChildrenCount
	else:	
		return int(node[followersCol])

def findRootTotalFollowers(socialNetwork, postCol, repostCol, followersCol):
	''' This function takes a tuple list of tuples which represents each row of csv without headers
	function must be given post, repost, and followers column id 
	function is primarly responsible for printing results and calling the CountFollowersBeneath function giving the root node'''
	for item in socialNetwork:
		if(int(item[repostCol]) == -1):
			print('' + str(item[int(postCol)]) + ': ' + str( countFollowersBeneath(socialNetwork, item, int(postCol), int(repostCol),int(followersCol))  ))

print('hello program')
tupleRows = ()
post = 0
repost = 1
follow = 2
f = open('social.csv')
csv_f = csv.reader(f)
next(csv_f, None)
for row in csv_f:
	tempTuple = (tuple(row),)
	tupleRows = tupleRows + tempTuple
findRootTotalFollowers(tupleRows, post, repost, follow)
