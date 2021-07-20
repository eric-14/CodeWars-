
def dbl_linear(n):
	
	# your code
    u =[1]
    for i in range(n):
        y = u[i]* 2 + 1
        z = u[i] * 3 + 1
        u.append(y)
        u.append(z)
    u = list(set(u))
        
    u.sort()
    
    return u[n]


       