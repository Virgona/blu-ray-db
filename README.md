# Blu-ray Collection Database

A personal SQL + Python project to track my physical Blu-ray and 4K film collection.

The goal of this project is to practise relational database design, SQL querying,
and building a small but usable backend application.

---

## Features
- Normalised relational database design
- Separate tables for movies, genres, formats, and distributors
- Foreign key constraints for data integrity
- Distributor classification (STANDARD vs BOUTIQUE)
- Python CLI for adding and viewing movies
- Menu-driven interface (no direct SQL required by user)

---

## Tech Stack
- MySQL
- Python 3
- mysql-connector-python
- python-dotenv

---

## Setup Instructions

### 1. Database setup
1. Open MySQL (CLI or GUI)
2. Run the schema file:
     ```sql
   SOURCE sql/schema.sql;
3. the database blu_ray_collection will be created automatically

### 2. Python
1. navigate to the project root folder
2. create and activate virtual environment:
    python -m venv venv
3. Activate the virtual environment:
    Windows:
        venv\Scripts\activate
    
    macOS / Linux:
        source venv/bin.activate
4. install dependencies:
    pip install mysql-connector-python python-dontenv

## 3. Environment Variables
1. create a .env file in the porject root with the following contents:
    DB_HOST=localhost
    DB_USER=root
    DB_PASSWORD=your_mysql_password
    DB_NAME=blu_ray_collection
    -- this file should be getting ignored by git

## 4. Run the App
1. run the project from the root folder:
    python python/add_movie.py

2. Follow the prompts from the menu! 😊