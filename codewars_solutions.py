''' If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

Additionally, if the number is negative, return 0.'''

def solution(number):
        amount = 0
        for num in range(3,number):
            if (num % 3 == 0) or (num % 5 == 0):
                amount += num
        return amount


'''Complete the solution so that it splits the string into pairs of two characters. 

If the string contains an odd number of characters then it should replace the missing 

second character of the final pair with an underscore ('_').'''

def solution1(s):
    s_list = []

    for i in range(0,len(s_list),2): 
        s_list.append(s[i:i+2])
        print(s_list)
    last_index = s_list[-1]
    if len(last_index) == 1:
        s_list[-1] = s_list[-1] + '-'
    return s_list

print(solution1('name'))