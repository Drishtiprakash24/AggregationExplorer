
from database import db

students_collection = db["students"]


def join_student_addresses():

    pipeline = [
        {
            "$lookup": {
                "from": "address",
                "localField": "town",
                "foreignField": "town",
                "as": "addressDetails"
            }
        },

        {
            "$unwind": "$addressDetails"
        },

        {
            "$project": {
                "_id": 0,
                "studentName": "$name",
                "town": "$town",
                "marks": "$marks",
                "city": "$addressDetails.city",
                "state": "$addressDetails.state",
                "pincode": "$addressDetails.pincode"
            }
        },

        {
            "$sort": {
                "studentName": 1
            }
        }
    ]

    return list(students_collection.aggregate(pipeline))


if __name__ == "__main__":

    print("\nSTUDENT ADDRESS JOIN ANALYSIS")
    print("=" * 60)

    results = join_student_addresses()

    if not results:
        print("No matching student-address records found.")

    for student in results:

        print("\nStudent:", student["studentName"])
        print("Town:", student["town"])
        print("Marks:", student["marks"])
        print("City:", student["city"])
        print("State:", student["state"])
        print("Pincode:", student["pincode"])
