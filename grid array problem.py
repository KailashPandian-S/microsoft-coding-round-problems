""" microsoft question - grid system ( the maximum of optimal path ) .Given two arrays with same length combined together like a grid. Need to reach the last index of the second array from first index of the first array.Only right and down movements are allowed. Find the maximum element in the optimal path."""



def solution(a,b,n):
    a=[3,4,6]
    b=[6,5,4]
    n = len(a)
    min = 99988873
    total = 0
    min_list = []
    j=0

    for i in range(n):
     if i==0 :
       first_part = a[:n-j] 
       second_part = [b[n-j-1]] 
       p = first_part + second_part
       
       
     else:
        first_part = a[: n-j] 
        second_part = b[n-j-1:]
        p= first_part + second_part
     j = j+1
     sum = 0 
     for k in range(len(p)): 
        sum += p[k]
     if sum <= min: 
        min = sum 
        min_list = [] + p 
    print(min_list)
    maxi = -767657632
    for m in range(len(min_list)):
      if maxi <= min_list[m]: 
        maxi = min_list[m] 
        
    print(maxi)


a=[1,2,3,2]
b=[2,3,4,2]
n = len(a)

solution(a,b,n)
