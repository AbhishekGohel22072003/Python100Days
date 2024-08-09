# Where do you want to put your treasure?

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = int(input("Where do you want to enter your treasure? (e.g. 11, 21, 32, etc.): "))

position_str = str(position)

if position_str not in ('11','12','13','21','22','23','31','32','33'):
    print("You have entered invalid input...")
else:
    position1 = int(position_str[0])-1
    position2 = int(position_str[1])-1
    
    map[position1][position2] = "X"
    
    print(f"{row1}\n{row2}\n{row3}")