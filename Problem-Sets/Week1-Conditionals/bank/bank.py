def main():
    #prompt the user for the greeting received
    greeting = input('Enter the greeting you received: ').strip().lower()
    if greeting.startswith('h'):
        if greeting.startswith('hello'):
            print('$0')
        else:
             print('$20')

    else:
        print('$100')

main()



