import hashlib
import json
import sys

def make_table(passlist, option):
    hashdic = {}
    for word in passlist:
        word = word.rstrip('\n')
        if option == "1":
            hashedpass = hashlib.md5(word.encode('utf-8')).hexdigest()
        elif option == "2":
            hashedpass = hashlib.sha1(word.encode('utf-8')).hexdigest()
        elif option == "3":
            hashedpass = hashlib.sha224(word.encode('utf-8')).hexdigest()
        elif option == "4":
            hashedpass = hashlib.sha256(word.encode('utf-8')).hexdigest()
        elif option == "5":
            hashedpass = hashlib.sha384(word.encode('utf-8')).hexdigest()
        elif option == "6":
            hashedpass = hashlib.sha512(word.encode('utf-8')).hexdigest()
        elif option == "7":
            hashedpass = hashlib.blake2b(word.encode('utf-8')).hexdigest()
        elif option == "8":
            hashedpass = hashlib.blake2s(word.encode('utf-8')).hexdigest()
        elif option == "9":
            hashedpass = hashlib.sha3_224(word.encode('utf-8')).hexdigest()
        elif option == "10":
            hashedpass = hashlib.sha3_256(word.encode('utf-8')).hexdigest()
        elif option == "11":
            hashedpass = hashlib.sha3_384(word.encode('utf-8')).hexdigest()
        elif option == "12":
            hashedpass = hashlib.sha3_512(word.encode('utf-8')).hexdigest()
        hashdic.update({hashedpass: word})
    return hashdic

def main():
    filename = input("Please enter password file:")
    passfile = open(filename, "r", errors='ignore')
    passlist = []
    for line in passfile:
        passlist.append(line.rstrip('\n'))
    print("What hash algorithm would you like to use: \n1 md5\n2 sha1\n"
          "3 sha224\n4 sha256\n5 sha384\n6 sha512\n7 blake2b\n8 blake2s\n"
          "9 sha3 224\n10 sha3 256\n11 sha3 384\n12 sha3 512")
    while True:
        option = input()
        if option == '1':
            hashlist = make_table(passlist, option)
            with open('md5.txt', 'w', ) as file:
                json.dump(hashlist, file)
            print("File saved in md5.txt")
            break
        elif option == '2':
            hashlist = make_table(passlist, option)
            with open('sha1.txt', 'w', ) as file:
                json.dump(hashlist, file)
            print("File saved in sha1.txt")
            break
        elif option == '3':
            hashlist = make_table(passlist, option)
            with open('sha224.txt', 'w', ) as file:
                json.dump(hashlist, file)
            print("File saved in sha224.txt")
            break
        elif option == '4':
            hashlist = make_table(passlist, option)
            with open('sha256.txt', 'w', ) as file:
                json.dump(hashlist, file)
            print("File saved in sha256.txt")
            break
        elif option == '5':
            hashlist = make_table(passlist, option)
            with open('sha384.txt', 'w', ) as file:
                json.dump(hashlist, file)
            print("File saved in sha384.txt")
            break
        elif option == '6':
            hashlist = make_table(passlist, option)
            with open('sha512.txt', 'w', ) as file:
                json.dump(hashlist, file)
            print("File saved in sha512.txt")
            break
        elif option == '7':
            hashlist = make_table(passlist, option)
            with open('blake2b.txt', 'w', ) as file:
                json.dump(hashlist, file)
            print("File saved in blake2b.txt")
            break
        elif option == '8':
            hashlist = make_table(passlist, option)
            with open('blake2s.txt', 'w', ) as file:
                json.dump(hashlist, file)
            print("File saved in blake2s.txt")
            break
        elif option == '9':
            hashlist = make_table(passlist, option)
            with open('sha3_224.txt', 'w', ) as file:
                json.dump(hashlist, file)
            print("File saved in sha3_224.txt")
            break
        elif option == '10':
            hashlist = make_table(passlist, option)
            with open('sha3_256.txt', 'w', ) as file:
                json.dump(hashlist, file)
            print("File saved in sha3_256.txt")
            break
        elif option == '11':
            hashlist = make_table(passlist, option)
            with open('sha3_384.txt', 'w', ) as file:
                json.dump(hashlist, file)
            print("File saved in sha3_384.txt")
            break
        elif option == '12':
            hashlist = make_table(passlist, option)
            with open('sha3_512.txt', 'w', ) as file:
                json.dump(hashlist, file)
            print("File saved in sha3_512.txt")
            break
        else:
            print("Please enter a valid option")
    sys.exit()

if __name__=="__main__":
    main()