# Flask server

This flask server is a REST API wih two models User and Address. It has multiple endpoints for certain operations it is a work in progress and documentation is missong.

## Installation

Install pipenv
    ```bash
    pip install pipenv
    ```
    

Init venv
    ```bash
    pipenv shell
    ```

Install dependencies
    ```bash
    pipenv install 
    ```

Populate the following in app/__init__.py file with your own URI for database
    ```python
    app.config['SQLALCHEMY_DATABASE_URI']=''
    ```


Run bootstrap.sh
    ```bash
    ./bootsrap.sh
    ```
To run tests
    ```bash
    pytest __tests__/tests.py
    ```