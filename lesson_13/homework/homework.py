#1)
# def to_uppercase(user_input):
#     return user_input.upper()
# print(to_uppercase(input("enter: ")))


#2)
# def to_lowercase(user_input):
#     return user_input.lower()
# print(to_lowercase(input("enter: ")))


#3)
# def is_palindrome(string):
#     return string == string[::-1]
# print(is_palindrome(input("enter a word: ")))


#4)
# def capitalize_first(string):
#     return string.capitalize()
#     return string[0].upper() + string[1:].lower()
# print(capitalize_first(input("enter: ")))


#5)
# def generate_initials(first_name, last_name):
#     first = first_name[0].upper()
#     last = last_name[0].upper()
#     return first + "." + last
# print(generate_initials(first_name=input("enter name: "),last_name=input("enter surname: ")))


#6)
def calculate_rectangle_area(length, width):
    return length*width
print(calculate_rectangle_area(4,9))