'''A program to split the RFID string into csv format: PIT, antenna, date, month, year, hour, minute, second
November 2018
@authors: James Eapen (jpe4)'''

import re

class Timestamp():
    def __init__(self, line = ''):
        if len(line) == 0:
            self.pit = ''
            self.antenna = ''
            self.month = ''
            self.date = ''
            self.year = ''
            self.hour = ''
            self.minute = ''
            self.second = ''
        else:
            self.timestamp = re.split('\W+', line)
            self.pit = self.timestamp[0]
            self.antenna = self.timestamp[1]
            self.month = self.timestamp[2]
            self.date = self.timestamp[3]
            self.year = self.timestamp[4]
            self.hour = self.timestamp[5]
            self.minute = self.timestamp[6]
            self.second = self.timestamp[7]

    def __str__(self):
        return str(self.pit + self.antenna + self.month + self.date + self.year + self.hour + self.minute + self.second)
    
    def get_timestamp_csv(self):
        return str(','.join(self.timestamp))    

if __name__ == '__main__':
    empty = Timestamp()
    bird = Timestamp('011016DCB7,1,6/13/2016 9:32:35')
    
    print(empty, bird)