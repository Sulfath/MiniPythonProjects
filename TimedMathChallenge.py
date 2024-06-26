import random
import time

OPERATORS = ["+","-","*"]
MIN_OPERAND = 3 
MAX_OPERAND= 12
MAX_PROBLEMS =10

def generate():
    left_operand = random.randint(MIN_OPERAND,MAX_OPERAND)
    right_operand = random.randint(MIN_OPERAND,MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr=str(left_operand) + " " + operator + " "+str(right_operand)
    ans = eval(expr)

    return expr,ans


ans =0 
wrong=0

start_time = time.time()

input("\n Press enter to start! ")
print("----------------------------")
for i in range (MAX_PROBLEMS):
    expr,ans = generate()
    while True:        
        guess = input("Problem #"+str(i+1)+" : " +expr + " = ") 
        if(guess==str(ans)):
            break
        wrong += 1

end_time = time.time()
total_time = round(end_time-start_time,2)   

print("----------------------------")
print("Nice work! you finished the challenge in "+str(total_time)+" seconds!")