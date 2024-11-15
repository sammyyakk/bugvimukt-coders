import instaloader

# Initialize Instaloader object
L = instaloader.Instaloader()

# Login to Instagram (credentials already saved in session file)
username = 'username' # Put your username here
password= "yourpassword" # Enter your password here

try:
    # Try to log in
    L.load_session_from_file(username)  # Load previous session if available
except FileNotFoundError:
    # If no previous session is found, login with username and password
    L.context.log("Session file does not exist - Logging in.")
    L.login(username, password)  # Login
    L.save_session_to_file()  # Save session for future use

print(f"Logged in as {username}")
