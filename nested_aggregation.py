
from database import users_collection


def unwind_connections():

    pipeline = [
        {
            "$unwind": "$connections"
        },

        {
            "$project": {
                "_id": 0,
                "userName": "$name",
                "connectionName": "$connections.name",
                "connectionStatus": "$connections.status"
            }
        }
    ]

    return list(users_collection.aggregate(pipeline))


def count_connection_status():

    pipeline = [
        {
            "$unwind": "$connections"
        },

        {
            "$group": {
                "_id": "$connections.status",
                "totalConnections": {"$sum": 1}
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

    print("\nINDIVIDUAL CONNECTIONS")
    print("=" * 50)

    for document in unwind_connections():
        print(document)

    print("\nCONNECTION STATUS ANALYSIS")
    print("=" * 50)

    for document in count_connection_status():
        print(document)
