#ABHINAV REDDY PUTTA 202149167
#SOLUTION:
#Break attempt using cipher-unicode190 (¾) https://www.youtube.com/watch?v=Dlto1VQ5Fv4 

def to_binary(lst):
    result =[]
    for i in lst:
        result.append(bin(i)[2:])
    return result


def to_8bit(lst):
    result = []
    for i in lst:
        w = i[0:8]
        x = i[8:16]
        y = i[16:24]
        z = i[24:32]

        result.append(w)
        result.append(x)
        result.append(y)
        result.append(z)
    return result

def to_uni_code(lst):
    result = []
    for i in lst:
        result.append(int(i,2))
    return result

def cipher_break(lst):
    for i in range (0,256):
        text = ''
        for j in lst:
            text+= chr(i^j)
        print("Break attempt using cipher-unicode "+str(i)+"("+chr(i)+")",text)

def main():

    hash = [3603614414, 3448017297, 3385444752, 3352415178, 3420248976, 3721515921, 3386886877, 3598829699, 4208118481, 2414407563, 4173892254]

    binary_hash = to_binary(hash)

    char_hash = to_8bit(binary_hash)

    uni_hash = to_uni_code(char_hash)

    cipher_break(uni_hash)

if __name__ == "__main__":
    main()