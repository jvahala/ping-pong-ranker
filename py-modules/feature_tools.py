import numpy as np 
from data_generation import genTestWinTable 
import utils



def userDifferentials(wins_table): 
	n = len(wins_table) 	#number of users 
	differentials = np.zeros((n,n))
	for i in range(n): 
		for j in range(n): 
			differentials[i,j] = wins_table[i,j]-wins_table[j,i]
	return differentials

def userPercentages(wins_table): 
	n = len(wins_table)
	percentages = np.zeros((n,n))
	for i in range(n):
		for j in range(n): 
			if i!=j: 
				percentages[i,j] = wins_table[i,j]/float(wins_table[i,j]+wins_table[j,i])
	return percentages


testwins = genTestWinTable(num_users=6, max_wins=10, seed_val=1)
testwins = np.array([[0,20,1,20],[1,0,20,1],[20,1,0,1],[1,20,20,0]])
differentials = userDifferentials(testwins)
percentages = userPercentages(testwins)
print testwins 
print differentials
print percentages

#each user has a weight that changes winning against them. 
#distance between users 
def measure(array_):
	n = len(array_)
	output = np.zeros((n,n))
	for i in range(n):
		for j in range(n):
			output[i,j] = np.dot(array_[i,:],array_[j,:])
	return output 

out = measure(percentages)
sumout=np.sum(out,axis=0)
sumout2 = [out[x,x] for x in range(len(out))]

print out, sumout,sumout2


