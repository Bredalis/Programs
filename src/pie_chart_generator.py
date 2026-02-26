
import matplotlib.pyplot as plt


class PieChart:
    """Class to collect data and generate a pie chart"""

    def __init__(self):
        self.names = []
        self.values = []
        self.question = ""

    def run(self):
        """Collects user input data."""
        print("\nPie chart with user-provided data")

        while self.question.lower() != "no":
            try:
                name = input("Enter the name: ")
                percentage = int(input("Enter the percentage: "))

                self.names.append(name)
                self.values.append(percentage)

            except ValueError:
                print("Error: Please enter valid numbers.")

            except Exception as error:
                print(f"Unexpected error: {error}")

            finally:
                self.question = input(
                    "\nDo you want to continue entering data? (yes/no): "
                )

    def plot(self):
        """Displays the pie chart."""
        plt.pie(self.values, labels=self.names)
        plt.title("Pie Chart")
        plt.show()


if __name__ == "__main__":
    pie_chart = PieChart()
    pie_chart.run()
    pie_chart.plot()
