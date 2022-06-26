from addition import returnSum
multiplicand, multiplier = "101", "100"
multiplicand_length, multiplier_length = len(multiplicand), len(multiplier)
n = multiplicand_length if multiplicand_length > multiplier_length else multiplier_length
a = ""
a = a.zfill(multiplicand_length)

def shiftBitRight(binnum):
    return "0"+binnum

for i in range(multiplier_length-1, -1, -1):
    # print("hello")
    if multiplier[i] == "0":
        a = shiftBitRight(a)
        # print("a = ",a)
    elif multiplier[i] == "1":
        result = returnSum(a, multiplicand.ljust(len(a), "0"))
        a = result[0]
        if result[1] == 1:  #if carry == 1
            a = "1" + a
        a = shiftBitRight(a)
        
    else:
        print("invalid input")
        exit

print(a)
# print(a=="01000011101111000")