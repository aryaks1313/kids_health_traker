

from database.db_connection import connect_db

def nutrient_status(consumed, required):

    if required == 0:
        return "N/A"

    percentage = (consumed / required) * 100

    if percentage < 80:
        return "Low"

    elif percentage <= 120:
        return "Normal"

    else:
        return "High"


def generate_nutrition_report(consumed, required):

    nutrients = [
        "calories",
        "protein",
        "carbohydrate",
        "fat",
        "calcium",
        "iron"
    ]

    report = []

    for nutrient in nutrients:

        report.append({

            "Nutrient": nutrient.capitalize(),

            "Consumed": round(consumed.get(nutrient, 0), 2),

            "Required": round(required.get(nutrient, 0), 2),

            "Status": nutrient_status(
                consumed.get(nutrient, 0),
                required.get(nutrient, 0)
            )
        })

    return report
