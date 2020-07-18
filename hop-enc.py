#!/user/bin/python
# coding=utf-8
# Script Written By Muhammad Hamza
# Editing My Script Will Not Make You a Coder
# Respect Coders
#--------------------------------------

import base64, zlib, marshal, os, sys, time, datetime
reload(sys)
sys.setdefaultencoding('utf8')



def exit():
    print "[!] Programme Ended"
    os.sys.exit()
    
    
def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)
        
        
def compiling():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;31mYou File Is Compiling\Encoding"+o),;sys.stdout.flush();time.sleep(1)
		
		
#Banner#
banner = """
\033[1;35md88888b   d8b   db    .o88b. 
\033[1;35m88'       888o  88   d8P  Y8 
\033[1;35m88ooooo   88V8o 88   8P      
\033[1;35m88~~~~~   88 V8o88   8b      
\033[1;35m88.       88  V888   Y8b  d8 
\033[1;35mY88888P   VP   V8P    `Y88P'       
\033[1;97m-----------------------------------------------
* Author : Muhammad Hamza
* Github : https://github.com/Hamzahash
* Youtube: HOP Anonymous
-----------------------------------------------     """
def tool_login():
    os.system('clear')
    print banner
    username = raw_input("Tool Username : ")
    if username =="hamza":
        os.system('clear')
        print banner
        print "Tool Username : "+username+ " (Correct)"
    else:
        print "Tool Username : "+username+ "\033[1;31m (Wrong)\033[0;97m"
        time.sleep(1)
        tool_login()
    password = raw_input("Tool Password : ")
    if password =="1626":
        os.system('clear')
        print banner
        print "Tool Username : "+username+ " (Correct)"
        print "Tool Password : "+password+ "  (Correct)"
        print
        psb("\033[1;32mLogged In Successfully\033[0;97m")
        time.sleep(1)
        menu()
    else:
        print "Tool Username : "+username+ " (Correct)"
        print "Tool Username : "+username+ "\033[1;31m  (Wrong)\033[0;97m"
        time.sleep(1)
        tool_login()
def menu():
    os.system('clear')
    print banner
    print "[1] Encrypt With Base64"
    print "[2] Encrypt With Marshal"
    print "[3] Encrypt With Zlib Base64"
    print "[4] Encrypt With Zlib Marshal Base64"
    print "[5] Contact Me On Facebook"
    print "[6] Exit"
    print
    menu_enc()

def menu_enc():
    enc = raw_input(" \033[1;31m▄︻̷̿┻̿═━一  \033[0;97m")
    if enc =="":
        print "Please Select Something"
        time.sleep(2)
        menu_enc()
    elif enc =="1":
        os.system('clear')
        print banner
        try:
            file = raw_input('Input File Path : ')
            print
            print(47*"-")
            fileopen = open(file).read()
            a = base64.b16encode(fileopen)
            b = "#File Coded By : Muhammad Hamza\n#Github : https://github.com/Hamzahash\nimport base64\nexec(base64.b16decode('" + a + "'))"
            c = file.replace('.py', 'enc.py')
            d = open(c, 'w')
            d.write(b)
            d.close()
            print
            compiling()
            print
            time.sleep(0.5)
            print
            print "\033[1;32mFile Successful Compiled/Encrypted\033[0;97m"
            print
            print"File Saved As : ", c
            print
            print(47*"-")
            print
            raw_input("[Press Enter To Back] ")
            menu()
        except IOError:
            print "File Not Found"
            menu()
    elif enc =="2":
        os.system('clear')
        print banner
        try:
            file = raw_input('Input File Path : ')
            print
            print(47*"-")
            fileopen = open(file).read()
            a = compile(fileopen, 'dg', 'exec')
            m = marshal.dumps(a)
            s = repr(m)
            b = "#File Coded By : Muhammad Hamza\n#Github : https://github.com/Hamzahash\nimport marshal\nexec(marshal.loads(" + s + "))"
            c = file.replace('.py', 'enc.py')
            d = open(c, 'w')
            d.write(b)
            d.close()
            print
            compiling()
            print
            time.sleep(0.5)
            print
            print "\033[1;32mFile Successful Compiled/Encrypted\033[0;97m"
            print
            print"File Saved As : ", c
            print
            print(47*"-")
            print
            raw_input("[Press Enter To Back] ")
            menu()
        except IOError:
            print "File Not Found"
            menu()
    elif enc =="3":
        os.system('clear')
        print banner
        try:
            file = raw_input('Input File Path : ')
            print
            print(47*"-")
            fileopen = open(file).read()
            c = zlib.compress(fileopen)
            d = base64.b16encode(c)
            b = "#File Coded By : Muhammad Hamza\n#Github : https://github.com/Hamzahash\nimport marshal,zlib,base64\nexec(zlib.decompress(base64.b16decode('" + d + "'))"
            f = file.replace('.py', 'enc.py')
            g = open(f, 'w')
            g.write(b)
            g.close()
            print
            compiling()
            print
            time.sleep(0.5)
            print
            print "\033[1;32mFile Successful Compiled/Encrypted\033[0;97m"
            print
            print"File Saved As : ", f
            print
            print(47*"-")
            print
            raw_input("[Press Enter To Back] ")
            menu()
        except IOError:
            print "File Not Found"
            menu()
    elif enc =="4":
        os.system('clear')
        print banner
        try:
            file = raw_input('Input File Path : ')
            print
            print(47*"-")
            fileopen = open(file).read()
            sa = compile(fileopen, 'dg', 'exec')
            sb = marshal.dumps(sa)
            c = zlib.compress(sb)
            d = base64.b16encode(c)
            e = "#File Coded By : Muhammad Hamza\n#Github : https://github.com/Hamzahash\nimport marshal,zlib,base64\nexec(marshal.loads(zlib.decompress(base64.b16decode('" + str(d) + "'))"
            f = file.replace('.py', 'enc.py')
            g = open(f, 'w')
            g.write(e)
            g.close()
            print
            compiling()
            print
            time.sleep(0.5)
            print
            print "\033[1;32mFile Successful Compiled/Encrypted\033[0;97m"
            print
            print"File Saved As : ", f
            print
            print(47*"-")
            print
            raw_input("[Press Enter To Back] ")
            menu()
        except IOError:
            print "File Not Found"
            menu()
    elif enc =="5":
        os.system('xdg-open https://www.facebook.com/muhammad.hamza1626')
        menu()
    elif enc =="6":
        exit()
    else:
        print "Wrong Input"
        time.sleep(1)
        menu_enc()


if __name__ == '__main__':
	tool_login()