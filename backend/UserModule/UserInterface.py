from abc import ABC, abstractmethod
from enum import Enum
from typing import List


class UserInterface(ABC):
    @abstractmethod
    def __init__(self, userID):
        self.userID = userID
    
    @abstractmethod
    def signIn(self, email: str, password: str):
        pass
    
    @abstractmethod
    def signOut(self):
        pass
    
    @abstractmethod
    def changeEmail(self, newEmail: str):
        pass
    
    @abstractmethod
    def changePassword(self, newPassword: str):
        pass


