# def greet(name):
#     print("hello", name)
    
# greet("gio")
# greet("ok")


# def calculator(num1,num2,operator):
#     if operator == "+":
#         return num1 + num2
#     elif operator == "-":
#         return num1 - num2
#     elif operator == "*":
#         return num1 * num2
#     elif operator == "/":
#         return num1 / num2
#     else:
#         return "invalid operation"
# user_num = float(input("enter number: "))
# user_num1 = float(input("enter number: "))
# choice = input("choose: +, -, *, / ~ ")
# print(calculator(user_num, user_num1, choice))


def finder(user_str, char):
    return user_str.find(char)

print(finder("gio", "o"))
print(finder("shishniashvili", "vili"))
print(finder("gio", "a"))
"gio".find()


# def check_palindrome(user_str):
#     if user_str == user_str[::-1]:
#         return True
#     else:
#         return False
# print(check_palindrome("racecar"))
# print(check_palindrome("washingmachine"))


# def remove_char(main_str, char):
#     res = ""
#     for i in main_str:
#         if i != char:
#             res += i
#     return res
# print(remove_char("word, button, click", "o"))
# print(remove_char("word, button, click", "u"))
# print(remove_char("word, button, click", "c"))