def calculate_bmi(height,weight):
    bmi=weight/(height**2)
    return round(bmi,2)

def bmi_category(bmi):
    if bmi<18:
        return 'Underweight'
    elif bmi<25:
        return "Normal weight"
    else:
        return 'Overweight'
