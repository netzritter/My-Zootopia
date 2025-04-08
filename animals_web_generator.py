import json

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


def generate_animal_summary(animals):
    """Generate a string with animal information."""
    animal_info = ""
    for animal in animals:
        animal_info += f"Name: {animal['name']}\n"
        animal_info += f"Diet: {animal.get('characteristics', {}).get('diet', 'Unknown')}\n"
        animal_info += f"Location: {animal['locations'][0]}\n"
        animal_info += f"Type: {animal.get('characteristics', {}).get('type', 'Unknown')}\n\n"
    return animal_info


def create_final_html(animals):
    """Replace placeholder with animal info and return final HTML string."""
    template = read_html("animals_template.html")
    animal_data_string = generate_animal_summary(animals)

    if template is None or animal_data_string is None:
        raise ValueError("Template or animal data string is None")

    final_html = template.replace("__REPLACE_ANIMALS_INFO__", animal_data_string)

    return final_html


def save_final_html_template(combined_content):
    with open("animals.html", "w", encoding="utf-8") as output_file:
        output_file.write(combined_content)
        print("HTML output successfully written to animals.html")


def main():
    # Load the animal data and the HTML template
    animals = load_data("animals_data.json")
    final_html = create_final_html(animals)

    # Write the combined content to the "animals.html" file
    save_final_html_template(final_html)


if __name__ == "__main__":
    main()
