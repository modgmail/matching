#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: m
"""
class School:
    """
    A class to represent a school.

    ...

    Attributes
    ----------
    
    Methods
    -------
    info(additional=""):
        Prints the person's name and age.
    """
    
    def __init__(self, df):
        """
        Constructs all the necessary attributes for the match object.

        Parameters
        ----------
            s : school
                instance of school
                s is a dataframe with all valid entries
                there is no data validation here  
        """
        self.id = df['Unique Identifier']
        self.name_official = df['Official School Name']
        self.name = df['Short School Name']
        self.class_level = df['Class Levels Available']
        self.slots = df['Slots']
        
        self.autistic = df['autistic'] 
        self.blind = df['blind'] 
        self.deaf = df['deaf']
        
        self.services = []
        if self.autistic:
                self.services.append('autistic') 
        if self.blind:
                self.services.append('blind') 
        if self.deaf:
                self.services.append('deaf') 
    
    def info(self):
        '''Print the school details
        
        Parameters
        ----------
        None
    
        Returns
        -------
        none
        '''
        print('School:')
        print('\tName:\t', self.name)
        print('\tID:\t\t', self.id)
        # print('Autistic: ', self.autistic)
        # print('Blind: ', self.blind)
        # print('Deaf: ', self.deaf)