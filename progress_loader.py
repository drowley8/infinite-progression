import random

def gen3():
    three = ''
    for i in range(3):
        three += chr(random.randint(97,122))
    return three

def main():
    f_o = open("load_file", 'w+')
    hexi = ''
    for i in range(0,16):
        for j in range(0,16):
            num_let = random.randint(0,1)
            if num_let is 1:
                hexi += chr(random.randint(48,57))
            else:
                hexi += chr(random.randint(65,70))
        f_o.write(f"{hexi}\n")
        hexi = ''
    f_o.close()
    f_i = open("load_file", 'r+')
    for line in f_i:
        print(f"{line.split()[0]}.{gen3()}")
    f_i.close()

if __name__ == "__main__":
    main()
