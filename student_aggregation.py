
from database import db

students_collection = db["students"]


def analyze_students():

    pipeline = [
        {
            "$group": {
                "_id": "$town",

                "totalStudents": {
                    "$sum": 1
                },

                "averageMarks": {
                    "$avg": "$marks"
                },

                "highestMarks": {
                    "$max": "$marks"
                },

                "lowestMarks": {
                    "$min": "$marks"
                },

                "studentNames": {
                    "$push": "$name"
                }
            }
        },

        {
            "$sort": {
                "_id": 1
            }
        }
    ]

    return list(students_collection.aggregate(pipeline))

def analyze_by_age():

    pipeline = [
        {
            "$group": {
                "_id": "$age",
                "numberOfStudents": {"$sum": 1},
                "averageMarks": {"$avg": "$marks"}
            }
        },
        {
            "$sort": {"_id": 1}
        }
    ]

    return list(students_collection.aggregate(pipeline))

if __name__ == "__main__":

    print("\nSTUDENT AGGREGATION ANALYSIS")
    print("=" * 50)

    results = analyze_students()

    for result in results:

        print("\nTown:", result["_id"])
        print("Total Students:", result["totalStudents"])
        print("Average Marks:", round(result["averageMarks"], 2))
        print("Highest Marks:", result["highestMarks"])
        print("Lowest Marks:", result["lowestMarks"])
        print("Student Names:", result["studentNames"])

    print("\nAGE-WISE ANALYSIS")

    for result in analyze_by_age():
        print(result)