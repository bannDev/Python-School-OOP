from user import User


class Student(User):

    def __init__(self, id, pin):

        """

        This method takes two arguments: id and pin.  It calls the
        # constructor of the base class.
        :param id:
        :param pin:

        """

        super().__init__(id, pin)  # Super is the function used for call the constructor

    def add_course(self, c_list):

        """

        this method adds a student to a course. It has one
        parameter: c_list, which is the list of Course objects. It
        asks user to enter the course he/she wants to add. If the
        course is not offered, display error message and stop.
        Otherwise, call the add_student method of the course to add
        the student. This method has no return value.
        :param c_list:

        """

        #  DEBUG: The parameter of add_student should be self._id instead of c_list which i originally put in
        #  and the if statement is incorrect from the teachers solution that was given. It should be
        #  equal to the input choice instead of the opposite. ORIGINAL CODE: if choice == course.get_course_code():
        #
        choice = input("Enter the class you want to add: ")
        for course in c_list:
            if course.get_course_code() == choice:
                course.add_student(self._id)  # calls the add student method and the id of the student to add
                break
        else:
            print("Course not found.")

    def drop_course(self, c_list):

        """

        This method drops a student from a course. It has one
        # parameter: c_list, which is the list of Course objects. It
        # asks user to enter the course he/she wants to drop.  If the
        # course is not offered, display error message and stop.
        # Otherwise, call the drop_student method of the course to drop
        # the student. This method has no return value.
        
        """
        #  Debugged the code with a for else so the print statement would not repeat
        #  This was the code i had debugged
        #  choice = input("Enter the class you want to add: ")
        #  for course in c_list:
        #  if choice not in c_list:
        #  print("Course not found.")  # Review the code
        #  else:
        #  course.drop_student()  # calls the add student method

        choice = input("Enter course you want to drop: ")
        for course in c_list:
            if choice == course.get_course_code():
                c_list.remove(course)
                break
        else:
            print("Course not found")

    def list_courses(self, c_list):

        """

        This method displays and counts courses a student has
        registered for.  It has one parameter: c_list, which is the
        list of Course objects.  It iterates over c_list to display
        and count courses the student is in the roster. This method
        has no return value.
        
        """
        courses = []
        for course in c_list:
            if course.student_in_course(self._id):
                courses.append(course.get_course_code())
        print(f"Course registered: {courses}")
        print(f"Number of courses registered: {len(courses)}")   # Len function counts the courses
