#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: m
"""
class Match:
    """
    A class to represent the match between a student  and a school.

    ...

    Attributes
    ----------
    
    Methods
    -------
    info(additional=""):
        Prints the person's name and age.
    """
    
    def __init__(self, student, school):
        """
        Constructs all the necessary attributes for the Match object.

        Parameters
        ----------
            student : Student
                The student to be matched
            school : School
                The school to be matched
        """
        self.student = student
        self.school = school        
        self.needsMet = []
        self.needsNotMet = []
        for need in student.needs:
            # self.needsMet = [s for s in school.services if need in s]
            if need in school.services:
                self.needsMet.append(need)
            if need not in school.services:
                self.needsNotMet.append(need)        
        self.score = self.initScore()        

    def initScore(self):
        """Calculate the score of the match
        
        Parameters
        ----------
        student : student
            the student
    
        Returns
        -------
        score : float
            the match score
        """
        num_needs = len(self.student.needs)
        num_needs_met = len(self.needsMet)
        if num_needs == 0:
            return 1
        return num_needs_met / num_needs

    def info(self):
        """print the match details
        
        Parameters
        ----------
        None
    
        Returns
        -------
        none        
        """
        self.student.info()
        self.school.info()
        print('Score: ', self.score)
        print('Needs not met:', self.needsNotMet)        
        print('-----------------------------------------------\n')