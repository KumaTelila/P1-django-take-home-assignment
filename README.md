
# Food Truck Finder

Food Truck Finder is a Django-based web application that helps users discover nearby food trucks in San Francisco.

## Installation

Follow these steps to install and run the project locally:

### Prerequisites

- Python 3.9 or higher
- pip (Python package manager)

### Clone the Repository

```bash
git clone https://github.com/KumaTelila/P1-django-take-home-assignment.git
cd P1-django-take-home-assignment
```

### Create and Activate Virtual Environment

```bash
python3 -m venv env
source env/bin/activate      # On Windows, use `env\Scripts\activate`
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Set Up Database

```bash
python manage.py migrate
```

### Load Data

```bash
python manage.py load_data
```

### Run the Server

```bash
python manage.py runserver
```

The application will be accessible at `http://localhost:8000`.

## Usage

1. Navigate to the homepage.
2. Pick a point on the map to find nearby food trucks.
3. View the list of nearby food trucks with their Facility Type, addresses, and Loaction Description.

## Technologies Used

- Django 4.2
- Python 3.x
- HTML/CSS
- JavaScript (Leaflet.js for map integration)

## Contributing

Contributions are welcome! Please submit any bug reports, feature requests, or pull requests through the repository's issue tracker and pull request system.

## License



--- 
