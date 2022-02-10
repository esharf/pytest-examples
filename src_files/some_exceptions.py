class ParentException(Exception):

    def __init__(self, *args, **kwargs):
        super(ParentException, self).__init__(*args, **kwargs)


class ChildException(ParentException):

    def __init__(self, *args, **kwargs):
        super(ChildException, self).__init__(*args, **kwargs)
