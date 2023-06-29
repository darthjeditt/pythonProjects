# Macro Counter App

The Macro Counter App is a GUI application built using the Tkinter library in Python. It allows users to track their meals and calculate the total macronutrients (protein, carbohydrates, and fat) and calories consumed.

## Setup and Dependencies
The Macro Counter App requires the following dependencies:
- Python (version 3 or above)
- Tkinter (included with Python)

## Project Overview
The Macro Counter App provides the following functionalities:

1. Create Macro Counter UI: Initializes the main application window and sets its properties. The UI includes tabs for "Meals" and "Calorie Calculator". The "Meals" tab allows users to add meals and displays the total macronutrients and calories. The "Calorie Calculator" tab calculates the recommended daily calorie intake based on user inputs.

2. Add Meal: Adds a meal to the list by entering the meal name, protein, carbohydrates, and fat. The entered values are validated, and if valid, the meal is added to the list and displayed in the UI. The total macronutrients and calories are automatically recalculated.

3. Calculate Totals: Calculates the total macronutrients (protein, carbohydrates, and fat) and calories based on the meals added. The totals are displayed in the UI.

4. Calculate Calories: Calculates the recommended daily calorie intake based on user inputs in the "Calorie Calculator" tab. The user selects their gender and enters their age, height, and weight. They can also choose the weight loss option. On clicking the "Calculate" button, the recommended calorie intake is displayed.

## Usage
1. Make sure you have the required dependencies installed.
2. Run the Python script containing the Macro Counter App code.
3. The Macro Counter App window will appear.
4. Use the "Meals" tab to add meals and view the total macronutrients and calories.
5. Use the "Calorie Calculator" tab to calculate the recommended daily calorie intake based on your inputs.

## Conclusion
The Macro Counter App provides a user-friendly interface for tracking meals and calculating macronutrients and calories. It can be used to monitor and manage nutrition goals. By leveraging the Tkinter library, the app provides an interactive experience for users to input their meal data and receive calculated results.