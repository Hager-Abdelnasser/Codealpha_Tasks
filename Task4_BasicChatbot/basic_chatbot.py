"""
CodeAlpha Internship - Task 4: Basic Chatbot
A simple rule-based chatbot with predefined replies.
Concepts: if-elif, functions, loops, input/output.
"""

from datetime import datetime


def get_response(user_input):
    """Return (reply, should_exit) based on the user's message."""
    text = user_input.strip().lower()

    if text in ("hello", "hi", "hey"):
        return "Hi!", False
    elif text in ("how are you", "how are you?"):
        return "I'm fine, thanks!", False
    elif text in ("what is your name", "what's your name", "your name"):
        return "I'm CodeBot, a simple rule-based chatbot.", False
    elif text in ("what can you do", "help"):
        return ("I can reply to: hello, how are you, what is your name, "
                "time, date, help, and bye."), False
    elif text == "time":
        return f"The time is {datetime.now().strftime('%H:%M')}.", False
    elif text == "date":
        return f"Today's date is {datetime.now().strftime('%Y-%m-%d')}.", False
    elif text in ("thanks", "thank you"):
        return "You're welcome!", False
    elif text in ("bye", "goodbye", "exit", "quit"):
        return "Goodbye!", True
    elif text == "":
        return "Please type something.", False
    else:
        return "Sorry, I didn't understand that. Type 'help' to see what I can do.", False


def main():
    print("=" * 40)
    print("   CodeBot - type 'bye' to exit")
    print("=" * 40)

    while True:
        user_input = input("You: ")
        reply, should_exit = get_response(user_input)
        print(f"Bot: {reply}")
        if should_exit:
            break


if __name__ == "__main__":
    main()
