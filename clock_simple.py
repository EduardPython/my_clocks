import tkinter as tk
import time


def update_clock():
    """
   Update the clock every second with the current time
    """
    # Get the current time
    current_time = time.strftime("%H:%M:%S")

    # Update the value of the clock widget with the current time
    clock.config(text=current_time)

    # Schedule the next update after 1 second
    clock.after(1000, update_clock)

# Create an application window


root = tk.Tk()
root.title("Clock")

# Create a clock widget
clock = tk.Label(root, font=("Aptos ExtraBold", 50), bg="black", fg="white")


# Place the clock widget in the application window
clock.pack(fill=tk.BOTH, expand=True)

# Start clock update
update_clock()

# Start the main loop of the application
root.mainloop()
