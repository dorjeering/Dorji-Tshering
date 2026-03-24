def calculate_bmi(weight, height):
    """Calculate BMI: weight (kg) / height (m)^2"""
    return weight / (height ** 2)


def get_user_input():
    """Get weight and height from user"""
    weight = float(input("Enter weight (kg): "))
    height = float(input("Enter height (meters): "))
    return weight, height


def classify_bmi(bmi):
    """Classify BMI into categories"""
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def display_bmi(bmi):
    """Display BMI result with category"""
    category = classify_bmi(bmi)
    print(f"\nYour BMI: {bmi:.2f}")
    print(f"Category: {category}")


# Main program
weight, height = get_user_input()
bmi = calculate_bmi(weight, height)
display_bmi(bmi)
