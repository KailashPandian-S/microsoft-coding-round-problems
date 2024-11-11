""" Given two integers as string , write a program to find out the minimum number of swaps needed to make these numbers closer to each other ie the difference should be low.Swapping can be done between the i  th index of one string and i th element of another string""" """

"""




str1 = input()   #get input from users
str2 = input()
n = len(str1)
swaps = 0 
for i in range(0,n): 
    if i != 0 : 
        digit_1 = str1[i]
        digit_2 = str2[i]
        if int(digit_1) >= int(digit_2):
            str1 = str1[:i] + digit_2 + str1[i+1:]
            str2 = str2[:i] + digit_1 + str2[i+1:]    #swap if digit of string 1 is large
            swaps = swaps + 1
print(swaps)   #printing minimum needed
