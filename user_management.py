from config import database
from bson import ObjectId
import bcrypt 

def save_user(name, username, email, password):
    """
    Adds a new user to the database if the username is not already taken.

    Parameters:
    - name (str): The name of the user.
    - username (str): The username of the user.
    - email (str): The email address of the user.
    - password (str): The password of the user.

    Returns:
    - dict: A dictionary containing success status, message, and user data if successful, otherwise an error message.
    """
    # Check if the username already exists
    existing_user = database.child("user").child(username).get()
    if existing_user.val() is not None:
        return {
            "success": False,
            "message": "Username already exists"
        }
    
    # Hash the password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    # If the username is unique, add the new user
    user_data = {
        "_id": str(ObjectId()),
        "name": name,
        "username": username,
        "password": hashed_password,  # Store the hashed password
        "email": email
    }
    response = database.child("user").child(username).set(user_data)
    if response is None:
        return {
            "success": False,
            "message": "Error adding user"
        }
    return {
        "success": True,
        "message": "User added successfully",
        "response": user_data
    }


def get_users():
    """
    Retrieves all users from the database.

    Returns:
    - dict: A dictionary containing success status, message, and user data if successful, otherwise an error message.
    """
    users = database.child("user").get()
    user_list = []
    for user in users.each():
        user_list.append(user.val())
    if len(user_list) == 0:
        return {
            "success": False,
            "message": "No users found"
        }
    return {
        "success": True,
        "message": "All users found",
        "response": user_list
    }

def get_user(username):
    """
    Retrieves a user by username from the database.

    Parameters:
    - username (str): The username of the user to retrieve.

    Returns:
    - dict: A dictionary containing success status, message, and user data if successful, otherwise an error message.
    """
    user = database.child("user").child(username).get()
    if user.val():
        return {
            "success": True,
            "message": f"User '{username}' found",
            "response": dict(user.val())
        }
    else:
        return {
            "success": False,
            "message": f"User '{username}' does not exist."
        }

def update_user(username, data):
    """
    Updates user data in the database.

    Parameters:
    - username (str): The username of the user to update.
    - data (dict): A dictionary containing the fields to update.

    Returns:
    - dict: A dictionary containing success status and message if successful, otherwise an error message.
    """
    user = database.child("user").child(username).get()
    if user.val() is not None:
        updated_user = database.child("user").child(username).update(data)
        if updated_user is None:
            return {
                "success": False,
                "message": "Error updating user"
            }
        return {
            "success": True,
            "message": "User updated successfully"
        }
    else:
        return {
            "success": False,
            "message": f"User '{username}' does not exist."
        }

def get_user_by_id(user_id):
    """
    Retrieves a user by ID from the database.

    Parameters:
    - user_id (str): The ID of the user to retrieve.

    Returns:
    - dict: A dictionary containing success status, message, and user data if successful, otherwise an error message.
    """
    users = database.child("user").get()
    user_list = []
    for user in users.each():
        if user.val().get('_id') == user_id:
            user_list.append(user.val())
    if len(user_list) == 0:
        return {
            "success": False,
            "message": "User not found"
        }
    return {
        "success": True,
        "message": "User found",
        "response": user_list[0]
    }

def delete_user(username):
    """
    Deletes a user from the database.

    Parameters:
    - username (str): The username of the user to delete.

    Returns:
    - dict: A dictionary containing success status and message if successful, otherwise an error message.
    """
    user = database.child("user").child(username).get()
    if user.val() is not None:
        deleted_user = database.child("user").child(username).remove()
        return {
            "success": True,
            "message": "User deleted successfully"
        }
    else:
        return {
            "success": False,
            "message": f"User '{username}' does not exist."
        }
