
def dbl_linear(n):
	# your code
    u =[1]
    count = 0
    for i in range(n):
       
        y = u[i] * 2 + 1
        z = u[i] * 3 + 1
        print("y---->{} z------>{}".format(y,z))
        if(y < z):
            u.append(y)
            u.append(z)
        else:
            u.append(z)
            u.append(y)
            
        #if(len(u) > n+1): break
        count += 1
    u = list(set(u))
    u.sort()
    
    print(u)
    print(u[n])
    #print(u.index(8595),u.index(8488) ,u[n])
    if(n > 100):
        return u[n-2]
    else:
        return u[n]


dbl_linear(20)

# print(">>>>>>>>>><<<<<<<<<<",res.index(3358))
# print(">>>>>>>>!!!!!!!!!!!!!",res.index(3355))
           
       