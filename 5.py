with open("text.txt", "r", encoding="utf-8") as f:
    words = f.read().splitlines()


input_word = input('Введите слово: ')


def prefix(s):
    v = [0] * len(s)
    for i in range(1, len(s)):
        k = v[i - 1]
        while k > 0 and s[k] != s[i]:
            k = v[k - 1]
        if s[k] == s[i]:
            k = k + 1
        v[i] = k
    return v


def kmp(s, t):
    # index = -1
    f = prefix(s)
    k = 0
    for i in range(len(t)):
        if k >= len(s):
            k - 1
            break
        while k > 0 and s[k] != t[i]:
            k = f[k - 1]
        if s[k] == t[i]:
            k = k + 1
        # if k == len(s):
            # index = i + 1 - len(s)
            # break
    return k


for i in words:
    prefix_x = kmp(i, input_word)
    if prefix_x and prefix_x < min(len(input_word), len(i)):
        print(input_word + i[prefix_x:])
