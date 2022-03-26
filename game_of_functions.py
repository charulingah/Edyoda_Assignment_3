'''Write a Python function to sum all the numbers in a list.



Sample List : (8, 2, 3, 0, 7)

Expected Output : 20'''


#Solution


def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total
total = sum((8, 2, 3, 0, 7))
print(F"8+2+3+0+7 = {total}")
