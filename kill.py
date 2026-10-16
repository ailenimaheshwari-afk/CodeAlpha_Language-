import matplotlib.pyplot as plt
import numpy as np

class DataVisualization:
    def __init__(self, categories, values):
        self.categories = categories
        self.values = values

    def bar_chart(self):
        plt.figure(figsize=(8, 5))
        plt.bar(self.categories, self.values, color="skyblue")
        plt.title("Bar Chart")
        plt.xlabel("Categories")
        plt.ylabel("Values")
        plt.show()

    def line_chart(self):
        plt.figure(figsize=(8, 5))
        plt.plot(self.categories, self.values, marker="o",
                 color="green")
        plt.title("Line Chart")
        plt.xlabel("Categories")
        plt.ylabel("Values")
        plt.grid(True)
        plt.show()

    def pie_chart(self):
        plt.figure(figsize=(7, 7))
        plt.pie(self.values, labels=self.categories,
                autopct="%1.1f%%", startangle=90)
        plt.title("Pie Chart")
        plt.show()

    def display_data(self):
        print("Data Summary")
        for category, value in zip(self.categories, self.values):
            print(f"{category}: {value}")


# Main program
categories = ["Python", "Java", "C++", "JavaScript"]
values = [40, 25, 20, 15]

visualizer = DataVisualization(categories, values)

visualizer.display_data()
visualizer.bar_chart()
visualizer.line_chart()
visualizer.pie_chart()
