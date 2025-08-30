import sys
from sqlalchemy.orm import sessionmaker
from db.setup import engine
from models.user import User
from models.item import Item
from models.location import Location

Session = sessionmaker(bind=engine)
session = Session()


def menu():
    print("\n--- Lost & Found CLI ---")
    print("1. Register User")
    print("2. Report Lost Item")
    print("3. Report Found Item")
    print("4. View All Items")
    print("5. Exit")


def register_user():
    """Register a new user with name + email."""
    name = input("Enter your name: ").strip()
    email = input("Enter your email: ").strip()

    if not name or not email:
        print(" Name and email cannot be empty.")
        return

    existing_user = session.query(User).filter_by(email=email).first()
    if existing_user:
        print("  A user with this email already exists.")
        return

    user = User(name=name, email=email)
    session.add(user)
    session.commit()
    print(f" User '{name}' registered successfully!")


def report_item(status):
    """Report a lost or found item."""
    name = input("Enter item name: ").strip()
    description = input("Enter item description: ").strip()
    location_name = input("Enter location: ").strip()
    user_email = input("Enter your email (to link the report): ").strip()

    if not all([name, description, location_name, user_email]):
        print("  All fields are required.")
        return

    # Get or create location
    location = session.query(Location).filter_by(name=location_name).first()
    if not location:
        location = Location(name=location_name)
        session.add(location)
        session.commit()

    # Get user
    user = session.query(User).filter_by(email=user_email).first()
    if not user:
        print("  User not found. Please register first.")
        return

    item = Item(
        name=name,
        description=description,
        status=status,
        location=location,
        user=user,
    )
    session.add(item)
    session.commit()
    print(f" {status.capitalize()} item '{name}' reported by {user.name}!")


def view_items():
    """View all reported items."""
    items = session.query(Item).all()
    if not items:
        print(" No items found in the system.")
        return

    for idx, item in enumerate(items, start=1):
        print(f"[{idx}] [{item.status.capitalize()}] {item.name} - {item.description} @ {item.location.name}")


def run():
    """Main CLI loop."""
    while True:
        menu()
        choice = input("Enter choice: ").strip()

        if choice == "1":
            register_user()
        elif choice == "2":
            report_item("lost")
        elif choice == "3":
            report_item("found")
        elif choice == "4":
            view_items()
        elif choice == "5":
            print(" Goodbye!")
            sys.exit()
        else:
            print("  Invalid choice. Please try again.")


if __name__ == "__main__":
    run()
