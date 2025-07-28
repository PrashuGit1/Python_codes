class User:
    def __init__(self, name, email):
        if not User.is_valid_email(email):
            raise ValueError("Invalid email address")
        self.name = name
        self.email = email

    @staticmethod
    def is_valid_email(email):
        return "@" in email and "." in email
