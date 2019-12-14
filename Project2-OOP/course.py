"""
        Course
        -----------------------------------------
        - course_code: String
        - max_size: Integer
        - roster: List
        -----------------------------------------
        + Course(c_code: String, m_size: Integer)
        + add_student(id: String)
        + drop_student(id: String)
        + display_roster()
        + change_max_size()
        + get_course_code(): String
        + student_in_course(id): Bool
        -----------------------------------------
"""


class Course():

    def __init__(self, c_code, m_size):

        """

        This method takes two arguments: c_code is course code;
        m_size is maximum class size. It uses c_code and m_size to
        initialize the instance variables course_code and max_size.
        Initialize roster to an empty list.

        """

        self.__course_code = c_code  # PRIVATE variable
        self.__max_size = m_size
        self.__roster = []

    def display_roster(self):

        """

        This method sorts and displays ID of the students enrolled in
        this course and the enrollment count.  It has no parameter
        and no return value.

        """
        self.__roster.sort()
        print(self.__roster)
        print("Number of students: ", len(self.__roster))

    def change_max_size(self):

        """
        This method changes the maximum class size.  It has no
        parameter.  It displays current enrollment count and current
        maximum class size.  It asks user to enter new max size.  If
        new max size is smaller than current enrollment count,
        display error message and ask for a new max size repeatedly
        until it is not smaller than current enrollment count.  It
        has no return value.
        
        """
        print("Current enrollment: ", len(self.__roster))
        print("Current max size: ", self.__max_size)

        while True:
            new_size = int(input("Enter new max size: "))
            if new_size < len(self.__roster):
                print("New max size cannot be smaller than current enrollment.")
            else:
                self.__max_size = new_size
                break

    def add_student(self, id):

        """
        This method adds a student to the roster.  It has one
        parameter: id, which is the ID of the student to be added.
        If the course is already full, display error message and
        stop.  If the student is already enrolled, display error
        message and stop.  Otherwise, add student to roster and
        display a message showing which student added to which
        course.  It has no return value.
        
        """

        if id in self.__roster:
            print("You are already enrolled in this course.")
        else:
            if len(self.__roster) < self.__max_size:
                self.__roster.append(id)
            else:
                print(f"Student {id} added to {self.__course_code}")

    def drop_student(self, id):

        """
        This method removes a student from roster.  It has one
        parameter: id, which is the ID of the student to be dropped.
        If the student is not enrolled, display error message and
        stop.  Otherwise, remove student from roster and display a
        message showing which student dropped from which course.
        It has no return value.
        
        """
        if id in self.__roster:
            self.__roster.remove(id)
            print(f"Student {id} removed from {self.__course_code}")
        else:
            print("You are not enrolled in this course.")

    def get_course_code(self):

        """
        This method has no parameter and returns the value of the
        instance variable course_code.
        
        """
        return self.__course_code

    def student_in_course(self, id):

        """
        This method tests whether a student is enrolled in this
        course. It has one parameter: id, which is the ID of the
        student to be tested.  If student is enrolled in this course,
        return true. Otherwise, return false.
        
        """
        if id in self.__roster:
            return True
        else:
            return False
