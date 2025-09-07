# Matplotlibary.py
import matplotlib.pyplot as plt
'''
# Line Plot

hours = [1,2,3,4,5,6,7,8]
visitors = [50,60,55,70,90,120,110,130]

plt.plot(hours, visitors,
         color = "green",
         marker = "o",                      # shape round(o), square(s), triangle(^)
         linestyle = "--",
         linewidth = 2,                     # line thickness
         label = "Visitors",                # top of the graph, plt.legend is mand*
         alpha = 1,                         # color brightness
         )                         

plt.title("Website Visitors Per Hour")
plt.xlabel("Hour of Day")
plt.ylabel("Number of Visitors")
plt.legend()
plt.grid(True)
plt.show()

'''

'''
#  Bar Graph

day = ["Sun", "Mon", 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
hours = [6, 4, 5, 4, 4, 7, 8]

plt.bar(day, hours,
        color = "green",
        alpha = 0.5,
        edgecolor = "black",
        label = "Time"
        )

plt.title("Mobile Screen Time Per Week")
plt.xlabel("Day of the Week")
plt.ylabel("Number of Hours")
plt.legend()
plt.show()

'''

# Histogram

marks = [45,55,60,72,68,80,90,55,67,70,
         85,40,60,75,78,82,95,50,62,65,
         58,73,77,69,71,88,92,55,63,59
         ]

plt.hist(marks,
         bins = 15,
         color= "red",
         edgecolor="black",
         label="marks",
         histtype= "step",
         
         )

plt.title("Distribution of Student Marks")
plt.xlabel("Marks Range")
plt.ylabel("Number of Students")
plt.legend()
plt.show()