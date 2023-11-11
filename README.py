# Statistics-Calculator
import math

print("THIS IS A STATISTICS CALCULATOR PROGRAMMED BY GCINASONKE")
list = []
list_length = int(input("Enter the number of elements in your dataset: "))

for i in range(list_length):
    x = input("Enter an element: ")    
    list.append(int(x))

list = sorted(list)

def mean():
    Mean = sum(list) / list_length   
    print("The mean is " + str(Mean))

mean()

def median():
    if list_length % 2 == 0:
        location = list_length // 2    
        Median1 = list[location]
        Median2 = list[location - 1]
        Median = (Median1 + Median2) / 2
        print("The median is " + str(Median))
    else:
        location = list_length // 2
        Median = float(list[location])
        print("The median is " + str(Median))

median()

def standard_deviation():
    list1 = [] 
    y = float(sum(list) / list_length)  
    for i in range(len(list)):
        h = list[i]
        h = h - y
        list1.append(h**2)
    s = math.sqrt(sum(list1) / list_length)
    print("The standard deviation is " + str(s))

standard_deviation()

