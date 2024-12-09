from pymongo import MongoClient
import csv
import urllib.parse

# MongoDB connection details
username = 'mongo_db_user'
host = 'mongo_host'
port = 27017
PASSWORD = 'mongo_pass'
uri = f'mongodb+srv://{username}:{PASSWORD}@{host}/'
MONGO_URI = uri
DATABASE_NAME = 'db_name'
COLLECTION_NAME = 'collection_name'


def connect_to_mongo(uri):
    """Connect to MongoDB and return the client."""
    client = MongoClient(uri)
    return client


def update_docs(client, database_name, collection_name, articles):
    """Fetch all article IDs."""
    db = client[database_name]
    collection = db[collection_name]
    articles_list = []
    for a in articles:
        articles_list.append(a[0])
    
    query = {'_id': {'$in': articles_list}}
    projection = {'_id': 1, 'operation': 1, "state": 1}  # fields

    articles = collection.find(query, projection)
    count = 0
    for article in articles:
        count += 1
        print(f"looping through articles {article['_id']}, count: {count}")
        new_state = 'PENDING'
        filter_query = {'_id': article['_id']}
        update_query = {'$set': {'state': new_state}}
        result = collection.update_one(filter_query, update_query)
        print(f"Matched and updated{result.matched_count}, modified{result.modified_count} articles")
    client.close()


def main():
    #connect
    client = connect_to_mongo(MONGO_URI)
    # read a csv file and update mongodb using the file data
    with open('articles.csv', 'r') as file:
        article_data = csv.reader(file)
        update_articles(client, DATABASE_NAME, COLLECTION_NAME, article_data)


if __name__ == "__main__":
    main()
