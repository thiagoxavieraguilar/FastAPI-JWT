# FastAPI JWT Authentication
 
###### FastAPI JWT Authentication is a secure and easy-to-use authentication solution for FastAPI web applications. It leverages JSON Web Tokens (JWT) to provide robust and scalable authentication functionality.
###### With FastAPI JWT Authentication, you can easily add user authentication and authorization to your FastAPI application. It supports multiple authentication 
###### strategies, including JWT-based authentication, token refreshing, and more.
###### By using FastAPI JWT Authentication, you can ensure that only authorized users can access your application's resources and data, improving your application's security and reliability.


## Setting up the environment
1. Install the virtual environment (virtualenv) using pip:
```
pip install virtualenv
```

2. Create a virtual environment inside your project directory:
```
python virtualenv venv
```
3. Activate the virtual environment:
On Windows:
```
venv\Scripts\activate.ps1
```

## Installing requirements
4. Install the project's requirements:
```
pip install -r requirements.txt
```

## Running the db
5. Make sure you have Docker installed on your machine, then run the Docker Compose:
```
docker-compose up -d
```

6. Run the Alembic upgrade command to update the database:
```
alembic upgrade head
```

## Running the project
7. Finally, start the server using Uvicorn:
```
uvicorn app.main:app --reload
```
