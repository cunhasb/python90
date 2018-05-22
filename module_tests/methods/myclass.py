class MyClass:
    """Instance method
    * can Modify object instance state
    *can modify class state.
    """

    def method(self):
        return 'instance method called', self

    """Class method
    *can't modify object instance state,
    *can modify class state.
    """
    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    """Static Method
    *can't modify object instance state,
    *can't modify class state.
    """
    @staticmethod
    def staticmethod():
        return 'static method called'
