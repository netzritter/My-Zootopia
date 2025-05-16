import json
import data_fetcher

def load_data(file_path):
    """Load a JSON file."""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def read_html(file_path):
    """Read HTML template as a string."""
    try:
        with open(file_path, "r", encoding="utf-8") as file_obj:
            return file_obj.read()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return ""


def serialize_animal(animal_obj):
    unique_animal_html = f'''
        <li class="cards__item">
            <div class="card__title">{animal_obj['name']}</div>
            <p class="card__text">
                <strong>Diet:</strong> {animal_obj.get('characteristics', {}).get('diet', 'Unknown')}<br/>
                <strong>Location:</strong> {animal_obj['locations'][0]}<br/>
                <strong>Type:</strong> {animal_obj.get('characteristics', {}).get('type', 'Unknown')}<br/>
            </p>
        </li>'''
    return unique_animal_html


def generate_animal_summary(animals):
    """Generate a string with animal information."""
    animal_info = ""
    for animal in animals:
        animal_info += serialize_animal(animal)
    return animal_info


def create_final_html(animals, searched_name):
    """Replace placeholder with animal info and return final HTML string."""
    template = read_html("animals_template.html")


    if not template:
        raise ValueError("Template or animal data string is empty")

    if not animals:
        animal_data_string = f'<h2 style="text-align: center;">The animal "{searched_name}" doesn\'t exist.</h2>'

    else:
        animal_data_string = generate_animal_summary(animals)


    final_html = template.replace("__REPLACE_ANIMALS_INFO__", animal_data_string)

    return final_html


def save_final_html_template(combined_content):
    with open("animals.html", "w", encoding="utf-8") as output_file:
        output_file.write(combined_content)
        print("HTML output successfully written to animals.html")


def main():

    display_chosen_animal = input("Enter a name of an animal: ")
    # Fetch animal data from the Ninjas API
    animals = data_fetcher.fetch_data(display_chosen_animal)

    final_html = create_final_html(animals, display_chosen_animal)

    # Write the combined content to the "animals.html" file
    save_final_html_template(final_html)


if __name__ == "__main__":
    main()
