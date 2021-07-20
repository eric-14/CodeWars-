def tickets(people):
    twenty = 0
    fifty = 0
    print("Length of people>>>>>>>>>>", len(people)-1)
    for i in people:
        if(i == 25):
            twenty += 1
            print("just added a new 25")
            if(i == people[len(people) -1]):
                    print("YES LINE 9")
                    return "YES"
            else: continue 
        elif(i == 50):
            fifty += 1
            print("just added a new 50")
            if(twenty >= 1):
                twenty -= 1
                if(i == people[len(people) -1]):
                    print("YES LINE 17")
                    return "YES"
                else: continue 
            else:
                print("NO LINE 20")
                return "NO"
        else:
            if((twenty*25 + fifty*50) >= 75):
                print("Twenty and fifties are above 75")
                if(fifty>=1 and twenty>=2):

                    print("fifty and twenty five above 1 fifty 2 twenty-fives")
                    fifty -= 1
                    twenty -= 2
                    if(i == people[len(people)-1]):
                        print("YES LINE 30")
                        return "YES"
                    else:continue
                elif(twenty >= 3):
                    twenty -= 3
                    print("3 twenty fives ")
                    if(i == people[len(people)-1]):
                            print("YES LINE 36")
                            return "YES"
                    else: continue 
                else:
                    print("NO LINE 39")
                    return "NO"
                        
            else:
                print("NO LINE 43")
                return "NO"
        
tickets( [25,25,
50,
50,
25,
25,
25,
25,
50,
100,
50,
50,
50,
50,
50,
50,
50,
50,
50,
50,
50,
100,
100,
100,
100,
100,
100,
100,
100,
100,
100,
25,
25,
25,
25,
50,
100,
50,
25,
25,
50,
100,
50,
100,
100,
25,
50,
100,
25,
25,
25,
50,
25,
50,
25,
50,
100,
25,
25,
50,
25,
25,
25,
25,
25,
25,
25,
50,
50,
50,
100,
100,
100,
100,
25,
25,
25,
25,
25,
100,
100])
