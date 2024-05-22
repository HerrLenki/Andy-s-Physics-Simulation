import math

orbit_list = [] #orbit radius
planet_list = [] #name
moon_list = [] #name
belt_list = [] #name
species_list = [] #name
star_list = [] #name
black_hole_list = []#name
planet_description_list = [] #type, life, mass, orbit object, orbit period
moon_description_list = [] # mass, radius, orbit object, orbit period
belt_description_list = [] #width, orbit object, orbit radius
species_description_list = [] #lifespan
star_description_list = [] #radius, temperature, mass
black_hole_description_list = [] #radius, mass

while True:
    print("\n") #makes everything easier to read, by adding a seperation line between commands
    thing_to_do = input("What would you like to do?: ")

    if thing_to_do == "create" or thing_to_do == "Create": #allows you to create things
        create_object = input("What do you want to create?: ") #asks what you want to create

        match create_object: #checks what create_object is
            case "Planet" | "planet":
                if star_list != [] or black_hole_list != []: #if a star or black hole exists
                    planet_name = input("What is the name of the planet?: ") #name
                    planet_mass = input("What is the mass of the planet?: ") #mass
                    planet_type = input("What is the type of the planet?: ") #type (currently useless)
                    planet_life = input("Does the planet support life?: ") #life (currently useless)
                    print("\n" + "The planet has to orbit a star or black hole.")
                    print("Here is a list of available objects: ") 
                    print(", ".join(star_list) + ", ".join(black_hole_list)) #creates the list of black holes and stars
                    orbit_object = input("What object does the planet rotate around?: ") #asks what the star or black hole, the planet orbits around, is
                    orbit_distance = input("What is the distance between " + planet_name + " and " + orbit_object + "?: ") #asks for the distance between the planet and the star
                    
                    if "".join(orbit_list).find(orbit_distance) == -1:
                        star_mass = 0 #introduces a variable for the mass of the star
                        for i in range(len(star_list) + len(black_hole_list)): #find the star or black hole and its values in the lists
                            if star_list[i] == orbit_object:
                                star_mass = star_description_list[2 + 3*i]
                                break 
                            if black_hole_list[i] == orbit_object:
                                star_mass = black_hole_description_list[1 + 2*i]
                                break

                        #calculating the orbital period with sqrt[4*pi*r^3 / G * M] and converts the result into days
                        orbit_period = (math.sqrt((4*math.pow(math.pi, 2)*math.pow(float(orbit_distance), 3)) / ((6.674 * math.pow(10, -11)) * float(star_mass)))) / 60 / 60 / 24
                        try: #add the planet details into the corresponding lists
                            planet_list.append(planet_name)
                            planet_description_list.extend([planet_type, planet_life, planet_mass, orbit_object, orbit_period])
                            orbit_list.append(orbit_distance)
                            print("\n" + "You created the following planet, that orbits around " + orbit_object + ":" + "\n" + "name: " + planet_name + "\n" + "type: " + planet_type + "\n" + "life: " + planet_life + "\n" + "orbital period: " + str(orbit_period) + "\n" + "mass: " + planet_mass)
                        except:
                            print("Error occured")
                    if "".join(orbit_list).find(orbit_distance) != -1:
                        print("There is already an object on this orbit")

                else: #if no star was created prior to the attempt to create a planet
                    print("You have to create a star or a black hole before creating a planet.")

            case "Moon" | "moon":
                if planet_list != []: #if a planet exists
                    moon_name = input("What is the name of the moon?: ")#name
                    moon_mass = input("What is the mass of the moon?: ") #mass
                    moon_size = input("What is the radius of the moon?: ") #radius
                    print(("\n" * 2) + "The moon has to orbit a planet.")
                    print("\n" + "Here is a list of the planets:" + "\n" + ", ".join(planet_list)) #displays list of planets
                    orbit_object = input("What planet does the moon orbit around?: ") #asks for the orbit object

                    planet_mass = 0.0 #introduces the planet_mass variable
                    for i in range(len(planet_list)): #search for the orbit object in planet_list and change the planet_mass according to the data
                        if planet_list[i] == orbit_object:
                            planet_mass = planet_description_list[2 + 5*i]
                            break

                    orbit_radius = input("What is the distance between the moon and the planet?: ") #asks for the distance between moon and planet
                    if "".join(orbit_list).find(orbit_radius) == -1:
                        #calculates length of a year on the moon
                        orbit_period = (math.sqrt((4*math.pow(math.pi, 2)*math.pow(float(orbit_distance), 3)) / ((6.674 * math.pow(10, -11)) * float(planet_mass)))) / 60 / 60 / 24                
                    
                        moon_list.append(moon_name) #adds moon to the list
                        moon_list.extend([moon_mass, moon_size, orbit_object, orbit_period]) #adds the moon details to the corresponding list
                        orbit_list.append(orbit_radius)
                        print("You created the following moon, that orbits around " + orbit_object + "with a distance of " + orbit_radius)
                        print("name:", moon_name, "\n" + "mass:", moon_mass, "\n" + "radius:", moon_size)
                    if "".join(orbit_list).find(orbit_radius) != -1:
                        print("There is already an object on this orbit")
                else:
                    print("You have to create a planet, before you create a moon.")

            case "Asteroid Belt" | "asteroid belt" | "Asteroid belt" | "Asteroidbelt":
                if star_list != [] or black_hole_list != [] or planet_list != []:
                    belt_name = input("What is the name of the asteroid belt?: ")
                    belt_width = input("What is the width of the asteroid belt?: ")

                    print("The asteroid belt has to orbit a star, black hole or planet.")
                    print("Here is a list of the available objects:")
                    print(", ".join(star_list) + ", ".join(black_hole_list) + ", ".join(planet_list))
                    orbit_object = input("What object does the asteroid belt orbit around?: ")
                    orbit_radius = input("What is the distance between the asteroid belt and the object?: ")
                    if "".join(orbit_list).find(orbit_radius) == -1:
                        print("You created the following asteroid belt", belt_name, "that orbits around", orbit_object, "with a distance of", orbit_radius + ".")
                        print("name:", belt_name + "\n" + "width:", belt_width)
                        belt_list.append(belt_name)
                        belt_description_list.extend([belt_width, orbit_object, orbit_radius])
                        orbit_list.append(orbit_radius)
                    if "".join(orbit_list).find(orbit_radius) != -1:
                        print("There is already an object on this orbit")
                else:
                    print("You have to create a star, a black hole or a planet, before you can create an asteroid belt.")

            case "Life" | "life" | "Species" | "species": #create a species
                species_name = input("What is the species called?: ") #name
                species_lifespan = input("What is the average lifespan of the species?: ") #lifespan

                print("You created the following species: " + "\n" + "name: " + species_name + "\n" + "lifespan: " + species_lifespan)
                #add the species details to the list
                species_list.append(species_name)
                species_description_list.append(species_lifespan)
            
            case "Star" | "star" | "Sun" | "sun": #create a star or black hole, depending on mass
                #the equation used to calculate if the star becomes a black hole, is wrong.
                star_name = input("What is the name of the star?: ") #name
                star_size = input("What is the radius of the star?: ") #radius (m)
                star_temperature = input("What is the temperature of the star?: ") #temperature (°k)
                #to calculate the mass of the star, with the given parameters, use the Stefan-Boltzmann-Law to get the luminosity and then use the Mass-Luminosity-relation to calculate the mass of the star
                stefan_boltzmann_constant = 5.67 * pow(10, -8) #defining the stefan-boltzmann constant
                star_luminosity = stefan_boltzmann_constant * (4 * math.pi * pow(float(star_size), 2)) * pow(float(star_temperature), 4) #calculate the energy, that the star radiates
                star_mass = pow(star_luminosity / (3.846 * pow(10, 26)), (1/3.5)) * (1.9891 * pow(10, 30)) #calculate the mass of the star
                #Lichtgeschwindigkeit^2 * (Radius / 2 * Gravitationskonstante) calculates the neccessary mass for the object to become a black hole (currently wrong equasion)
                if (pow(3 * pow(10, 8), 2) * (float(star_size) / (2 * (6.674 * pow(10, -11)))) <= star_mass): #if the mass of the star exceeds the limit, the star instantly becomes a black hole
                    print("You created the following black hole: " + "\n" + "name:", star_name + "\n" "size:", star_size + "\n" + "temperature:", star_temperature + "\n" + "mass:", str(star_mass))
                    #add the black hole details into the corresponding lists
                    black_hole_list.append(star_name)
                    black_hole_horizon = 2 * (6.674 * pow(10, -11)) * (star_mass / (3 * pow(10, 8)))
                    black_hole_description_list.extend([black_hole_horizon, star_mass])
                else:# if the star doesnt collapse into a black hole
                    print("You created the following star: " + "\n" + "name:", star_name + "\n" + "size:", star_size + "\n" + "temperature:", star_temperature + "\n" + "mass:", str(star_mass))
                    #adds the star details into the corresponding lists
                    star_list.append(star_name)
                    star_description_list.extend([star_size, star_temperature, star_mass])
    
    if thing_to_do == "Destroy" or thing_to_do == "destroy": #remove an object from the programm
        destroy_object_type = input("What kind of object do you want to destrory?: ") #asks for the type of object to destroy

        match destroy_object_type:
            case "Planets" | "planets" | "Planet" | "planet": #if you choose to destroy a planet
                print("Here is a list of the available planets:")
                print(", ".join(planet_list)) #creates the list of the available planets
                destroy_object = input("Which planet do you want to destroy?: ") #asks for the planet to destroy
                destroy_index = 0 #introduces the variable for the destroy_index variable
                for i in range(len(planet_list)): #find the object in the planet_list and change the destroy_index to its index
                    if planet_list[i] == destroy_object:
                        destroy_index = i
                        break
                planet_list.pop(0 + destroy_index) #remove the planet name from the planet_list
                planet_description_list.pop(0 + 5 * destroy_index) #removes the details of the planet from the corresponding list
                planet_description_list.pop(0 + 5 * destroy_index)
                planet_description_list.pop(0 + 5 * destroy_index)
                planet_description_list.pop(0 + 5 * destroy_index)
                print("The planet was successfully destroyed.")
            
            case "Moon" | "moon":
                print("Here is a list of the available moons:" + "\n" + ", ".join(moon_list))
                destroy_object = input("Which moon do you want to destroy?: ")
                destroy_index = 0
                for i in range(len(moon_list)):
                    if moon_list[i] == destroy_object:
                        destroy_index = i
                        break
                planet_list.pop(0 + destroy_index)
                planet_description_list.pop(0 + 4*destroy_index)
                planet_description_list.pop(0 + 4*destroy_index)
                planet_description_list.pop(0 + 4*destroy_index)
                planet_description_list.pop(0 + 4*destroy_index)
                print("The moon was successfully destroyed.")

            case "Asteroid Belt" | "asteroid belt" | "Asteroid belt" | "Asteroidbelt":
                print("Here is a list of the available asteroid belts:" + "\n" + ", ".join(belt_list))
                destroy_object = input("Which asteroid belt do you want to destroy?: ")
                destroy_index = 0
                for i in range(len(belt_list)):
                    if belt_list[i] == destroy_object:
                        destroy_index = i
                        break
                belt_list.pop(0 + destroy_index)
                belt_description_list.pop(0 + 3*destroy_index)
                belt_description_list.pop(0 + 3*destroy_index)
                belt_description_list.pop(0 + 3*destroy_index)
                print("The asteroid belt was successfully destroyed.")

            case "Species" | "species" | "Life" | "life": #if you choose to destroy a species
                print("Here is a list of the available species:")
                print(", ".join(species_list)) #creates a list of the available species
                destroy_object = input("Which species do you want to destroy?: ") #asks for the specific species to destroy
                destroy_index = 0 #introduces the destroy_index variable
                for i in range(len(species_list)): #search for the species in the species_list and change destroy_index to its index
                    if species_list[i] == destroy_object:
                        destroy_index = i
                        break
                species_list.pop(0 + destroy_index) #remove the species name from the list
                species_description_list.pop(0 + destroy_index) #remove the species details from the list
                print("The species was successfully anihilated.")
            
            case "Star" | "star" | "Sun" | "sun": #if you choose to destroy a star
                print("Here is a list of the availaible stars:")
                print(", ".join(star_list)) #creates a list of the available stars
                destroy_object = input("Which star do you want to destroy?: ") #asks fro the specific star to destroy
                destroy_index = 0 #introduces the destroy_index variable
                for i in range(len(star_list)): #search for the star in the star_list and change destroy_index to its index
                    if star_list[i] == destroy_object:
                        destroy_index = i
                        break
                star_list.pop(0 + destroy_index) #remove the name of the star from the list
                star_description_list.pop(0 + 3 * destroy_index) #remove the star details from the list
                star_description_list.pop(0 + 3 * destroy_index)
                star_description_list.pop(0 + 3 * destroy_index)
                print("The star was successfully destroyed.")

            case "Black Hole" | "black hole" | "Black hole" | "Blackhole" | "blackhole": #if you choose to destroy a black hole
                print("Here is a list of the available black holes:")
                print(", ".join(black_hole_list)) #creates a list of the available black holes
                destroy_object = input("Which black hole do you want to destroy?: ") #asks for the specific black hole to destroy
                destroy_index = 0 #introduces the destroy_index variable
                for i in range(len(black_hole_list)): #searches for the black hole in the black_hole_list
                    if black_hole_list[i] == destroy_object:
                        destroy_index = i
                        break
                black_hole_list.pop(0 + destroy_index) #remove the name of the black hole from the list
                black_hole_description_list.pop(0 + 2 * destroy_index) #remove the black hole details from the list
                black_hole_description_list.pop(0 + 2 * destroy_index)
                print("The black hole was successfully destroyed.")
    
    if thing_to_do == "info" or thing_to_do == "Info": #request information about an object
        info_object = input("What info do you request?: ") #asks for the type of object you want to know more about
        
        match info_object:
            case "Planets" | "planets" | "Planet" | "planet": #if you want to know more about a planet
                print("Here is a list of the currently available planets: " + "\n" + ", ".join(planet_list)) #shows a list of the available planets
                planet_to_check = input("What planet do you want to know more about?: ") #asks for the specific planet you want to know more about
                planet_index = 0 #introduces the planet_index variable
                for i in range(len(planet_list)): #searches for the planet in the planet_list
                    if planet_list[i] == planet_to_check:
                        planet_index = i
                        break
                try:
                    print("Here is the requested info regarding " + planet_to_check) #displays the requested information about the planet
                    print("type: " + planet_description_list[0 + 5 * planet_index])
                    print("life: " + planet_description_list[1 + 5 * planet_index])
                except:
                    print("Error occured")
            
            case "Moon" | "moon":
                print("Here is a list of the currently available moons:" + "\n" + ", ".join(moon_list))
                moon_to_check = input("What moon do you want to know more about?: ")
                moon_index = 0
                for i in range(len(moon_list)):
                    if moon_list[i] == moon_to_check:
                        moon_index = i
                        break
                try:
                    print("Here is the requested info regarding", moon_to_check)
                    print("mass:", moon_description_list[0 + 4*moon_index])
                    print("radius:", moon_description_list[1 + 4*moon_index])
                    print("orbit object:", moon_description_list[2 + 4*moon_index])
                    print("year length:", moon_description_list[3 + 4*moon_index])
                except:
                    print("Error occured")

            case "Asteroid Belt" | "asteroid belt" | "Asteroid belt" | "Asteroidbelt":
                print("Here is a list of the currently available asteroid belts" + "\n" + ", ".join(belt_list))
                belt_to_check = input("What asteroid belt do you want to know more about?: ")
                belt_index = 0
                for i in range(len(belt_list)):
                    if belt_list[i] == belt_to_check:
                        belt_index = i
                        break
                try:
                    print("Here is the requested info regarding", belt_to_check)
                    print("width:", belt_description_list[0 + 3*belt_index])
                    print("orbit object:", belt_description_list[1 + 3*belt_index])
                    print("orbit radius:", belt_description_list[2 + 3*belt_index])
                except:
                    print("Error occured")


            case "Species" | "species" | "Life" | "life": #if you want to know more about a planet
                print("Here is a list of the currently available species: " + "\n" + ", ".join(species_list)) #displays a list of the available species
                species_to_check = input("What species do you want to know more about?: ") #asks for the specific species you want to know more about
                species_index = 0 #introduces the species_index variable
                for i in range(len(species_list)): #searches for the species in the species_list
                    if species_list[i] == species_to_check:
                        species_index = i
                        break
                try:
                    print("Here is the requested info regarding " + species_to_check) #displays the requested information about the species
                    print("lifespan: " + species_description_list[0 + species_index])
                except:
                    print("Error occured")
            
            case "Star" | "star" | "Sun" | "sun": #if you want to know more about a star
                print("Here is a list of the currently available stars: " + "\n" + ", ".join(star_list)) #displays a list of the available stars
                star_to_check = input("Which star do you want to know more about?: ") #asks for the specific star you want to know more about
                star_index = 0 #introduces the star_index variable
                for i in range(len(star_list)): #searches for the star in the star_list
                    if star_list[i] == star_to_check:
                        star_index = i
                        break
                try:
                    print("Here is the requested info regarding", star_to_check) #display the requested information about the star
                    print("size:", star_description_list[0 + 3 * star_index])
                    print("temperature:", star_description_list[1 + 3 * star_index])
                    print("mass:", star_description_list[2 + 3* star_index])
                except:
                    print("Error occured")
            
            case "Black Hole" | "black hole" | "Black hole" | "Blackhole" | "blackhole": #if you want to know more about a black hole
                print("Here is a list of the currently available black holes: " + "\n" + ", ".join(black_hole_list)) #displays a list of the available black holes
                black_hole_to_check = input("Which black hole do you want to know more about?: ") #asks for the specific black hole you want to know more about
                black_hole_index = 0 #introduces the black_hole_index variable
                for i in range(len(black_hole_list)): #searches for the black hole in the black_hole_list
                    if black_hole_list[i] == black_hole_to_check:
                        black_hole_index = i
                        break
                try:
                    print("Here is the requested info regarding " + black_hole_to_check) #displays the requested information about the black hole
                    print("name:", black_hole_list[black_hole_index])
                    print("size:", black_hole_description_list[0 + (2 * black_hole_index)])
                    print("mass:", black_hole_description_list[1 + (2 * black_hole_index)])
                except:
                    print("Error occured")

    if thing_to_do == "Exit" or thing_to_do == "exit": #stops the programm
        print("Shutting down...")
        quit() #stops the programm