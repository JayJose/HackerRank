import string

strng = 'We promptly judged antique ivory buckles for the next prize'
strng = strng.replace(' ', '').lower()

az = string.ascii_lowercase

counts = {}
for a in az:
    counts[a] = 0

for val in strng:
    if val in counts:
        counts[val] = counts[val] + 1
    else:
        counts[val] = 1

if min((counts.values())) == 0:
    print('not pangram')
else:
    print('pangram')
