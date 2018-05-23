# iterators train sequence


class Train(object):

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
