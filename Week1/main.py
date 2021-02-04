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

#Call function
Q1()
Q2()