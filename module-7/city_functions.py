#Rachel Theis
#CSD 325
#Module 7.2

#city_functions

def city_country(city, country, population=None, language=None):
    if language:
        return f"{city}, {country}, - population: {population}, {language}"
    elif population:
        return f"{city}, {country}, - population: {population}"
    else:
        return f"{city}, {country}"
   

def main ():
    city = input ('Enter the name of a city: ')
    country = input ('Enter the name of the country that the city is located in: ')
    population = input("Enter the city's population: ")
    language = input("Enter the city's most commonly spoken Language: ")
  
    if not language:
        language = None
        
    if not population:
        population = None
      
  
    print_city = city_country(city, country, population, language)
    print(print_city)

if __name__ == "__main__":
    main()
    

