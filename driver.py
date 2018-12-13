'''Uses the Timestamp module to create a csv file with all RFID parameters separated
November 2018
@author: James Eapen (jpe4)
'''

from timestamp import Timestamp
import box_list
import os
import sys
from gui import *

class Converter:
    
    def __init__(self):
        '''initialize variables in use'''
        self.bad_count = 0 #number of bad files found
        self.times = [] #list of string objects in the Timestamp class; deleted after each file is worked with
        self.lst = [] #list of files selected by user from gui
        self.bad_year = '' #filename of each file with bad year

    def get_times(self, box_file):
        '''adds each line from input file as an object to list'''
        del self.times[:] #clear the list of timestamp objects
        with open(box_file) as file:
            for line in file:
                time = Timestamp(line)
                self.times.append(time)
    
    def write_times(self, new_csv_file):
        '''writes each comma separated string to the new csv file'''
        with open(new_csv_file, 'w+') as csv:
            csv.write(str('PIT, antenna, month, date, year, hour, minute, second,\n'))
            for time in self.times:
                csv.write(str(time.get_timestamp_csv() + '\n'))
    
    def filenames(self, box_file):
        '''creates a filename with .csv suffix using original filename'''
        for char in box_file:
            if char == '.':
                index = box_file.index(char)
        csv_filename = str(box_file[:index] + '.csv')
        return csv_filename    
            
    def check_bad(self, box_file, year):
        '''writes filenames of box files that have the wrong year by checking against 
        correct year received from user input in gui'''
        if len(self.lst) == 0:
            raise ValueError('No files selected')
        
        if len(year) < 4:
            raise ValueError("No year entered to check against")
        
        self.get_times(box_file)
        count = 0
        with open('bad_year.txt', 'a') as bad_file:
            for time in self.times:
                self.bad_year = ''
                if time.year != year:
                    count += 1
            if count > 1:
                bad_file.write(str(box_file) + '\n')
                self.bad_count += 1
                print('Bad year: ', box_file, file = sys.stderr)
                self.bad_year = str(box_file) + '\n'
                
    def make_csv(self, box_file):
        '''calls get_times and write_times'''
        if len(self.lst) == 0:
            raise ValueError('No files selected')
        self.get_times(box_file)
        self.write_times(self.filenames(box_file))
        del self.times[:]


    def files(self):
        if len(self.lst) == 0:
            raise ValueError('No files selected')
    

#if __name__ == '__main__':
    
