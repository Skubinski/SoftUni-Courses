count_of_numbers = int(input())
even = []
odd = []
positive = []
negative = []
for numbers in range(count_of_numbers):
    number = int(input())
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)
    if number >= 0:
        positive.append(number)
    else:
        negative.append(number)
type_of_numbers = input()
if type_of_numbers == "even":
    print(even)
elif type_of_numbers == "odd":
    print(odd)
elif type_of_numbers == "positive":
    print(positive)
elif type_of_numbers == "negative":
    print(negative)