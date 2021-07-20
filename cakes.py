def cakes(recipe, available):
    array = []
    checklist =[]
    for item,amount in recipe.items():
        for ing, q in available.items():
            if(len(recipe) > len(available)):
                return 0
            if(ing == item):
                array.append(q/amount)
                checklist.append(item)
                
    x  = [x for x in recipe.keys() if x not in checklist]
    if(x):return 0
        
    return int(min(array))
cakes({flour: 500, sugar: 200, eggs: 1}, {flour: 1200, sugar: 1200, eggs: 5, milk: 200})