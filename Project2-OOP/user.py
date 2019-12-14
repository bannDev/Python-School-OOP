class User():

    def __init__(self, id, pin):
        """
        This method takes two arguments: id and pin.  It uses these
        # arguments to initialize corresponding instance variables.
        :param id:
        :param pin:

        """

        self.id = id
        self.pin = pin

    def get_id(self):

        """
        This method has no parameter and returns the value of the
        instance variable id
        :return:

        """

        return self.id

    def get_pin(self):

        """
        This method has no parameter and returns the value of the
        instance variable pin.
        :return:

        """

        return self.pin
