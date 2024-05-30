#Python In A Nutshell
MAX_LINES = 3
#Get the Deposirt
def deposit():
    while True:
        amount = input('Enter the amount to deposit: ')
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print('Amount must be greater than 0')
        else:
            print('Invalid amount')

    return amount

def get_number_of_lines():
    while True:
        lines = input('Enter the number of lines (1-'+str(MAX_LINES)+')')
        if lines.isdigit():
            lines = int(lines)
            if lines > 0:
                break
            else:
                print('Number of lines must be greater than 0')
        else:
            print('Invalid number of lines')
    return lines

def main():
    balance = deposit() 

main()