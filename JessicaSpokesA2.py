def main():
    TOTAL_HOLES = 0
    TOTAL_SHOT_NUM = 0
    SHOT_NUM = 0
    name = input("What is your name? \n")
    print("Welcome {}. \n\nLets play golf, CP1401 style!\n".format(name))
    par = int(input("Choose a par for this course (between 3-5 inclusive) \n"))
    while par not in range(3, 6):
        par = int(input("I'm sorry, you must choose a number between 3-5 inclusive. Please enter again. \n"))
    distance = int(input("How many meters to the hole (between 195-250 inclusive)? \n"))
    while distance not in range(195, 251):
        distance = int(input("Invalid distance.\nHow many meters to the hole (between 195-250 inclusive)? \n"))
    options = input("(I)nstructions \n(P)lay round \n(Q)uit \n").upper()
    options = check_options(options)
    while options != "Q":
        if options == "I":
            print("This is a simple golf game in which each hole is 230m game away with par 5. You are able to "
                  "\nchoose from 3 clubs, the Driver, Iron or Putter. The Driver will hit around 100m, the Iron around "
                  "\n30m and the Putter around 10m. The putter is best used very close to the hole. "
                  "\n\nFor each shot, you may use a driver, iron or a putter - each shot will vary in distance. "
                  "\nThe average distance each club can hit is:"
                  "\n\tDriver = 100m\n\tIron = 30m\n\tPutter = 10m")
            options = input("\nGolf!\n(I)nstructions \n(P)lay round \n(Q)uit \n").upper()
        elif options == "P":
            TOTAL_HOLES += 1
            run_play(distance, par, TOTAL_HOLES, TOTAL_SHOT_NUM, SHOT_NUM)
            options = input("Golf!\n(I)nstructions \n(P)lay round \n(Q)uit \n").upper()
    if options == "Q":
        print("Farewell and thanks for playing {}.".format(name))
        for rounds in (1, TOTAL_HOLES+1):
            print(get_final_score(SHOT_NUM, par, TOTAL_SHOT_NUM, rounds))


# get_final_score calculates and displays the final score
def get_final_score(SHOT_NUM, par, TOTAL_SHOT_NUM, rounds):
    if SHOT_NUM > par:
        shots_to_par = SHOT_NUM - par
        TOTAL_SHOT_NUM += SHOT_NUM
        print("Round {}: {} shots. {} over par.".format(rounds, SHOT_NUM, shots_to_par))
        return
    elif SHOT_NUM < par:
        shots_to_par = par - SHOT_NUM
        TOTAL_SHOT_NUM += SHOT_NUM
        print("Round {}: {} shots. {} under par.".format(rounds, SHOT_NUM, shots_to_par))
        return
    else:
        TOTAL_SHOT_NUM += SHOT_NUM
        print("Round {}: {} shots. On par.".format(rounds, SHOT_NUM))
        return


# check_options checks to see whether the option is the right letter of I, P, or Q.
def check_options(options):
    while options not in ["I", "P", "Q"]:
        print("Invalid menu choice.\n\nLet's play golf, CP1401 style!\n")
        options = input("(I)nstructions \n(P)lay round \n(Q)uit \n").upper()
        check_options(options)
    if options in ["I", "P", "Q"]:
        return options


# run_play starts and runs through the golf game.
def run_play(distance, par, TOTAL_HOLES, TOTAL_SHOT_NUM, SHOT_NUM):
    from random import randint
    print("This hole is a {:.0f}m par {}.\n".format(distance, par))
    while distance >= 1:
        print("You are {:.0f}m away from the hole, after {} shot /s.".format(distance, SHOT_NUM))
        random_num = randint(80, 121)
        club_selection = input("Club selection: press D for Driver, I for Iron, P for Putter.").lower()
        print("Choose club: {}".format(club_selection))
        while club_selection not in ("d", "i", "p"):
            print("\nInvalid club selection - air swing :(")
            print("You're shot went 0m.")
            SHOT_NUM += 1
            print("You are {:.0f}m away from the hole, after {} shot /s.".format(distance, SHOT_NUM))
            club_selection = input("Club selection: press D for Driver, I for Iron, P for Putter.").lower()
        if club_selection == "d":
            if distance > random_num:
                distance -= random_num
            else:
                distance = random_num - distance
            print("\nYour shot went {}m.".format(random_num))
            SHOT_NUM += 1
        elif club_selection == "i":
            iron = 30 * random_num / 100
            if distance > iron:
                distance = distance - iron
            else:
                distance = iron - distance
            print("\nYour shot went {:.0f}m.".format(iron))
            SHOT_NUM += 1
        else:
            if distance > 10:
                putter = 10 * random_num / 100
            else:
                putter = distance * random_num / 100
            if distance > putter:
                distance = distance - putter
            else:
                distance = putter - distance
            print("\nYour shot went {:.0f}m.".format(putter))
            SHOT_NUM += 1
    if SHOT_NUM > par:
        shots_to_par = SHOT_NUM - par
        TOTAL_SHOT_NUM += SHOT_NUM
        print("Clunk... After {} hits, the ball is in the hole! \nDisappointing. You are {} over par.".format
              (SHOT_NUM, shots_to_par))
        print("You're overall score is {} and you are {} over par after {} hole(s)."
              .format(TOTAL_SHOT_NUM, shots_to_par, TOTAL_HOLES))
        return
    elif SHOT_NUM == par:
        TOTAL_SHOT_NUM += SHOT_NUM
        print("Clunk... After {} hits, the ball is in the hole! And that's par.".format(SHOT_NUM))
        print("You're overall score is {} and you are on par after {} hole(s).".format(TOTAL_SHOT_NUM, TOTAL_HOLES))
        return
    else:
        shots_to_par = par - SHOT_NUM
        TOTAL_SHOT_NUM += SHOT_NUM
        print("Clunk... After {} hits, the ball is in the hole! \nCongratulations, you are {} under par"
              .format(SHOT_NUM, shots_to_par))
        print("You're overall score is {} and you are {} under par after {} hole(s)."
              .format(TOTAL_SHOT_NUM, shots_to_par, TOTAL_HOLES))
        return


main()
