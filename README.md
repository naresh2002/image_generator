# Image Generator Django Application
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

5. Install Redis and start the Redis server (ensure it's running on the default port 6379):  
    ```bash
    sudo apt-get install redis-server
    sudo service redis-server start
    ```

6. Make migrations for the Django application:  
    ```bash
    python manage.py makemigrations
    ```

7. Migrate schemas to the PostgreSQL database:  
    ```bash
    python manage.py migrate
    ```

8. Start the Celery worker to handle image generation tasks:  
    ```bash
    celery -A Image_Generator worker --loglevel=info
    ```

9. Start the server:  
    ```bash
    python manage.py runserver
    ```
