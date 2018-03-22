txt = input("Sisesta lause: ")
reverse = ""

i = len(txt) - 1
while i >= 0:
    reverse += txt[i]
    i -= 1

print(reverse)
