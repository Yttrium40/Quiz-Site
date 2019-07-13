from django.contrib.auth.models import User

def validate_new_user(username, password, confirm_password):
    error_messages = []
    if len(username) == 0:
        error_messages.append('Username may not be empty.')
    if len(password) == 0:
        error_messages.append('Password may not be empty.')
    if password != confirm_password:
        error_messages.append('Passwords do not match.')
    if User.objects.filter(username=username).exists():
        error_messages.append('Username already taken.')
    return error_messages
