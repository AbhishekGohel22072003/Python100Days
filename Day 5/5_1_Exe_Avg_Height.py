heights = input("Enter the heights of all the students, separated with comma. : ").split(',')

for i in range (0,len(heights)):
    heights[i] = int(heights[i])


# print(heights)

# print(type(heights[0]))
sum = 0
for i in heights:
    sum = sum+i

print(f'Average of the heights of all the students is: {sum/len(heights)}')