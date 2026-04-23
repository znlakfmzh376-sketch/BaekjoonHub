import sys
input = sys.stdin.readline

vowels = ['a','e','i','o','u']

while True:
    s = input().strip()
    if s == 'end':
        break

    has_vowel = False
    vowel_streak = 0
    consonant_streak = 0
    flag = True

    for i in range(len(s)):
        if s[i] in vowels:
            has_vowel = True
            vowel_streak += 1
            consonant_streak = 0
        else:
            consonant_streak += 1
            vowel_streak = 0   # ← 수정

        if vowel_streak == 3 or consonant_streak == 3:
            flag = False

        if i > 0:
            if s[i] == s[i-1] and s[i] not in ['e','o']:
                flag = False

    if has_vowel and flag:
        print(f'<{s}> is acceptable.')
    else:
        print(f'<{s}> is not acceptable.')