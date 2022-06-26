from tokenize import Name
from unicodedata import name
from addition import returnSum


#input2 is to be subtracted from input 1

def twosComplement(binbits):
    ones_complement = ""
    twos_complement = ""
    for i in binbits:
        if i == "0":
            ones_complement +="1"
        else:
            ones_complement +="0"

    result = returnSum(ones_complement, "1")
    twos_complement = result[0]
    if result[1] == 1:
        twos_complement = "1"+result[0]
    return twos_complement

def returnDifference(first_no, second_no):
    len1 = len(first_no)
    len2 = len(second_no)
    maxlen = len1 if len1 > len2 else len2
    if len1 > len2:
        second_no = second_no.zfill(maxlen)
    elif len2> len1:
        first_no = first_no.zfill(maxlen)

    twos_complement_2 = twosComplement(second_no)
    # print("twos complement = ",twos_complement_2)
    result = returnSum(first_no, twos_complement_2)
    return result

if __name__ == "__main__":
    input1 = input("Enter the first unsigned binary number ")
    input2 = input("Enter the second unsigned binary number ")
    len1 = len(input1)
    len2 = len(input2)
    if len1 > len2:
        input2 = input2.zfill(len1)
    else:
        input1 = input1.zfill(len2)
    print("The difference of the given two numbers is",returnDifference(input1, input2)[0])
