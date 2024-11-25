# user_age = int(input("enter your age: "))
# if user_age > 0 and user_age <= 10:
#     print("ფასდაკლება, 20 დოლარი")
# elif user_age > 10 and user_age <= 15:
#     print("ფასდაკლება, 10 დოლარი")
# elif user_age > 15 and user_age <= 18:
#     print("ფასდაკლება 5 დოლარი")
# else:
#     print("ფასდაკლება არ გაქვს")
# print("გადაიხადე თანხა")


# 90-100: A
# 80-90: B
# 70-80: C
# 60-70: D
# 50-60: E
# 0-50: F

# score = int(input("enter your score: "))
# if score >= 0 and score < 50: print("F")
# elif score >= 50 and score < 60: print("E")
# elif score >= 60 and score < 70: print("D")
# elif score >= 70 and score < 80: print("C")
# elif score >= 80 and score < 90: print("B")
# elif score >= 90 and score <= 100: print("A")


# for i in range(10, 36):
#     if i % 2 == 0:
#         print(i, "ლუწია")
#     else:
#         print(i, "კენტია")


# start = int(input("enter starting number: "))
# end = int(input("enter ending number: "))
# if end > start:
#     for i in range(start, end+1):
#         if i % 2 == 0:
#             print(i, "ლუწია")
#         else:
#             print(i, "კენტია")
# else:
#     print("starting number is needed to be smaller than the ending number")


# start = int(input("enter starting number: "))
# end = int(input("enter ending number: "))
# if end > start:
#     for i in range(start, end+1):
#         if i % 4 == 0:
#             print(i, "არის ოთხის ჯერადი")
# else:
#     print("starting number is needed to be smaller than the ending number")


start = int(input("enter starting number: "))
end = int(input("enter ending number: "))
sum = 0
if end > start:
    for i in range(start, end+1):
        if i % 2 == 0:
            sum += i
    print(sum)
else:
    print("starting number is needed to be smaller than the ending number")