# Lost & Found CLI  
#### A command-line application to manage lost and found items in various locations, August 30, 2025  
#### By **Alex Rooney Mwangi**

## Description  
Lost & Found CLI is a Python command-line application designed to help users report lost or found items and track their locations efficiently. The system allows users to register, report lost or found items, and view all items currently in the system.  

The app uses **SQLAlchemy ORM** for database management and follows **object-oriented programming (OOP) best practices**, ensuring maintainable and scalable code. Users, items, and locations are connected via relationships, providing a realistic simulation of a lost-and-found system.

---

## Setup / Installation Requirements  

1. **Clone or download the repository** from GitHub:  
   ```bash
   git clone <repository-url>
   cd lost_and_found

2. **Ensure Python 3.12+ is installed.**

3. **Create and activate a virtual environment using Pipenv.**

     pipenv shell

     pipenv install

4. **Initialize the database and create tables.**

   PYTHONPATH=$(pwd) python -m db.init_db

5. **Run the CLI  application.**\
    python cli.py

---

## Features/Workflow
The Lost & Found CLI provides the following functionalities:

1. **Register User.**

   -Users provide a name and email.

   -Each user is uniquely identified by email.

2. **Report Lost item.**

    -Users can report items as lost.

    -Users provide item name, description, and location.

    -The system links the item to the reporting user and location.

3. **Report Found item.**

    -Similar to lost items but marked as "found."

4. **View All items.**

    -Displays all items in the system, showing status (Lost/Found), name, description, and location.

    -Uses lists to organize and display items in the CLI.

    ---

## Data Model
**User**

   -id (primary key)

   -name

   -email (unique)

   -Relationship:a user can report multiple items.

**item**

  -id (primary key)

  -name

  -description

  -status (lost/found)

  -location_id (foreign key)

  -user-id (foreign key)

  -Relationships:linked to a user and a location

**Location**

  -id (primary key)

  -name (unique)

  -Relationship:can have multiple items

---

## Technologies Used

  -Python 3.12

  -SQLAlchemy ORM

  -SQLite3

  -Pipenv

  ---

## Known Bugs

There are currently no known issues with this application.

---

## Support and Contact Details
For any questions, feedback, or concerns, feel free to reach out:

  -Email:***

  ---

## License
This project is licensed under the MIT License.

Copyright (c) 2025 Alex Rooney Mwangi  