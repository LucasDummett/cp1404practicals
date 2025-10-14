"""
Word Occurrences
Estimate: 30 Minutes
Actual: 40 Minutes
"""

word_to_count = {}
user_string = input("Please write a sentence: ").strip().split(" ")
for word in user_string:
    word_to_count[word] = word_to_count.get(word, 0) + 1
words_and_counts = sorted(word_to_count.items())

max_length_word = max(len(word) for word, count in words_and_counts)

for word, count in words_and_counts:
    print(f"{word:{max_length_word}} : {count}")


