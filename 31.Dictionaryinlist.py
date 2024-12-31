"""
You are going to write a program that addds to a travel_log.You can see a travel_log which is a list that contains two dictionaries.

write a function that will work with the following line of code on line 21 to add the entry for Russia to the travel_log

"""
#this is a lista
travel_log = [    

    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris","Lille","Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berline", "Hamburg", "stuttgart"]
    },
]

#Write the function that will allow new countries to be added to the travel_log
#this function takes positional arguments
def add_new_country(add_country,add_visit,add_city):
    new_country = {} #we created a new dictionary and added the data through arguments
    new_country["country"] = add_country
    new_country["visits"] = add_visit
    new_country["cities"] = add_city
    travel_log.append(new_country) # then we addded this new dictionary to the travel_log list

add_new_country("Russia",2,["Moscow", "Saint Petersburg"])
print(travel_log)