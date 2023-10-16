# NoSQL Project

## Project Overview
This project focuses on working with MongoDB, a NoSQL database, and Python to perform various operations like listing databases, creating a new database, inserting documents, querying, updating, and more. You'll gain hands-on experience with NoSQL databases and learn to perform essential operations in a MongoDB environment.

## How to Get Started
Before you begin, you need to install MongoDB and set up your development environment. Here's a step-by-step guide to help you get started:

### Prerequisites
- **Ubuntu 18.04 LTS**: This project is designed to work on Ubuntu 18.04 LTS.
- **Python 3.7**: Make sure you have Python 3.7 installed.
- **MongoDB 4.2**: Install MongoDB 4.2 as your NoSQL database.

### Installing MongoDB
1. Import the MongoDB public GPG key:
   ```bash
   $ wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | apt-key add -
   ```

2. Add the MongoDB repository to your sources list:
   ```bash
   $ echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" > /etc/apt/sources.list.d/mongodb-org-4.2.list
   ```

3. Update your package list and install MongoDB:
   ```bash
   $ sudo apt-get update
   $ sudo apt-get install -y mongodb-org
   ```

### Start MongoDB
To start MongoDB, run the following commands:
```bash
$ sudo service mongod start
$ mongo --version
```

### Python Dependencies
To work with MongoDB in Python, you'll need the PyMongo library. You can install it using pip:
```bash
$ pip3 install pymongo
```

## Running the Tasks
In this project, you will perform various tasks using MongoDB and Python scripts. The tasks include:

1. **List All Databases**: Write a script that lists all databases in MongoDB.

2. **Create a Database**: Write a script that creates or uses the database `my_db`.

3. **Insert Document**: Write a script that inserts a document in the collection `school`.

4. **List All Documents**: Write a script that lists all documents in the collection `school`.

5. **List All Documents by Match**: Write a script that lists all documents with `name` equal to "Holberton school" in the collection `school`.

6. **Count Documents**: Write a script that displays the number of documents in the collection `school`.

7. **Update Documents**: Write a script that adds a new attribute to a document with `name` equal to "Holberton school" in the collection `school`.

8. **Delete Documents by Match**: Write a script that deletes all documents with `name` equal to "Holberton school" in the collection `school`.

9. **List All Documents in Python**: Write a Python function that lists all documents in a collection.

10. **Insert a Document in Python**: Write a Python function that inserts a new document in a collection based on keyword arguments.

11. **Change School Topics**: Write a Python function that changes all topics of a school document based on the name.

12. **Log Stats**: Write a Python script that provides statistics about Nginx logs stored in MongoDB.

13. **Regex Filter**: Lists all documents with `name` starting with "Holberton" in the collection `school`.

14. **Top Students**: Returns all students sorted by average score.

15. **Log Stats - New Version**: Provides improved log statistics with the top 10 most present IPs.

## Project Structure
Here's the structure of this project:

- `0-list_databases`: Script for listing all databases.
- `1-use_or_create_database`: Script for creating a database.
- `2-insert`: Script for inserting a document.
- `3-all`: Script for listing all documents.
- `4-match`: Script for listing documents by match.
- `5-count`: Script for counting documents.
- `6-update`: Script for updating documents.
- `7-delete`: Script for deleting documents.
- `8-main.py`: Python script for listing all documents.
- `9-insert_school.py`: Python script for inserting a document.
- `10-update_topics.py`: Python script for updating school topics.
- `11-schools_by_topic.py`: Python script for listing schools by topic.
- `12-log_stats.py`: Python script for log statistics.
- `100-find`: Script for regex filter.
- `101-students.py`: Python script for finding top students.
- `102-log_stats.py`: Improved Python script for log statistics.

Feel free to explore each script and perform the tasks one by one.

**Have fun learning NoSQL and MongoDB with this project!**
```
