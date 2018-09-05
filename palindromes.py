s = 'aaabbbb'

counts = {}
for c in s:
    if c not in counts:
        counts[c] = 1
    else:
        counts[c] = counts[c] + 1

evens, odds = 0, 0

for c in counts:
    if counts[c] % 2 == 0:
        evens = evens + 1
    else:
        odds = odds + 1

if odds <= 1 and evens >= 1:
    print(True)
else:
    print(False)
