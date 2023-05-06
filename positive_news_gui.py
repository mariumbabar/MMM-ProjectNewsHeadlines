import tkinter as tk
from positive_news_scraper import get_headlines

# Create a tkinter window and label to display headlines
window = tk.Tk()
window.title("Positive News Headlines")
headline_label = tk.Label(window, text="\n".join(get_headlines()))
headline_label.pack()

# Run the GUI
window.mainloop()
