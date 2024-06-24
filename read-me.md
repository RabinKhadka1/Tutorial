# Ecommerce Setup using React / Python / Postgre Database

This project sets up a Flask backend with an integrated PostgreSQL database for an e-commerce setup. The services are containerized using Docker and managed via Docker Compose.

## Prerequisites

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Setup & Running


1. **Build and Start the Services**:
   ```
   docker-compose up -d
   ```

2. **Accessing the App**:
   After running the above command, the Flask backend should be accessible at [http://localhost:5000](http://localhost:5000).

## Database Initialization

The PostgreSQL database will automatically be initialized using the SQL commands in `db_script/init.sql`.

## Structure

- `/app`: Contains the Flask app files including `app.py`.
- `/db_script`: Contains SQL scripts to initialize the database. 
- `Dockerfile`: Docker configuration for building the Flask backend service.
- `docker-compose.yml`: Docker Compose configuration for managing multi-container services.

## Troubleshooting

1. **Database Initialization Errors**:
   Ensure that the `init.sql` script does not contain errors. Initialization scripts will only be run the first time the database container starts. If you modify the `init.sql` and want to apply changes, destroy the PostgreSQL container's volume and recreate it.

2. **Flask App Errors**:
   Ensure that the Flask app and its dependencies are correctly set up. Check the logs using:
   ```
   docker-compose logs backend
   ```
