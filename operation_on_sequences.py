import math
def solve(arr):
    # your code
    results = []
    P=0
    for index in range(0,len(arr),4):
        P +=(arr[index] **2 + arr[index+1] ** 2 ) * (arr[index+2]**2 + arr[index+3]**2)
    print("Line 9 P ",P)
    #diophantine equation
    #get the largest sqrt closest to the value  then see which one's remainder has a sqrt 
    for x in range(0,int(P/2)):
        for y in range(0,int(P/2)): 
            if(x**2 + y**2) >  P or  (x**2 + y**2) < P:
                continue
            if(x**2 + y**2) == P:
                return [x,y]
                
print("solution",solve([1, 3, 1, 2, 1, 5, 1, 9]))