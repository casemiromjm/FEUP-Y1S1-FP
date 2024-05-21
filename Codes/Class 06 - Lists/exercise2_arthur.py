def mastermind(guesses, codes):
    x = 0
    y = 0
    for i in range(len(guesses)):
          if (guesses[i]==codes[i]):
            x+=1
            codes[i]="2"
    for i in range(len(guesses)):
        for a in range(3):
            if (codes[a]==guesses[i]):
                y+=1
                codes[a]="2"
                break

    return (x,y)