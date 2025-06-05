import os
import sys
import django

# Add the current directory to Python path
sys.path.append("/Users/angelinemarcellelukito/MS Project Learn/backend")

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from heavenlyvitamin.models import User
from datetime import date

def populate_users():
    users_data = [
        {
            "username": "amlukito",
            "first_name": "Angel",
            "last_name": "Lukito",
            "email": "amlukito@gmail.com",
            "phone_number": "94567890", 
            "birthdate": date(2005, 5, 15)
        },
        {
            "username": "daveg",
            "first_name": "Dave",
            "last_name": "Green",
            "email": "daveg@yahoo.com",
            "phone_number": "94123456",
            "birthdate": date(2004, 8, 22)
        },
        {
            "username": "natalielee",
            "first_name": "Natalie",
            "last_name": "Lee",
            "email": "natalielee@hotmail.com",
            "phone_number": "94789012",
            "birthdate": date(1995, 3, 10)
        }
    ]

    for user_data in users_data:
        try:
            user = User.objects.create(**user_data)
            print(f"Created user: {user.username}")
        except Exception as e:
            print(f"Error creating user {user_data['username']}: {str(e)}")


if __name__ == '__main__':
    #User DB
    print("Starting user population script...")
    populate_users()
    print("User population complete!")