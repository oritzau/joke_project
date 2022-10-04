import os
os.system('color')

def joke_deliver(setup, punchline):
    bold = 'a'
    while bold.lower() != 'y' or bold.lower() != 'n':
        underline = input('Underline? (Y / N) ')
        if underline.lower() == 'y':
            find_string = input('What words?: ')
            under_string = ('\033[4m' + find_string + '\033[0m')
            punchline_w_under = punchline.replace(find_string, under_string)
            os.system('cls')
            print(setup + '\n\n')
            nothing_var = input('Press Enter to view ')
            os.system('cls')
            print(punchline_w_under)
            break
        if underline.lower() == 'n':
            os.system('cls')
            print(setup + '\n\n')
            nothing_var = input('Press Enter to view ')
            os.system('cls')
            print(punchline)
            break
if __name__ == '__main__':
    joke_deliver(input('Setup: '), input('Punchline: '))
