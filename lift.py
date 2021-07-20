class Dinglemouse(object):

    def __init__(self, queues, capacity):
       
        self.queues = [list(elem) for elem in queues]
        self.no_of_people = sum(len(x) for x in self.queues)
        self.max_capacity = capacity
        self.capacity = 0
        self.position = 0
        self.no_floors = len(queues)
        self.ascending = 1
        self.lift_load = []
        self.floors_stopped = []
        self.no_exited = 0

        
       
    def same_direction(self,dest):
        if(self.ascending == 1 and (dest > self.position)):
            return True
        elif(self.ascending == 0  and (dest < self.position)):
            return True
        else:
            return False 
    
    def check_queue(self,*args):
        
        queue_1 = []
        for subl in args:
            for item in subl:
                queue_1.append(item)
        for floor in queue_1:
           
            if(self.same_direction(floor)):
                if(self.capacity >= self.max_capacity): return 
                self.lift_load.append(floor)
                if(floor != []):
                   
                    self.queues[self.position].remove(floor)
                    self.no_of_people -=1   
                self.capacity += 1
                if(self.capacity >= self.max_capacity):
                    break
            else:
                self.queues[self.position].remove(floor)
                self.queues[self.position].append(floor)
                
    def alight_from_lift(self):
        if(self.position in self.lift_load):
            self.no_exited = self.lift_load.count(self.position)
            self.lift_load = [person for person in self.lift_load if person != self.position]
            self.capacity -= self.no_exited
        else:return

    def be_clever(self):
        if(self.ascending ==1 ):
            if(len(self.lift_load)==0 and self.no_of_people==0):
                self.ascending = 0
                return True      
        elif(self.ascending ==0):
            if(len(self.lift_load)==0 and sum(len(self.queues[x]) for x in range(self.position+1))==0): 
                self.ascending = 1
                return True
            
    def theLift(self):
            while(len(self.lift_load) != 0 or self.no_of_people != 0):
                if(self.ascending == 1):
                    self.position = 0 
                    for i in range(self.no_floors):
                        self.position = i 
                        if(self.be_clever()):
                            break
                        if(self.position == 0):
                           
                            self.check_queue(self.queues[self.position])
                            
                            self.floors_stopped.append(self.position)
                        elif(self.position > 0 and self.position+1 < self.no_floors ):
                            
                            if((len(self.queues[self.position])== 0) and (self.position not in self.lift_load)):
                                continue 
                            if(self.capacity >= self.max_capacity and (self.position not in self.lift_load)):
                                continue  
                            elif((self.position in self.lift_load) or (len(self.queues[self.position]) != 0)):
                                count_lift = len(self.lift_load)
                                count_people = self.no_of_people
                                
                                self.alight_from_lift()    
                               
                                self.check_queue(self.queues[self.position])
                                
                                if((self.no_of_people != count_people) or (len(self.lift_load) != count_lift)):
                                       
                                        self.floors_stopped.append(self.position) 
                        elif(self.position+1 == self.no_floors):
                            if(self.capacity >= self.max_capacity and (self.position not in self.lift_load)):
                                self.ascending = 0
                                break
                            if((len((self.queues[self.position]))== 0) and (self.position not in self.lift_load)):
                                self.ascending = 0
                                break
                            elif((self.position in self.lift_load) or (len(self.queues[self.position]) != 0)):
                                count_lift = len(self.lift_load)
                                count_people = self.no_of_people
                                
                                self.alight_from_lift()    
                                self.check_queue(self.queues[self.position])
                                if((self.no_of_people != count_people) or (len(self.lift_load) != count_lift)):
                                        self.floors_stopped.append(self.position) 
                                self.ascending = 0
                            
                        
                if(self.ascending == 0):
                    for i in range(self.no_floors):
                        self.position = self.no_floors - i - 1
                        if(len(self.lift_load)==0 and self.no_of_people==0):
                            self.floors_stopped.append(0)
                            break
                        # if(self.be_clever()):
                        #     break

                        if(self.position == 0):
                            
                            # if(len(self.lift_load) > 0  and self.no_of_people !=0):
                            #     self.ascending = 1
                            #     print("LINE 114 SELF.POSITION 0 WHILE DESCENDING")
                            #     break
                            count_lift = len(self.lift_load)
                            count_people = self.no_of_people
        
                            self.alight_from_lift()
                            self.check_queue(self.queues[self.position])
                            
                            if((count_lift != len(self.lift_load)) or (self.no_of_people != count_people)):
                                self.floors_stopped.append(self.position)
                            elif(len(self.lift_load)==0 and self.no_of_people ==0):
                                 self.floors_stopped.append(self.position)
                                
                        elif(self.position <=  self.no_floors -1 ):
                            
                            if(self.capacity >= self.max_capacity and (self.position not in self.lift_load) and len(self.queues[self.position])==0):
                                continue  
                            if((len(self.queues[self.position])== 0) and ( self.position not in self.lift_load)):
                                continue 
                            if(self.position in self.lift_load or (len(self.queues[self.position]) != 0)):
                                count_lift = len(self.lift_load)
                                count_people = self.no_of_people
                                self.alight_from_lift()
                                self.check_queue(self.queues[self.position])
                                if((len(self.lift_load) != count_lift) or (self.no_of_people != count_people)):
                                    self.floors_stopped.append(self.position)
               


            return self.floors_stopped

#break when the lift_load and queues is empty


lift = Dinglemouse(  ( (),   (3,),  (4,),    (),   (5,),  (),    () ),6)
answer = lift.theLift()
print("THIS IS MT ANSWER AFTER CODEING THE LIFT MOVEMENT",answer)

