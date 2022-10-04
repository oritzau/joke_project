import time
import os
os.system('color')

def joke_deliver(setup, punchline):
    bold = 'a'
    space = '\n'
    while bold.lower() != 'y' or bold.lower() != 'n':
        underline = input('Underline? (Y / N) ')
        if underline.lower() == 'y':
            find_string = input('What words?: ')
            under_string = ('\033[4m' + find_string + '\033[0m')
            punchline_w_under = punchline.replace(find_string, under_string)
            delay = float(input('Delay: '))
            print(50 * '\n')
            time.sleep(1.25)
            print(setup + '\n\n')
            time.sleep(delay)
            print(punchline_w_under)
            break
        if underline.lower() == 'n':
            delay = float(input('Delay: '))
            print(50 * '\n')
            time.sleep(1.25)
            print(50 * '\n' + setup + '\n\n')
            time.sleep(delay)
            print(punchline)
            break
if __name__ == '__main__':
    joke_deliver(input('Setup: '), input('Punchline: '))
