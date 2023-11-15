import tkinter as tk
import time
import math


def create_clock():
    """
    Create a window with analog clock
    """
    # Create a window
    window = tk.Tk()
    window.title("Analog Clock")
    window.configure(bg="black")  # Set background color to black

    # Create a canvas for the clock
    canvas = tk.Canvas(window, width=400, height=400, bg="black", highlightthickness=0)
    canvas.pack()

    # Start updating the clock
    update_clock(canvas)

    # Start the main application loop
    window.mainloop()


def update_clock(canvas):
    """
    Update the clock with the current time
    """
    # Get the current time
    current_time = time.localtime()

    # Get the hour, minute, and second from the current time
    hour = current_time.tm_hour
    minute = current_time.tm_min
    second = current_time.tm_sec

    # Clear the canvas
    canvas.delete("all")

    # Draw the clock face on the canvas
    draw_clock_face(canvas)
    draw_hour_marks(canvas)
    draw_minute_marks(canvas)

    # Draw the hands
    # Calculate the angle based on hour and minute
    draw_hand(canvas, hour * 30 + minute / 2, 85, 7, "#ECECEC")
    # Calculate the angle based on minute and second
    draw_hand(canvas, minute * 6 + second * 0.1, 125, 2.5, "#ECECEC")
    # Show second hand
    draw_hand(canvas, second * 6, 140, 1.5, "red")

    # Schedule the next update after 1 second
    canvas.after(1000, update_clock, canvas)


def draw_clock_face(canvas):
    """
    Draw the clock face on the canvas
    """
    radius = 150
    center_x = 200
    center_y = 200

    # Draw the outer circle of the clock face
    canvas.create_oval(center_x - radius, center_y - radius, center_x + radius,
                    center_y + radius, outline="#ECECEC", width=1, fill="black")


def draw_hour_marks(canvas):
    """
    Draw hour marks on the clock face
    """
    radius = 150
    center_x = 200
    center_y = 200

    # Draw the hour numbers on the clock face
    for hour in range(1, 13):
        angle = math.radians(hour * 30 - 90)
        x = center_x + math.cos(angle) * (radius - 40)
        y = center_y + math.sin(angle) * (radius - 40)

        # Set the font size and style for numbers 3, 6, 9 and 12
        if hour in [3, 6, 9, 12]:
            font = ("Aptos ExtraBold", 26, "bold")
        else:
            font = ("Aptos", 14)

        canvas.create_text(x, y, text=str(hour), font=font, fill="#ECECEC")


def draw_minute_marks(canvas):
    """
    Draw small lines for the minutes on the clock face
    """
    radius = 150
    center_x = 200
    center_y = 200

    # Draw 60 small lines for minutes
    for minute in range(60):
        angle = math.radians(minute * 6 - 90)
        inner_radius = radius - 10
        outer_radius = radius - 5 if minute % 15 == 0 else radius - \
            17  # length and width for 15, 30, 45, and 60 minutes
        x1 = center_x + math.cos(angle) * inner_radius
        y1 = center_y + math.sin(angle) * inner_radius
        x2 = center_x + math.cos(angle) * outer_radius
        y2 = center_y + math.sin(angle) * outer_radius

        # Set width to 3 for 15, 30, 45, and 60 minutes, else 1
        line_width = 5 if minute % 15 == 0 else 1
        canvas.create_line(x1, y1, x2, y2, fill="gray", width=line_width)


def draw_hand(canvas, angle, length, width, color):
    """
    Draw a hand on the canvas
    """
    center_x = 200
    center_y = 200

    # Calculate the end point of the needle
    x = center_x + math.cos(math.radians(angle - 90)) * length
    y = center_y + math.sin(math.radians(angle - 90)) * length

    # Draw a hand
    canvas.create_line(center_x, center_y, x, y, width=width, fill=color)


if __name__ == "__main__":
    # Create an application window
    create_clock()
