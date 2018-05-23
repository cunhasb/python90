# follwing iterator class


class Train(object):

    def __init__(self, cars):
        self.cars = cars

    def __len__(self):
        return self.cars

    def __iter__(self):
        return TrainIterator(self)


class TrainIterator(object):

    def __init__(self, train):
        self.train = train
        self.current = 0

    def __next__(self):  # Python3
        if self.current < len(self.train):
            self.current += 1
            return 'car #%s' % (self.current)
        else:
            raise StopIteration()

    next = __next__  # Python 2 compatibility
