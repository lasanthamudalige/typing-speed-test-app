from tkinter import *
from time import sleep

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

    global time_label
    time_label = Label(text=f"Time  01:00", font="15", bg="grey")
    time_label.pack()

    paragraph = Label(text=words, font='15', bg="grey",
                      fg="white", wraplength=900)
    paragraph.pack(pady=10)

    global text
    text = Text(root, height=10, width=100)
    text.pack(pady=10)

    # text.insert("1.0", words)
    text["state"] = "disabled"

    start_btn = Button(text="Start", bd=0, command=start)
    start_btn.pack(pady=10)

    root.mainloop()


def start():
    time_left = 59

    text["state"] = "normal"

    while time_left >= 0:
        time_label.config(text=f"Time  00:{time_left:02d}")
        root.update()
        time_left -= 1
        sleep(1)

    text["state"] = "disabled"

    get_wpm()


def get_wpm():
    input_words = text.get("1.0", END)
    input_words = input_words.strip().split(" ")
    print(len(input_words))

    correct_words = 0
    for input_word, word in zip(input_words, words):
        if input_word == word:
            correct_words += 1


if __name__ == "__main__":
    main()
