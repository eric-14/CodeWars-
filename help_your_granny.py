import math
def tour(friends, friend_towns, home_to_town_distances):

    friend_town_list =[]
    for friend in friends:
        for ftown in friend_towns:
            if (ftown[0]  == friend):
                friend_town_list.append(ftown)


    print("real friend towns ", friend_town_list)

    first_town = home_to_town_distances.get(friend_town_list[0][1])
    distance = first_town
    
    for i in range(0,len(friend_town_list)+1,1):
        if (i == len(friend_town_list)-1):
            distance += home_to_town_distances.get(friend_town_list[i][1])
            continue
        elif( i > len(friend_town_list)-1):
            break
        first_town1 = home_to_town_distances.get(friend_town_list[i][1])
        second_town = home_to_town_distances.get(friend_town_list[i+1][1])
        distance_to_town2 = math.sqrt((second_town**2)-(first_town1**2))
        distance += distance_to_town2  
    return int(distance)


friends1 = ["A1", "A2", "A3", "A4", "A5"]
fTowns1 = [["A1", "X1"], ["A2", "X2"], ["A3", "X3"], ["A4", "X4"]]
distTable1 = {"X1": 100.0, "X2": 200.0, "X3": 250.0, "X4": 300.0}

print("result of the function",tour(friends1, fTowns1, distTable1))

