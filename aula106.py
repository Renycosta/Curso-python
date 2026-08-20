# try, except, else e finally
try:
    print("Abrir arquivo")
except ZeroDivisionError as error:
    print(error.__class__.__name__)
    print(error)
    print("Dividiu por zero")
except IndexError as error:
    print("IndexError")
except (NameError, ImportError):
    print("NameError, ImportError")
else:
    print("Não deu erro")
finally:
    print("Fechar arquivo")