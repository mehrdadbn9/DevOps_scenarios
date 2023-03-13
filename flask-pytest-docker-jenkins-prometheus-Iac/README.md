# User Collector App

This is a simple Flask application that collects user data via a form and stores it in a database.

## Installation

To install and run the application locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/your-github-username/user-collector-app.git
   cd user-collector-app
   ```

2. Create a virtual environment and activate it:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Start the Flask development server:

   ```bash
   export FLASK_APP=app.py
   export FLASK_ENV=development
   flask run
   ```

5. Navigate to `http://localhost:5000` in your web browser to access the application.

## Running Tests

To run the unit tests for the application, use the following command:

```bash
pytest
```

## Building and Running with Docker

To build a Docker image of the application, use the following command:

```bash
docker build -t user-collector-app .
```

To run the Docker image, use the following command:

```bash
docker run -p 5000:5000 user-collector-app
```
