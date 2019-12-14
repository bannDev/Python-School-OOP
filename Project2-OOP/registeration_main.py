# ----------------------------------------------------------------
# Author: Stavros Bannoura
# Date: November 26, 2019
#
# This program creates a class registration system.  It allows
# users to log in as students or administrators.  A student
# user can add courses, drop courses and list courses he/she has
# registered for.  An administrator user can show class rosters
# and change maximum class sizes.
# -----------------------------------------------------------------

from course import Course
from student import Student
from admin import Admin

from project2_helper import student


def main():
    """

    This function manages the whole registration system.  It has
    no parameter.  It creates student list, administrator list
    and course list.  It uses a loop to allow users to create
    student and administrator sessions until the user wants to
    stop. Call either the student_session function or the
    admin_session function, depending on what the user
    chooses. This function has no return value.

    """

    student_list = []
    admin_list = []
    course_list = []

    init_lists(course_list, student_list, admin_list)

    while True:
        choice = int(input("Enter 1 if you are a student, 2 for administrator, 0 to quit: "))
        if choice == 1:
            student_session(course_list, student_list)  # passing the student list parameters
            break
        elif choice == 2:
            admin_session(course_list, admin_list)
            break
        elif choice == 0:
            print("End of choices in the list")
            break


def login(u_list):

    """

    This function allows a student or administrator to log in.
    # It has one parameter: u_list, which is a list of User objects
    # (Student objects and Admin objects are User objects). This
    # function asks user to enter ID and PIN. If they match the data
    # of an element  in u_list, display message of verification and
    # return the index of that element (e.g. return 0 if it is the
    # first element of the list, 1 if it is the second element, and
    # so on).  Otherwise, it displays error message and returns -1.

    :param u_list:
    :return:
    """
    element = -1  # This is used for the error message that returns -1
    user_id = input("Enter ID: ")
    user_pin = input("Enter PIN: ")
    for user in u_list:
        if user.get_id() == user_id and user.get_pin() == user_pin:
            print("ID and PIN verified. ")
            element += 1  # This will add the element to the first list and 2nd list and so on
            break
    else:
        print("ID and PIN incorrect.")
    return element


def student_session(c_list, s_list):

    """
    This function creates a student session.  It has two
    parameters: c_list is the list of Course objects; s_list is
    the list of Student objects.  It calls the login function
    for the student user to log in.  If login is successful, it uses
    a loop to allow the user to add, drop and list courses until
    the user wants to exit. It call methods of the Student object
    to handle the tasks.  This function has no return value.
    :param c_list:
    :param s_list:
    :return:

    """

    user_student = login(s_list)
    if user_student == -1:  # This is referring to the login return statement of -1
        return

    while True:
        course = int(input("Enter 1 to add course, 2 to drop course, 3 to see courses you have registered, 0 to exit: "))
        if course == 1:
            s_list[user_student].add_course(c_list)  # adds user_student to s_list then calls c_list from add_course()
        elif course == 2:
            s_list[user_student].drop_course(c_list)
        elif course == 3:
            s_list[user_student].list_courses(c_list)
        elif course == 0:
            print("Student session has ended.")
            break


def admin_session(c_list, a_list):

    """
    
    This function creates an administrator session.  It has two
    parameters: c_list is the list of Course objects; a_list is
    the list of Admin objects.  It calls the login function for
    the administrator user to log in.  If login is successful, it
    uses a loop to allow the user to show class roster and change
    max class size. It calls methods of the Admin object to handle
    the tasks.  This function has no return value.
    
    """
    user_admin = login(a_list)
    if user_admin == -1:  # This is from the return statement in the login function
        return

    while True:
        course = int(input("Enter 1 to show class roster, 2 to change max class size, 0 to exit: "))
        if course == 1:
            a_list[user_admin].show_roster(c_list)  # adds user_admin to s_list then calls c_list from add_course()
        elif course == 2:
            a_list[user_admin].change_max_size(c_list)
        elif course == 0:
            print("Admin session has ended.")
            break

def init_lists(c_list, s_list, a_list):

    """
    This function adds elements to course_list, student_list and
    admin_list.  It makes testing and grading easier.  It has
    three parameters: c_list is the list of Course objects;
    s_list is the list of Student objects; a_list is the list of
    Admin objects.  This function has no return value.
    
    """

    course1 = Course("CSC121", 2)
    course1.add_student("1004")
    course1.add_student("1003")
    c_list.append(course1)
    course2 = Course("CSC122", 2)
    course2.add_student("1001")
    c_list.append(course2)
    course3 = Course("CSC221", 1)
    course3.add_student("1002")
    c_list.append(course3)

    student1 = Student("1001", "111")
    s_list.append(student1)
    student2 = Student("1002", "222")
    s_list.append(student2)
    student3 = Student("1003", "333")
    s_list.append(student3)
    student4 = Student("1004", "444")
    s_list.append(student4)

    admin1 = Admin("7001", "777")
    a_list.append(admin1)
    admin2 = Admin("8001", "888")
    a_list.append(admin2)


main()
