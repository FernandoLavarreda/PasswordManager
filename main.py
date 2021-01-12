# Fernando Jose Lavarreda Urizar
# Main progam to generate password

import random as rd
import db_manipulation as mdb

def gen_password(length):
    """Generate a random password given a desired length"""
    chars = "abcdefghijklmnopqrstuvwxyz0123456789!?()\\/&%$#"
    pwd = ""
    for _ in range(length):
        esc = rd.choice([0, 1])
        rnd = rd.randint(0, len(chars))
        if esc == 1 and rnd <= 25:
            pwd+=chars[rnd].upper()
        else:
            pwd+=chars[rnd]
    return pwd


option = "n"
while option != "6":
    if mdb.viewOne("M4IN")[0] != "NULL" and mdb.viewOne("M4IN")[0] != "":
        master = input("Enter master password or Q to quit:\t")
        while master != mdb.viewOne("M4IN")[0] and master != "Q":
            master = input("Try again:\t")
        if master == "Q":
            break
        print("Password Manager:\n1. View all passwords\n2. Change Password\n3. Delete site\n4. Copy to clipboard\n5. Add new Site\n6. EXIT\n")
        option = input("Option:\t")
        print("\n")
        if option == "1":
            print(mdb.viewAll())

        elif option == "2":
            name = input("Name of the site:\t")
            rand = input("Random Password(Y/N)?\t").upper()
            if rand == "Y":
                size = input("Length of password: ")
                while not size.isdigit():
                    size = input("Length of password: ")
                pd = gen_password(int(size))
            else:
                pd = input("Enter the new password:\t")
            mdb.changePassword(name, pd)

        elif option == "3":
            name = input("Name of the site:\t")
            mdb.deleteWebsite(name)

        elif option == "4":
            number = input("Enter the number of the site to copy the password:\t")
            while not number.isdigit():
                number = input("Enter the number of the site to copy the password:\t")
            mdb.copyToClipboard(int(number))

        elif option == "5":
            site_name = input("Enter the name of the site:\t")
            rand = input("Random Password(Y/N)?\t").upper()
            if rand == "Y":
                size = input("Length of password: ")
                while not size.isdigit():
                    size = input("Length of password: ")
                pd = gen_password(int(size))
            else:
                pd = input("Enter the new password:\t")
            mdb.addWebsite(site_name, pd)

        elif option == "6":
            break

        else:
            print("Action not recognized\n")
    else:
        choice = input("Set a password for the manager or quit(Y/Q):\t").upper()
        if choice == "Y":
            master = input("Set up your master password, no spaces allowed:\t")
            while " " in master or master == "NULL" or len(master)<8:
                if master == "NULL":
                    print("NULL is reserved")
                if len(master<8):
                    print("Password too short")
                master = input("Set up your master password, no spaces allowed:\t")
            mdb.changePassword("M4IN", master)
        else:
            break
