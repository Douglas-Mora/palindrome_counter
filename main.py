import math as m
def count_palindromes(a, b):
    counting = 0
    for number in range(m.ceil(a),m.floor(b)+1):
        if str(number) == str(number)[::-1]:
            counting += 1
    if counting == 0:
        return-1
    else:
     return counting
    
    
print(count_palindromes(0,3))