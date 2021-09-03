# ITP Week 2 Day 1 (In-Class) Practice

# Dictionary

person_1 = {
    "first_name": "Scooby",
    "favorite_snack": "Rare Candy",
    "wears_glasses": True
    }

# verify the type of person_1 to be a dictionary by using type
print(type(person_1))

# add a key value pair to person_1 with the last_name of Doo
person_1.update({"last_name": "Doo"}) # Good for JSON interaction.
print(person_1.items())

# update person_1 favorite_snack to "Scooby Snacks"
# person_1["favorite_snack"] = "Scooby Snacks"
person_1.update({"favorite_snack": "Scooby Snacks"}) # preferred method

# Remove the "wears_glasses" key:value from person_1
person_1.pop("wears_glasses")