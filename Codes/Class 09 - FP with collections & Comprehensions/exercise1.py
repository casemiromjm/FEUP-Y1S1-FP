#def pair_diff(pair):
#    return pair[1] - pair[0] 
# can be reduced to a lambda func

def differences(alist):
    zipped_list = list(zip(alist, alist[1:]))
    difference_list = list(map(lambda pair: pair[1] - pair[0], zipped_list))

    return difference_list