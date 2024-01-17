#!/usr/bin/env python3
"""
Auth class
Require auth with stars
"""
from flask import request
from typing import List, TypeVar
from os import getenv


class Auth():
    """
    Manage the
    API authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Require authorization
        """
        if path is None or excluded_paths is None or not len(excluded_paths):
            return True
        if path[-1] != '/':
            path += '/'
        for i in excluded_paths:
            if i.endswith('*'):
                if path.startswith(i[:1]):
                    return False
        if path in excluded_paths:
            return False
        else:
            return True

    def authorization_header(self, request=None) -> str:
        """
        Authorization header
        """
        if request is None:
            return None
        if not request.headers.get("Authorization"):
            return None
        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Current user
        """
        return None

    def session_cookie(self, request=None):
        """
        Returns a cookie
        Value from a request
        """
        if request is None:
            return None
        session_name = getenv('SESSION_NAME')
        return request.cookies.get(session_name)
