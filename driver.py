'''Uses the Timestamp module to create a csv file with all RFID parameters separated
November 2018
@author: James Eapen (jpe4)
'''

from timestamp import Timestamp
import box_list
import os
import sys

times = []
def get_times(box_file):
    '''adds each timestamp from a file as an object to list'''
    with open(box_file) as file:
        for line in file:
            time = Timestamp(line)
            times.append(time)

def write_times(new_csv_file):
    '''writes each csv timestamp to the new csv file'''
    with open(new_csv_file, 'w+') as csv:
        csv.write(str('PIT, antenna, month, date, year, hour, minute, second,\n'))
        for time in times:
            csv.write(str(time.get_timestamp_csv() + '\n'))

def filenames(box_file):
    '''creates a new filename for the new csv file'''
    for char in box_file:
        if char == '.':
            index = box_file.index(char)
    csv_filename = str(box_file[:index] + '.csv')
    return csv_filename    
            
def make_csv(box_file):
    '''calls get_times and write_times'''
    get_times(box_file)
    write_times(filenames(box_file))
    print(str(box_file) + ' converted')

def check_bad(box_file):
    '''writes filenames of box files that have the wrong year'''
    get_times(box_file)
    count = 0
    with open('bad_year.txt', 'a') as bad_file:
        for time in times:
            if time.year != '2018' or int(time.month) < 5:
                count += 1
        if count > 1:
            bad_file.write(str(box_file) + '\n')
            print('Bad year: ', box_file, file = sys.stderr)

def driver(self):
    for each in box_list.names:
        make_csv(each)
        check_bad(each)
        del times[:]     

if __name__ == '__main__':
            
    for each in box_list.names:
        make_csv(each)
        check_bad(each)
        del times[:] 
