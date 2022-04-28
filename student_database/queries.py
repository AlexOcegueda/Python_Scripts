import student_data as data


###########################################################################################
# This function is used by other functions to display a list of student's id & names
###########################################################################################
def list_students(student_ids):
    for student_id in student_ids:
        print(student_id, data.students[student_id]['firstName'],
              data.students[student_id]['lastName'])


def student_information():
    """
    ###########################################################################################
    # Display the student information
    # Example of report
    # -----------------------------------
    # ID: 31 Bob Smith
    #	Groups: basketball, track, student council
    #	English [80, 100]
    #	Science [100, 80]
    ###########################################################################################
    """
    print('=' * 80)
    print("Student Information")
    print('=' * 80)

    # for key (student id), value (student info dict) in 2D data.students dict items
    for student_id, student_info in data.students.items():
        # display student id (key) and name (value)
        print('ID:', student_id, student_info.get('firstName'), student_info.get('lastName'))

        print('\tGroups: ', end='')
        # unpack all groups and display by comma separated
        print(*student_info.get('groups'), sep=',')

        for subject, grades in data.grades.items():
            print('\t', subject, grades.get(student_id))
        
            

###########################################################################################
# All Sports List
###########################################################################################
def all_sports_list():
    print('=' * 80)
    print("All Sports")
    print('=' * 80)

    sports = list()

# for key (season), value (season sports set) in 2D data.sports dict items
    for season, season_sports in data.sports.items():
        # for each sport in season sports set
        for sport in season_sports:
            # add sport to sports list
            sports.append(sport)

    print(*sports, sep=', ')

def each_class_genders():
    """
    ###########################################################################################
    # Each Class Genders
    #
    # Example of class_gender dict:
    # -----------------------------------
    # 'math': {'Female': 3, 'Male': 1}
    # 'english': {'Female': 3, 'Male': 2}
    # 'science': {'Female': 3, 'Male': 2}
    #
    # Example of report
    # -----------------------------------
    # Math: Male = 1 Female = 3
    # English: Male = 2 Female = 3
    # Science: Male = 2 Female = 3
    #
    ###########################################################################################
    """
    print('=' * 80)
    print("Each Class Genders")
    print('=' * 80)

    class_genders = dict()
    # building the class_genders dictionary
    # --------------------------------------------------------------------------------------
    # for key (class name), value (class grades dict) in data.grades dict items
    for class_name, class_grades in data.grades.items():
    # initialize the class_
        class_ = dict()
        # for key (student id), value (student grades list) in class grades dict (value) items
        for student_id, student_grades in class_grades.items():
            student_gender = data.students

            if student_id in data.students and student_id not in class_name:
                # add student id (key) to class_
                class_[student_id] = student_grades
                
    #		get gender for the current student id (key) from the 2D data.students dict
    #		if to increment the correct gender counter
    #	append to the class gender dict, using the class as the key, and...
    #   a dict with female and male counts (see above example)


###########################################################################################
# Sue Smith Class LIst
###########################################################################################
def sue_smith_class_list():
    print('=' * 80)
    print("Sue Smith Class List")
    print('=' * 80)

    sue_smith_classes = list()


# building the sue_smith_classes list
# --------------------------------------------------------------------------------------
# for key (student id), value (student info dict) in 2d data.students dict items
#	get first and last names from the student info dict (value)
#	if the first name = Sue and the last name = Smith
#		for key (class), value (class grades dict) in 2D data.grades dict items
#			if student id (outer key) in class grades dict (value)
#				add the class name (key) to sue_smith_classes list with the append method

# sort the list

# for loop for displaying sue_smith_classes list

###########################################################################################
# Students in Science not Math
###########################################################################################
def students_in_science_not_math():
    print('=' * 80)
    print("Students in Science but not in Math")
    print('=' * 80)

    science_not_math = list()

    # building science_not_math list
    # --------------------------------------------------------------------------------------
    # for key (student id) in 2d students dict keys
    #	if student id (key) in data.grades Science and student id (key) NOT in data.grades Math
    #		append student id (key) to science_not_math list

    # sort the list

    list_students(science_not_math)


###########################################################################################
# NonSports groups
###########################################################################################
def non_sports_groups():
    print('=' * 80)
    print("NonSports Groups")
    print('=' * 80)

    sports = set()
    non_sports = list()


# build the sports set
# --------------------------------------------------------------------------------------
# for key (season), value (season sports set) in 2D data.sports dict items
#	append the season sports set to the sports set using update method (multiple values)

# build the non_sports list
# --------------------------------------------------------------------------------------
# for key (student id), value (student info dict) in data.students dict items
#    student groups = student info dict groups
#    whats left = student groups - sports set
#    if len whats left (not 0)
#        append *whats left to non_sports list using the * to convert the set to a tuple

# sort the non_sports list

# for loop for displaying the non_sports list


###########################################################################################
# All Season Sports Students
###########################################################################################
def all_seasons_sports_students():
    print('=' * 80)
    print("All Seasons Sports Students")
    print('=' * 80)

    all_seasons = list()

    # build the all season list
    # --------------------------------------------------------------------------------------
    # for key (student id), value (student info) in 2d data.students items
    #    student groups = student info dict groups
    #    if student groups & data.sports fall \
    #            and student groups & data.sports winter \
    #            and student groups & data.sports spring \
    #            and student groups & data.sports summer
    #        append student id (key) to all_seasons list

    # sort the list

    list_students(all_seasons)


###########################################################################################
# Students classes same as Sue Smith
###########################################################################################
def student_classes_same_as_sue_smith():
    print('=' * 80)
    print("Students Classes same as Sue Smith")
    print('=' * 80)

    sue_smith_classes = set()
    same_as_sue_smith = list()
    students_classes = dict()


# build both sue_smith_classes set, and students_classes dict
# --------------------------------------------------------------------------------------
# for key (student id), value (student info dict) in 2D data.students dict items
#    student_classes = set()
#    first_name = student info dict firstName
#    last_name = student info dict lastName
#    for key (class name), value (class grades dict) in 2D data.grades items
#        if student id (outer key) in class grades dict
#            append class name (key) to student_classes set using add
#    if name equals Sue Smith
#       set sue_smith_classes list to student_classes
#    else
#		add the student id (outer key) students_classes value to student_classes

# for loop for building same_as_sue_smith list
# for key (student id), value (classes) in students_classes items
#    if classes (value) equals sue_smith_classes
#        append student id (key) to same_as_sue_smith list


# sort same_as_sue_smith list

# list_students(same_as_sue_smith)


###########################################################################################
# Students with low grades
###########################################################################################
def students_with_low_grades():
    print('=' * 80)
    print("Students with Low Grades")
    print('=' * 80)

    low_grades = set()

    # building low_grades set
    # --------------------------------------------------------------------------------------
    # for key (student id), value (student info) in 2D data.students items
    #    for key (class name), value (student grades dict) in data.grades items
    #        if student id (outer key) in student grades dict (value)
    #            grade total = sum of student grades student_id (outer key) to grade total
    #	 grade count = len of student grades student_id (outer key) to grade count
    #	 calculate average
    #            if average < 70
    #               add student id (outer key) to low_grades set

    # convert to list and sort

    # list_students(low_grades_list)
