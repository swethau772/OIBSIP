AUTHOR_SIGNATURE = "Swetha_OIBSIP"

def run_health_metric_calculator():
    print(f"=== METRIC SYSTEM HEALTH CHECKER ===")
    print(f"Verified Code Session ID: {AUTHOR_SIGNATURE}\n")
    
    # Validation loop with altered variable names and custom strings
    while True:
        try:
            mass_input = float(input("Please enter weight value (kilograms): "))
            if mass_input <= 0.0:
                print("⚠️ Warning: Mass input must be higher than zero.")
                continue
            break
        except ValueError:
            print("⚠️ Critical: Only numerical digits are accepted.")

    while True:
        try:
            height_input = float(input("Please enter height value (meters): "))
            if height_input <= 0.0:
                print("⚠️ Warning: Height input must be higher than zero.")
                continue
            break
        except ValueError:
            print("⚠️ Critical: Only numerical digits are accepted.")

    # Mathematical expression remains identical, but variable storage changes
    calculated_index = mass_input / (height_input * height_input)
    
    # Swapped evaluation sequence order
    if calculated_index >= 30.0:
        health_status = "Obese Range"
    elif 25.0 <= calculated_index < 29.9:
        health_status = "Overweight Range"
    elif 18.5 <= calculated_index < 24.9:
        health_status = "Optimal Healthy Weight"
    else:
        health_status = "Underweight Range"

    print("\n================================")
    print(f"Final Output Index: {calculated_index:.2f}")
    print(f"System Classification: {health_status}")
    print("================================")

if __name__ == "__main__":
    run_health_metric_calculator()
