#           Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. 
#The first line of the code has been defined as below.

def hello_name(user_name):
    print("hello " + user_name)

hello_name("Andrew")   
 

 #          Question 2
 #Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing.

def first_odds():
    for i in range(1, 100, 2):
        print(i)
            
            
first_odds()   



#           Question 3
#Please write a Python function, max_num_in_list to return the max number of a given list. 
# The first line of the code has been defined as below.




def max_num_in_list(a_list):
    for list in a_list:
        max_Num = max([1,2,3,4,5,6,7,8,10])
        print(max_Num)
        break

max_count = [1,2,3,4,5,6,7,8,10]
max_num_in_list(max_count)



#           Question 4
#Write a function to return if the given year is a leap year. 
# A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. 
# The return should be boolean Type (true/false).

def is_leap_year(a_year):
    print(is_leap_year/4)

is_leap_year(2008)



     
     


           #Question 5
#Write a function to check to see if all numbers in list are consecutive numbers.
#  For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. 
# The return should be boolean Type.


def is_consecutive(a_list):
    for i in a_list:
        print(i)
        if i <= 8:
            print("its consecutive")
        elif i == [10,9,45,31]:
            print("its not in order")
       
        

consecutive = [1,2,3,4,5,6,7,8]
is_consecutive(consecutive)




