print("TEXT ANALYZER TOOL")
print("-" * 20)
print("Enter a paragraph (press Enter on an empty line to finish):")

paragraph_lines = []

while True:
    line = input()
    if line == "":
        break
    paragraph_lines.append(line)

paragraph = " ".join(paragraph_lines)

print("\nParagraph captured successfully.\n")
clean_text = ""
for char in paragraph:
    if char.isalnum() or char.isspace():
        clean_text += char

clean_text = clean_text.lower()

print("Text cleaned successfully.\n")
stopwords = [
    "the", "is", "a", "an", "and", "or", "to", "of", "in",
    "on", "for", "with", "as", "by", "at", "from"
]

words = clean_text.split()

filtered_words = []
for word in words:
    if word not in stopwords:
        filtered_words.append(word)

print("Stopwords removed successfully.\n")
# Word count
total_words = len(filtered_words)

# Sentence count (using original paragraph)
sentence_count = 0
for char in paragraph:
    if char in ".!?":
        sentence_count += 1

if sentence_count == 0:
    sentence_count = 1  # to avoid division by zero

average_words_per_sentence = total_words / sentence_count

print("Text Statistics:")
print("Total Words:", total_words)
print("Total Sentences:", sentence_count)
print("Average Words per Sentence:", round(average_words_per_sentence, 2))
print()
from collections import Counter

word_frequency = Counter(filtered_words)

top_five_words = word_frequency.most_common(5)

print("Top 5 Most Frequent Words:")
for word, count in top_five_words:
    print(word, ":", count)

print()

file = open("analysis_result.txt", "w")

file.write("TEXT ANALYZER RESULTS\n")
file.write("---------------------\n\n")

file.write(f"Total Words: {total_words}\n")
file.write(f"Total Sentences: {sentence_count}\n")
file.write(f"Average Words per Sentence: {round(average_words_per_sentence, 2)}\n\n")

file.write("Top 5 Most Frequent Words:\n")
for word, count in top_five_words:
    file.write(f"{word} : {count}\n")

file.close()

print("Results exported successfully to analysis_result.txt")
