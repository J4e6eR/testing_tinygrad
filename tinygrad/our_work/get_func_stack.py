import inspect
import sys
from typing import Optional, List
import faulthandler 

faulthandler.enable()

def generate_stack(self, ignore_function: List= [],count: int = 10, counter:bool = False):
  ignore_function = ['generate_stack'] + ignore_function
  for i in list(reversed(inspect.stack())):
    if ignore_function and i.function not in ignore_function:
      print(f"Function = {i.function} called from {i.filename} at line number ={i.lineno}")
    elif ignore_function == None:print(f"Function = {i.function} called from {i.filename} at line number ={i.lineno}")
  
    # Determines whether the object we pass has counter as attribute or not
    if counter:
      if hasattr(self, 'counter') and i.function == inspect.currentframe().f_code.co_name and self.counter <= count:self.counter += 1;print(f"\nCOUNTER = {self.counter}\n")
      elif hasattr(self, 'counter') == False: print(f"\n\nThe {type(self)} has no counter, please add it\n\n"); sys.exit(1)
      elif self.counter > count: sys.exit(1)      