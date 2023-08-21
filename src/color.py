'''
This line starts the definition of a Python class named Color. A class is a 
blueprint for creating objects that will have certain attributes (variables) and methods (functions) associated with them.
'''
class Color:
    '''
    The self parameter refers to the instance of the object being created, 
    and light and dark are parameters that will be used to set the light and dark attributes of the object.
    '''
    def __init__(self, light, dark):
        '''This line assigns the value of the light parameter passed to the constructor to the light attribute of the object. 
        This attribute will hold the "light" color associated with the instance.'''
        self.light = light
        self.dark = dark