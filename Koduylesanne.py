f = open("floats.txt")

text=f.read()
lines=text.split()

i=0
sum=0                           
for line in lines:
    i+=1
    sum+=float(line)
print(sum/i)

f.close()


