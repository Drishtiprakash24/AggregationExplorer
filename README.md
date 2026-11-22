# MongoDB Aggregation Explorer

## Project Overview
MongoDB Aggregation Explorer is a Python Flask-based web application designed to demonstrate and explore MongoDB's Aggregation Framework.

The project helps users understand how aggregation pipelines process and analyze data using different stages and operators.

## Technologies Used
- Python
- Flask
- MongoDB
- PyMongo
- HTML, CSS and JavaScript

## Features
- Interactive web interface for exploring MongoDB aggregation.
- Demonstration of aggregation pipeline stages.
- Data filtering, grouping, sorting and projection.
- Examples of aggregation operations.

## Requirements
- Python 3.11 or later
- MongoDB Community Server
- MongoDB Shell (mongosh)

## Installation and Execution

1. Clone or download this repository.
2. Open the project folder in VS Code or PowerShell.
3. Create a virtual environment:

   ```powershell
   python -m venv venv
   ```

4. Activate the environment:

   ```powershell
   .\venv\Scripts\Activate.ps1
   ```

5. Install dependencies:

   ```powershell
   pip install -r requirements.txt
   ```

6. Ensure that MongoDB Server is running locally.
7. Run the Flask application:

   ```powershell
   python app.py
   ```

8. Open your browser and visit:

   `http://127.0.0.1:5000/`

## Database
The application uses a local MongoDB database. Follow the project's database initialization instructions or scripts, if provided, to prepare the sample collections.

## Academic Project
Developed as an individual M.Tech AI & Data Science project.

**Note:** Update this README if your application uses different startup commands, database settings, or initialization steps.