import random

for y in range(1000000):
    line = ''
    for x in range(80):
        line += chr(random.randint(32,126))
    print(line)
