from dotenv import load_dotenv
import os
import firebase 


# Load environment variables
# load_dotenv()

# Initialize Firebase app
config = {
    "apiKey": os.getenv("apiKey"),
    "authDomain": os.getenv("authDomain"),
    "databaseURL": os.getenv("databaseURL"),
    "projectId": os.getenv("projectId"),
    "storageBucket": os.getenv("storageBucket"),
    "messagingSenderId": os.getenv("messagingSenderId"),
    "appId": os.getenv("appId"),
    "measurementId": os.getenv("measurementId")
}
app = firebase.initialize_app(config)

# Firebase authentication and database instances
auth = app.auth()
database = app.database()
