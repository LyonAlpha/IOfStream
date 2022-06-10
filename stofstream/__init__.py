from colorama import Fore
import datetime as dt

def write_file(filename:str, text:str, newline:bool = True):
    try:    
        with open(filename, 'w') as f:
            if newline == True:
                f.writelines(text)
            else:
                f.write(text)
    except Exception as e:
        print(e)
        
def append_file(filename:str, text:str, newline:bool=True):
    try:
        if newline == True:
            with open(filename, 'a') as f:
                f.writelines('\n')
                f.writelines(text)
        elif newline == False:
            with open(filename, 'a') as f:
                f.writelines(text)
    except Exception as e:
        print(e)
        
def clear_file(filename:str):
    try:
        with open(filename, 'w') as f:
            f.writelines('')
    except Exception as e:
        print(e)
        
def create_file(filename:str):
    try:
        with open(filename, 'x') as f:
            return True
    except Exception as e:
        print(e)
def write_and_read_file(filename:str, text:str='', seek_number:int=0):
    try:
        with open(filename, 'w+') as f:
            f.writelines(text)
            f.seek(seek_number)
            listLines = f.readlines()
            lines = listLines[0]
            return lines
    except Exception as e:
        print(e)
        
def read_and_write_file(filename:str, text:str=''):
    try:
        with open(filename, 'w+') as f:
            f.writelines(text)
            lines = f.readlines()
            return lines
    except Exception as e:
        print(e)

##############################################################################################################################
##############################################################################################################################
####################################################Logger####################################################################
##############################################################################################################################
##############################################################################################################################


class Log():
    def __init__(self, name:str, message:str, level:str, filenamewithlogtype:str=None, willprint:bool=True):
        self.message = message
        self.level = level.upper()
        self.name = name.upper()
        self.filename = filenamewithlogtype
        self.willprint = willprint
        
        if self.filename == 'default':
            today = dt.datetime.today()
            self.filename = f"{today.month:02d}-{today.day:02d}-{today.year}.log"
        
        elif self.filename != 'default' and self.filename != None:
            self.filename = filenamewithlogtype
        
        else:
            pass
        
        if self.level == 'CRITICAL' and self.willprint:
            append_file(self.filename, f'{self.name} --> {self.level} --> + {self.message}')
            print(Fore.RED + self.name + ' --> ' + self.level + ' --> ' + self.message + Fore.RESET)
            
        elif self.level == 'WARNING' and self.willprint:
            append_file(self.filename, f'{self.name} --> {self.level} --> + {self.message}')
            print(Fore.RED + self.name + ' --> ' + self.level + ' --> ' + self.message + Fore.RESET) #TODO Change This To Orange By Using Another Library Instead Of Colorama
            
        elif self.level == 'ERROR' and self.willprint:
            append_file(self.filename, f'{self.name} --> {self.level} --> + {self.message}')
            print(Fore.YELLOW + self.name + ' --> ' + self.level + ' --> ' + self.message + Fore.RESET)
            
        #TODO Add More Logger Methods
    
    # The Following Lines Are For Testing
                
    #def print_attributes(self):
        #print(self.message)
        #print(self.level)
        #print(self.filename)
        #print(self.willprint)
