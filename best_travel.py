import math
def choose_best_sum(t, k, ls):
    # your code
    sum_close_values = [] 

    list_close_values = []   

    for j in range(0,len(ls)-1,k):
        for m in range(0,len(ls)-1,k):
            for n in range(0,len(ls)-1,k):
                sum1 =ls[j]
                i=1
                list_inside= []
                list_inside.append(sum1)
                while(i < k):
                    sum1+=ls[j+i]
                    list_inside.append(ls[j+i])
                    i += 1

                list_close_values.append(list_inside)
                sum_close_values.append(sum1)

    closest_difference =[]
    
    for i in sum_close_values:
        closest_difference.append(math.abs(i-t))
    
    index = closest_difference.index(math.min(closest_difference))

    return list_close_values[index]

ls = [50, 55, 57, 58, 60]
t = 174 
k=3

print("The result is ",choose_best_sum(t,k,ls))


