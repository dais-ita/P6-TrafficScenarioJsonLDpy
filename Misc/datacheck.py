'''
Created on 31 Mar 2017

@author: Federico Cerutti <federico.cerutti@acm.org>
'''

def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False
    
    
def isint(value):
    try:
        int(value)
        return True
    except ValueError:
        return False