# Fixed Login function to correctly check both email and password

def Login(request):
    email = request.get("email", None)
    password = request.get("password", None)  # Assuming 'password' is also a required field

    if not (email and password):  # Corrected condition to check both fields
        return {"success": False, "message": "Email and Password are required"}
    else:
        return {"success": True, "message": "Login successful"}