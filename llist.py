# Write a Python program that:
# 1.   Creates a list of numbers from 1 to 10.
# 2.   Extracts the first five elements from the list.
# 3.   Reverses these extracted elements.
# 4.   Prints both the extracted list and the reversed list

l=[i for i in range(1,11)]    #list comprehension
# for i in range(1,11):
#     l.append(i)
print("original list:",l)
b=l[:5]
print("Extracted first five elements:",b)
# b.reverse()
# print(b)      or
# print(list(reversed(b)))  or
print("Reversed extracted elements:",b[::-1])