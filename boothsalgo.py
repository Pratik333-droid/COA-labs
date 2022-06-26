from addition import returnSum
from subtraction import returnDifference
def arithmeticShiftRight(ac, q):
    temp_ac, temp_q= "", ""
    temp_q0 = q[-1]
    temp_ac = ac[0]
    for i in range(len(ac)-1):
        temp_ac+= ac[i]
    
    temp_q = ac[-1]
    for i in range(len(q)-1):
        temp_q += q[i]


    return temp_ac, temp_q, temp_q0
    
def calculateProduct(multiplicand, multiplier):
    q = multiplier
    len1 = len(multiplicand)
    len2 = len (multiplier)
    maxlen = len1 if len1 > len2 else len2
    q = q.zfill(maxlen) if len1 > len2 else q
    multiplicand = multiplicand.zfill(maxlen) if len1 < len2 else multiplicand
    q0 = "0"
    ac = ""
    ac = ac.zfill(maxlen +1)
    # n = len(multiplier)
    for i in range(maxlen):
        test_string = q[-1] + q0
        if test_string == "11" or test_string == "00":
            ac, q, q0 = arithmeticShiftRight(ac, q)
        elif test_string == "01":
            ac = returnSum(ac, multiplicand)[0]
            ac, q, q0 = arithmeticShiftRight(ac, q)
        elif test_string == "10":
            ac = returnDifference(ac, multiplicand)[0]
            print (f" difference ac = {ac}, q = {q}, q0 = {q0}")
            ac, q, q0 = arithmeticShiftRight(ac, q)
        print (f"ac = {ac}, q = {q}, q0 = {q0}")
    
    return ac+q


if __name__ == "__main__":
    m = "0011"
    q = "1101" #twos complement representation
    result = calculateProduct(m, q)
    print("The product is", result)
    decimal = 0
    count = 0
    for i in range(len(result)-1, -1, -1):
        decimal += int(result[i])* (2**count)
        count+=1
    # print("The decimal value of the product is",decimal)
