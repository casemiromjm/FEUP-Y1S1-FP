#it is not working 100%

global_carry = 0

def string_sum(num1, num2):
    global global_carry
    num_sum = ""

    num1_reversed = num1[::-1]
    num2_reversed = num2[::-1]
    num_paired = zip(num1_reversed, num2_reversed)

    if global_carry != 0:
        carry = global_carry
    else:
        carry = 0
    for pair in num_paired:
        result = str((int(pair[0]) + int(pair[1]) + carry) % 10)
        carry = (int(pair[0]) + int(pair[1]) + carry) // 10
        num_sum =  result + num_sum
        global_carry = carry
    return num_sum

def add(num1, num2):
    int_num1, float_num1 = num1.split(".")
    int_num2, float_num2 = num2.split(".")

    if len(int_num1) != len(int_num2):
        if len(int_num1) > len(int_num2):
            while len(int_num1) != len(int_num2):
                int_num2 = "0" + int_num2
        if len(int_num2) > len(int_num1):
            while len(int_num1) != len(int_num2):
                int_num1 = "0" + int_num1
    if len(float_num1) != len(float_num2):
        if len(float_num1) > len(float_num2):
            while len(float_num1) != len(float_num2):
                float_num2 = float_num2 + "0"
        if len(float_num2) > len(float_num1):
            while len(float_num1) != len(float_num2):
                float_num1 = float_num1 + "0"

    #first sum the floats, then the int
    sum_float = string_sum(float_num1, float_num2)
    sum_int = string_sum(int_num1, int_num2)

    if sum_float[0] == 0:
        sum_float = sum_float[1:]
    if sum_float[len(sum_float) -1] == 0:
        sum_float = sum_float[:len(sum_float) -2]

    if sum_int[0] == 0:
        sum_int = sum_int[1:]
    if sum_int[len(sum_int) -1] == 0:
        sum_int = sum_int[:len(sum_int) -2]

    return f"{sum_int}.{sum_float}"