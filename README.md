# Image Generator
A Django web application that allows users to generate multiple images from text inputs simultaneously using Stability AI's Text-to-Image API.
Utilizes Django with Celery for handling asynchronous tasks and Redis as the message broker.
Ensures proper request data validation, secure image generation, and organized display of generated images.

The project is designed to manage user-submitted text prompts, trigger image generation tasks, and display the results in a user-friendly interface.


## Installation Requirements

1. **Decouple** to get env variables configuration from .env file:  
    ```bash
    pip install python-decouple
    ```
2. **Django** and **psycopg2-binary** for PostgreSQL database connectivity:  
    ```bash
    pip install django psycopg2-binary
    ```
3. **Celery** for asynchronous task management:  
    ```bash
    pip install celery
    ```
4. **Redis** as the message broker for Celery:  
    ```bash
    pip install redis
    ```
5. **requests** for making API calls to Stability AI:  
    ```bash
    pip install requests
    ```

## How to Run This Project

1. Clone the repository in your local machine.  
    ```bash
    git clone https://github.com/naresh2002/image_generator.git
    ```

2. Navigate to the project directory and create a `.env` file inside the parent folder (Paragraph_API).  
    ```bash
    cd image_generator
    touch .env
    ```

3. Write the following configuration in the `.env` file:  
    ```plaintext
    DATABASE_NAME={{DATABASE_NAME}}
    DATABASE_USER={{DATABASE_USER}}
    DATABASE_PASS={{DATABASE_PASS}}
    STABILITY_API_KEY={{YOUR_STABILITY_API_KEY}}
    ```

4. Go to your PostgreSQL shell and create a new database as `{{DATABASE_NAME}}`.  
    a. To enter PostgreSQL shell in terminal for Ubuntu (varies for different OS):  
    ```bash
    sudo -u postgres psql
    ```
    b. In PostgreSQL shell:  
    ```sql
    CREATE DATABASE {{DATABASE_NAME}};
    ```

5. Make migrations for the Django application:  
    ```bash
    python manage.py makemigrations
    ```

6. Migrate schemas to the PostgreSQL database:  
    ```bash
    python manage.py migrate
    ```

7. Install Redis and start the Redis server (ensure it's running on the default port 6379):  
    ```bash
    sudo apt-get install redis-server
    sudo service redis-server start
    ```

8. Start the Celery worker to handle image generation tasks:  
    ```bash
    celery -A Image_Generator worker --loglevel=info
    ```

9. Start the server:  
    ```bash
    python manage.py runserver
    ```

10. Access the application by navigating to **http://127.0.0.1:8000** in your web browser.


## URL Endpoints

1. **Home Page** (/):  
    **Description**: Allows users to input text prompts to generate images. Users can add multiple prompts, and the text fields are validated for emptiness and length.

2. **Generate Page** (/generate/):  
    **Description**: Displays a message indicating that images are being generated. Users can click a button to view all generated images.

3. **Show All Images Page** (/all/):  
    **Description**: Displays all generated images in descending order of creation, showing the prompt used for generation and the time of creation.


## Project Structure

1. **Celery Configuration**: Handles the task queue for image generation using Celery and Redis.

2. **Django Models**: Stores information about generated images, including the associated prompt and timestamp.

3. **Frontend**: Simple HTML forms for user input and display of generated images, styled directly within the HTML files.


## Features

1. **Image Generation:** Users can input text prompts to generate images using Stability AI.

2. **Asynchronous Processing:** Image generation tasks are handled asynchronously using Celery and Redis, ensuring smooth operation without blocking the user interface.

3. **Organized Display:** Generated images are displayed in descending order, with options to view all results.
