def cookie():
    # Ask user for number of cookies

    cookies = float(input("How many cookies would you like to make?"))

    # Calulate sugar ((1.5 * cookies) / 48)
    sugar = (1.5 * cookies) / 48.0

    # Calculate butter (cookies / 48)
    butter = cookies / 48

    # Calculate flour ((2.75 * cookies) / 48)
    flour = (2.75 * cookies) / 48

    # cookie results
    print("To make ", cookies, " cookies, you will need:\n", \
          format(sugar, '.2f'), " cups of sugar\n", \
          format(butter, '.2f'), " cups of butter\n", \
          format(flour, '.2f'), " cups of flour", sep='')

cookie()