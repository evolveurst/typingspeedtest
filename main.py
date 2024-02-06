import time
import random
import tkinter as tk

common_words = [
    "the", "be", "to", "of", "and", "a", "in", "that", "have", "I", "it", "for",
    "not", "on", "with", "he", "as", "you", "do", "at", "this", "but", "his", "by",
    "from", "they", "we", "say", "her", "she", "or", "an", "will", "my", "one",
    "all", "would", "there", "their", "what", "so", "up", "out", "if", "about",
    "who", "get", "which", "go", "me", "when", "make", "can", "like", "time",
    "no", "just", "him", "know", "take", "people", "into", "year", "your", "good",
    "some", "could", "them", "see", "other", "than", "then", "now", "look", "only",
    "come", "its", "over", "think", "also", "back", "after", "use", "two", "how",
    "our", "work", "first", "well", "way", "even", "new", "want", "because", "any",
    "these", "give", "day", "most", "us"
]
start_time = 0
words_to_type=""
def calculate_typing_speed(text, time_taken):
    words = len(text.split())
    minutes = time_taken / 60
    wpm = words / minutes
    return wpm

def test_typing_speed():
    def generate_words():
        randomword = random.sample(common_words, 10)
        global words_to_type
        strconverted = ''.join(randomword)
        words_to_type += strconverted
        sentence.config(text=" ".join(randomword))

    def finish_test():
        global words_to_type
        end_time = time.time()
        time_taken = end_time - start_time
        input_text = user_input.get('1.0', tk.END).strip()
        wpm = calculate_typing_speed(input_text, time_taken)

        result_label.config(text=f"Your typing speed: {wpm:.2f} WPM")

        generate_words()

    def check_input(event):
        typed_text = user_input.get('1.0', tk.END).replace(" ", "")
        if len(typed_text) > len(words_to_type):
            generate_words()



    def start_test():
        global start_time
        start_time = time.time()
        start_button.config(state=tk.DISABLED)
        user_input.config(state=tk.NORMAL)
        user_input.delete('1.0', tk.END)
        user_input.focus()
        user_input.bind("<KeyRelease>", check_input)
        window.after(60000, finish_test)

    window = tk.Tk()
    window.title("Typing Speed Test")

    instruction_label = tk.Label(window, text="Type the following words:")
    instruction_label.pack()

    sentence = tk.Label(window, text="")
    sentence.pack()

    user_input= tk.Text(window, height=5, width=30)
    user_input.pack()
    user_input.config(state=tk.DISABLED)

    start_button = tk.Button(window, text="Start", command=start_test)
    start_button.pack()

    result_label = tk.Label(window, text="")
    result_label.pack()

    generate_words()

    window.mainloop()

test_typing_speed()