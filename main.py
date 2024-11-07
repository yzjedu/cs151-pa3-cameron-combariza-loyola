

#Purpose: creates a circle using *
#Parameters: none
#Return: none
def ASCII_circle():
    print("\n     ****\n    *      *\n   *        *\n   *        *\n    *      *\n      ****")



#Purpose: creates a set of lines using *
#Parameters: none
#Return: none
def ASCII_lines():
    print("\n    |     |     |\n    |     |     |\n    |     |     |")

#Purpose: creates an emoji using *
#Parameters: none
#Return: none

def ASCII_emoji():
    print("\n ¯\_(ツ)_/¯ ")


#Purpose: creates a ??? using *
#Parameters: none
#Return: none
def ASCII_word():
    print("\n*******   ***  ***   ******   ********  ***  ***  ***  ***  ***\n********  ***  ***  ********  ********  **** ***  ***  ***  ***\n***  ***  ***  ***  ***  ***  ***       ********  ***  ***  ***\n***  ***  ***  ***  ***  ***  ***       ********  ***  ***  ***\n*******   ********  ***  ***  ******    *** ****  ***   ****** \n******    ********  ***  ***  ******    ***  ***  ***    ****  \n***       ***  ***  ***  ***  ***       ***  ***  ***  ***  ***\n***       ***  ***  ***  ***  ***       ***  ***  ***  ***  ***\n***       ***  ***  ********  ********  ***  ***  ***  ***  ***\n***       ***  ***   ******   ********  ***  ***  ***  ***  ***")


# Purpose: creates a batman symbol using *
# Parameters: none
# Return: none

def ASCII_batman():
    print("\n                   ***********************\n               *********************************\n           *******   *     *       *    *    *******\n        *******   ***      **     **     ***   *******\n      ******   *****       *********      *****    *****\n    ******  ********       *********       ******    *****\n   ****   **********       *********       *********   *****\n  ****  **************    ***********     ************   ****\n ****  *************************************************  ****\n****  ***************************************************  ****\n****  ****************************************************  ****\n****  ****************************************************  ****\n ****  ***************************************************  ****\n  ****  *******     ****  ***********  ****     *********  ****\n   ****   *****      *      *******      *      ********  ****\n    *****   ****             *****             ******   *****\n      *****   **              ***              **    ******\n       ******   *              *              *   *******\n         *******                                *******\n            ********                         *******\n               *********************************\n                    ***********************")
#found from https://www.asciiart.eu/comics/batman, author did not name themselves posted to this ascii art

#Purpose: call functions
#Parameters: none
#Return: none

def main():
    while True:
        print("\nPlease choose an option:")
        print("1. Output a circle, 2. set of lines, 3. an emoji, 4. a word, 5. batman symbol 6. exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            ASCII_circle()
        elif choice == '2':
            ASCII_lines()
        elif choice == '3':
            ASCII_emoji()
        elif choice == '4':
            ASCII_word()
        elif choice == '5':
            ASCII_batman()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please select a number between 1 and 4.")