def add(num1,num2):

    p1 = num1.index(".")
    p2 = num2.index(".")
    
    if len(num1[p1+1:])>len(num2[p2+1:]):
        num2 += "0" * (len(num1[p1+1:])-len(num2[p2+1:]))
    elif len(num1[p1+1:])<len(num2[p2+1:]):
        num1 += "0" * (len(num2[p2+1:])-len(num1[p1+1:]))
    if len(num1[:p1])>len(num2[:p2]):
        num2 = "0" * (len(num1[:p1])-len(num2[:p2])) + num2
    elif len(num1[:p1])<len(num2[:p2]):
        num1 = "0" * (-len(num1[:p1])+len(num2[:p2])) + num1
    
    result=''
    carry = 0
    for i in range(len(num1)):
        i = len(num1) - i-1
        
        if num1[i] == '.':
            result = "." + result
        else:
            result = str((int(num1[i])+int(num2[i])+carry)%10) + result
            carry = ((int(num1[i])+int(num2[i])+carry)//10)
            
    if carry!=0:
        result = str(carry) + result
    
    #normalize
    for i in range(len(result)):
        if result[i] != "0" and result[i] != ".":
            reslef = result[i:]
            break
    for i in range(len(reslef)):
        i = len(reslef) - i-1
        if reslef[i] != "0" and reslef[i] != ".":
            res = reslef[:i+1]
            break
        
    
    
    return res
