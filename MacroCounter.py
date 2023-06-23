import tkinter as tk
from tkinter import ttk


class MacroCounterApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Macro Counter")
        self.geometry("400x600")
        self.minsize(300, 200)  # Set minimum size for the window

        self.meals = []

        self.create_widgets()

    def create_widgets(self):
        self.tabControl = ttk.Notebook(self)

        self.tabMeals = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tabMeals, text="Meals")
        self.tabControl.pack(expand=True, fill="both")

        self.labelTitle = tk.Label(self.tabMeals, text="Macro Counter", font=("Arial", 16, "bold"))
        self.labelTitle.pack(pady=10)

        self.frameInput = tk.Frame(self.tabMeals)
        self.frameInput.pack(pady=10)

        self.labels = ["Meal Name:", "Protein (g):", "Carbohydrates (g):", "Fat (g):"]
        self.entries = []

        for i, label in enumerate(self.labels):
            tk.Label(self.frameInput, text=label).grid(row=i, column=0, padx=5, pady=5)
            entry = tk.Entry(self.frameInput)
            entry.grid(row=i, column=1, padx=5, pady=5)
            self.entries.append(entry)

        self.buttonAdd = tk.Button(self.tabMeals, text="Add Meal", command=self.addMeal)
        self.buttonAdd.pack(pady=10)

        self.frameMeals = tk.Frame(self.tabMeals)
        self.frameMeals.pack()

        self.labelMealsTitle = tk.Label(self.frameMeals, text="Your Meals", font=("Arial", 12, "bold"))
        self.labelMealsTitle.pack(pady=5)

        self.listboxMeals = tk.Listbox(self.frameMeals, width=40, height=8)
        self.listboxMeals.pack(padx=10, pady=5)

        self.frameTotals = tk.Frame(self.tabMeals)
        self.frameTotals.pack(pady=10)

        self.labelTotalsTitle = tk.Label(self.frameTotals, text="Total", font=("Arial", 12, "bold"))
        self.labelTotalsTitle.pack(pady=5)

        self.labelProteinTotal = tk.Label(self.frameTotals, text="Total Protein: 0 g")
        self.labelProteinTotal.pack()

        self.labelCarbsTotal = tk.Label(self.frameTotals, text="Total Carbohydrates: 0 g")
        self.labelCarbsTotal.pack()

        self.labelFatTotal = tk.Label(self.frameTotals, text="Total Fat: 0 g")
        self.labelFatTotal.pack()

        self.labelCaloriesTotal = tk.Label(self.frameTotals, text="Total Calories: 0 kcal")
        self.labelCaloriesTotal.pack()

        self.tabControl.add(self.createCalorieTab(), text="Calorie Calculator")

    def createCalorieTab(self):
        tabCalorie = ttk.Frame(self.tabControl)

        labelCalorieTitle = tk.Label(tabCalorie, text="Calorie Calculator", font=("Arial", 16, "bold"))
        labelCalorieTitle.pack(pady=10)

        frameCalorieInput = tk.Frame(tabCalorie)
        frameCalorieInput.pack(pady=10)

        tk.Label(frameCalorieInput, text="Gender:").grid(row=0, column=0, padx=5, pady=5)

        genderVar = tk.StringVar()
        genderVar.set("male")

        maleRadio = tk.Radiobutton(frameCalorieInput, text="Male", variable=genderVar, value="male")
        maleRadio.grid(row=0, column=1, padx=5, pady=5)

        femaleRadio = tk.Radiobutton(frameCalorieInput, text="Female", variable=genderVar, value="female")
        femaleRadio.grid(row=0, column=2, padx=5, pady=5)

        entries = []

        labels = ["Age:", "Height (cm):", "Weight (kg):"]
        for i, label in enumerate(labels):
            tk.Label(frameCalorieInput, text=label).grid(row=i + 1, column=0, padx=5, pady=5)
            entry = tk.Entry(frameCalorieInput)
            entry.grid(row=i + 1, column=1, padx=5, pady=5)
            entries.append(entry)

        lossCheckboxVar = tk.IntVar()
        lossCheckbox = tk.Checkbutton(tabCalorie, text="Weight Loss", variable=lossCheckboxVar)
        lossCheckbox.pack(pady=10)

        buttonCalculate = tk.Button(tabCalorie, text="Calculate", command=lambda: self.calculateCalories(entries, genderVar.get(), lossCheckboxVar.get()))
        buttonCalculate.pack(pady=10)

        self.labelResult = tk.Label(tabCalorie, text="", font=("Arial", 12))
        self.labelResult.pack()

        return tabCalorie

    def addMeal(self):
        mealEntries = [entry.get() for entry in self.entries]

        if all(mealEntries):
            self.meals.append(dict(zip(["name", "protein", "carbs", "fat"], mealEntries)))
            self.listboxMeals.insert(tk.END, mealEntries[0])

            for entry in self.entries:
                entry.delete(0, tk.END)

            self.calculateTotals()

    def calculateTotals(self):
        totalProtein = sum(float(meal["protein"]) for meal in self.meals)
        totalCarbs = sum(float(meal["carbs"]) for meal in self.meals)
        totalFat = sum(float(meal["fat"]) for meal in self.meals)

        self.labelProteinTotal.config(text=f"Total Protein: {totalProtein} g")
        self.labelCarbsTotal.config(text=f"Total Carbohydrates: {totalCarbs} g")
        self.labelFatTotal.config(text=f"Total Fat: {totalFat} g")

        totalCalories = round((totalProtein * 4) + (totalCarbs * 4) + (totalFat * 9), 2)
        self.labelCaloriesTotal.config(text=f"Total Calories: {totalCalories} kcal")

    def calculateCalories(self, entries, gender, isWeightLoss):
        age, height, weight = [entry.get() for entry in entries]

        if gender and age and height and weight:
            bmr = 10 * float(weight) + 6.25 * float(height) - 5 * int(age) + (5 if gender == "male" else -161)
            activityLevel = 1.2 if not isWeightLoss else 1.0  # Sedentary activity level for weight loss
            recommendedCalories = round(bmr * activityLevel)
            self.labelResult.config(text=f"Recommended Calories: {recommendedCalories} kcal")


if __name__ == "__main__":
    app = MacroCounterApp()
    app.mainloop()
