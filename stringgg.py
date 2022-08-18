word="garry"
x=[]
for w in word:
    if w not in x:
        x.append(w)
    else:
        print(f"{w} is occuring more than once")