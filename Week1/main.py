import Q7 as q7


def q1():
    print("Who broke my heart?")
    response = input()
    print(f"My first love, {response}, broke my heart for the first time.")
    print("And I was like baby, baby, baby, oh.")


def q2():
    print("Who sees me rolling (Cops, Wardens, Other)?")
    response = input()
    if response == "Cops":
        print("They see me rolling. They hating. They hoping they gonna catch me riding dirty!")
    elif response == "Wardens":
        print("My music's so loud. I'm swanging. They hoping they gonna catch me riding dirty!")
    else:
        print("Trying to catch me riding dirty!")


def q3():
    print("How many times should I break free?")
    number_of_time = int(input())
    print("I'm stronger than I've been before...")
    while number_of_time > 0:
        print(f"...{number_of_time}: this is the part when I break free")
        number_of_time = number_of_time - 1
    print("Cause I can't resist it no more!")


def explain(what, where):
    if (what == "Monster") and (where == "Bed"):
        print("I'm friends with the monster that's under my bed")
    elif (what == "Doctor") and (where == "Hospital"):
        print("You're trying to save me, stop holding your breath")
    else:
        print("You think I'm crazy, yeah, you think I'm crazy")


def q4():
    # The following are calls to the function for testing purposes
    explain("Monster", "Bed")
    explain("Doctor", "Hospital")
    explain("Stranger", "Street")


def q5():
    number_of_points = 0
    print("Let's find out how you sleep...")
    for count in range(1, 5):
        print("...Baby, how do you sleep when you lie to me?")
        response = input()
        if response == "Very well":
            number_of_points = number_of_points - 10
            print("I'm hopin' that my love will keep you up tonight.")
        elif response == "Poorly":
            number_of_points = number_of_points + 20
            print("All that fear and all that pressure.")
        else:
            print("Love to you is just a game.")
    print(f"You achieved {number_of_points} points.")


def describe_friend(friend):
    if friend == "50 Cent":
        return "He be getting rich or die trying."
    elif friend == "Dr Dre":
        return "He be needing California love."
    elif friend == "Rihanna":
        return "She be needing an umbrella."
    else:
        return "They be cool."


def display_friend(friend):
    print(f"The {friend} can be described as follows:")
    print(describe_friend(friend))


def run():
    print("Enter a friend: ")
    friend = input()
    print("Enter the word [describe/display]: ")
    response = input()
    if response == "describe":
        print(describe_friend(friend))
    elif response == "display":
        display_friend(friend)
    else:
        print("Invalid command")


def q6():
    # describe_friend()
    # display_friend()
    run()


# Call function
# q1()
# q2()
# q3()
# q4()
# q5()
# q6()
q7.question7()
