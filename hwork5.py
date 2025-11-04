frontend_students = {"Alice", "Bob", "Charlie", "David"}
backend_students = {"Eve", "Charlie", "Frank", "Grace"}

backend_students.add("Hannah")
frontend_students.remove("Bob")

both_courses = frontend_students.intersection(backend_students)
print(both_courses)

only_backend = backend_students.difference(frontend_students)
print( only_backend)

all_students = frontend_students.union(backend_students)
print("Total unique students:", len(all_students))
print("List of all unique students:", all_students)

course_dict = {
    "Frontend": len(frontend_students),
    "Backend": len(backend_students)
}

for course, count in course_dict.items():
    print(f"Course: {course}, Students: {count}")

new_course_dict = {
    **course_dict,
    "Fullstack": course_dict["Frontend"] + course_dict["Backend"]
}

print("Updated course dictionary with Fullstack:", new_course_dict)