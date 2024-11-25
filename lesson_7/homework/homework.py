#თავიდან იწერება if და მერე ვუწერთ პირობა და ბოლოში იწერება :
#: შემდეგ იწერება კოდის ბლოკი.
#თუ if-ის პირობა არასწორია მაშინ გაიშვება else-ის კოდის ბლოკი


# user_age = int(input("enter your age: "))
# if user_age <= 18:
#     print("your under/at the age of 18")
# else:
#     print("your over the age of 18")


# user_num = int(input("enter your number: "))
# if user_num <= 0:
#     print("უარყობითი")
# else:
#     print("დადებითი")


user_num = int(input("enter you number: "))
user_num1 = int(input("enter your second number: "))
if user_num > user_num1:
    print(user_num, "უფრო მეტია ვიდრე", user_num1)
else:
    print(user_num1, "უფრო მეტია ვიდრე", user_num)