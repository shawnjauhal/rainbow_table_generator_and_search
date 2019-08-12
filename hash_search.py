import hashlib
import json
import sys

def hash_search(hash_pass, hashlist):
    run_hash = True
    while run_hash == True:
        password = hashlist.get(hash_pass)
        if password == None:
            print('Password is not found')
        else:
            print (password)
        run_again = input("Would you like to run again(Y/n)")
        if run_again.lower() == 'y':
            hash_pass = input(
                "Please enter the hash you would like to crack: ")
        elif run_again.lower() == 'n':
            sys.exit()

def main():
    print("What hash algorithm would you like to use: \n1 md5\n2 sha1\n"
          "3 sha224\n4 sha256\n5 sha384\n6 sha512\n7 blake2b\n8 blake2s\n"
          "9 sha3 224\n10 sha3 256\n11 sha3 384\n12 sha3 512")
    while True:
        option = input()
        if option == '1':
            with open('md5.txt') as json_file:
                hashlist = json.load(json_file)
            break
        elif option == '2':
            with open('sha1.txt') as json_file:
                hashlist = json.load(json_file)
            break
        elif option == '3':
            with open('sha224.txt') as json_file:
                hashlist = json.load(json_file)
            break
        elif option == '4':
            with open('sha256.txt') as json_file:
                hashlist = json.load(json_file)
            break
        elif option == '5':
            with open('sha384.txt') as json_file:
                hashlist = json.load(json_file)
            break
        elif option == '6':
            with open('sha512.txt') as json_file:
                hashlist = json.load(json_file)
            break
        elif option == '7':
            with open('blake2b.txt') as json_file:
                hashlist = json.load(json_file)
            break
        elif option == '8':
            with open('blake2s.txt') as json_file:
                hashlist = json.load(json_file)
            break
        elif option == '9':
            with open('sha3_224.txt') as json_file:
                hashlist = json.load(json_file)
            break
        elif option == '10':
            with open('sha3_256.txt') as json_file:
                hashlist = json.load(json_file)
            break
        elif option == '11':
            with open('sha3_384.txt') as json_file:
                hashlist = json.load(json_file)
            break
        elif option == '12':
            with open('sha3_512.txt') as json_file:
                hashlist = json.load(json_file)
            break
        else:
            print("Please enter a valid option")
    hash_pass = input("Please enter the hash you would like to crack: ")
    hash_search(hash_pass, hashlist)

if __name__ == "__main__":
    main()