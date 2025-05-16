# 🦁 Animal Website Builder

Generate a beautiful, static HTML page showcasing information about any animal 
powered by the Ninjas Animals API and simple Python!

---

## 🚀 Features

- **Fetch animal data**  
  Pulls diet, habitat, classification, and more via the Ninjas Animals API.


- **Dynamic HTML generation**  
  Injects JSON data into a customizable HTML template.


- **Graceful error handling**  
  Alerts you if the template is missing or the animal isn’t found.


- **Zero-dependency front-end**  
  Pure HTML/CSS (no frameworks) so it’s lightning-fast and easy to style.

---

## 🛠️ Prerequisites

- Python 3.7 or higher  
- [requests](https://pypi.org/project/requests/)  
- [python-dotenv](https://pypi.org/project/python-dotenv/)  

---

## 🎬 Usage
- **Prompt: You’ll be asked to enter an animal name (e.g., “fox”).**

- **Output: A file named *animals.html* is created in your project root folder.**

- **View: Open *animals.html* in your browser to see the animal cards!**

---

## 📝 File Overview
*website_builder.py* is the main script that:

- prompts for an animal name

- fetches data via data_fetcher.py

- injects data into animals_template.html

- writes out animals.html

*data_fetcher.py* handles the communication with the Ninjas API using your API_KEY.

*animals_template.html* contains the static HTML/CSS boilerplate and a placeholder for dynamic content.

*animals.html* is the auto-generated file with your chosen animal’s data.
