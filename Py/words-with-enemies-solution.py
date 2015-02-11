left , right = raw_input().split()
for c in left + right:
    if c in left and c in right:
        left, right = left.replace(c, "", 1), right.replace(c, "", 1)
print(left, right)
print("Tie" if len(left)==len(right) else ("Left wins" if len(left)>len(right) else "Right wins"))
