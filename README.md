
# User Management System

The User Management System is a simple application that facilitates user registration, authentication, retrieval, update, and deletion operations. It employs Firebase Realtime Database for efficient storage and management of user data.

## Features

- **User Registration**: Register new users by providing their name, username, email, and password. The passwords are securely hashed using bcrypt before being stored in the database.
  
- **User Authentication**: Authenticate users by verifying their username and password against the hashed password stored in the database.
  
- **User Retrieval**: Retrieve user data by username or user ID.
  
- **User Update**: Update user data such as name, email, or password.
  
- **User Deletion**: Delete a user from the database.

## Setup Instructions

1. **Clone the Repository or Create a Folder**
   
   Clone the repository from GitHub or create a new folder for your project.

2. **Create a Virtual Environment**

   Use the following commands to create and activate a virtual environment:

   ```bash
   # For macOS
   python3 -m venv env
   source ./env/bin/activate

   # For Windows
   python -m venv env
   source ./env/Scripts/activate
   ```

3. **Install Dependencies**

   Install the required dependencies using pip:

   ```bash
   pip install python-dotenv firebase-rest-api bcrypt
   ```

4. **Firebase Setup**

   Follow these steps to set up Firebase:
   
   - Login to Firebase and create a new project.
   - Add a new app using the web app option and copy the provided config details.
   - Create a real-time database and set it to test mode.
   - Create a `.env` file in your project directory and paste the Firebase config details:

     ```dotenv
     apiKey=your_api_key
     authDomain=your-project-id.firebaseapp.com
     databaseURL=https://your-project-id.firebaseio.com
     projectId=your-project-id
     storageBucket=your-project-id.appspot.com
     messagingSenderId=your_messaging_sender_id
     appId=your_app_id
     measurementId=your_measurement_id
     ```

## Usage

Create a `main.py` file and import the required functions from the `user_management` module:

```python
from user_management import save_user, get_users, get_user, update_user, get_user_by_id, delete_user
```

Use the functions to perform desired operations:

```python
# Save a new user
save_user("John Doe", "johndoe", "johndoe@example.com", "password123")

# Retrieve all users
users = get_users()
print(users)

# Retrieve a user by username
user = get_user("johndoe")
print(user)

# Update user data
update_user("johndoe", {"email": "newemail@example.com"})

# Retrieve a user by ID
user_by_id = get_user_by_id("user_id")
print(user_by_id)

# Delete a user
delete_user("johndoe")
```