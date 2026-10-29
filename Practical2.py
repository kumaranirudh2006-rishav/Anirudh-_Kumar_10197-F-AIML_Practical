#                            /////////////////////// Practical - 02 ///////////////////////

# Students
students = ["Anirudh", "Rishav", "Gunu", "Sunny"]

# Branches
branches = ["cse", "ai", "ds", "cs"]

# Enrollment (student, branch)
enrollments = [
    ("Anirudh", "ai"),
    ("Rishav", "cse"),
    ("Gunu", "ds"),
    ("Sunny", "ai")
]

# Count students enrolled in AI
def count():
    student_list = [
        student for student, branch in enrollments
        if branch == "ai"
    ]
    print(len(student_list))

count()
