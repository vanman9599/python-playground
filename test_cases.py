sentence = input("Enter a sentence: ")
sentence_length = len(sentence)


file_name = input("Enter a file name ")
file_name = f"{file_name}"

with open(file_name, "w") as f:
    f.write(sentence)
    f.close()

print(f"You've written {sentence_length}  characters fo {file_name}")
