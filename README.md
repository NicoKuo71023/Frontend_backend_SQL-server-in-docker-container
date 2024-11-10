# Titanic Data Web Service - Docker Flask-Vue-MySQL Practice

This project sets up a basic web service architecture using Docker Compose. It includes a frontend Nginx web server, a Flask backend, and a MySQL database, with an initial SQL command file to create a new user in the database.

## Project Structure

- **Frontend**: Nginx web server that manages incoming requests and serves static frontend content.
- **Backend**: Flask application that handles requests and communicates with the MySQL database.
- **Database**: MySQL, with an initial SQL script to set up the database and create a user.

## Files

- **docker_web_hw.yml**: Docker Compose file to set up the services.
- **Initial SQL file**: Script to initialize the MySQL database with a new user.

## Setup Instructions

### 1. Extract the Project Archive

Unzip the `docker_flask_vue_mysql_practice.tar.gz` file and navigate to the extracted directory:

```bash
tar -xzvf docker_flask_vue_mysql_practice.tar.gz
cd docker_flask_vue_mysql_practice
```

### 2. Load Docker Images

Load the three images (Nginx, Flask, MySQL) into Docker:

```bash
docker load -i nginx_test_20240908.tar
docker load -i flask_test_20240907.tar
docker load -i mysql_test_20240907.tar
```

### 3. Start the Services

Use Docker Compose to start all services as defined in `docker_web_hw.yml`:

```bash
docker-compose -f docker_web_hw.yml up
```

### 4. Access the Web Interface

Open a browser and enter your server's IP address to access the web service:

```
http://your_ip_address
```

## Docker Compose Configuration

The `docker_web_hw.yml` file includes the following services:

- **MySQL Server** (`mysql-server`):
  - Port: `3306:3306`
  - Environment: Sets MySQL root password and database name.
  - Volume: Includes an initial SQL file to set up the database.
  
- **Flask Backend** (`flask_test`):
  - Port: `5000:5000`
  - Command: Ensures Flask starts after MySQL is initialized.
  
- **Nginx Web Server** (`nginx_test`):
  - Port: `80:80`
  - Depends on Flask to ensure it starts only after Flask is ready.

## Network

All services are connected via a Docker network called `my_network` with a bridge driver.

## License

This project is for educational purposes.
