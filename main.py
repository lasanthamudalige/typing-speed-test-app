from tkinter import *

# Declaring type testing paragraph
global words
words = "The Black Death was one of the most devastating pandemics in human history, resulting in the deaths of an " \
        "estimated 75 to 200 million people in Eurasia and peaking in Europe from 1346 to 1353. The bacterium " \
        "Yersinia pestis, resulting in several forms of plague, is believed to have been the cause. The plague " \
        "created a series of religious, social, and economic upheavals, which had profound effects on the course of " \
        "European history. The Black Death is thought to have originated in the dry plains of Central Asia, " \
        "where it then traveled along the Silk Road, reaching Crimea by 1343. From there, it was most likely carried " \
        "by Oriental rat fleas living on the black rats that were regular passengers on merchant ships, " \
        "spreading throughout the Mediterranean and Europe. The Black Death is estimated to have killed 30-60% of " \
        "Europe's total population. In total, the plague may have reduced the world population from an estimated 450 " \
        "million down to 350-375 million in the 14th century. The world population as a whole did not recover to " \
        "pre-plague levels until the 17th century. The plague recurred as outbreaks in Europe until the 19th century. "

root = Tk()


def main():
    root.title("Typing speed test")
    root.geometry("1000x600")
    root.configure(bg="grey")

    # Timer label
    global time_label
    time_label = Label(text="Time  00:60", font="15", bg="grey")
    time_label.pack()

    # Paragraph label
    paragraph = Label(text=words, font='15', bg="grey",
                      fg="white", wraplength=900)
    paragraph.pack(pady=10)

    # input text
    global text
    text = Text(root, height=10, width=100)
    text.pack(pady=10)

    # disabling text until user press start
    text["state"] = "disabled"

    # start button
    start_btn = Button(text="Start", bd=0, command=start)
    start_btn.pack(pady=10)

    root.mainloop()


# When user press start button countdown start from 60 seconds
def start():
    time_left = 60

    # Set test to normal for user to type words
    text["state"] = "normal"

    count_down(60)


def count_down(time_left):
    # Updating time label with the time left
    time_label.config(text=f"Time  00:{time_left:02d}")
    root.update()

    # If time is greater than 0 call the countdown function and reduce 1 from time_left
    if time_left > 0:
        root.after(1000, count_down, time_left - 1)
    #  If time is equal to 0 disable text to stop user from entering words
    else:
        text["state"] = "disabled"
        get_wpm()


def get_wpm():
    # Get text user entered from start to end
    input_words = text.get("1.0", END)
    # Remove whitespace and split from spaces to separate words
    input_words = input_words.strip().split(" ")

    # Split the paragraph from spaces
    words_list = words.split(" ")

    correct_chars = 0
    correct_words = 0
    # Compare user's words and paragraph words
    for (input_word, word) in zip(input_words, words_list):
        if input_word == word:
            # Get correct words and correct letter amount
            correct_words += 1
            correct_chars += len(input_word)

    # Show how many words and chars user entered correctly
    time_label.config(text=f"{correct_chars} CPM ({correct_words} WPM)")


if __name__ == "__main__":
    main()
