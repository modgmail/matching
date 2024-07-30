#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: m
"""
# import numpy as np
import pandas as pd
import Student as s
import School as sc

def init_from_excel(file):
    """Inialise the students and schools from excel file
    
    Parameters
    ----------
    file : str
        full path to excel file

    Returns
    -------
    students, schools : list<Students>, list<Schools>
        a list of Students, a list of Schools
    """
    students_df = pd.read_excel(file, sheet_name='Sheet1')
    students_df['autistic'] = students_df.apply(lambda row: True if row['Austic'] == 'Yes ' else False, axis=1)
    students_df['blind'] = students_df.apply(lambda row: True if row['Blind'] == 'Yes ' else False, axis=1)
    students_df['deaf'] =  students_df.apply(lambda row: True if row['Deaf'] == 'Yes ' else False, axis=1)
    
    schools_df = pd.read_excel(file, sheet_name='Sheet2')
    schools_df['autistic'] = schools_df.apply(lambda row: True if row['Autism'] == 'Yes' else False, axis=1)
    schools_df['blind'] = schools_df.apply(lambda row: True if row['Blind'] == 'Yes' else False, axis=1)
    schools_df['deaf'] = schools_df.apply(lambda row: True if row['Deaf'] == 'Yes' else False, axis=1)
    
    students = {}
    for i, stud in students_df.iterrows():
        students[stud['Unique Identifier']] = s.Student(stud)
    
    schools= {}
    for i, school in schools_df.iterrows():
        schools[school['Unique Identifier']] = sc.School(school)
    
    return students, schools
    # return students_df, schools_df

def getBestMatch(matches):
    """Get the best match from a list of matches.
    There might be more than 1 school with the maximum score
    We return the first school on the list 

    bestMatches = matches[matches.score == matches.score.max()]
    bestMatch = matches.sort_values(by='score', ascending=False).iloc[0]
    I forget why I'm not using DataFrames
    
    Parameters
    ----------
    matches : list<Match>
        A list 

    Returns
    -------
    match : Match
        The best match
    """    
    bestMatch = ''
    bestScore = 0
    for match in matches:
        if match.score > bestScore:
            bestMatch = match
            bestScore = match.score        
    return bestMatch

file = '../data/Example Student Dataset DRAFT.xlsx'
students, schools = init_from_excel(file)
#%%
# students[234567].needs
# schools[10002].services

# matches = students[234567].getMatches(schools)
# matches[1].info()

# best = getBestMatch(matches)
# best.info()
#%%
bestMatches = []
for student in students.values():
    matches = student.getMatches(schools)
    best = getBestMatch(matches)
    bestMatches.append(best)
    # best.info()
    # print(best.score)

ids = []
for match in bestMatches:
    # print(match.school.id)
    ids.append(match.school.id)
ids

uniqs = set(ids)
counts = {}
for u in uniqs:
    counts[u] = ids.count(u)
# print(counts)

for k,v in counts.items():
    if v > schools[k].slots:
        print('School over subscribed!!!')
        schools[k].info()
        print("It is the best match school for", v, "students")