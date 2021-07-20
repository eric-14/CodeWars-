import math
def solve(x,y):
    primes = []
    
    i= 0
    j= 0
    count = 0
    p = 0
    next =  0 

    while(p < y):

        p = (2**i) * (3**j) + 1
        print("i == {} \t j == {} \t p == {}  ".format(i,j,p))
        if(p > y): break
        primes.append(p)
        i+=1
        count+=1
        if(count % 3==0 ): 
            j+=1
            i =1  
            count = 0

        next+=1
    
    

       
        
       
        
        #primes.append(p)
        
    primes.sort()
  
    a= []
    for n in primes:
        if(n >= x):
            a.append(n)
    for x in a:      
        print(">>>>>>>>>>>>>>>>>>>>>>>", a)
    print("len a", len(a))


    return len(a)


solve(100,1000)