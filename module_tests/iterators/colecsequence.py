"""collection implementation iterators train sequence
What do you gain?
You are now being more explicit that you are implementing a sequence, and you are inherenting five more methods with it. __getitem__,__contains__,__iter__,__reversed__,index,count
"""
import collections


class Train(collections.Sequence):

    def __init__(self, cars):
        self.cars = cars

    def __len__(self):
        return self.cars

    def __getitem__(self, key):
        index = key if key >= 0 else self.cars + key
        if 0 <= index < len(self):  # index 2 -> car #3
            return 'car #%s' % (index + 1)
        else:
            raise IndexError('no car at %s' % key)
