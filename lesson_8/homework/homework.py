# end = int(input("შეიყვანეთ თქვენი ნომერი: "))
# for i in range(end):
#     if i % 2 == 0:
#         print(i)
#         print("თქვენი რიცხვი ლუწია")


# user_num = int(input("enter your number: "))
# product = 1
# for i in range(user_num + 1):
#     if i % 2 == 1:
#         product = product * i
# print(product)


# for i in range(56):
#     if i % 2 == 0:
#         print(i / 2)
#     else:
#         print(i * 2)


user_age = int(input("enter your age: "))
is_student = input("are you a student: y/n ")
if is_student == "yes" or is_student == "y":
    is_student = True
else:
    is_student = False

if user_age < 18:
    if is_student:
        print("50%")
    else:
        print("30%")
else:
    if is_student:
        print("20%")
    else:
        print("no discount")
print("procceed to payment")