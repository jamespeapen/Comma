from tkinter import *
from tkinter import ttk
import time
import timestamp
from driver import *
from tkinter.filedialog import askopenfile, askopenfiles

class App():
    '''GUI window for the converter'''
    def __init__(self, window):
        '''initialize the converter object, and messages'''
        self.converter = Converter() #initialize converter instance
        self.file_number = len(self.converter.lst) #number of files selected
        self.message = StringVar() #program status label
        self.file = StringVar() #file status label
        self.hidden = False  #set bad file display to hidden
        self.correct_year = StringVar()
        
        #setup labels and inputs       
        main_label = Label(window, text = 'CSV file creator')
        main_label.grid(row = 0, column = 0, columnspan = 3, sticky = W)        
        
        browse_button = Button(window, text = 'Browse files', command = self.browse, height = 1, width = 15)
        browse_button.grid(row = 1, column = 0, sticky = W)

        convert_button = Button(window, text = 'Convert files', command = self.convert, height = 1, width = 15)
        convert_button.grid(row = 2, column = 0, columnspan = 2, sticky = W)
        
        check_button = Button(window, text = 'Check year', command = self.check, height = 1, width = 15)
        check_button.grid(row = 3, column = 0, sticky = W)
        
        bad_files = Button(window, text = 'Show/hide bad files', command = self.toggle)
        bad_files.grid(row = 9, column = 0, sticky = W)
        
        year_label = Label(window, text = 'Enter correct year: ')
        year_label.grid(row = 3, column = 1, sticky = E)
        
        correct_year = Entry(window, textvariable = self.correct_year, width = 5)
        correct_year.grid(row = 3, column = 2, sticky = W)

        #progress bar
        self.progress = ttk.Progressbar(window, orient = 'horizontal', length = 147, mode = 'determinate')
        self.progress.grid(row = 6, sticky = W)
        
        #message label
        self.message.set('Select files to convert')
        self.message_label = Label(window, textvariable = self.message)
        self.message_label.grid(row = 7, column = 0, columnspan = 3, sticky = W)
        
        #file processing label
        self.file.set('0 files selected')
        self.file_label = Label(window, textvariable = self.file)
        self.file_label.grid(row = 8, column = 0, columnspan = 10, sticky = W)
        
        self.text = Text(window, height = 25, width = 70)

    def browse(self):
        '''opens a file browsing dialog and makes a list of the selected files'''
        self.message.set('Browsing...')
        self.progress['maximum'] = 29
        filename = askopenfiles(filetypes = (("Text files", "*.txt", ".TXT"),("All files", "*.*") ))
        self.converter.lst = (list(map(lambda f: f.name, filename)))
        self.file.set('{0} files selected'.format(len(self.converter.lst)))
        print(self.converter.lst)
        print(len(self.converter.lst))
                                                      
    def convert(self):
        '''converts the selected files to csv and 
        checks for files with bad dates, writing them to a text file'''
        try:
            self.converter.files()
        except ValueError as e:
            self.message.set(e)
            
        self.converter.bad_count = 0
        self.message.set('Converting...')
        self.progress['maximum'] = 100 
        self.progress['value'] = 0
    
        count = 0   #count for the progress bar
        for each in self.converter.lst:
            self.file.set('Converting ' + each)            
            self.converter.make_csv(each)
            count += 1                                 
            percent = ((count/len(self.converter.lst))*100)
            self.progress['value'] = percent
            
            del self.converter.times[:]
            time.sleep(0.02)
            root.update_idletasks()
        self.message.set('Done')
        self.file.set('Converted {0} files.'.format(len(self.converter.lst)))
        self.progress['value'] = 0
    
    def check(self):        
        try:
            print(self.correct_year.get())
            self.file.set('')      
            self.message.set('Checking...')
            root.update_idletasks()
            self.progress['value'] = 0
            self.converter.bad_count= 0
            count = 0
            for each in self.converter.lst:
                self.message.set('Checking...' + each)
                self.converter.check_bad(each, self.correct_year.get())
                count += 1            
                percent = ((count/len(self.converter.lst))*100)
                self.progress['value'] = percent
                self.progress['maximum'] = 100 
                self.text.insert(INSERT, self.converter.bad_year)
                time.sleep(0.02)
                root.update_idletasks()
            self.message.set('{0} bad files found'.format(self.converter.bad_count))
        except ValueError as e:
            self.message.set(e)
        
    def toggle(self):
        '''toggles between showing and hiding the bad file display'''
        if self.hidden:
            self.text.grid_remove()
        else:
            self.text.grid(row = 12, column = 0, columnspan = 10)
        self.hidden = not self.hidden
        
if __name__ == '__main__':
    root = Tk()
    root.title('Comma')
    app = App(root)
    root.mainloop()
    
