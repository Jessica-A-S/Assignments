def main():
    print("This program will calculate your sleep-debt over 5 days.")
    total_sleep = 0
    for count in range(1, 6):
        sleep_per_day = int(input("Please enter Day {} sleep: ".format(count)))
        total_sleep += sleep_per_day
    print("The total hours that you slept were: \n{} hours".format(total_sleep))
    recommended_hours = 40
    sleep_debt = recommended_hours - total_sleep
    print("Your sleep debt over this period of time is: \n{} hours".format(sleep_debt))
    if sleep_debt >= 1:
        print("You need more sleep!")
    else:
        print("You've had enough sleep. Lucky you!")


main()
