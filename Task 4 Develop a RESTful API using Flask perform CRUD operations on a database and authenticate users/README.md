# Flask REST API with JWT Authentication

This project is a RESTful API built with Flask, SQLAlchemy, Flask-Migrate, and Flask-JWT-Extended. The application includes user authentication and CRUD operations for items.

## Features

- User registration and login with JWT authentication
- CRUD operations for items
- SQLAlchemy for database ORM
- Flask-Migrate for database migrations

## Requirements

- Python 3.8+
- Flask
- Flask-RESTful
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-JWT-Extended
- Werkzeug

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```

2. Create and activate a virtual environment:
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Set up the database:
    ```sh
    flask db init
    flask db migrate
    flask db upgrade
    ```

5. Set the environment variable for the JWT secret key:
    ```sh
    export JWT_SECRET_KEY='your_jwt_secret_key'  # On Windows use `set JWT_SECRET_KEY=your_jwt_secret_key`
    ```

## Running the Application

1. Start the Flask application:
    ```sh
    flask run
    ```

2. The API will be available at `http://127.0.0.1:5000/`.

## API Endpoints

### User Registration
- **URL:** `/register`
- **Method:** `POST`
- **Payload:**
    ```json
    {
        "username": "your_username",
        "password": "your_password"
    }
    ```
- **Response:**
    ```json
    {
        "message": "User created successfully"
    }
    ```

### User Login
- **URL:** `/login`
- **Method:** `POST`
- **Payload:**
    ```json
    {
        "username": "your_username",
        "password": "your_password"
    }
    ```
- **Response:**
    ```json
    {
        "access_token": "your_jwt_token"
    }
    ```

### Get All Items
- **URL:** `/items`
- **Method:** `GET`
- **Headers:**
    ```json
    {
        "Authorization": "Bearer your_jwt_token"
    }
    ```
- **Response:**
    ```json
    [
        {
            "id": 1,
            "name": "Item 1",
            "description": "Description of Item 1"
        },
        ...
    ]
    ```

### Create an Item
- **URL:** `/items`
- **Method:** `POST`
- **Headers:**
    ```json
    {
        "Authorization": "Bearer your_jwt_token"
    }
    ```
- **Payload:**
    ```json
    {
        "name": "Item Name",
        "description": "Item Description"
    }
    ```
- **Response:**
    ```json
    {
        "id": 1,
        "name": "Item Name",
        "description": "Item Description"
    }
    ```

### Get an Item
- **URL:** `/item/<int:item_id>`
- **Method:** `GET`
- **Headers:**
    ```json
    {
        "Authorization": "Bearer your_jwt_token"
    }
    ```
- **Response:**
    ```json
    {
        "id": 1,
        "name": "Item Name",
        "description": "Item Description"
    }
    ```

### Delete an Item
- **URL:** `/item/<int:item_id>`
- **Method:** `DELETE`
- **Headers:**
    ```json
    {
        "Authorization": "Bearer your_jwt_token"
    }
    ```
- **Response:**
    ```json
    {
        "message": "Item deleted"
    }
    ```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

Flask==2.0.3
Flask-RESTful==0.3.9
Flask-SQLAlchemy==2.5.1
Flask-Migrate==3.1.0
Flask-JWT-Extended==4.3.1
Werkzeug==2.0.3

Muhammad Uwaim Qureshi
