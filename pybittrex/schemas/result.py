"""Result schemas for the API"""
from dataclasses import dataclass

from pybittrex.schemas.base import BaseResponse


@dataclass
class Result(BaseResponse):
    """Result schema"""
    pass
