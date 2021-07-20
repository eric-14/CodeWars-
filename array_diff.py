def array_diff(a, b):
    #your code here
    return [x for x in a if x not in b]

print(">>>>>>><<<<<<<{}".format(array_diff([1,2,2,2,3],[2])))