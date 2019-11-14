from random import randint, shuffle
from os import system, rename, remove, getcwd
from time import sleep
from getpass import getpass
from Crypto.Cipher import AES
from hashlib import sha256, md5
from pickle import loads, dumps
import shutil
import gzip
import anydbm

system("title PASSTORE")
dat = anydbm.open("main.db", "c")
system("attrib +s +h main.db")
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
sim = ['`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-',
       '+', '=', '{', '[', '}', ']', '|', '\\', ';', ':', '"', "'", '<', ',', ".", "<", '>', '/', '?']
alphabet_capital = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
                    'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def password():
    passwords = ""
    for a in range(randint(1, 5)):
        passwords = passwords + (alphabet[randint(0, len(alphabet) - 1)])
    for b in range(randint(1, 5)):
        passwords = passwords + str((str(num[randint(0, len(num) - 1)])))
    for c in range(randint(1, 5)):
        passwords = passwords + (sim[randint(0, len(sim) - 1)])
    for d in range(randint(1, 5)):
        passwords = passwords + (alphabet_capital[randint(0, len(alphabet_capital) - 1)])
    new_passwords = list(passwords)
    for e in range(randint(1, 5)):
        shuffle(new_passwords)
    passwords = "".join(new_passwords)
    return passwords


def encrypted(key5, enc):
    key5 = sha256(key5).digest()
    iv = md5(password()).digest()
    encrypts = AES.new(key5, AES.MODE_CBC, IV=iv)
    while len(enc) % 16 != 0:
        enc = enc + "\n"
    pickle = [encrypts.encrypt(enc), iv]
    return dumps(pickle)


def decrypted(key6, dec, what):
    key2 = sha256(key6).digest()
    pickled = dat[what]
    iv = loads(pickled)
    encrypts = AES.new(key2, AES.MODE_CBC, IV=iv[1])
    while len(dec) % 16 != 0:
        dec = dec + "\n"
    return encrypts.encrypt(dec)


def decrypts(key7, decal):
    decal1 = loads(decal)
    key7 = sha256(key7).digest()
    decrypter = AES.new(key7, AES.MODE_CBC, IV=decal1[1])
    word = decrypter.decrypt(decal1[0])
    list_word = list(word)
    while list_word[-1] == "\n":
        list_word.pop(-1)
    words = "".join(list_word)
    return words


if len(dat) == 0:
    while True:
        system("cls")
        master = getpass("Set your master password\n: ")
        key1 = getpass("Enter your encryption key\n: ")
        if len(master) < 8 or len(key1) < 8:
            system("cls")
            print "BOTH MASTER PASSWORD AND ENCRYPTION KEY SHOULD HAVE A MINIMUM OF 8 CHARACTERS\n"
            system("pause")
            continue
        key4 = getpass("Enter the same encryption key again\n: ")
        if key4 == key1:
            system("cls")
            if master == key4:
                print "ENTER A DIFFERENT MASTER PASSWORD AND ENCRYPTION KEY\n\n\n"
                system("pause")
                continue
            dat["master"] = dumps(encrypted(key4, master))
            dat.close()
            dat = anydbm.open("main.db", "c")
            forget = password()
            dat["forget"] = dumps(encrypted(key4, forget))
            print "Your forget code(code used when you forget your password) is\n: ", forget, "\n\n\n"
            print "IT IS USED TO RECOVER A FORGOTTEN PASSWORD\n"
            system("pause")
            break
        else:
            print "\n\nTHE KEYS YOU ENTERED ARE NOT THE SAME!!!\n\n"
            system("pause")


while True:
    system("cls")
    mannered = loads(dat["master"])
    forgotten = loads(dat["forget"])
    master = raw_input("Enter your master password, or forget code if you forgot your password\n: ")
    if master != "":
        keg = getpass("Enter your encryption key\n: ")
        mastered = decrypted(keg, master, "master")
        remembered = decrypted(keg, master, "forget")
        if remembered == forgotten[0]:
            while True:
                system("cls")
                master = getpass("Set your new master password\n: ")
                key1 = getpass("Enter your new encryption key\n: ")
                if len(master) < 8 or len(key1) < 8:
                    system("cls")
                    print "BOTH MASTER PASSWORD AND ENCRYPTION KEY SHOULD HAVE A MINIMUM OF 8 CHARACTERS\n"
                    system("pause")
                    continue
                key4 = getpass("Enter the same new encryption key again\n: ")
                if key4 == key1:
                    system("cls")
                    if master == key4:
                        print "ENTER A DIFFERENT MASTER PASSWORD AND ENCRYPTION KEY\n\n\n"
                        system("pause")
                        continue
                    dat["master"] = str(encrypted(key4, master))
                    dat.close()
                    dat = anydbm.open("main.db", "c")
                    forget = password()
                    dat["forget"] = str(encrypted(key4, forget))
                    print "Your forget code(code used when you forget your password) is\n:", forget, "\n\n\n"
                    print "IT IS USED TO RECOVER A FORGOTTEN PASSWORD\n"
                    system("pause")
                    break
                else:
                    print "\n\nTHE KEYS YOU ENTERED ARE NOT THE SAME!!!\n\n"
                    system("pause")
        elif mastered == mannered[0]:
            while True:
                dat = anydbm.open("main.db", "c")
                system("cls")
                inp = raw_input("Menu:\n1) Create a new password\n2) "
                                "View your passwords\n3) Remove a password\n"
                                "4) Change a password\n"
                                "5) Backup\n6) About\n7) Exit\n: ")
                if inp == "1":
                    system("cls")
                    master = getpass("Enter the master password\n: ")
                    mastered = decrypted(keg, master, "master")
                    if mastered == mannered[0]:
                        system("cls")
                        print "Enter the name of the account you want to set a password for"
                        name = raw_input("or press enter to go back to the main menu\n: ")
                        if name != "":
                            system("cls")
                            get = input("Enter:\n1) Generate a password\n2) Enter a custom password\n: ")
                            name = name.upper()
                            if get == 1:
                                dat[name] = encrypted(keg, password())
                                dat.close()
                                print "\nYOUR NEW PASSWORD HAS BEEN ADDED!!\n\n"
                                system("pause")
                            elif get == 2:
                                system("cls")
                                news = getpass("Enter your password\n: ")
                                dat[name] = encrypted(keg, news)
                                dat.close()
                                print "\n\nYOUR PASSWORD HAS BEEN ADDED!!!\n\n"
                                system("pause")
                elif inp == "2":
                    system("cls")
                    master = getpass("Enter the master password\n: ")
                    mastered = decrypted(keg, master, "master")
                    if mastered == mannered[0]:
                        system("cls")
                        system("cls")
                        gen = raw_input("Enter:\n1) To view all passwords\n2)"
                                        " To view a specific password\n3) Back\n: ")
                        if gen == "1":
                            system("cls")
                            master = getpass("Enter the master password\n: ")
                            mastered = decrypted(keg, master, "master")
                            if mastered == mannered[0]:
                                system("cls")
                                if len(dat) > 1:
                                    for i in dat:
                                        if i != "master" and i != "forget":
                                            print i + ": " + decrypts(keg, dat[i])
                                        else:
                                            continue
                                else:
                                    print "NO SAVED PASSWORDS!!!"
                                print "\n\n"
                                system("pause")
                        elif gen == "2":
                            system("cls")
                            master = getpass("Enter the master password\n: ")
                            mastered = decrypted(keg, master, "master")
                            if mastered == mannered[0]:
                                system("cls")
                                if len(dat) == 1:
                                    print "NO SAVED PASSWORDS!!!"
                                else:
                                    che = raw_input("Enter the name of the account\n: ")
                                    che = che.upper()
                                    system("cls")
                                    if che not in dat:
                                        print "NO ACCOUNT WITH THIS NAME!!!\n\n"
                                        system("pause")
                                        if che in dat and che != "master" and che != "forget":
                                            print che + ": " + decrypts(keg, dat[che])
                                print "\n\n"
                                dat.close()
                                system("pause")
                elif inp == "3":
                    system("cls")
                    master = getpass("Enter the master password\n: ")
                    mastered = decrypted(keg, master, "master")
                    if mastered == mannered[0]:
                        system("cls")
                        iexp = raw_input("Enter the account you would like to remove\n: ")
                        iexp = iexp.upper()
                        if iexp in dat:
                            del dat[iexp]
                            print "\n\nTHE ACCOUNT HAS BEEN DELETED\n\n"
                            system("pause")
                            break
                        dat.close()
                elif inp == "4":
                    system("cls")
                    master = getpass("Enter the master password\n: ")
                    mastered = decrypted(keg, master, "master")
                    if mastered == mannered[0]:
                        system("cls")
                        iexp = raw_input("Enter the account you would like to change the password\n: ")
                        iexp = iexp.upper()
                        if iexp in dat:
                            old = getpass("Enter the old password\n: ")
                            if old == decrypts(keg, dat[iexp]):
                                dat[iexp] = encrypted(keg, password())
                                dat.close()
                                print "\n\nTHE PASSWORD HAS BEEN CHANGED!!!\n\n"
                                system("pause")
                elif inp == "5":
                    system("cls")
                    enter = input("1) Backup your passwords\n2) Open a backup file\n: ")
                    if enter == 1:
                        direct = raw_input("Enter the directory to save the backup to\n: ")
                        back = open("main.db", "rb")
                        backup = gzip.open("BACKUP", "wb")
                        shutil.copyfileobj(back, backup)
                        back.close()
                        backup.close()
                        shutil.move("BACKUP", direct)
                    elif enter == 2:
                        direct_in = raw_input("Enter the full directory of the backup file\n: ")
                        shutil.copy(direct_in, getcwd())
                        back_in = gzip.open("BACKUP", "rb")
                        back_out = open("main1.db", "wb")
                        shutil.copyfileobj(back_in, back_out)
                        back_in.close()
                        back_out.close()
                        dat.close()
                        remove("main.db")
                        remove("BACKUP")
                        rename("main1.db", "main.db")
                        system("attrib +s +h main.db")
                elif inp == "6":
                    system("cls")
                    print "PASSSTORE version 1.3.0"
                    sleep(1)
                    print "\nPROGRAMMED BY:\n-------------\nKAMIL MUKTAR\n\n"
                    print "SPECIAL THANKS TO:\n-------\"------\"--"
                    print "NADIA AHMED\nMUKTAR ABDURAHIM\nFAKIHA ABDURAHIM\nDR. ALIA IBRAHIM\n\n"
                    sleep(3)
                    print "THANKS TO:\n------\"--"
                    print "ELIAS AMHA\nROBEL GRMAY\nABINET TASSEW\n\n"
                    sleep(1)
                    system("pause")
                elif inp == "7":
                    dat.close()
                    exit(1)
                else:
                    system("cls")
                    print "\n\n ENTER A VALID CHOICE!!!"
            dat = anydbm.open("main.db", "c")
