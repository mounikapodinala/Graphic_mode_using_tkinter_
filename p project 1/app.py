import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def create_pie_chart():
    # Sample data for the pie chart
    labels = ['A', 'B', 'C', 'D']
    sizes = [30, 25, 20, 25]

    # Create a figure and axis for the pie chart
    fig = Figure(figsize=(6, 6))
    ax = fig.add_subplot(111)
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # Embed the pie chart in a Tkinter canvas
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack()

# Create the main application window
root = tk.Tk()
root.title("Pie Chart Example")

# Create a button to generate the pie chart
generate_button = ttk.Button(root, text="Generate Pie Chart", command=create_pie_chart)
generate_button.pack(pady=10)

# Start the main event loop
root.mainloop()
