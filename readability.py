
def count_sentences(text):
    sentences = 0

    for char in text:
        if char in ('!' , '?' , '.' ):
            sentences += 1

    return sentences

def count_word(text):
    return len(text.split())

def count_letters(text):
    letters = 0
    for char in text:
        if char.isalpha():
            letters += 1

    return letters

def main():

    text = input("Text: ")

    letters = count_letters(text)
    words = count_word(text)
    sentences = count_sentences(text)

    L = (letters/words) * 100
    S = (sentences/words) * 100
    index = .0588 * L - 0.296 * S - 15.8

    result = round(index)

    if result < 1:
        print("Before Grade 1" )

    elif result >= 16:
        print("Grade 16+")

    else:
        print("Grade" ,result)


if __name__ == "__main__":
    main()