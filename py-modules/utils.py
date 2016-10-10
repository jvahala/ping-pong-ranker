import numpy as np 

def softmax(x,rescale_=False): 
	if rescale_: 
		x_ = rescale(x)
	else: 
		x_ = x
	expx = np.exp(-1.0*np.array(x_))		#take exponential of the -x(i) values in x 
	total = np.sum(expx)	#for use in the denominator
	return expx/float(total)

def rescale(x,max_=10):
	x_scaled = [k/400*float(max_) for k in x]
	return x_scaled