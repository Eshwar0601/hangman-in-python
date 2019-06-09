import random



def funword():
    word = ["car",
    "bike",
    "hunting",
    "person",
    "computer",
    "mobile",
    "cycle",
    "wheel",
    "robot",
    "wood",
    "tree",
    "rainbow",
    "bubble",
    "backpack"]
    return random.choice(word)





def check(word,guesses,guess):
    status = '              '
    matches=0
    for letter in word:
        if letter in guesses:
            status += letter                 
        else:
            status += '*'
        if letter == guess:
            matches += 1
        
    if matches > 1:
        print("You found it, the word contains",matches," ",guess,)
    elif matches == 1:
        print("You found it, the word contains a", guess)
    else:
        print("the word does not have a letter  ",guess) 
        
    return status    




def main():
    guesses=[]
    word = funword()
    guessed = False
    print("it is a ",len(word),"letter word")
    #print(word)

    while not guessed:
        text= "guess it by typing a single letter or a {}-letters   ".format(len(word)) 
        guess = input(text)
        
        if guess in guesses:
            print("you have already guessed",guess,"try again")
        elif len(guess) == len(word):
            guesses.append(guess)
            guessed = True
            if guess == word:
                guessed = True
            else:
                print("sorry that is not  correct")
        elif len(guess) == 1:
            guesses.append(guess)
            result = check(word,guesses,guess) 
            if result == word:
                guessed = True
            else:
                print(result)
        else:
            print("invalied entry")

    print("You guessed it right the word is :",guessed)


        









main()



