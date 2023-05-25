<<<<<<< HEAD
def calc(a, b, c):
    if c == 'soma' or "+":
        return a + b
    elif c == 'subtração' or '-':
        return a - b
    elif c == 'divisão' or '/':
        return a / b
    elif c == 'produto' or '*':
        return a * b
m = int(input("Informe 2 valores:\n"))
n = int(input())
o = input("Agora informe a operação:\n")

=======
def calc(a, b, c):
    if c == 'soma' or "+":
        return a + b
    elif c == 'subtração' or '-':
        return a - b
    elif c == 'divisão' or '/':
        return a / b
    elif c == 'produto' or '*':
        return a * b
m = int(input("Informe 2 valores:\n"))
n = int(input())
o = input("Agora informe a operação:\n")

>>>>>>> c6ba8be6982ee07369fbc0eac5147651905c539d
print(calc(m, n, o))