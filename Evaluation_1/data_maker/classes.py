from itertools import count
from dataclasses import dataclass, field

@dataclass
class Person:
    """Class for Person Record"""
    first_name:str
    last_name:str
    phone_number:str
    mortgage_renewed:bool
    is_financial_advisor:bool
    id:int = field(default_factory=count().__next__)

@dataclass
class Appointment:
    """Class for an apointment record"""
    financial_advisor_id:int
    customer_id:int
    day:str
    office_location_id: int
    id:int = field(default_factory=count().__next__)

@dataclass
class CallNotes:
    """Notes about customers from phone calls"""
    financial_advisor_id:int
    customer_id:int
    note:str
    id:int = field(default_factory=count().__next__)

@dataclass
class Office:
    """Class for office record"""
    name:str
    id:int = field(default_factory=count().__next__)

@dataclass
class Mortgage:
    """Class for Mortgage Record"""
    customer_id:int
    term:int
    amount:int
    paid_off:bool
    id:int = field(default_factory=count().__next__)