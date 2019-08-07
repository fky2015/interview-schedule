"""validators for model."""
from django.core.exceptions import ValidationError


def validate_username(value: str):
    """username must be a student ID."""
    if not value.isdigit():
        raise ValidationError("username must be a student ID.")


def validate_mobile(value: str):
    """mobile number must be valid."""
    if not value.isdigit() or len(value) != 11:
        raise ValidationError("Error mobile number.")
