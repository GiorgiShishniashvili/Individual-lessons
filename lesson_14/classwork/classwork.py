# def count_vowels(string):
#     vowels = "aeiou"
#     count = 0
#     for char in string.lower():
#         if char in vowels:
#             count += 1
#     return count
# print(count_vowels(string=input("enter a word: ")))


# def find_max(user_list):
#     max = user_list[0]
#     for number in user_list:
#         if number > max:
#             max = number
#     return max
# print(find_max([10,44,61,24,7,9,41,32,1,2]))


def square_sum(user_list):
    sum = 0
    for num in user_list:
        sum += num*num
    return sum
print(square_sum([10,44,61,24,7,9,41,32,1,2]))