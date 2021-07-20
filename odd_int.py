def find_it(seq):
    seq.sort()
    arr =[]
    i=0
    count = 1
    j=1

    #                       [20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]
    while(True):
        if(j >= (len(seq)-1)):
            if(seq[i-1] == seq[j]):
                count +=1 
                if(count % 2 != 0):
                    return seq[j]
            else:
                return seq[j]
                
        
        if(seq[i] == seq[j]):
            count += 1
            print("inside first if i = {}  j = {} seq[i] = {} seq[j] = {} count = {}".format(i,j, seq[i],seq[j],count))
            i = j 
            # if(j < len(seq)):
            #     j+=1
            # else:
            #     if(seq[i-1] == seq[j]):
            #         count +=1 
            #         if(count % 2 != 0):
            #             return seq[j]
            #     else:
            #         return seq[j]
                    

            if(seq[j] != seq[i]):
                if(count % 2 != 0): 
                    print("inside count >>>>>>>>>>>>><<<<<<<< {} {} {}".format(count, seq[i] , seq[j]))
                    return seq[i]
                count = 1
                i = j 
                j += 1 
        
        else:
            if(count % 2 != 0): 
                print("inside count >>>>>>>>>>>>><<<<<<<< {} {} {}".format(count, seq[i] , seq[j]))
                return seq[i]
            count = 1
            print("inside else <<<<<<<<>>>>>>> count=={} \t no=={}".format(count,seq[i]))
            
           
            
            
find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5])