
#5.1.2 Write a program to illustrate operations of Tuple:len(), max(), min(), sum(), any(),
# Creating a Tuple with Mixed Datatypes
T1 =(5,'Welcome',7.0,'Geeks', 6+9j)
print("\nTuple with Mixed Datatypes: ")
print(T1)
# Accessing Tuple with Indexing
print("\nFirst element of Tuple is: ")
print(T1[0])
# Unpacking values of Tuple1
a,b,c,d,e=T1
print("#Unpacked values of Tuple1 are:",a," ",b," ",c," ",d," ",e)
# Concatenation of tuples
T2 = ('Hi', 'Wel', 'Come')
T3 = T1 + T2
print("Result of concatenation of T1 and T2:",T3)
# Operations on Tuples
T4=(5,1,23,6,1,66,25)
#len(), max(), min()
print("Length of a given Tuple T4 is:",len(T4))
print("Max element in a given Tuple T4 is:",max(T4))
print("Min element in a given Tuple T4 is",min(T4))
print("Sum of all elements in a given Tuple T4 is",sum(T4))
print("any=",any(T4))
print("All=",all(T4))
print("Elements of T4 after sorting are:",sorted(T4))

#Write a program to find common values between two lists.

list1 = [1, 2, 3, 4, 5, 6]
list2 = [3, 5, 7, 9]
list3 = [3, 4, 5, 10]
# Using the set intersection method
common_elements = list(set(list1).intersection(list2, list3))
print("Common elements using intersection():", common_elements)
# Using the bitwise AND operator
common_elements_operator = list(set(list1) & set(list2) & set(list3))
print("Common elements using & operator: ", common_elements_operator)

