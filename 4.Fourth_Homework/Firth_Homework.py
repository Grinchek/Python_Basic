text = input("Enter your text: ")
reserverd_words = input("Enter reserved words(by space): ")
my_text = text.split()
for i in range(len(my_text)):
    if my_text[i] in reserverd_words:
        my_text[i] = my_text[i].upper()
for i in range(len(my_text)):
    print(my_text[i], end=" ")
