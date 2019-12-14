from user import User


class Admin(User):

    def __init__(self, id, pin):

        """
        This method takes two arguments: id and pin.  It calls the
        constructor of the base class.
        :param id: ??
        :param pin: ??

        """

        super().__init__(id, pin)  # Super is the function used for calling the constructor

    def show_roster(self, c_list):

        """
        
        This method displays the roster of a course.  It has one
        parameter: c_list, which is the list of Course objects.  It
        asks user to enter the course he/she wants to see the roster.
        If the course is not offered, display error message and stop.
        Otherwise, call the display_roster method of the course to
        display the roster.  This method has no return value.
        
        """
        choice = input("Enter course: ")
        for course in c_list:
            if choice == course.get_course_code():  # uses the course object and calls the get course code
                course.display_roster()
                break

    def change_max_size(self, c_list):

        """
        
        This method changes the maximum size of a course.  It has
        one parameter: c_list, which is the list of Course objects.
        It asks user to enter the course he/she wants to change max
        size.  If the course is not offered, display error message
        and stop.  Otherwise, call the change_max_size method of the
        course to maximum size.  This method has no return value.
        
        """
        choice = input("Enter course: ")
        for course in c_list:
            if choice == course.change_max_size():
                course.change_max_size()  # calls change max size method-course.py
                break
            else:
                print("Course not found.")
