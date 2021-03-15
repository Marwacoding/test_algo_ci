def average_length():
    sentence = input("Please type your sentence")
    words = sentence.split()
    average = sum(len(word) for word in words) / len(words)
    print(average)

average_length()