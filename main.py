

#Purpose: creates a circle using *
#Parameters: none
#Return: none
def ascii_circle():
    print("\n      ****\n    *      *\n   *        *\n   *        *\n    *      *\n      ****")



#Purpose: creates a set of lines using *
#Parameters: none
#Return: none
def ascii_lines():
    print("\n*************\n*************\n*************")


#Purpose: creates a ??? using *
#Parameters: none
#Return: none
def ascii_word():
    print("\n*******   ***  ***   ******   ********  ***  ***  ***  ***  ***\n********  ***  ***  ********  ********  **** ***  ***  ***  ***\n***  ***  ***  ***  ***  ***  ***       ********  ***  ***  ***\n***  ***  ***  ***  ***  ***  ***       ********  ***  ***  ***\n*******   ********  ***  ***  ******    *** ****  ***   ****** \n******    ********  ***  ***  ******    ***  ***  ***    ****  \n***       ***  ***  ***  ***  ***       ***  ***  ***  ***  ***\n***       ***  ***  ***  ***  ***       ***  ***  ***  ***  ***\n***       ***  ***  ********  ********  ***  ***  ***  ***  ***\n***       ***  ***   ******   ********  ***  ***  ***  ***  ***")


# Purpose: creates a batman symbol using *
# Parameters: none
# Return: none

def ascii_batman():
    print("\n                   ***********************\n               *********************************\n           *******   *     *       *    *    *******\n        *******   ***      **     **     ***   *******\n      ******   *****       *********      *****    *****\n    ******  ********       *********       ******    *****\n   ****   **********       *********       *********   *****\n  ****  **************    ***********     ************   ****\n ****  *************************************************  ****\n****  ***************************************************  ****\n****  ****************************************************  ****\n****  ****************************************************  ****\n ****  ***************************************************  ****\n  ****  *******     ****  ***********  ****     *********  ****\n   ****   *****      *      *******      *      ********  ****\n    *****   ****             *****             ******   *****\n      *****   **              ***              **    ******\n       ******   *              *              *   *******\n         *******                                *******\n            ********                         *******\n               *********************************\n                    ***********************")
#found from https://www.asciiart.eu/comics/batman, author did not name themselves posted to this ascii art

#Purpose: call functions
#Parameters: none
#Return: none

def main():
    while True:
        print("\nPlease choose an option:")
        print("1. a circle \n2. set of lines \n3. Phoenix \n4. batman symbol \n5. exit")

        choice =input("Enter your choice (1-5): ")

        if choice == '1':
            ascii_circle()
        elif choice == '2':
            ascii_lines()
        elif choice == '3':
            ascii_word()
        elif choice == '4':
            ascii_batman()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("invalid input")

main()