'''Write a Python program to reverse a string.



Sample String : "1234abcd"

Expected Output : "dcba4321"

'''

#solution


st1 = "1234abcd"

st2 = ""

for i in st1:
    st2 = i + st2

#reversed
print(st2)
