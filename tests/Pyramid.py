
# num=int(input("Enter the number of row of pyramid :  "))
#-------------------------------------------
num =5
for i in range(num):
        # Printing spaces
        print(' ' * (num - i - 1), end='')
        # Printing asterisks
        print('*' * (2 * i + 1))
#
# -------------------------------------------
#Right-aligned Triangle pattern of astrisks(*)
# for i in range(num+1):
#     print(" "*(num-i), end=" ")
#     print("*"*i)
#-------------------------------------------
# Left-aligned triangels patter of astrisks(*)
# for i in range(1, num+1):
#     print("*"*i)
