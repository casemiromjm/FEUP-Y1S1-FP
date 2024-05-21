def academy_awards(alist):
    quantity_awards = {}
    
    for cat, film in alist:
        quantity_awards[film] = 0

    for cat, film in alist:
        if film in quantity_awards.keys():
            quantity_awards[film] += 1
    
    return quantity_awards