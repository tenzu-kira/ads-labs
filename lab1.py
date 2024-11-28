string = input()
flag = 0
lifo = []
brackets = {
    "(": ")",
    "{": "}",
    "[": "]"
}
for i in range(len(string)):
    if string[i] in [")", "]", "}"]:
        try:
            if string[i] == lifo[-1]:
                lifo.pop()
                continue
            else:
                flag = 1
                break
        except IndexError:
            flag = 1
            break
    try:
        lifo.append(brackets[string[i]])
    except KeyError:
        print("string shouldnt contain non-brackets")
        flag = 1
        break
if (lifo != []) or flag:
    print("wrong string")
else:
    print("all good")
print(brackets.get("a"))