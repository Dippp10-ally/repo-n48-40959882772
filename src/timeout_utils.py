"""Timeout helpers."""


def validate_timeout(seconds):
    """Reject negative timeouts."""
    if seconds < 0:
        raise ValueError("seconds must be non-negative")
    return seconds
