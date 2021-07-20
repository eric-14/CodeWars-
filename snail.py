def snail(snail_map):
    result=[]
    index = len(array)
    for i in range(len(array)):
       for j in range(len(array)):
            if(i==0):
               result.append(array[i][j])
            
            if((i>0 and i < len(array)-1 ) and j==len(array)-1):
                j = len(array)-1
                result.append(array[i][j])
            if(i == len(array)-1):
                 result.append(array[i][len(array)-j-1])
            if((i == len(array)-1) and j== 0):
                print("line 15 home run")
                for k in range(len(array)-1):
                    for m in range(len(array)):
                        print("line 18 k and m ",k ,m)
                        result.append(array[k][len(array)-m])


    print("line 17 result",result)    
            # print(array[i][j]) 
            # result.append(array[i][j])
            # if(i > 1 and j == len(array)):
                # for i in range(len(array) - 1 ):
                    # result.append(array[i][j])
            
                    # print("line 14 RESULT ",array[i][j])
    return result      

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
# print("type of the array ",len(array))





snail(array)