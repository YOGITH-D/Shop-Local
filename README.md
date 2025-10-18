🏡 Shop-Local: Hyper-Local Community Marketplace

Project Description

Shop-Local is a prototype for a hyper-local digital marketplace designed specifically for small, contained communities, such as apartment complexes, residential layouts, or university dormitories.

The core idea is to enable residents to easily and securely buy, sell, or exchange items and products with their immediate neighbors. This platform aims to foster community engagement, promote sustainability by encouraging reuse, and eliminate the hassle of dealing with distant buyers/sellers.

This repository represents the Minimum Viable Product (MVP), providing the fundamental framework for user authentication and basic product listing management.

✨ MVP Features

The current prototype supports the following core functionalities:

User Authentication: Secure registration and login for community members.

Item Listing: Users can post items for sale, including a product name, price, and description.

Secure Hashing: Password security implemented using Bcrypt.

Session Management: Persistent user sessions using Flask-Login.

⚙️ Technology Stack

This application is built entirely on the Python ecosystem:

Backend Framework: Flask

Database ORM: Flask-SQLAlchemy (defaulting to SQLite for development)

Forms Management: Flask-WTF / WTForms

Security: Flask-Bcrypt (Password Hashing)

💻 Installation and Setup

To run this project locally, you need to have Python installed.

1. Clone the Repository

git clone [https://github.com/YOGITH-D/Shop-Local.git](https://github.com/YOGITH-D/Shop-Local.git)
cd Shop-Local


2. Set up a Virtual Environment

It is highly recommended to use a virtual environment to manage dependencies.

# Create the virtual environment
python3 -m venv venv

# Activate the virtual environment
# On Linux/macOS:
source venv/bin/activate
# On Windows (Command Prompt):
.\venv\Scripts\activate


3. Install Dependencies

All required libraries are listed in the requirements.txt file.

pip install -r requirements.txt


4. Run the Application

The application can be started using the run.py file.

python run.py


The application will now be running on your local machine, usually accessible at:
http://127.0.0.1:5000/

🚀 Future Scope

This MVP provides a strong foundation. Next steps could include:

Image Uploads: Allowing users to upload photos of their items.

Messaging System: Enabling direct communication between buyer and seller.

User Profiles: Dedicated pages for viewing a seller's history and ratings.

Search and Filter: Advanced tools for easily finding items.