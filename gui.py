from tkinter import *
from tkinter import ttk
import time
import timestamp
from driver import *
import box_list
from tkinter.filedialog import askopenfile, askopenfiles
#from progress import *

class App():
    
    def __init__(self, window):
        self.file_number = len(box_list.names)
        self.message = StringVar()
        self.file = StringVar()
        window = window
        main_label = Label(window, text = 'Text time to csv time converter')
        main_label.grid(row = 0, column = 0, columnspan = 3)
        
        browse_button = Button(window, text = 'Browse files', command = self.browse, height = 1, width = 8)
        browse_button.grid(row = 2, column = 0, sticky = W)

        convert_button = Button(window, text = 'Convert files', command = self.convert, height = 1, width = 8)
        convert_button.grid(row = 4, column = 0, sticky = W)
        
        check_button = Button(window, text = 'Check files', command = self.check, height = 1, width = 8)
        check_button.grid(row = 6, column = 0, sticky = W)
        
        self.progress = ttk.Progressbar(window, orient = 'horizontal', length = 200, mode = 'determinate')
        self.progress.grid(row = 7, sticky = W)
        
        self.message.set('Select files to convert')
        self.message_label = Label(window, textvariable = self.message)
        self.message_label.grid(row = 8, column = 0, columnspan = 3, sticky = W)
        
        self.file_label = Label(window, textvariable = self.file)
        self.file_label.grid(row = 10, column = 0, columnspan = 3, sticky = W)
        
        #bar = Progress(window, len(box_list.names))
        #bar.grid(row = 11, column = 0, columnspan = 5)

        
        list = []
    def browse(self):
        self.message.set('Browsing...')
        self.progress['maximum'] = 29
        filename = askopenfiles(filetypes = (("Text files", "*.txt"),("All files", "*.*") ))
        self.message.set(list(map(lambda f: f.name, filename)))
        lst = (list(map(lambda f: f.name, filename)))

        print(lst)
                                                      
    def convert(self):
        self.message.set('Converting...')
        self.progress['maximum'] = 100 
        self.progress['value'] = 0

        count = 0
        for each in box_list.names:
            self.file.set('Converting: ' + each)            
            make_csv(each)
            check_bad(each)
            #progress bar update
            count += 1            
            percent = ((count/self.file_number)*100)
            self.progress['value'] = percent
            
            del times[:]
            time.sleep(0.02)
            root.update_idletasks()
        self.message.set('Done')
        self.file.set('Converted {0} files'.format(len(box_list.names)))
        self.progress['value'] = 0
    
    def check(self):
        self.message.set('Checking...')
        count = 0
        for each in box_list.names:
            check_bad(each)
            count += 1            
            percent = ((count/self.file_number)*100)
            self.progress['value'] = percent
            self.progress['maximum'] = 100 
            self.progress['value'] = 0
        
if __name__ == '__main__':
    root = Tk()
    root.title('Comma')
    app = App(root)
    root.mainloop()