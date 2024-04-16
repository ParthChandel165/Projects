def calculate_bmi(weight_kg, height_m):
    """Calculate BMI (Body Mass Index)"""
    bmi = weight_kg / (height_m ** 2)
    return bmi

def interpret_bmi(bmi):
    """Interpret BMI value"""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("Welcome to the BMI Calculator")
    print("----------------------------")

    weight_kg = float(input("Enter your weight in kilograms: "))
    height_m = float(input("Enter your height in meters: "))

    bmi = calculate_bmi(weight_kg, height_m)
    interpretation = interpret_bmi(bmi)

    print("\nYour BMI is: {:.2f}".format(bmi))
    print("Interpretation:", interpretation)

if __name__ == "__main__":
    main()