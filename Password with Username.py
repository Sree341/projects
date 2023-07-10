def username(last_name, birth_year):
    return("{}{}".format(last_name[:4], birth_year))
print(username("Ivanov", "1985")) 
# Should display "Iva1985" 
print(username("Rodríguez", "2000")) 
# Should display "Rod2000" 
print(username("Deng", "1991")) 
# Should display "Den1991"
print(username("Sree", "1993"))