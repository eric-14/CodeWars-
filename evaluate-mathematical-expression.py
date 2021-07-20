""" 
tests = [
    ["1 + 1", 2],
    ["8/16", 0.5],
    ["3 -(-1)", 4],
    ["2 + -2", 0],
    ["10- 2- -5", 13],
    ["(((10)))", 10],
    ["3 * 5", 15],
    ["-7 * -(6 / 3)", 14]
]

You need to support multiple levels of nested parentheses, ex. (2 / (2 + 3.33) * 4) - -6
And the following are invalid expressions

1 - - 1    // Invalid
1- - 1     // Invalid
6 + - (4)  // Invalid
6 + -(- 4) // Invalid


"""
"""
Solving the problem as if it is a syntax analyzer 




"""
import re
def calc(expression):
    # parsing
    total = 0
    def bracket(expression):
    value = []
    operand =[]
    operands = '[\+|\-|\/|\*]'
    operands =  re.compile(operands)
    for i in expression:
        if(expression[i].isdigit()):
            value.append(expression[1])
        else if(operands.match(expression[i])):
            
        
    
    print("Line 17 expession",expression)

   
    close_bracket= '[)]'
    

    opening_bracket = '[(]'
    
    pat  = re.compile(digit)

    #assuming i wont be given default expressions
    #assuming all the spaces have been removed
    def operations(v1,v2,operations_string):
        if(operations_string == "+"):
            return float(v1) + float(v2 )
        elif(operations_string == "-"):
            return  float(v1) - float(v2 )
        elif(operations_string == "*"):
            return  float(v1) * float(v2 )
        elif(operations_string == "/"):
            return float(v1) / float(v2)
    
    def rules(ending_index, expression):
        #identify if it is open bracket then return the operand that is required 

        minus_minus = '[-(-] | [-(\d]   | [--]'
        minus = '[-]'
        minus_plus = '[-(+] | [+(-] + [-(\d]  | -+ | +- '
        add = '[+]'
        add_add = '[+(+] | [+(\d] | ++'
        close_bracket = '[)]'
        opening_bracket = '[(]'

        # # search_range = expression.splice(starting_index,-1)

        if(minus_minus.match(expression)):
            x = minus_minus.match(expression).end() + 1 
             
            #perform all operations in the bracket

            # digit , operand , digit)
            if((expression.index(x).isdisgit() and operands.match(expression.index(x+1))) and (expressions.index(x+2).isdigit() and close_bracket.match(expressions.index(x+3))) ):
                result = operations(expressions.index(x),expressions.index+2,expressions.index(x+1))
                return result, '-'

            # operand, digit , )
            elif((operands.match(expression.index(x)) and expressions.index(x+1).isdigit()) and (close_bracket.match(expressions.index(x+2)))):
                return expressions.index(x+1).isdigit(),'-'
            # re.subn(minus_minus,minus,expression)
            # re.subn(close_bracket,)
        
        #     #construct for operand, digit, operand . )

        # elif(minus_plus.match(expression)):
        #      x = re.ending_index_of_match + 1 
          
        #     if((expression.index(x).isdisgit() and operands.match(expression.index(x+1))) and (expressions.index(x+2).isdigit()) ):
        #         result = operations(expressions.index(x),expressions.index+2,expressions.index(x+1))
            
        #     elif((operands.match(expression.index(x)) and expressions.index(x+1).isdigit()) and (close_bracket.match(expressions.index(x+2)))):
        #         re.subn(minus_minus,minus,expression)
        #         re.subn(close_bracket,)
            
        #     #construct for operand, digit, operand . )

        # elif(add_add.match(expression)):
        #       x = re.ending_index_of_match + 1 
             
        #     #perform all operations in the bracket

        #     # digit , operand , digit)
        #     if((expression.index(x).isdisgit() and operands.match(expression.index(x+1))) and (expressions.index(x+2).isdigit()) ):
        #         result = operations(expressions.index(x),expressions.index+2,expressions.index(x+1))
        #     # operand, digit , )
        #     elif((operands.match(expression.index(x)) and expressions.index(x+1).isdigit()) and (close_bracket.match(expressions.index(x+2)))):
        #         re.subn(minus_minus,minus,expression)
        #         re.subn(close_bracket,)
            
        #     #construct for operand, digit, operand . )

            



        
    #make this the entry point of the code 
    #like an int main so that code execution can start from this point
    def bracket(expresssion):

        #removing all spaces hopefully 
        name = ''
        for i in expressions:
            if(i.isspace()):
                continue
            name = name + i
        expressions = name
        len = len(expressions)

        for i in range(0,len,3):
    
            if((expression.index(i).isdigit() and operand.match(expression.index(i+1))) and (expression.index(i+2).isdigit())):
                calcution = operation(expression.index(i), expression.index(i+2),expression.index(i+1))
                if(i+2 == len-1):
                    total = calculation
                else:
                    #if the first 3 values in the expressions 
                    # do not complete the calcluation call rules to deal with the rest

                    value_from_rules , operand_from_rules = rules(i,expression) 

                    total = operations(total, value_from_rules, operand_from_rules)
                
        






    return total





calc("1 / (2)")

    #     digit_stack = []
    #     if(i.isdigit()):
    #     while(!close_bracket.match(i)):
    #         if(i.isdigit()):
    #             digit_stack.append(i)
    #             continue 
    #         elif(operands.match(i)):
    #             operations(digit_stack.pop(), expression.index(i.index+ 1))
                


        
    
    # for i in expression:
    #     if(i.isspace()):
    #         continue
    #     if(open_bracket.match(i)):
    #         while()
    #     x = pat.search(expression)
    #     v1,v2= x.group(1,2)
    #     print("line 33 regular expresssions",v1)
   


    # for i in expression:
    #     if(expression.charAt(i) === "("):
    #         j = 0
    #         while(stack.pop() != ")"):
    #             stack.push(charAt(i+j))
    #             j+=1
    #     if(stack):
    #         for i in range(len(stack)):
    #             re.search(r'[+-/*]',)








    # return # evaluated expression



