#!/usr/bin/env python3
"""
UserSession class
"""

from models.base import Base


class UserSession(Base):
    """
    UserSession class for session
    Authentication using a DB.
    """

    def __init__(self, *args: list, **kwargs: dict):
        """
        Initialize class instance
        """
        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get('user_id')
        self.session_id = kwargs.get('session_id')
