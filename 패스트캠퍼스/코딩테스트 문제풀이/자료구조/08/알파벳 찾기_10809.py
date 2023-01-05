alphabet = input()
table = ["-1"] * (ord('z') - ord('a') + 1)
a = ord('a')
for i, alpha in enumerate(alphabet):
    if table[ord(alpha) % a] == "-1": table[ord(alpha) % a] = str(i)

print(" ".join(table))