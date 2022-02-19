from pandas import *
import matplotlib.pyplot as plot
from matplotlib import use, rcParams
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.pyplot import Figure
import tkinter as tk
import numpy as np
import pandas as pandas

use("TkAgg")
rcParams.update({"figure.autolayout": True})

# Open and save each dataset as a variable
july_data = read_csv("2020_July.csv", sep = ",")
august_data = read_csv("2020_August.csv", sep = ",")
september_data = read_csv("2020_September.csv", sep = ",")

def averageEachLocation(unique_device_codes, data_set):	
	
	"""Averages the NSB values for each location in a given data set"""
	
	paired_list = []
	for i in unique_device_codes:
		location_data = data_set[data_set['device_code'] == i]
		location_mean = location_data['nsb'].mean()
		paired_list.append((i, round(location_mean,2)))
	return paired_list

# Create a list of unique location codes for each data set
unique_device_code_july = (july_data['device_code'].unique())
unique_device_code_august = (august_data['device_code'].unique())
unique_device_code_september = (september_data['device_code'].unique())

# Compare unique location codes across all three data sets and create a list of and location codes that appear in all three data sets
august_september_shared_codes = []
for i in unique_device_code_september:
	if i in unique_device_code_august:
		august_september_shared_codes.append(i)
shared_codes = []
for i in august_september_shared_codes:
	if i in unique_device_code_july:
		shared_codes.append(i)

# Sort the unique location codes alphabetically 
shared_codes = sorted(shared_codes)

# List of real location names in same order as the sorted location codes
full_location_names = [
"Sai Kung, Hong Kong",
"Seoul, Korea",
"Cape D'Aguilar, Hong Kong",
"Daejeon, Korea",
"South Brandenberg, Germany",
"Pokfulam, Hong Kong",
"Tsuen Wan, Hong Kong",
"Taroko National Park, Taiwan",
"Intahanon Mountain, Thailand",
"Kowloon, Hong Kong",
"Muju-gun, Korea",
"Chiang Mai, Thailand",
"Ouro Fino, Brazil",
"Shek Pik, Hong Kong",
"Seoul, Korea",
"Taipei, Taiwan",
"Kowloon, Hong Kong",
"Shah Alam, Malaysia",
"Bongrae Mountain Summit, Korea",
"Ziesel, Germany"
]

# Call function to create a paired list [(Location Code, NSB)] for each data set

july_averages_by_location = averageEachLocation(shared_codes, july_data)
august_averages_by_location = averageEachLocation(shared_codes, august_data)
september_averages_by_location = averageEachLocation(shared_codes, september_data)

# Create separate data frame for each paired list
july_df = pandas.DataFrame(july_averages_by_location, columns = ['Location', 'NSB'])
august_df = pandas.DataFrame(august_averages_by_location, columns = ['Location', 'NSB'])
september_df = pandas.DataFrame(september_averages_by_location, columns = ['Location', 'NSB'])

# Replace location codes with real location names in each data frame
july_df['Location'] = july_df['Location'].replace(shared_codes,full_location_names)
august_df['Location'] = august_df['Location'].replace(shared_codes, full_location_names)
september_df['Location'] = september_df['Location'].replace(shared_codes, full_location_names)

# Initialize GUI
window = tk.Tk()
window.title("Night Sky Brightness Averages by Location")
button_width = 20
button_height = 5
y_ticks = [*range(0,21,2)]


# Create separate frames for graph window and button tray
frm_graph = tk.Frame(master=window, relief = tk.SUNKEN, borderwidth = 5)
frm_buttons = tk.Frame(master=window, relief = tk.RAISED, borderwidth = 5)

# Create each button, assign to the correct frame, assign label, size, and colors
btn_july = tk.Button(master=frm_buttons, text="July 2020", width = button_width, height = button_height, bg="blue", fg="white")
btn_july.pack(side =tk.LEFT)
btn_august = tk.Button(master=frm_buttons, text="August 2020", width = button_width, height = button_height, bg="blue", fg="white")
btn_august.pack(side=tk.LEFT)
btn_september = tk.Button(master=frm_buttons, text="September 2020", width = button_width, height = button_height, bg="blue", fg="white")
btn_september.pack(side=tk.LEFT)
btn_all_months = tk.Button(master=frm_buttons, text="All Months", width = button_width, height = button_height, bg="blue", fg="white")
btn_all_months.pack(side=tk.LEFT)

frm_graph.pack(side=tk.TOP)
frm_buttons.pack()

# Create how to handle each button click
def printJuly(event):
	# First loop clears the frame
	for widget in frm_graph.winfo_children():
		widget.destroy()
	figure1 = plot.Figure(figsize=(6,5), dpi=100)
	ax1 = figure1.add_subplot()
	bar_graph = FigureCanvasTkAgg(figure1, frm_graph)
	bar_graph.get_tk_widget().pack()		
	july_df.plot(kind='bar', ax=ax1, zorder = 3)
	ax1.set_title("Average NSB by Location--July 2020")
	ax1.set_xticklabels(full_location_names)	
	ax1.set_yticks(y_ticks)
	ax1.grid(zorder = 0)
	ax1.grid(axis = 'x')
	print(july_df)
	print()

def printAugust(event):
	for widget in frm_graph.winfo_children():
		widget.destroy()	
	figure1 = plot.Figure(figsize=(6,5), dpi=100)
	ax1 = figure1.add_subplot()
	bar_graph = FigureCanvasTkAgg(figure1, frm_graph)
	bar_graph.get_tk_widget().pack()		
	august_df.plot(kind='bar', ax=ax1, zorder = 3)
	ax1.set_title("Average NSB by Location--August 2020")
	ax1.set_xticklabels(full_location_names)
	ax1.set_yticks(y_ticks)
	ax1.grid(zorder = 0)
	ax1.grid(axis = 'x')
	print(august_df)
	print()

def printSeptember(event):
	for widget in frm_graph.winfo_children():
		widget.destroy()
	figure1 = plot.Figure(figsize=(6,5), dpi=100)
	ax1 = figure1.add_subplot()
	bar_graph = FigureCanvasTkAgg(figure1, frm_graph)
	bar_graph.get_tk_widget().pack()		
	september_df.plot(kind='bar', ax=ax1, zorder = 3)
	ax1.set_title("Average NSB by Location--September 2020")
	ax1.set_yticks(y_ticks)
	ax1.set_xticklabels(full_location_names)
	ax1.grid(zorder = 0)
	ax1.grid(axis = 'x')
	print(september_df)	
	print()


# Create x-axis locations for each of the bars in the grouped bar chart
w = .2
bar2 = np.arange(len(full_location_names))
bar1 = [i-w for i in bar2]
bar3 = [i+w for i in bar2]

def printAllMonths(event):
	for widget in frm_graph.winfo_children():
		widget.destroy()
	figure1 = plot.Figure(figsize=(6,5), dpi=100)
	ax1 = figure1.add_subplot()
	bar_graph = FigureCanvasTkAgg(figure1, frm_graph)
	bar_graph.get_tk_widget().pack()
	ax1.bar(bar1, july_df['NSB'], color='b', width = .2, align='center', zorder = 3, label="July")
	ax1.bar(bar2, august_df['NSB'], color='y', width = .2, align='center', zorder = 3, label="August")
	ax1.bar(bar3, september_df['NSB'], color='r', width = .2, align='center', zorder = 3, label="September")
	ax1.set_title("Average NSB by Location July/August/September")	
	ax1.set_xticks(bar2)
	ax1.set_xticklabels(full_location_names, rotation=90)	
	ax1.set_yticks(y_ticks)
	ax1.grid(zorder =0)
	ax1.grid(axis = 'x')
	ax1.legend()


# Bind buttons to functions
btn_july.bind("<Button-1>", printJuly)
btn_august.bind("<Button-1>", printAugust)
btn_september.bind("<Button-1>", printSeptember)
btn_all_months.bind("<Button-1>", printAllMonths)

window.mainloop()

