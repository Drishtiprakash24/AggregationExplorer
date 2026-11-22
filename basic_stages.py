
from database import db

students = db["students"]


def sort_students():
    pipeline = [
        {"$sort": {"marks": -1}}
    ]
    return list(students.aggregate(pipeline))


def top_three_students():
    pipeline = [
        {"$sort": {"marks": -1}},
        {"$limit": 3}
    ]
    return list(students.aggregate(pipeline))


def random_students():
    pipeline = [
        {"$sample": {"size": 3}}
    ]
    return list(students.aggregate(pipeline))


if __name__ == "__main__":

    print("\nSORTED STUDENTS")
    for student in sort_students():
        print(student["name"], student["marks"])

    print("\nTOP THREE STUDENTS")
    for student in top_three_students():
        print(student["name"], student["marks"])

    print("\nRANDOM THREE STUDENTS")
    for student in random_students():
        print(student["name"], student["marks"])
