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

def solution(s):
    s_list = []

    for i in range(0,len(s),2): 
        s_list.append(s[i:i+2])

    if len(s_list) != 0 and len(s_list[-1]) == 1:
         s_list[-1] = s_list[-1] + '_'
    return s_list


'''In this simple Kata your task is to create a function that turns a string into a Mexican Wave.

 You will be passed a string and you must return an array of strings where an uppercase letter is 

 a person standing up.'''


def wave(people):
    people_list =[]
    for i in range(len(people.rstrip())): 
        if people[i] != ' ':
            people_list.append(people[:i] + people[i].upper() + people[i+1:])

    return people_list


'''
'''