def is_valid_password(password):
    if len(password) < 8:
        return False

    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    digits = "0123456789"

    has_upper = any(char in uppercase for char in password)
    has_lower = any(char in lowercase for char in password)
    has_digit = any(char in digits for char in password)

    return has_upper and has_lower and has_digit