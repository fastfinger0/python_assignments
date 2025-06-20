input_sentence = input("Enter a sentence: ")

words = input_sentence.split()
reversed_words = words[::-1]
output_sentence = " ".join(reversed_words)

print(f"Output after reverse = \"{output_sentence}\"") 