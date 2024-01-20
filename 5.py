with open("text.txt", "r", encoding="utf-8") as f:
    words = f.read().splitlines()

input_word = input('Введите слово: ')

for word in words:
    for i in range(len(input_word) - 1, 1, -1):  # 1, len(input_word)
        if i + 1 <= len(word) and input_word.endswith(word[:i]):
            # print(i, input_word[i - 1:], word[:i])
            print(input_word + word[i:])
            break


