import API.v1
import Model
from Persistence.datamanager import data_manager

countries = [
    {"name": "Germany", "code": "DE", "cities": [
        {"name": "Berlin", "zipcode": "10115"},
        {"name": "Munich", "zipcode": "80331"},
        {"name": "Hamburg", "zipcode": "20095"},
        {"name": "Cologne", "zipcode": "50667"},
        {"name": "Frankfurt", "zipcode": "60311"},
    ]},
    {"name": "United States", "code": "US", "cities": [
        {"name": "New York", "zipcode": "10001"},
        {"name": "Los Angeles", "zipcode": "90001"},
        {"name": "Chicago", "zipcode": "60601"},
        {"name": "Houston", "zipcode": "77001"},
        {"name": "Phoenix", "zipcode": "85001"},
    ]},
    {"name": "United Kingdom", "code": "UK", "cities": [
        {"name": "London", "zipcode": "EC1A 1BB"},
        {"name": "Birmingham", "zipcode": "B1 1AA"},
        {"name": "Manchester", "zipcode": "M1 1AG"},
        {"name": "Glasgow", "zipcode": "G1 1AA"},
        {"name": "Liverpool", "zipcode": "L1 8JQ"},
    ]}
]

for i in range(len(countries)):
    Model.Country(name=countries[i]["name"], code=countries[i]["code"])
    for j in range(len(countries[i]["cities"])):
        Model.City(name=countries[i]["cities"][j]["name"], zipcode=countries[i]["cities"][j]["zipcode"], country_id=i+1)

data_manager.save()

API.v1.app.run()