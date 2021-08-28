import random
def bubble_sort(i):
    for i in range(len(li)-1):
        for j in range(len(li)-i-1):
            if li[j]<li[j+1]:
                li[j],li[j+1] = li[j+1],li[j]


li= [1232,4345,53,534,234,666666,7777]
bubble_sort(li)
print(li)
x=min(li)
print(x)