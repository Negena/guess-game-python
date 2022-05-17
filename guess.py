def guess(question,answer):
    total_guess = 3
    user = input(question)
    total_guess -=1
    while answer != user and total_guess != 0: 
        print(f"you have {total_guess} guesses left")
        user = input(question)
        total_guess -=1
    if total_guess == 0 :
        print("you run out of guesses , you losed")
    if answer == user : 
        print("you won")
        


guess("what is my name ?","nigina")
guess("my favourite fruit ?","kiwi")