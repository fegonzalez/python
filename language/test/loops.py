

# while with 'else' clause

words=['cat', 'dog', 'window', "owe"]
w_index=0
w = words[w_index]
while len(w)<4:
    if w_index > len(words):
        break;
    w = words[w_index]
    print("words[", w_index, "] = ", words[w_index])
    w_index+=1
else:
        print(words[w_index], "out of range")
