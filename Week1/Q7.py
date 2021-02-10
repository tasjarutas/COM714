def question7():
    print("Enter a phrase: ")
    phrase = input()
    print("Choose the option")
    print("1. inside")
    print("2. left")
    print("3. right")
    print("4. grid")
    print("-------------------")
    choice = int(input())
    num_dashes = len(phrase) + 4
    if (choice == 1):
        print ("-"*num_dashes)
        print ("| {} |".format(phrase))
        print("-" * num_dashes)
    elif (choice == 2):
        print("{} {}".format(" "*len(phrase), "-"*num_dashes))
        print("{}|{}|".format(phrase, " "*num_dashes))
        print("{} {}".format(" "*len(phrase), "-"*num_dashes))
    elif (choice == 3):
        print("{}{}".format("-"*num_dashes," "*len(phrase)))
        print("|{}| {}".format(" "*num_dashes, phrase))
        print("{}{}".format("-"*num_dashes," "*len(phrase)))
    elif (choice == 4):
        n = 3
        print("-" *(num_dashes*n))
        for i in range(n):
            print("| {} |".format((phrase+' ')*n))
        print("-" *(num_dashes*n))
    # else:
    #     print ("Invalid Choice")
