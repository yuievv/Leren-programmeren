print('Geef een woord: ')
woord1 = input().strip()

print('Geef nog een woord: ')
woord2 = input().strip()

if len(woord1) > len(woord2):
    print('Woord 1 heeft meer letters dan woord 2')
elif len(woord1) < len(woord2):
    print('Woord 1 heeft minder letters dan woord 2')
else:
    print('Woord 1 heeft evenveel letters als woord 2')