n = int(input("Enter number of elements: "))

arr = []

print("Enter", n, "elements:")
for i in range(n):
    arr.append(int(input()))

maximum = arr[0]
minimum = arr[0]

for i in range(1, n):
    if arr[i] > maximum:
        maximum = arr[i]

    if arr[i] < minimum:
        minimum = arr[i]

print("Maximum element:", maximum)
print("Minimum element:", minimum)
