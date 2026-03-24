def calculate_bmi(weight, height):
    """
    Calculate Body Mass Index (BMI).
    
    Parameters:
    weight (float): Weight in kilograms
    height (float): Height in meters
    
    Returns:
    float: BMI value
    """
    bmi = weight / (height ** 2)
    return bmi


def bmi_category(bmi):
    """
    Determine the BMI category based on BMI value.
    
    Parameters:
    bmi (float): BMI value
    
    Returns:
    str: BMI category
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"


# Main program
print("=" * 40)
print("         BMI Calculator")
print("=" * 40)

try:
    weight = float(input("Enter your weight (kg): "))
    height = float(input("Enter your height (meters): "))
    
    # Validate inputs
    if weight <= 0 or height <= 0:
        print("Error: Weight and height must be positive values!")
    else:
        # Calculate BMI
        bmi = calculate_bmi(weight, height)
        category = bmi_category(bmi)
        
        # Display results
        print("\n" + "=" * 40)
        print(f"Your BMI: {bmi:.2f}")
        print(f"Category: {category}")
        print("=" * 40)
        
except ValueError:
    print("Error: Please enter valid numbers!")
