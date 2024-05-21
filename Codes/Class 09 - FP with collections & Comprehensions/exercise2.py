def variance(alist):
    x_average = sum(alist)/len(alist)
    variance = sum(map(lambda x: (x - x_average)**2, alist))/len(alist)
    
    return round(variance, 3)