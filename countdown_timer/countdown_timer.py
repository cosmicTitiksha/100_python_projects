import time
import os

def countdown_timer():
    print("------------------------------------------------CountDown Timer---------------------------------------------------------")
    total_seconds = 0
    while True:
        try:
            total_seconds = int(input("Enter the time in seconds : "))
            if total_seconds > 0:
                break
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Please enter a Valid number.")
    print(f"Countdown starting from {total_seconds} seconds.")
    time.sleep(1)

    while total_seconds > 0:
        # Clear the console for a clean update (Windows uses 'cls', Unix/macOS uses 'clear')
        os.system('cls' if os.name == 'nt' else 'clear')
        minutes = total_seconds // 60
        seconds = total_seconds % 60

        time_display = f"{minutes:02d}:{seconds:02d}"
        # Display the time. The end='\r' makes the next print statement overwrite this one.
        print(f"⏰ Time remaining : {time_display}", end='\r', flush= True)

        # Pause for exactly one second
        time.sleep(1)

        # Decrement the total time
        total_seconds -= 1

    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n\n 🎉 TIME'S UP! The countdown has finished! 🎉 \n\n")


if __name__ == '__main__':
    countdown_timer()