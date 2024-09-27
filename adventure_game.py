# You can use this workspace to write and submit your adventure game project.
# Run the game by entering python3 adventure_game.py in the terminal
import time
import random


# a function that makes sleep after every print
def print_pause(message):
    print(message)
    time.sleep(2)


choices_list = [1, 2]
# validate numbers 1 or 2 in the user input


def response(answer):
    #print(type(answer))
     while True:
        try:
            answer = int(answer)
            if answer in choices_list:
                return answer
            else:
                answer = input("Please enter 1 or 2:")
        except ValueError:
            answer = input("Please enter 1 or 2:")
    
# increase score winning,and play again or exit


def winning(total_score):
    print_pause("You've got a score bonus!!!")
    total_score += 10
    print_pause(f"Your score now is{total_score}")
    print_pause("YOU have WON !!")
    answer = response(input("enter 1 to play again , or 2 to exit :"))
    if answer == 1:
        main()
    else:
        return

# decrease score and losing


def losing(total_score):
    total_score -= 5
    print_pause("Your score has been decreased!")
    print_pause(f"Your score now is{total_score}")
    print_pause("YOU have LOSED !!")
    answer = response(input("enter 1 to play again , or 2 to exit :"))
    if answer == 1:
        main()
    else:
        return


def main():

    wrong_list = ["presidency building", "rural village", "trekking"]
    right_list = ["beach", "sightseeing"]

    # the last level of the game fuction
    def place(total_score):
        right_random = random.choice(right_list)
        wrong_random = random.choice(wrong_list)
        question_random = [right_random, wrong_random]
        random.shuffle(question_random)

        print_pause(
            "Now ,you should choose where to go there or activities to do.")
        answer = response(input(
            f"To go to a {question_random[0]} enter 1"
            f",to go to a {question_random[1]} enter 2:"))

        if answer == 1:
            if question_random[0] in right_list:
                print_pause("Enjoyable!!!")
                print_pause(
                    "It's a good way to spend your time in another country.")
                total_score += 15
                winning(total_score)
            elif question_random[0] not in right_list:
                print_pause("It's not a good way to spend your time there.")
                losing(total_score)

        elif answer == 2:
            if question_random[1] in right_list:
                print_pause("Enjoyable!!!")
                print_pause(
                    "It's a good way to spend your time in another country.")
                total_score += 15
                winning(total_score)
            elif question_random[1] not in right_list:
                print_pause("It's not a good way to spend your time there.")
                losing(total_score)

    # second path function

    def countries2_path():
        total_score = 0
        quick_way = [countries1_path, place]
        the_way = random.choice(quick_way)
        if the_way == place:
            total_score += 5
            print_pause(f"Your score now is {total_score}")
            place(total_score)
        else:
            countries1_path()

    transports_list = ["your car", "plane", "ship"]
    random_transports = random.sample(transports_list, 2)
    first_way, second_way = random_transports
    # first path function

    def countries1_path():
        total_score = 0
        print_pause("Now..how do you want to go there..? ")
        answer = response(input(
            f"To go by {first_way} enter 1 , to go by {second_way} enter 2:"
        ))

        if answer == 1:
            if first_way == "ship":
                print_pause("Sorry, but it's a very slow transport .")
                losing(total_score)
            else:
                print_pause("Suitable and fast choise!!")
                total_score += 15
                print_pause(f"your score has been {total_score}")
                place(total_score)

        elif answer == 2:
            if second_way == "ship":
                print_pause("Sorry, but it's a very slow transport .")
                losing(total_score)
            else:
                print_pause("Suitable and fast choise!!")
                total_score += 15
                print_pause(f"your score has been {total_score}")
                place(total_score)

    print_pause("Welcome to the Travellers game!!")
    print_pause("You are going to travel..good right?!!")
    print_pause("Where do you prefer to go ?")
  #  variables for choosing a random country
    countries1 = ["Spain", "Italy", "Netherland", "Greek"]
    countries2 = ["Egypt", "USA", "Canada", "Russia"]
    random_country1 = random.choice(countries1)
    random_country2 = random.choice(countries2)
    random_countries = [random_country1, random_country2]

    answer = response(input(
        f"To go to {random_countries[0]} enter 1 ,To go to {random_countries[1]} enter 2:"
    ))

    # path number "1" a group of countries
    if answer == 1:
        print_pause("It's good for Summer, right ?!!")
        countries2_path()

    # path number "2" another group of countries
    elif answer == 2:
        print_pause("It's great for staying for a long time !!")
        countries1_path()


main()
