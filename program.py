def BMR(weight, height, age):
    BMR = 10 * int(weight) + float(6.25) * int(height) - 5 * int(age) + 5
    return BMR

def output(weight, height, age, BMR):
	return """
Your weight is {} kg.
Your height is {} cm.
Your age is {} years old.
Your BMR (Basal metabolic rate) is {}. 
""". format(weight, height, age, BMR)

def main():
    weight = raw_input("What is your weight? (kg)")
    height = raw_input("What is your height?(cm) ")
    age = raw_input("How old are you?")
    BMR = 10 * int(weight) + float(6.25) * int(height) - 5 * int(age) + 5
    print output(weight, height, age, BMR)

main()
