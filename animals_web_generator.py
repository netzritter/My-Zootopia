import json

def load_data(file_path):
    """Load as JSON file"""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


animals = load_data("animals_data.json")


def print_specific_animal_data(animals_db):
    for animal in animals:
        if "name" in animal:
            print("Name:", animal["name"].upper())

        diet = animal.get("characteristics", {}).get("diet")
        if diet:
            print("Diet:", diet)

        # Print first location and check if locations exist
        locations = animal.get("locations")
        if locations and len(locations) > 0:
            print("Location:", locations[0])

        animal_type = animal.get("characteristics", {}).get("type")
        if animal_type:
            print("Type:", animal_type.capitalize())
        print()

def main():

    print_specific_animal_data(animals)

if __name__ == "__main__":
    main()
