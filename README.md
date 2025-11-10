# Project Setup and Usage Guide

This guide provides instructions for setting up and running the application, even if you are not a developer.

## Prerequisites

Before you begin, ensure you have the following installed:

*   **Python:**  Download and install Python 3.10 or higher from the official Python website (https://www.python.org/downloads/).
*   **Git:** Download and install Git from the official Git website (https://git-scm.com/downloads).
*   **uv:** Install uv using pip: `pip install uv`
*   **Docker:** Download and install Docker from the official Docker website (https://www.docker.com/products/docker-desktop/).

## Setup Instructions

1.  **Clone the Repository:**

    Open a terminal or command prompt and navigate to the directory where you want to store the project. Then, run the following command to clone the repository:

    ```bash
    git clone https://github.com/nishchitbh/ird-backend.git
    cd ird-backend
    ```

2.  **Install Dependencies:**

    Install the required Python packages using uv sync:

    ```bash
    uv sync
    ```

3.  **Environment Variables:**
    Create a `.env` file in the project root directory. Add the following environment variables to this file.  These variables are crucial for the application to function correctly.
    ```
    ENV=dev
    MONGODB_HOST=localhost
    MONGODB_PORT=27017
    AUTH_SECRET=
    ACCESS_TOKEN_EXPIRY_TIME=30
    ALGORITHM=HS256
    UPLOAD_FOLDER=static/uploads
    ALLOWED_EXTENSIONS=.jpg,.jpeg,.png,.webp
    CHUNK_SIZE=1048576
    MAX_FILE_SIZE = 10485760
    COMPANY_DOMAIN=ird.com.np
    REDIS_URL=redis://localhost:6379/
    MONGO_INITDB_ROOT_USERNAME=
    MONGO_INITDB_ROOT_PASSWORD=
    MONGO_INITDB_DATABASE=
    ```
    **Note:** The application requires `MONGODB_HOST` for the MongoDB connection, `AUTH_SECRET` for authentication, `ACCESS_TOKEN_EXPIRY_TIME` (in days) for access token expiry, and `ALGORITHM` for the hashing algorithm. Please replace `your_auth_secret` with a secure, randomly generated string. Also, ensure that `MONGODB_PORT` is correctly set and other variables are configured according to your needs.

## Running the Application

1.  **Start MongoDB and Redis using Docker:**

    Run the following commands to start MongoDB and Redis instances using Docker:

    ```bash
    docker run -d -p 27017:27017 --name mongodb mongo:latest
    docker run -d -p 6379:6379 --name redis redis:latest
    ```

    These commands start MongoDB and Redis servers, mapping their default ports to the host machine.

2.  **Start the Application:**

    Run the following command to start the FastAPI application:

    ```bash
    uv run uvicorn main:app --reload
    ```

    This command starts the server using Uvicorn, a production-ready ASGI server. The `--reload` flag enables automatic reloading of the server whenever you make changes to the code. Open your browser to `http://127.0.0.1:8000`.

## Testing the Features

1.  **Access the API Documentation:**

    Once the application is running, you can access the automatically generated API documentation by opening your web browser and navigating to `http://127.0.0.1:8000/docs`. This documentation provides interactive tools for testing the API endpoints.

2.  **Available Endpoints:**

    The following endpoints are available for testing:

    *   **Login:** Authenticates a user with username and password.
    *   **Signup:** Creates a new user.
    *   **Get Current User:** Retrieves the current user's information.
    *   **Update Current User:** Updates the current user's information.
    *   **Change Password:** Allows the current user to change their password.
    *   **Delete User:** Deletes a user (requires authentication).
    *   **Reset Password:** Resets a user's password (requires authentication).
    *   **Update Other User:** Updates another user's information (admin functionality).
