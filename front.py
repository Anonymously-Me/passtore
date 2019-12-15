import easygui

def loginpage():
    return easygui.multpasswordbox(msg="LOGIN (press ok with both fields empty to sign up)", 
                    title="passtore",fields=('Username', 'Password'))
def signuppage():
    return easygui.multpasswordbox(msg="SIGNUP", 
                    title="passtore",fields=('Username', 'Email' , 'Password'))

class Menu:
    def main(self):
        return easygui.choicebox(msg='Choose an option', title='passtore', 
                choices=['Add Password', 'View Password(s)', 'Change Master Password', 'About', 'Exit'])
    def auth(self):
        return easygui.passwordbox(msg='AUTHETICATION', title='passtore')

    def addpmenu(self):
        return easygui.multpasswordbox(msg='Add Password', title='passtore', fields=('Account Name', 'password'))

    def viewpmenu(self):
        return easygui.choicebox(msg='Choose an option', title='passtore',
                choices=['View all passwords', 'View a specific password'])
    
    def changempmenu(self):
        return easygui.passwordbox(msg='CHANGE MASTER PASSWORD', title='passtore')
    
    def about(self):
        msg = """passtore v2.0\nPROGRAMMED BY:\nKAMIL MUKTAR\n\nSPECIAL THANKs TO:\nNADIA AHMED\n
            MUKTAR ABDURAHIM\nFAKIHA ABDURAHIM\nDR. ALIA IBRAHIM\n\nTHANKS TO:\nELIAS AMHA\n ROBEL GRMAY\nABINET TASSEW"""
        return easygui.textbox(msg='ABOUT', title='passtore', text=msg)
