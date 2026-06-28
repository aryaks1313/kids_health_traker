from datetime import date
def calculate_age_days(dob):
    today=date.today()
    age_days=(today-dob).days
    return age_days


