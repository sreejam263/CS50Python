def convert(prompt):
    output = prompt.replace(":)", "🙂").replace(":(", "🙁") #Replacing an emoticon with an emoji
    return output

def main():
    msg = input('Please enter your message with emoticon: ')
    print(convert(msg))

main()
