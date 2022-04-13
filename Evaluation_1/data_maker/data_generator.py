import csv
import random
from typing import List, Tuple, Any
from data_maker.classes import Person, Appointment, CallNotes, Office, Mortgage
import datetime, calendar
from dataclasses import asdict
import os

class DataMaker():
    '''DataMaker creates fictional data for Evalation 1
    '''
    def __init__(self, first_names:List[str], last_names:List[str], 
        customer_popualtion:int, financial_advisor_count:int):
        self.first_names = first_names
        self.last_names = last_names
        self.customers = customer_popualtion
        self.financial_advisors = financial_advisor_count 
        self.area_code = random.randint(100, 999)
        self.next_three = list(map(lambda x: random.randint(100, 999)*x, [1]*4))
    
    def _write_csv(self, filename:str, records:List[Any]) ->None:
        '''a function that writes a csv from a records list'''
        records_dicts = [asdict(record) for record in records]
        cols = records_dicts[0].keys()
        with open(f'{filename}.csv', 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=cols)
            writer.writeheader()
            for data in records_dicts:
                writer.writerow(data)

    def _create_person(self, is_financial_advisor:bool = False)->Person:
        '''a function that creates a fictional person record'''
        return Person(
            random.choice(self.first_names).replace(' ',''),
            random.choice(self.last_names).replace(' ',''),
            f'({self.area_code}){random.choice(self.next_three)}-{random.randint(1000,9999)}',
            bool(random.getrandbits(1)),
            is_financial_advisor
            )

    def _create_people(self) -> Tuple[List[Person],List[Person]]:
        '''a function that creates fictional people records'''
        customers:List[Person] = [self._create_person() for i in range(self.customers)]
        financial_advisors:List[Person] = [self._create_person(True) for i in range(self.financial_advisors)]
        return customers, financial_advisors

    def _create_appointments(self, customer_ids:List[int], financial_advisor_ids:List[int], office_ids: List[int]) -> List[Appointment]:
        '''a function that creates fictional appointment records'''
        month_days = [(n,calendar.monthrange(2022, n)[1]) for n in range(3,6)]
        days = [datetime.date(2022, month[0], day) for month in month_days for day in range(1, month[1]+1)]
        appointments:List[Appointment] = []
        for cid in customer_ids:
            financial_advisor = random.choice(financial_advisor_ids)
            day = random.choice(days)
            office_id = random.choice(office_ids)
            appointments.append(Appointment(financial_advisor,cid,day,office_id))
        return appointments
    
    def _create_notes(self, customer_ids:List[int], financial_advisor_ids:List[int],) -> List[CallNotes]:
        '''a function that creates fictional call notes'''
        note_values: List[str] = ['I think this customer will renew', 
            'I don\'t think this customer will renew',
            'this customer has passed away', 
            'I called this customer many times but they never answered']
        notes:List[CallNotes] = []
        for cid in customer_ids:
            note = CallNotes(
                financial_advisor_id = random.choice(financial_advisor_ids),
                customer_id = cid,
                note = random.choice(note_values)
            )
            notes.append(note)
        return notes

    def _create_offices(self) -> List[Office]:
        '''a function that creates fictional office records'''
        office_names = ['Head office', 'high branch', 'low branch', 'creek branch']
        return [Office(name) for name in office_names]


    def _create_mortgages(self, customers:List[Person]) -> List[Mortgage]:
        '''a function that creates fictional mortgages'''
        mortgages:List[Mortgage] = []
        for customer in customers:
            if customer.mortgage_renewed:
                m = Mortgage(
                    customer_id=customer.id,
                    term = random.choice([5,10,20,25]),
                    amount = random.randint(100000,2000000),
                    paid_off = False
                )
            else:
                paid_off = bool(random.getrandbits(1))
                if paid_off: 
                    term = 0
                    amount = 0
                else:
                    term = random.choice([5,10,20,25])
                    amount = random.randint(100000,2000000)
                m = Mortgage(
                    customer_id=customer.id,
                    term = term,
                    amount = amount,
                    paid_off = paid_off
                )
            mortgages.append(m)
        return mortgages

    def _make_data(self)-> Tuple[List[CallNotes],List[Office],List[Appointment],List[Mortgage],List[Person]]:
        '''a function that creates fictional data'''
        #create people
        people:Tuple[List[Person], List[Person]] = self._create_people()
        all_people:List[Person] = people[0] + people[1]
        #create a list of callnotes
        financial_advisor_ids:List[int] = [person.id for person in people[1]]
        customers_with_calls:int = len(people[0])*7//10
        customers_with_calls_ids:List[int] = [person.id for person in people[0][customers_with_calls:]]
        notes:List[CallNotes] = self._create_notes(customers_with_calls_ids,financial_advisor_ids)
        #create a list of offices
        offices:List[Office] = self._create_offices()
        office_ids = [office.id for office in offices]
        #create a list of appointments
        customers_with_appointments:int = len(people[0])*4//10
        customers_with_appointments_ids:List[int] = [person.id for person in people[0][customers_with_appointments:]]
        appointments:List[Appointment] = self._create_appointments(customers_with_appointments_ids,financial_advisor_ids, office_ids)
        #create a list of mortages
        mortgages:List[Mortgage] = self._create_mortgages(people[0])
        return notes, offices, appointments, mortgages, all_people

    def _write_data(self, data = Tuple[List[CallNotes],List[Office],List[Appointment],List[Mortgage],List[Person]])-> None:
        '''a function that writes fictional data to csvs'''
        filenames = ['callnotes', 'offices','appointments','mortgages','people']
        for filename, records in list(zip(filenames, data)):
            self._write_csv(os.path.join('.','sample_data',filename), records)

    def dump(self)->None:
        '''a function that dumps fictional data to csvs'''
        data = self._make_data()
        self._write_data(data)
