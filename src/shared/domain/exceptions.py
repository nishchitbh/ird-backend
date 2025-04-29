class AppException(Exception):
    """Base exception class for the application."""

    def __init__(self, message: str = "An error occurred", status_code: int = 400):
        self.detail = message
        self.status_code = status_code
        super().__init__(message)


class PasswordValidationException(AppException):
    def __init__(self, message: str):
        super().__init__(message, 400)


class DatabaseException(AppException):
    """Exception for database errors."""

    def __init__(self, message: str = "Database operation failed"):
        super().__init__(message, 500)


class AuthenticationFailedException(AppException):
    """Exception for authentication errors."""

    def __init__(self, message: str = "Incorrect username or password"):
        super().__init__(message, 401)


class InvalidUpdateException(AppException):
    """Exception for invalid update operations."""

    def __init__(self, message: str = "Invalid update operation"):
        super().__init__(message, 400)  # 400 Bad Request


class UserAlreadyExistsException(AppException):
    """Exception raised when trying to create a user that already exists."""

    def __init__(self, message: str = "User already exists"):
        super().__init__(message, 409)  # 409 Conflict


class ItemNotFoundException(AppException):
    """Exception raised when an item is not found."""

    def __init__(self, message: str = "Item not found"):
        super().__init__(message, 404)  # 404 Not Found


class UnauthorizedException(AppException):
    def __init__(self, message: str = "Unauthorized"):
        super().__init__(message, 401)


class ForbiddenException(AppException):
    def __init__(self, message: str = "Forbidden"):
        super().__init__(message, 403)  # 403 Forbidden


class MissingValueException(AppException):
    """Exception raised when a required field is missing."""

    def __init__(self):
        # 422 Unprocessable Entity
        super().__init__("Missing required field!", 422)
