# YouTube Data Harvesting and Warehousing

## Introduction
This Python script is designed for extracting data from the YouTube Data API, transforming it, and then warehousing it in MongoDB and MySQL. The Streamlit app provides a user interface to perform these operations and visualize insights from the collected data.

## Dependencies
- pandas
- plotly.express
- streamlit
- streamlit_option_menu
- mysql.connector
- pymongo
- googleapiclient
- Pillow

## Configuration
Before running the script, make sure to install the required dependencies. You also need to set up the following configurations:
- MongoDB Atlas: Update the `pymongo.MongoClient` connection string with your MongoDB Atlas connection details.
- MySQL Database: Update the `sql.connect` parameters with your MySQL database credentials.
- YouTube API: Obtain an API key from the Google Cloud Console and update the `api_key` variable in the script.

## Usage
1. Run the script: `python script.py`.
2. Open the Streamlit app in your web browser.
3. Choose from the sidebar options: Home, Extract & Transform, View.
    - **Home**: Displays an overview of the project.
    - **Extract & Transform**: Extracts data from YouTube API, stores it in MongoDB, and transforms it for MySQL. Also provides options to upload data to MongoDB and transform it to MySQL.
    - **View**: Allows you to view insights derived from the data stored in MySQL.

## Extract & Transform
### Extract
- Enter YouTube Channel_ID to extract data.
- Click "Extract Data" to display information about the channel.
- Click "Upload to MongoDB" to upload channel details, video details, and comment details to MongoDB.

### Transform
- After extracting data, go to the "Transform" tab.
- Select a channel from the dropdown menu.
- Click "Submit" to transform and insert data into the MySQL database.

## View
- Select a question from the dropdown menu to view insights derived from the data stored in MySQL.

## Important Notes
- Make sure to handle sensitive information securely, especially API keys and database credentials.
- Ensure that you have the necessary permissions to access and modify databases.

Feel free to explore the code for more details on the data extraction, transformation, and visualization processes.
Link: https://www.linkedin.com/posts/amruthavallim_hello-linkedin-community-im-excited-to-activity-7129362736626495488-P4Ln?utm_source=share&utm_medium=member_desktop 
