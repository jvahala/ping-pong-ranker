import numpy as np 

def genTestWinTable(num_users=5,max_wins=10,seed_val=1): 
	'''
	Purpose: 
	Creates an array of win-loss data with each number being the wins that the row user had against the column user
		u1	u2	u3	u4	u5
	u1[ [ 0  8  9  5  0]
	u2  [ 0  0  7  6  9]
	u3  [ 2  4  0  2  4]
	u4  [10  2  4  0  7]
	u5  [ 9  1  7  0  0]]

	Inputs: 
	num_users = number of users that exist for the dataset
	max_wins = max number of wins that a user can have against another user

	Outputs:
	ndarray object with the table defined in purpose 
	'''
	np.random.seed(seed_val)
	win_table = np.random.randint(0, max_wins+1, (num_users,num_users) )
	for i in range(num_users): 
		win_table[i,i] = 0
	return win_table
