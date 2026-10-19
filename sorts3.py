n = int(input())
films = []
voices = []
index = {}

for _ in range(n):
    name = input()
    if name in index:
        voices[index[name]] += 1
    else:   
        index[name] = len(films)
        films.append(name)
        voices.append(1)
data = []
for i in range(len(films)):
    data.append([films[i], voices[i]])
print(data)