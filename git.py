import os, random

current = 18
for y in range(4):
    for i in range(100):
        d = str(i) + 'days ago'
        rand = random.randrange(1, 12)
        with open('test.txt', 'a') as file:
            file.write(d + '\n')
        os.system('git add test.txt')
        os.system(f'git commit --date=" 20{current}-{str(rand)}-{d}" -m 1')
    current += 1
os.system('git push -u origin main -f')
