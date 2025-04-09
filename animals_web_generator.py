import json
import requests

def fetch_animals_via_api(animal_name):
    name = 'fox'
    api_url = 'https://api.api-ninjas.com/v1/animals?name={}'.format(name)
    response = requests.get(api_url, headers={'X-Api-Key': 'NNR+gvwnOieCOlD1UTKwgg==TOmLuXY9iC6jQMko'})
    if response.status_code == requests.codes.ok:
        return response.json()
    else:
        print("Error:", response.status_code, response.text)
        return []


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


def create_final_html(animals):
    """Replace placeholder with animal info and return final HTML string."""
    template = read_html("animals_template.html")
    animal_data_string = generate_animal_summary(animals)

    if not template or not animal_data_string:
        raise ValueError("Template or animal data string is empty")

    final_html = template.replace("__REPLACE_ANIMALS_INFO__", animal_data_string)

    return final_html


def save_final_html_template(combined_content):
    with open("animals.html", "w", encoding="utf-8") as output_file:
        output_file.write(combined_content)
        print("HTML output successfully written to animals.html")


def main():
    # Fetch animal data from the API instead of the local JSON file
    animals = fetch_animals_via_api("fox")

    if not animals:
        print("No animal data found.")
        return
    final_html = create_final_html(animals)

    # Write the combined content to the "animals.html" file
    save_final_html_template(final_html)


if __name__ == "__main__":
    main()
