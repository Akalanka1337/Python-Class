user_input = input("Enter the numbers").split()

int_list = list(map(int, user_input))

print ("Maximum =",max(int_list), "\nMinimum =",min(int_list))
