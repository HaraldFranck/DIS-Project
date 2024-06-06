# DIS-Project

## Overview
For our DIS-project, we've developed a web-app that allows users to search within a database of the 1000 highest rated movies from IMDb. This guide will help you set up and start using the application on your local system.

## Initial Setup

### Configure the Application
Before running the application, you need to update the database connection settings:
  - Open the `init_db.py` file in an editor.
  - Locate line 8 and change the password from 'passwor' to your own Postgres master password.
  - Save the changes.

### Install Dependencies
Ensure you have Python installed on your system and then set up the required libraries:
  - Open a terminal or command prompt.
  - Navigate to the project directory:
    ```
    cd path/to/DIS-Project
    ```
  - Install the required Python packages:
    ```
    pip install -r requirements.txt
    ```

### Run the Application
After configuring and installing the necessary dependencies, you can start the application:
  - In the same terminal, execute:
    ```
    python app.py
    ```
  - Upon successfully running the command, you should see a message indicating the server is running, similar to:
    ```
    * Running on http://127.0.0.1:5000
    ```
  - Copy the shown address and paste it into your preferred web browser to access the web app.

## Using the Application
To search for movies in the database:
  1. Enter search criteria into one or more of the fields (e.g., Actor: Mikkelsen, Genre: Drama).
  2. Click the 'Search' button or press ENTER.
  3. The results page will display all movies matching your criteria, such as 'Adams Æbler', 'Druk', 'Efter Brylluppet', and 'Jagten'.
  4. To perform another search, simply return to the search page and enter new criteria.

Enjoy exploring the highest rated movies from IMDb in our DIS-Project web app!
