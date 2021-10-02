import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
symbols = "[]{}()*;/,_-"

all = lower + upper + numbers + symbols

length = 8
password = "".join(random.sample(all,length))
print(password)