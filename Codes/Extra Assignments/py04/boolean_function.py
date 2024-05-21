def validate(grade):
    return ((type(grade) == float or type(grade) == int) and grade >= 0 and grade <= 100)