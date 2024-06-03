- [Management-Backend](#Management-Backend)
  - [Prerequisites](#prerequisites)
  - [Project Setup](#project-setup)
    - [1. **Clone the repository**](#1-clone-the-repository)
    - [2. **Install dependencies**](#2-install-dependencies)
    - [3. **Activate the pipenv shell**](#3-activate-the-pipenv-shell)
    - [4. **Generate a secret key**](#4-generate-a-secret-key)
    - [5. **Fill the `.env` file**](#5-fill-the-env-file)
    - [6. **Set up the development database**](#6-set-up-the-development-database)
    - [7. **Run the development server**](#7-run-the-development-server)
    - [7.1 Add new Superuser](#71-add-new-superuser)
    - [8. **Troubleshooting**](#8-troubleshooting)
      - [8.1 ZoneInfoNotFoundError: 'No time zone found with key utc'](#81-zoneinfonotfounderror-no-time-zone-found-with-key-utc)
  - [Solution for testing mail server](#solution-for-testing-mail-server)
  - [Development Progress](#development-progress)
    - [URL Patterns and Their Functions](#url-patterns-and-their-functions)

# Management-Backend

Welcome to the Management-Backend Django project repository. This README provides you with the necessary information to set up and contribute to the development of the Management-Backend application.

## Prerequisites

Before you begin, ensure you have the following installed on your development machine:

- Python 3.11.x (only this version)
- pipenv
- Docker and Docker Compose

## Project Setup

### 1. **Clone the repository**

   ```sh
   git clone https://github.com/RCSS-Tournament-Manager/manager-backend.git
   cd management-backend
   ```

### 2. **Install dependencies**

   We use pipenv to manage project dependencies and virtual environments. To install the required packages, run:

   ```sh
   python -m pip install pipenv 
   pipenv install --dev
   ```

### 3. **Activate the pipenv shell**

   This will spawn a new shell subprocess, which can be deactivated by simply closing it, or by running `exit`.

   ```sh
   python -m pipenv shell
   ```

### 4. **Generate a secret key**

   Generate a Django secret key that will be used in your `.env` file:

    ```sh
    python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
    ```
    Or use **openssl**
    ```sh
    openssl rand -hex 32
    ```

### 5. **Fill the `.env` file**

   Create a `.env` file in the root directory of the project and fill it with the necessary environment variables. Here's a template to get you started:

   ```plaintext
   # Django settings
   DEBUG=True
   SECRET_KEY=<Your generated secret key>
   ALLOWED_HOSTS=127.0.0.1,localhost

   # Email settings for development
   EMAIL_HOST=localhost
   EMAIL_PORT=1025
   EMAIL_HOST_USER=
   EMAIL_HOST_PASSWORD=
   EMAIL_USE_TLS=False
   ```

   Replace `<Your generated secret key>` with the key generated in the previous step.

### 6. **Set up the development database**

   We use SQLite for development purposes. To set up your database, run:

   ```sh
   python manage.py migrate
   ```

### 7. **Run the development server**

   To start the Django development server, run:

   ```sh
   python manage.py runserver
   ```

   The server will start at `http://127.0.0.1:8000/`.
   
   API document `http://127.0.0.1:8000/api/docs/swagger/#/api/api_schema_retrieve`

### 7.1 Add new Superuser

   ```sh
   python manage.py createsuperuser
   ```
   ****

### 8. **Troubleshooting**

#### 8.1 ZoneInfoNotFoundError: 'No time zone found with key utc'

```bash
pip install tzdata
```

## Solution for testing mail server

> 1- Mailhug (as Docker)
> 2- Mailpit (recommended)
> 3- MailTrap (External service)

### 1- Docker Compose (only for mail service)

The project includes a `docker-compose.yml` file which sets up all the necessary services for the application, including a mail service for development purposes.

To start all services, run:

```sh
docker-compose up -d
```

This command will start the services in detached mode. You can view the logs for the services using:

```sh
docker-compose logs -f
```

To stop the services, use:

```sh
docker-compose down
```

the mailhug service is available at `http://127.0.0.1:8025/`.


### 2- Mailpit directly as exe file

Mailpit is a small, fast, low memory, zero-dependency, multi-platform email testing tool & API for developers.

It acts as an SMTP server, provides a modern web interface to view & test captured emails, and contains an API for automated integration testing.

Mailpit was originally inspired by MailHog which is no longer maintained and hasn't seen active development for a few years now.

[https://github.com/axllent/mailpit](https://github.com/axllent/mailpit)

### 3- MailTrap.io
also you can use any external service for testing smtp like [mailtrap.io](https://mailtrap.io/home)