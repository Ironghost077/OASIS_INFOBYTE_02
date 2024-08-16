import eel

eel.init(".")

@eel.expose
def bmi_calculator(height, weight):
    try:
        height = float(height)
        weight = float(weight)

        if height > 0:
            bmi = weight / ((height / 100) ** 2)
            bmi_category = ""

            if bmi < 18.5:
                bmi_category = "Underweight"
            elif 18.5 <= bmi <= 24.9:
                bmi_category = "Normal"
            elif 25 <= bmi <= 29.9:
                bmi_category = "Overweight"
            elif bmi >= 30:
                bmi_category = "Obesity"
            else:
                return "Something went wrong"

            return f"Your BMI is {bmi:.1f} ({bmi_category})"
        else:
            return "Height must be greater than zero"

    except ValueError:
        return "Please enter valid numerical values for height and weight"
    except Exception as e:
        return str(e)

eel.start("main.html", size=(800, 600))
