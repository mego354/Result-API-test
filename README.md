# Medical Data API

This project is an API designed for an educational device that reads medical results such as blood pressure, temperature, heart rate, blood oxygen levels, and blood sugar levels. The API allows a microcontroller to save these results in a web application, making the data available for further analysis and monitoring.

## Table of Contents

- [Technologies Used](#technologies-used)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [API Endpoint](#api-endpoint)
  - [Example Usage](#example-usage)
- [Contributing](#contributing)
- [License](#license)

## Technologies Used

- Django
- SQLite (default, can be replaced with any other database)
- JSON

## Features

- **Data Collection:** The API collects data from a microcontroller.
- **Data Storage:** Saves medical readings such as temperature, blood pressure, heart rate, blood oxygen level, and blood sugar level.
- **User Authentication:** Basic authentication for accessing the API.
- **Data Visualization:** Access saved data through a web application.

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/mego354/Result-API-test-.git
    cd MedicalDataAPI
    ```

2. **Apply migrations:**

    ```sh
    python manage.py migrate
    ```

3. **Create a superuser:**

    ```sh
    python manage.py createsuperuser
    ```

4. **Run the development server:**

    ```sh
    python manage.py runserver
    ```

## Usage

### API Endpoint

- The API endpoint for submitting data is:

    ```
    http://HOST_URL/arduino_data/
    ```

    Replace `HOST_URL` with the actual host URL, e.g., `http://127.0.0.1:8000/arduino_data/` for local development.

### Example Usage

1. **Prepare the data:**

    Copy the following `curl` command:

    ```sh
    curl -X POST -H "Content-Type: application/json" -d "{\"temp\": 36.6, \"press\": 1013, \"h_rate\": 72, \"b_oxy\": 98, \"sugar\": 5.5}" http://127.0.0.1:8000/arduino_data/
    ```

2. **Open Command Prompt:**

    Open your command prompt or terminal.

3. **Paste the command:**

    Paste the copied `curl` command into the command prompt.

4. **Execute the command:**

    Press `Enter` to execute the command. This will send a POST request to the API with the medical data.

5. **Verify the result:**

    Go to the main page of the web application to see the submitted results.

### User Authentication

- **Username:** megahd
- **Password:** firstuser

Use these credentials to authenticate your API requests if necessary.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## Contact

For any inquiries or issues, please contact [me](https://github.com/mego354).
