# Project Setup and Usage Guide

This guide provides instructions for setting up and running the application, even if you are not a developer.

## Prerequisites

Before you begin, ensure you have the following installed:

*   **Python:**  Download and install Python 3.10 or higher from the official Python website ([https://www.python.org/downloads/](https://www.python.org/downloads/)).
*   **Git:** Download and install Git from the official Git website ([https://git-scm.com/downloads](https://git-scm.com/downloads)).

## Setup Instructions

1.  **Clone the Repository:**

    Open a terminal or command prompt and navigate to the directory where you want to store the project. Then, run the following command to clone the repository:

    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

    Replace `<repository_url>` with the actual URL of the project repository and `<repository_directory>` with the name of the directory where the project will be cloned.

2.  **Create a Virtual Environment:**

    It is recommended to create a virtual environment to isolate the project dependencies. Run the following commands:

    ```bash
    python -m venv env
    env\Scripts\activate  # On Windows
    source env/bin/activate # On macOS and Linux
    ```

3.  **Install Dependencies:**

    Install the required Python packages using pip:

    ```bash
    pip install -r requirements.txt
    ```

4.  **Environment Variables:**

    Create a `.env` file in the project root directory. Add the following environment variables to this file.  These variables are crucial for the application to function correctly.
    ```
    MONGODB_HOST=mongodb://localhost:27017
    AUTH_SECRET=your_auth_secret
    ACCESS_TOKEN_EXPIRY_TIME=30
    ALGORITHM=HS256
    ```
    **Note:** The application requires `MONGODB_HOST` for the MongoDB connection, `AUTH_SECRET` for authentication, `ACCESS_TOKEN_EXPIRY_TIME` (in days) for access token expiry, and `ALGORITHM` for the hashing algorithm. Please replace `your_auth_secret` with a secure, randomly generated string.

## Running the Application

1.  **Start the Application:**

    Run the following command to start the FastAPI application:

    ```bash
    uvicorn src.main:app --reload
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

3.  **Testing Endpoints:**

    Use the API documentation to test the available endpoints. You can send requests and view the responses directly in the browser. Ensure that the application is behaving as expected.

## Troubleshooting

*   **Dependency Issues:** If you encounter issues during the dependency installation, make sure that you have the correct version of Python installed and that pip is up to date.
*   **Application Errors:** Check the application logs for any error messages. The logs can provide valuable information for debugging.
*   **Environment Variables:** Double-check that all required environment variables are set correctly in the `.env` file.

## Additional Information

*   For more detailed information about the project, refer to the project documentation or source code.