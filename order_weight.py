def order_weight(string):
    string = string.split(" ")
   # print("this is the new string",string)
    we_dict = {}
    
    for weight in string:
        sum_v=0
        for w in weight:
            sum_v+=int(w)
        we_dict[sum_v] = weight
            
       
        
    keys = list(we_dict.keys())
    keys.sort()
    #print("trying to sort the keys",keys)
    
    result = []
    
    for key in keys:
        result.append(we_dict.get(key))
        #print("key :",we_dict.get(key),type(we_dict[key]) )
   # print("this is my result",result)
    
    return " ".join(result)
        


order_weight("2000 10003 1234000 44444444 9999 11 11 22 123")