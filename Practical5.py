#                                  /////////////////////////// Practical - 05 //////////////////////////


# Timetable Database
# tt(day, time, subject, faculty, room)

timetable = [
    ("monday", "9:00", "python", "ajay", 101),
    ("monday", "10:00", "aiml", "sanjay", 102),
    ("tuesday", "9:00", "dbms", "verma", 101),
    ("tuesday", "10:00", "python", "ajay", 104)
]


# Find faculty schedule
def faculty_sc(Faculty):
    for Day, Time, Subject, F, Room in timetable:
        if F == Faculty:
            print(Day, Time, Subject, Room)


# Find faculty for a subject
def find_faculty(Subject):
    for Day, Time, S, Faculty, Room in timetable:
        if S == Subject:
            print(Faculty)


# Find room for a time and subject
def find_room(Time, Subject):
    for Day, T, S, Faculty, Room in timetable:
        if T == Time and S == Subject:
            print(Room)


# Function calls
print("Ajay's Schedule:")
faculty_sc("ajay")

print("\nFaculty for AIML:")
find_faculty("aiml")

print("\nRoom for Python at 9:00:")
find_room("9:00", "python")
