# Which of the following option is best?

# Option 1
for i in range(1,6):
    str_i = str(i)
    print((str_i+" ")*i)

# Option 2
rows = 6
for i in range(rows): 
    for j in range(i): 
        print(i, end=' ')
    print(' ')
# Conclusion:
# Option 1 is the better choice due to its simplicity, readability, and efficiency.



    
    
    
    
print('\n\n\n\n')


# Option 1

for i in range(1,6):
    str_i = str(i)
    j = 6-i
    print((str_i+" ")*j)
    
    
# Option 2

rows = 5
b = 0
for i in range(rows, 0, -1):
    b += 1
    for j in range (1, i + 1) :
        print(b, end=' ')
    print('\r')
# Conclusion:
# Option 1 is preferable due to its simplicity, readability, and slight efficiency advantage. 
# It achieves the same pattern with less code and fewer operations.
