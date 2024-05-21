LE = int(input())
RE = int(input())
PE = int(input())
TE = int(input())

def grade(LE, RE, PE, TE):
    final_grade = (LE + RE + 13 * PE + 5 * TE) / 100
    return final_grade

if (LE < 0 or LE > 100) or (RE < 0 or RE > 100) or (PE < 0 or PE > 100) or (TE < 0 or TE > 100):
    print("Input error")
elif PE < 40 or TE < 40:
    print("RFF")
else:
    final_grade = grade(LE, RE, PE, TE)
    final_grade = round(final_grade)
    print(final_grade)