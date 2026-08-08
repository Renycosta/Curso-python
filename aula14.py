a = "A"
b = "B"
c = 1.1
formato = "a={} b={} c={:.2f}".format(a, b, c)
formato2 = "a={0} a={0} a={0}".format(a, b, c)
formato3 = "a={nome1} b={nome2} c={nome3}".format(nome1=a, nome2=b, nome3=c)

print(formato)
print(formato2)
print(formato3)