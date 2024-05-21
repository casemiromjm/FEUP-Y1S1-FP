def mastermind(guesses, codes):
    correctPosition = 0
    correctColor = 0
    for i in range(len(guesses)):
        if guesses[i] == codes[i]:
            correctPosition += 1
            codes[i] = "CORRECT POSITION"
    for i in range(len(guesses)):
        for j in range(len(guesses)):    
            if codes[j] == guesses[i]:
                correctColor += 1
                codes[j] = "CORRECT COLOR"
                break

    return (correctPosition, correctColor)