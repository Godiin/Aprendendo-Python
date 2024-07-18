def hello ():
    print('hello Worlds!')

hello()

def fazer_login(email, senha):
    print("bem vindo")
    print("usuario" + email)

fazer_login("tdi@tecnicasdeinvasao.com", "1234567")

def plus(n1, n2):
    return(n1 + n2) #under the return there is no life

resultado = plus(10, 10)
print(resultado)

def add_https(dominio):
    juntar = "https://" + dominio
    return juntar

print(add_https("tecnicasdeinvasao.com"))
print(add_https("ilhasnet.com.br"))