# Yingyi Mei
# Period 4
# January 19, 2024
# Magic 8-Ball

# Initialize
import random

possible_responses = ["For sure!", "No doubt about it!", "Maybe not...",
                      "Not in a million years...", "Indications says yes",
                      "Unable to determine at this time", "Hmm...not sure",
                      "Of course!", "Never", "Maybe next time?", "Yeah...absolutely not",
                      "Of course not...", "Probably not", "Yes!"]
previous_response = None
valid_response = True

# Main
print("Welcome to the Magic 8-Ball!")

# While Loop to allow user to ask questions until they do not want to
while True:
    question_asked = input("\nAsk a yes or no question, make sure it ends in a question mark!: ")

    # Check if the user input is a question
    if question_asked.endswith("?"):

        # While loop to choose new response was already generated in the last question
        current_response = random.choice(possible_responses)
        while current_response == previous_response:
            current_response = random.choice(possible_responses)
        print(current_response)
        previous_response = current_response

        # Check if the user still wants to ask a question with validation of input
        ask_another = input("Would you like to ask another question? Choose (y) or (n), (yes or no): ").lower()
        while valid_response:
            if ask_another == "no" or ask_another == "n":
                # To break the inner while loop if user does not want to ask again
                valid_response = False
            elif ask_another == "yes" or ask_another == "y":
                # To break the inner while loop, but will not break the outer loop
                break
            else:
                # Validate response
                print("That is not a valid response. Choose (y) or (n), (yes or no): ")
                ask_another = input("Would you like to ask another question?: ").lower()

        # To break the outer while loop if user does not wish to ask again
        if not valid_response:
            break

    else:
        print("That is not a question. Make sure it ends in a question mark!")
