while True:
    word= input ("what do you think Grandma likes?")
    if len(word) < 5:
        print(f"Grandma doesn't like {word}!")
    else:
        print(f"Grandma likes {word}")

    print("")