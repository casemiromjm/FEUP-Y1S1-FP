hours = int(input())
minutes = int(input())

def convert_hours():
    if hours > 12:
        hours_formatted = hours - 12
    elif hours == 0:
        hours_formatted = 12
    else:
        hours_formatted = hours
    return hours_formatted

def ampm_checker():
    if hours >= 12:
        return "pm"
    else:
        return "am"

hours_converted = convert_hours()
timeperiod = ampm_checker()

if hours not in range(0,24) or minutes not in range(0,60):
    print("INVALID DATE FORMAT")
elif minutes != 0:
    print(f"{hours_converted}:{minutes:02} {timeperiod}")
else:
    print(f"{hours_converted} {timeperiod}")