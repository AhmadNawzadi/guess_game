import random


if __name__ == "__main__":

    easy_attempts = 10
    hard_attempts = 5


    def start_game():
        print("Welcome to the Number Guess Game!")
        print("I am thinking of a number between 1 and 100.")
        random_choice = random.randint(1, 100)
        print(f"RANDOM NUMBER IS : {random_choice}")
 
        difficulty_level = input("Choose the difficulty level. 1 for easy and 2 for hard! : ")
        if difficulty_level == '1':
            attempts = easy_attempts
            while attempts > 0:
                compare_numbers(attempts, random_choice)
                attempts -= 1
        else:
            attempts = hard_attempts
            while attempts > 0:
                compare_numbers(attempts, random_choice)
                attempts -= 1


    def compare_numbers(attempts, random_choice):
        print(f"You have {attempts} remaining to find the number.")
        user_guess = int(input("Guess a number: "))
        if user_guess == random_choice:
            print("Wow! you have guessed the number correctly!")
            exit()
        elif attempts == 1:
            print("Youl lose! You have no more chance!")
        elif user_guess > random_choice and attempts > 0:
            print("Too high!")
        elif user_guess < random_choice and attempts > 0:
            print("Too low!")
        else:
            print("YOU LOSE")
 

    start_game()
 