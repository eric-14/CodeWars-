def variance(numbers): 
    # your code here
    sum=0
    var = 0
    for i in numbers:
        sum += i
        
    mean = sum / len(numbers)
    print("len >>>>>>>>>", len(numbers))
    print("><<<<<<<>",mean)
    for i in numbers:
        var += (i - mean)**2
    print("var>>>>>>>>>",var/len(numbers))
    return var/len(numbers)

variance([8, 9, 10, 11, 12])