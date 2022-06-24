from addition import returnSum

input1 = input("Enter the first unsigned binary number ")
input2 = input("Enter the second unsigned binary number ")

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


twos_complement_2 = twosComplement(input2)
result = returnSum(input1, twos_complement_2)
if result[1] == 1: #if the difference is positive
    difference = result[0]
    print("The difference is positive and is equal to",difference)
else:
    difference = twosComplement(result[0])
    print("The difference is negative and is equal to", difference)