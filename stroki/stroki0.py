text = '''хакеры, слили, в, сеть, данные, пакистанской,
          энергетической, компании, k-Electric'''

d = text.split()
r = len(d)

for g in range(r // 2):
    print(d[g].upper(), end = '')
s = r - r // 2
while s < r:
    print(d[s].lower(), end = '')
    s += 1   