
from database import users_collection


def match_users(name):
    pipeline = [
        {
            "$match": {
                "name": name
            }
        }
    ]

    return list(users_collection.aggregate(pipeline))


def group_users_by_eye_color():
    pipeline = [
        {
            "$group": {
                "_id": "$eyeColor",
                "totalUsers": {"$sum": 1},
                "names": {"$push": "$name"}
            }
        },
        {
            "$sort": {
                "_id": 1
            }
        }
    ]

    return list(users_collection.aggregate(pipeline))


if __name__ == "__main__":

    print("\n--- GROUP BY EYE COLOR ---\n")

    results = group_users_by_eye_color()

    for result in results:
        print(result)
