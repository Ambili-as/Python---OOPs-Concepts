#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Build a program to manage a university's course catalog.


# In[ ]:


#define a base class Course that has the following properties:
#course_code: a string representing the course code (e.g., "CS101")
#course_name: a string representing the course name (e.g., "Introduction to Computer Science")
#credit_hours: an integer representing the credit hours for the course (e.g., 3)


# In[ ]:


#You also want to define two subclasses CoreCourse and ElectiveCourse,
#which inherit from the Course class. 
#CoreCourse should have an additional property required_for_major
#which is a boolean representing whether the course is required for a particular major. 
#ElectiveCourse should have an additional property elective_type 
#which is a string representing the type of elective (e.g., "general", "technical", "liberal arts").


# In[16]:


# Base Class
class Course:
    def __init__(self, course_code, course_name, credit_hours):
        self.course_code = course_code
        self.course_name = course_name
        self.credit_hours = credit_hours

    def display_course(self):
        """Display course details."""
        print("Course Code: " ,self.course_code)
        print("Course Name: ",self.course_name)
        print("Credit Hours: " ,self.credit_hours)


# Subclass for Core Courses
class CoreCourse(Course):
    def __init__(self, course_code, course_name, credit_hours, required_for_major):
        super().__init__(course_code, course_name, credit_hours)
        self.required_for_major = required_for_major
    def display_course(self):
        """Display core course details."""
        super().display_course()
        print("Required for Major: 'Yes' " if self.required_for_major else 'No')


# Subclass for Elective Courses
class ElectiveCourse(Course):
    def __init__(self, course_code, course_name, credit_hours, elective_type):
        super().__init__(course_code, course_name, credit_hours)
        self.elective_type = elective_type

    def display_course(self):
        """Display elective course details."""
        super().display_course()
        print("Elective Type: ",self.elective_type)


# Course Catalog to Manage Courses
class CourseCatalog:
    def __init__(self):
        self.courses = []

    def add_course(self, course):
        """Add a course to the catalog."""
        self.courses.append(course)
        print("Course ",course.course_name, "added successfully!")

    def display_catalog(self):
        """Display all courses in the catalog."""
        if not self.courses:
            print("The course catalog is empty.")
        else:
            print("Course Catalog:")
            for course in self.courses:
                course.display_course()
                print("-" * 20)



# In[17]:


# Example 
if __name__ == "__main__":
    catalog = CourseCatalog()

    # Creating courses
    core_course = CoreCourse("CS101", "Introduction to Computer Science", 3, True )
    elective_course1 = ElectiveCourse("EC201", "Electronics and Communication", 3, "Photonics")
    elective_course2 = ElectiveCourse("CE102", "Civil Engineering", 2, "Structural")

    # Adding courses to the catalog
    catalog.add_course(core_course)
    catalog.add_course(elective_course1)
    catalog.add_course(elective_course2)

    # Displaying the catalog
    catalog.display_catalog()


# In[ ]:





# In[20]:



    


# In[ ]:





# In[ ]:





# In[ ]:




