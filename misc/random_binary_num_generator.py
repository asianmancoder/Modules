def get_randint():
    
    num = random.randint(0, 1)

    return num
 
def generate_bin_num(n):
    s = ""
 
    for i in range(n):
        x = findRandom()
        s += str(x)

    print(s)
