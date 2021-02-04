import Q7 as q7

def Q1():
    print("Who broke my heart?")
    response = input()
    print(f"My first love, {response}, broke my heart for the first time.")
    print("And I was like baby, baby, baby, oh.")

def Q2():
    print("Who sees me rolling (Cops, Wardens, Other)?")
    response = input()
    if (response == "Cops"):
        print ("They see me rolling. They hating. They hoping they gonna catch me riding dirty!")
    elif (response == "Wardens"):
        print("My music's so loud. I'm swanging. They hoping they gonna catch me riding dirty!")
    else:
        print("Trying to catch me riding dirty!")

def Q3():
    print ("How many times should I break free?")
    numberoftime = int(input())
    print("I'm stronger than I've been before...")
    while (numberoftime > 0):
        print(f"...{numberoftime}: this is the part when I break free")
        numberoftime=numberoftime-1
    print("Cause I can't resist it no more!")

def explain(what, where):
    if ((what=="Monster")and(where =="Bed")):
        print("I'm friends with the monster that's under my bed")
    elif ((what=="Doctor")and(where =="Hospital")):
        print("You're trying to save me, stop holding your breath")
    else:
        print("You think I'm crazy, yeah, you think I'm crazy")

def Q4():
    #The following are calls to the function for testing purposes
    explain("Monster", "Bed")
    explain("Doctor", "Hospital")
    explain("Stranger", "Street")

def Q5():
    numberOfpoints=0
    print("Let's find out how you sleep...")
    for count in range(1,5):
        print("...Baby, how do you sleep when you lie to me?")
        response = input()
        if (response == "Very well"):
            numberOfpoints = numberOfpoints -10
            print("I'm hopin' that my love will keep you up tonight.")
        elif (response == "Poorly"):
            numberOfpoints = numberOfpoints + 20
            print("All that fear and all that pressure.")
        else:
            print("Love to you is just a game.")
    print(f"You achieved {numberOfpoints} points.")

def describe_friend(friend):
    if (friend == "50 Cent"):
        return ("He be getting rich or die trying.")
    elif (friend == "Dr Dre"):
        return ("He be needing California love.")
    elif (friend == "Rihanna"):
        return ("She be needing an umbrella.")
    else:
        return ("They be cool.")

def display_friend(friend):
    print(f"The {friend} can be described as follows:")
    print (describe_friend(friend))


def run():
    print("Enter a friend: ")
    friend = input()
    print("Enter the word [describe/display]: ")
    response = input()
    if (response == "describe"):
        print (describe_friend(friend))
    elif (response == "display"):
        display_friend(friend)
    else:
        print("Invalid command")


def Q6():
    #describe_friend()
    #display_friend()
    run()

#Call function
#Q1()
#Q2()
#Q3()
#Q4()
#Q5()
#Q6()
q7.Q7()