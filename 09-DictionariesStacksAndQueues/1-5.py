# Create an array with 5 dictionaries, each containing a country and its population.
# Then, print the array contents. Sample result:

# COUNTRY  POPULATION
# Poland   38000000
# …        …
# …        …
# …        …
# …        …

countries = [
{"country":"Poland", "population":38000000},
{"country":"Turkey", "population":55645000},
{"country":"Thailand", "population":2140000},
{"country":"Slovakia", "population":2455000},
{"country":"Germany", "population":50000000}
]

print("COUNTRY      POPULATION")

for dict in countries:
    print(f"{dict['country']}       {dict['population']}")