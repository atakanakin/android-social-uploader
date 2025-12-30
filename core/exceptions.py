"""Custom exceptions for the Android social uploader."""


class AndroidAutomationError(Exception):
    """Base exception for Android automation errors."""
    pass


class DeviceConnectionError(AndroidAutomationError):
    """Raised when unable to connect to Android device."""
    pass


class UploadError(AndroidAutomationError):
    """Raised when upload process fails."""
    pass