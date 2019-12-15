## THIS IS WHERE THE MAIN PROGRAM WILL BE
from front import *

if __name__=='__main__':
    file = {}
    while True:
        a = loginpage()
        b = Menu()
        if a[0]=='' and a[1]=='':
            c = signuppage()
            a[0], a[1] = c[0], c[2]
            file[a[0]]=a[1]
        elif a[0] in file and a[1]==file[a[0]]: pass
        else: continue
        d = b.main()
        if d=='Add Password':
            b.addpmenu()
        elif d=='View Password(s)':
            b.viewpmenu()
        elif d=='Change Master Password':
            b.changempmenu()
        elif d=='About':
          b.about()
        else: 
          break
