import tkinter as tk
from tkinter import messagebox
import time

def start_countdown():
    try:
        
        user_input = entry.get()
        countdown_time = int(user_input)
        
        while countdown_time > 0:
            # Update the label with the remaining time
            mins, secs = divmod(countdown_time, 60)
            time_format = f'{mins:02d}:{secs:02d}'
            timer_label.config(text=time_format)
            window.update()
            time.sleep(1)
            countdown_time -= 1
        
        # Time's up message
        timer_label.config(text="00:00")
        messagebox.showinfo("Time's up", "The countdown has finished!")
    
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number.")

# Create the main application window
window = tk.Tk()
window.title(" Vignesh-Countdown Timer")

# Create a frame to hold the widgets
frame = tk.Frame(master=window, padx=15, pady=15)
frame.pack()

# Create an entry widget to take the countdown time from the user
entry_label = tk.Label(master=frame, text="Enter time in seconds:")
entry_label.pack()
entry = tk.Entry(master=frame, width=10)
entry.pack()

# Create a label to display the countdown timer
timer_label = tk.Label(master=frame, text="00:00", font=("Helvetica", 48))
timer_label.pack(pady=15)

# Create a start button to start the countdown
start_button = tk.Button(master=frame, text="Start Countdown", command=start_countdown)
start_button.pack()

# Run the Tkinter event loop
window.mainloop()
