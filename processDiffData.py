

with open('kanjiDiff.txt', 'r', encoding='utf8') as f:
    kanjidata = eval(f.read())

with open('vocabDiff.txt', 'r', encoding='utf8') as f:
    vocabdata = eval(f.read())

kanjirating = {i: '' for i in range(101)}
vocabrating = {i: [] for i in range(101)}

for lvl in range(1, 61):
    lvldata = kanjidata[lvl]
    maxdiff = max(lvldata)[0]
    for diff, char in lvldata:
        percentage = round(diff / maxdiff * 100)
        kanjirating[percentage] += char
    lvldata = vocabdata[lvl]
    maxdiff = max(lvldata)[0]
    for diff, char in lvldata:
        percentage = round(diff / maxdiff * 100)
        vocabrating[percentage].append(char)

print(kanjirating)
print(vocabrating)