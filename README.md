# Django RESTful API Project

Welcome to the Django RESTful API project! This project includes a RESTful API application built using Django.

## Setup and Running

To set up and run the application, follow these steps:

1. **Clone this repository to your local machine:**
````````````````````````````````````````````````````
git clone <repository_url>
````````````````````````````````````````````````````

2. **Navigate into the project directory:**
````````````````````````````````````````````````````
cd <project_directory>
````````````````````````````````````````````````````

3. **Create and activate a virtual environment:**
````````````````````````````````````````````````````
python3 -m venv venv  # On macOS/Linux
source venv/bin/activate # On macOS/Linux

python -m venv venv # On Windows
venv\Scripts\activate # On Windows
````````````````````````````````````````````````````

4. **Install dependencies:**
````````````````````````````````````````````````````
pip install -r requirements.txt
````````````````````````````````````````````````````

5. **Navigate into the app folder**
````````````````````````````````````````````````````
cd kaizn
````````````````````````````````````````````````````

6. **Start the development server:**
````````````````````````````````````````````````````
python manage.py runserver
````````````````````````````````````````````````````

7. Access the API endpoints at `http://localhost:8000/`

## API Documentation

### User Endpoints

#### Register User

Registers a new user.

- URL: `/register/`
- Method: `POST`
- Request Body:
  - `username` (string, required): The username of the new user.
  - `password1` (string, required): The password of the new user.
  - `password2` (string, required): Confirmation of the password.

#### Login User

Logs in an existing user.

- URL: `/`
- Method: `POST`
- Request Body:
  - `username` (string, required): The username of the user.
  - `password` (string, required): The password of the user.

---

### Product Endpoints

#### List Products

Retrieves a list of products.

- URL: `/product/`
- Method: `GET`
- Query Parameters:
  - `search_query` (string, optional): Search query to filter products.
  - `category` (string, optional): Filter products by category.
  - `stock_status` (float, optional): Filter products by stock status.
  - `sort_by` (string, optional): Sort products by a field.

#### Create Product

Creates a new product.

- URL: `/CreateProduct/`
- Method: `POST`
- Request Body:
  - `sku` (string, required): The SKU of the product.
  - `name` (string, required): The name of the product.
  - `category` (string, required): The category of the product.
  - `tags` (string, required): The tags associated with the product.
  - `stock_status` (float, required): The stock status of the product.
  - `available_stock` (float, required): The available stock of the product.

---

### Password Reset Endpoints

#### Request Password Reset

Sends a password reset email to the user.

- URL: `/reset_password/`
- Method: `GET`

#### Confirm Password Reset

Confirms the password reset request.

- URL: `/reset/<uidb64>/<token>/`
- Method: `GET`
- Path Parameters:
  - `uidb64` (string, required): User ID encoded in base64.
  - `token` (string, required): Token for password reset.

#### Complete Password Reset

Completes the password reset process.

- URL: `/reset_password_complete/`
- Method: `GET`

---

This documentation outlines all the endpoints in this application, along with their corresponding URLs, methods, parameters, and request/response formats. 

## Unit Tests

Unit tests have been provided for each API endpoint to ensure functionality and reliability. To run the tests, use the following command:
````````````````````````````````````````````````````
python manage.py test
````````````````````````````````````````````````````








