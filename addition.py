def Xor(x,y):
    if x==y:
        return 0
    else:
        return 1 

def Or(*bits):
    for bit in bits:
        if bit == 1:
            return 1
    return 0
def And(*bits):
    for bit in bits:
        if bit == 0:
            return 0
    return 1

def calcSum(a, b, c):
    return Xor(a, Xor(b,c))

def calcCarry(a, b, c):
    return (Or(And(a,b), And(b, c), And(a,c)))
    
def returnSum(num_one, num_two):
    n = len(num_one) if len(num_one) > len(num_two) else len(num_two)

    if len(num_one)<len(num_two):
        num_one = num_one.zfill(n)
    else: 
        num_two = num_two.zfill(n)
    sum = ""
    carry = 0
    for i in range(n-1, -1, -1):
        sum = str(calcSum(int(num_one[i]), int(num_two[i]), carry)) + sum
        carry = calcCarry(int(num_one[i]), int(num_two[i]), carry)
    # if carry == 1:
    #     return "1"+sum
    return (sum, carry)


if __name__ == "__main__":
    input1 = input("Enter the first unsigned binary number ")
    input2 = input("Enter the second unsigned binary number ")
    result = returnSum(input1, input2)
    print(result[0], result[1])
    # print(type(result[0]), type(result[1]))
    # print(result[1]=="1")