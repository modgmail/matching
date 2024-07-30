#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: m
"""
# import pandas as pd
import Match as m

class Student:
    """
    A class to represent student.

    ...

    Attributes
    ----------
    
    Methods
    -------
    getMatches(schools):
        Get a list of the matches to each school in the list of schools

    info():
        Prints the person's name and age.    
    """
    
    def __init__(self, df):
        """
        Constructs all the necessary attributes for the match object.

        Parameters
        ----------
            df : pandas DataFrame
                A dataframe with all valid entries.
                There is no data validation here.
        """
        self.id = df['Unique Identifier']
        self.first_name = df['First Name']
        self.last_name = df['Last Name']
        self.dob = df['Birthday']
        # we're not using age 
        # self.age = df["Today's date minus birthdate"] 
        self.class_level = df['Class Level'] 

        # keys = ['autistic', 'blind', 'deaf'] 
        self.autistic = df['autistic'] 
        self.blind = df['blind'] 
        self.deaf = df['deaf']

        self.needs = []
        if df['autistic']:
                self.needs.append('autistic') 
        if df['blind']:
                self.needs.append('blind') 
        if df['deaf']:
                self.needs.append('deaf')

    def getMatches(self, schools):
        """Get a list of the matches to each school in the list of schools
        
        Parameters
        ----------
        schools : list<School>
            A list of schools to match to the student
    
        Returns
        -------
        matches : list<Match>
            A list of matches to each school in the list
        """
        matches = []
        for school in schools.values():
            matches.append(m.Match(self, school))
        return matches

    def info(self):
          '''Print the school details
          
          Parameters
          ----------
          None
      
          Returns
          -------
          none        
          '''
          print('Student:')
          print('\tName: \t', self.first_name, self.last_name)
          print('\tID: \t', self.id)
          print('\tSpecial needs:', self.needs)
