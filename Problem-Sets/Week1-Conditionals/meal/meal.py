def main():
    #user input
    time = input('What time is it?').strip().lower()
    final_time = convert(time)
    if 7<=final_time<=8:
        print('Breakfast time')
    elif 12<= final_time<=13:
        print('Lunch time')
    elif 18<= final_time<=19:
        print('Dinner time')

def convert(time):
    hours, minutes = time.split(":")
    final_time = float(hours) + (float(minutes)/60)
    return final_time


if __name__ == "__main__":
    main()
