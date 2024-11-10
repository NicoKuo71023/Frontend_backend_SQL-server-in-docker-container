# Titanic Data Web Service

This project is a basic web service architecture that renders the Titanic dataset on a frontend using an Nginx server, a Flask backend, and a MySQL database.

## Project Structure

- **Frontend**: Nginx server that handles requests and serves the frontend content.
- **Backend**: Flask application to process requests and retrieve data from the MySQL database.
- **Database**: MySQL, storing Titanic data.

## Features

- Load and render Titanic dataset (`titanic.csv`) on the frontend.
- REST API endpoint provided by Flask to retrieve Titanic data.
- Nginx server to manage incoming HTTP requests and serve frontend assets.

## Setup Instructions

### Prerequisites

Ensure you have the following installed:
- Docker
- Docker Compose

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/titanic-web-service.git
cd titanic-web-service
