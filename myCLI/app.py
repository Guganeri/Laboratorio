import os

def showtime():
    print("""
██╗░░██╗░█████╗░██████╗░██████╗░███████╗███╗░░██╗██╗███╗░░██╗░██████╗░
██║░░██║██╔══██╗██╔══██╗██╔══██╗██╔════╝████╗░██║██║████╗░██║██╔════╝░
███████║███████║██████╔╝██║░░██║█████╗░░██╔██╗██║██║██╔██╗██║██║░░██╗░
██╔══██║██╔══██║██╔══██╗██║░░██║██╔══╝░░██║╚████║██║██║╚████║██║░░╚██╗
██║░░██║██║░░██║██║░░██║██████╔╝███████╗██║░╚███║██║██║░╚███║╚██████╔╝
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚══════╝╚═╝░░╚══╝╚═╝╚═╝░░╚══╝░╚═════╝░
""")

def showmenu():
    print('Menu')
    print('1. Agent Verify')
    print('2. APM Verify')
    print('3. Exit\n')

def invalid_option():
    print('Invalid option!\n')
    input('Press Enter to continue...')
    main()

def finish_app():
    os.system('clear')
    print('Poweroff...\n')

def choose_option():
    try:
        op = int(input(''))
        match op:
            case 1:
                print('Agent Verify')
            case 2:
                print('APM Verify')
            case 3:
                finish_app()
            case _:
                invalid_option()
    except:
        invalid_option()

def main():
    os.system('clear')
    showtime()
    showmenu()
    choose_option()

if __name__ == '__main__':
    main()