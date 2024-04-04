chislo = input()
posl_chisel = input().split()
s = []
for i in posl_chisel:
    if i[0] == chislo:
        s.append(i)
print(s)
