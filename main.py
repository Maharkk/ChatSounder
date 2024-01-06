import pyttsx3

if __name__ == '__main__':
    # An improved and engaging welcome message
    print("Welcome to ChatSounder 2.0!")
    print("Let your words come to life with our text-to-speech magic.")
    print("Created by Mahar.")

    engine = pyttsx3.init()

    while True:
        # Prompt the user to enter text to be spoken
        user_input = input("Enter your message (type 'q' to quit): ")

        # Check if the user wants to quit by entering 'q'
        if user_input.lower() == "q":
            engine.say("Goodbye, friend! Thanks for using ChatSounder.")
            engine.runAndWait()
            break

        # Speak the user's input
        engine.say(user_input)
        engine.runAndWait()
