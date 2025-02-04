                                        # 1
def count_by(x, n):

    result = []
    i = 1
    while i <= n:
        result.append(x * i)
        i += 1
    return result             


						                # 2

def get_planet_name(id):
    name = ""
    if id == 1:
        name = "Mercury"
    elif id == 2:
        name = "Venus"
    elif id == 3:
        name = "Earth"
    elif id == 4:
        name = "Mars"
    elif id == 5:
        name = "Jupiter"
    elif id == 6:
        name = "Saturn"
    elif id == 7:
        name = "Uranus"
    elif id == 8:
        name = "Neptune"
    return name

                                          # 3

def human_years_cat_years_dog_years(human_years):
    if human_years == 1:
        return [human_years, 15, 15]
    elif human_years == 2:
        return [human_years, 24, 24]
    else:
        cat_years = 24 + (human_years - 2) * 4
        dog_years = 24 + (human_years - 2) * 5
        return [human_years, cat_years, dog_years]

					                   # 4

def twice_as_old(dad_years_old, son_years_old):
  
    difference = dad_years_old - 2 * son_years_old
    
 
    years_ago_or_in_future = abs(difference)
    
    return years_ago_or_in_future

                                         # 5

def greet(language) -> str:
    greetings = {
        "english": "Welcome", "czech": "Vitejte", "danish": "Velkomst",
        "dutch": "Welkom", "estonian": "Tere tulemast", "finnish": "Tervetuloa",
        "flemish": "Welgekomen", "french": "Bienvenue", "german": "Willkommen",
        "irish": "Failte", "italian": "Benvenuto", "latvian": "Gaidits",
        "lithuanian": "Laukiamas", "polish": "Witamy", "spanish": "Bienvenido",
        "swedish": "Valkommen", "welsh": "Croeso"
    }
    return greetings.get(str(language).lower(), "Welcome")

