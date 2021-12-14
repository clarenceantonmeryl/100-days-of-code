"""
dictionary = {1:2,
              2:3,
              3:4,}

for thing in dictionary:
    print(thing, dictionary[thing])


student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}

grade = ""

for key in student_scores:
    if student_scores[key] >= 91:
        grade = "Outstanding"
    elif student_scores[key] >= 81:
        grade = "Exceeds Expectations"
    elif student_scores[key] >= 71:
        grade = "Acceptable"
    else:
        grade = "Fail"

    student_grades[key] = grade

for key in student_scores:
    print(f"{key}: {student_grades[key]}")

"""


travel_log = [
    {
        "country": "France",
        "cities_visited": [
            "Paris",
            "Lille",
            "Dijon"
        ],
        "number_of_visits": 12
    },
    {
        "country": "Germany",
        "cities_visited": [
            "Berlin",
            "Hamburg",
            "Stuttgart"
        ],
        "number_of_visits": 5
    }
]


def add_new_country(country, cities_visited, number_of_visits):
    country_dictionary = {}
    country_dictionary["country"] = country
    country_dictionary["cities_visited"] = cities_visited
    country_dictionary["number_of_visits"] = number_of_visits
    travel_log.append(country_dictionary)


add_new_country(country="Russia", cities_visited=["Moscow", "Saint Petersburg"], number_of_visits=2)

print(travel_log)

starting_dictionary = {
    "a": 9,
    "b": 8,
}

final_dictionary = {
    "a": 9,
    "b": 8,
    "c": 7,
}

starting_dictionary["c"] = 7

final_dictionary = starting_dictionary["c"] = 7


print(starting_dictionary)
print(final_dictionary)
