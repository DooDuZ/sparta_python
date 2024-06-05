import sys
import re
from collections import defaultdict

sentences = []

lng = 0
status = 0
END = "EndOfText"
NOWORDS = "There is no such word."

answer = []


def count_word(s):
    word_count = defaultdict(int)

    case = []

    for line in s:
        if line == "":
            continue

        alpha = re.findall(r"\b\w+\b", line)

        for a in alpha:
            w = a.lower()
            word_count[w] = word_count[w] + 1

    for key in word_count.keys():
        if word_count[key] == lng and len(key) > 1:
            case.append(key)

    if not case:
        case.append(NOWORDS)

    case.sort()
    answer.append(case)


# 입력 받기
while True:
    try:
        if status == 0:
            lng = int(sys.stdin.readline())
            status = 1
            continue

        sentence = sys.stdin.readline().rstrip()

        if sentence == "xx":
            break

        if sentence == END:
            status = 0

            count_word(sentences)

            sentences.clear()

            continue

        sentences.append(sentence)

    except:
        break


for a in answer:
    print("\n".join(a))
    print()
