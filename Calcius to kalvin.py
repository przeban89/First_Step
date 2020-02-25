class TooColodException(Exception):
    def __init__(self, temp):
        super().__init__('Temperature {} is bilow to absolute zero!'.format(temp))

def celcius_to_kalvin(temp):

    if temp < -273.15:
        raise TooColodException(temp)
    return temp + 273.15


celcius_to_kalvin(20)