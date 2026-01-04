#Write a program to print all elements of a list.
arr = [5, 10, 15, 20]

for x in arr:
    print(x)

#Write a program to find the sum of all elements in an array.
arr = [20, 10, 5, 20]
sum = 0
for i in range(len(arr)):
    sum = sum + arr[i]

print("Sum =", sum)

#Write a program to find the largest element in an array.
arr = [12, 45, 7, 22]
largest = arr[0]
for i in range(len(arr)):
    if arr[i] > largest:
        largest = arr[i]
print("largest value =", largest)

#Count the number of even and odd elements in a list.
arr = [1, 2, 3, 4, 5, 6]
even = 0
odd = 0

for i in range(len(arr)):
    if arr[i] % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1
print("no of odd values =", odd)
print("no of even values =", even)

#Reverse an array
arr = [1, 2, 3, 4, 5]

start = 0
end = len(arr) - 1

while start < end:
    temp = arr[start]
    arr[start] = arr[end]
    arr[end] = temp

    start = start + 1
    end = end - 1

print("Reversed array:", arr)


#Search an element
arr = [10, 20, 30, 40]
n = int(input("Enter the value to search for"))
flag = True
i = 0
while flag == True and i<len(arr):
    if arr[i] == n:
        flag = False 
    else:
        i = i + 1
if flag == False:
    print("element", n, "found")
else:
    print("element", n, "not found")

#Array input from user
n = int(input("enter no of elements you want to add"))
arr = []
for i in range(n):
    arr.append(int(input("Enter element: ")))
print(arr)

