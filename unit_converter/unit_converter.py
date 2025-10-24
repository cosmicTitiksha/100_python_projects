# This program is for unit conversion.
# TEMPERATURE : Celsius <-> Fahrenheit
# Length : meters <-> feet <-> inches
# Mass : kilograms <-> pounds
m = True
# loop begun
while m:
    # asking for what category of conversion has to be performed
    query = input("What category(temperature/length/mass/exit) conversion you wanna perform ? :")
    # Temperature category
    if query.lower() == 'temperature':

        # Line giving info about what categories of conversion exist

        print("Only 'Celsius <-> Fahrenheit' conversion is available yet.")
        inp = input("Enter the input(celsius/fahrenheit) unit : ")

        # Celsius to fahrenheit
        if inp.lower() == 'celsius':
            inp_num = float(input("Enter the number(in celsius) : "))
            c_to_f = inp_num*9/5 + 32
            print(f"{inp_num} degree celsius = {c_to_f:.3f} degree fahrenheit.")

        # fahrenheit to celsius
        elif inp.lower() == 'fahrenheit':
            inp_num = float(input("Enter the number(in fahrenheit) : "))
            f_to_c = (inp_num-32)*5/9
            print(f"{inp_num} degree fahrenheit = {f_to_c:.3f} degree celsius.")
        else:
            print("Invalid entry.")
    
    # Length category
    elif query.lower() == 'length':

        # Line giving info about what categories of conversion exist
        print("Only 'meters <-> feet <-> inches' conversion is available yet.")

        inp = input("Enter the input(meters/feet/inches) unit : ")
        if inp.lower() == 'meters':
            out = input("Enter the target unit (feet/inches) : ")
            # Meters to feet
            if out.lower() == 'feet':
                inp_num = float(input("Enter the number(in meters) : "))
                m_to_f = inp_num*3.28084
                print(f"{inp_num} meters = {m_to_f:.3f} feet.")

            # Meters to inches
            elif out.lower() == 'inches':
                inp_num = float(input("Enter the number(in meters) : "))
                m_to_i = inp_num*39.3701
                print(f"{inp_num} meters = {m_to_i:.3f} inches.")
            else:
                print("Invalid entry.")
        elif inp.lower() == 'feet':
            out = input("Enter the target unit (meters/inches) : ")

            # feet to meters
            if out.lower() == 'meters':
                inp_num = float(input("Enter the number(in feet) : "))
                f_to_m = inp_num*0.3048
                print(f"{inp_num} feet = {f_to_m:.3f} meters.")

            # feet to inches
            elif out.lower() == 'inches':
                inp_num = float(input("Enter the number(in feet) : "))
                f_to_i = inp_num*12
                print(f"{inp_num} feet = {f_to_i:.3f} inches.")
            else:
                print("Invalid entry.")
        elif inp.lower() == 'inches':
            out = input("Enter the target unit (meters/feet) : ")

            # inches to meters
            if out.lower() == 'meters':
                inp_num = float(input("Enter the number(in inches) : "))
                i_to_m = inp_num/39.3701
                print(f"{inp_num} inches = {i_to_m:.3f} meters.")

            # inches to feet
            elif out.lower() == 'feet':
                inp_num = float(input("Enter the number(in inches) : "))
                i_to_f= inp_num/12
                print(f"{inp_num} inches = {i_to_f:.3f} feet.")
            else:
                print("Invalid entry.")
    
    # Mass category
    elif query.lower() == 'mass':
        
        # Line giving info about what categories of conversion exist
        print("Only 'Kilograms <-> pounds' conversion is available yet.")

        inp = input("Enter the input(kilograms/pounds) unit : ")

        # kilograms to pounds
        if inp.lower() == 'kilograms':
            inp_num = float(input("Enter the number(in kilograms) : "))
            k_to_p = inp_num*2.20462
            print(f"{inp_num} kilograms = {k_to_p:.3f} pounds.")

        # pounds to kilograms
        elif inp.lower() == 'pounds':
            inp_num = float(input("Enter the number(in pounds) : "))
            p_to_k = inp_num/2.20462
            print(f"{inp_num} pounds = {p_to_k:.3f} kilograms.")
        else:
            print("Invalid entry.")
    
    # Other categories...which do not exist yet
    else:
        print("Invalid entry")
        x = input("Have more stuffs to convert (y/n) ? : ")
        if x.lower() == 'y':
            m = True
        elif x.lower() == 'n':
            print("Visit Again! 👋")
            m = False
        else:
            print("Invalid entry. Exiting")
            m = False