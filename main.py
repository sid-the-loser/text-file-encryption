import pickle as pk
import random

ch = input("Encrypt or Decrypt (1 or 2): ")
filename = input("Choose the file (txt files only!): ")
random.seed(input("Enter the password: "))

if ch == "1": # Encrypt
    f = open(filename, "r")
    lst = []
    for i in f.read():
        lst.append(ord(i)+random.random())
    f1 = open(filename+".enc", "bw")
    pk.dump(lst, f1)
    f1.close()

elif ch == "2": # Decrypt
    f = open(filename, "br")
    lst = pk.load(f)
    f1 = open(filename+".dec", "w")
    for i in lst:
        char = round(i-random.random())
        f1.write(chr(char) if (char > 32  and char < 127) or char == 10 else (chr(32) if char <= 32 else chr(126)))
    f1.close()
