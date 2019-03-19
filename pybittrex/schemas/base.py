"""Base schemas from which all other schemas are derived."""

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class BaseResponse:
    """Base class for responses"""
    success: bool
    message: str
    result: Any
