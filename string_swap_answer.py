# man = "Barra"
# woman = "Mary"
# man_woman = man + " " + woman

# swapped_names = "".join([man_woman.split()[0][0]] + [man_woman.split()[1][1:]])

# print(man_woman.split()[0][0]) # output: "B"
# print(man_woman.split()[1][1:]) # output: "ary"

# print("Swapped Names: ", swapped_names)

# string = input("Enter a string:")
# new_string = ""

# first_letter = string[0]  # Get the first letter
# middle_letter = string[len(string) // 2]  # Get the middle letter
# last_letter = string[len(string) - 1]  # Get the last letter

# new_string = first_letter + middle_letter + last_letter  # Concatenate them
# print(new_string)

# Input 3 strings from the user
string_one = input("Enter the first string:")
string_two = input("Enter the second string:")
string_three = input("Enter the third string:")

# Extract characters from each string
first_letter = string_one[0]
middle_letter = string_two[len(string_two) // 2]
last_letter = string_three[len(string_three) - 1]

new_string = first_letter + middle_letter + last_letter

print("New Combined String: ", new_string)



