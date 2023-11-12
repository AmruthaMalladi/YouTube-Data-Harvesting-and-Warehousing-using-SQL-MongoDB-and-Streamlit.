# Import Libraries
import json
import re
import logging
import os

import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import pymongo
import mysql.connector
import sqlalchemy
from sqlalchemy import create_engine

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Configure Streamlit GUI
st.set_page_config(layout='wide')

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Constants
MONGO_DB_URL = 'mongodb://localhost:27017/'
MYSQL_DB_URL = 'mysql+mysqlconnector://root:root@localhost/youtube_db'
API_KEY = os.environ.get('YOUTUBE_API_KEY')  # Use environment variable for API key

# ...

# Define a function to retrieve channel data
def get_channel_data(youtube, channel_id):
    try:
        channel_request = youtube.channels().list(
            part='snippet,statistics,contentDetails',
            id=channel_id)
        channel_response = channel_request.execute()

        if 'items' not in channel_response:
            st.write(f"Invalid channel id: {channel_id}")
            st.error("Enter the correct 11-digit **channel_id**")
            return None

        return channel_response

    except HttpError as e:
        logger.error('YouTube API error: %s', e)
        st.error('Server error (or) Check your internet connection (or) Please Try again after a few minutes', icon='🚨')
        return None

    except Exception as e:
        logger.error('An error occurred: %s', e)
        st.write('An unexpected error occurred. Please try again.')

# ...

# Define a function to retrieve video comments
def get_video_comments(youtube, video_id, max_comments):
    try:
        request = youtube.commentThreads().list(
            part='snippet',
            maxResults=max_comments,
            textFormat="plainText",
            videoId=video_id)
        response = request.execute()

        return response

    except HttpError as e:
        logger.error('YouTube API error while fetching comments: %s', e)
        return None

    except Exception as e:
        logger.error('An error occurred while fetching comments: %s', e)
        return None

# ...

# Define a function to retrieve video data
def get_video_data(youtube, video_ids):
    video_data = []

    for video_id in video_ids:
        try:
            request = youtube.videos().list(
                part='snippet, statistics, contentDetails',
                id=video_id)
            response = request.execute()

            video = response['items'][0]

            # Get comments if available (comment function call)
            try:
                video['comment_threads'] = get_video_comments(youtube, video_id, max_comments=2)
            except:
                video['comment_threads'] = None

            # Duration format transformation (Duration format transformation function call)
            duration = video.get('contentDetails', {}).get('duration', 'Not Available')
            if duration != 'Not Available':
                duration = convert_duration(duration)
            video['contentDetails']['duration'] = duration

            video_data.append(video)

        except HttpError as e:
            logger.error('YouTube API error while fetching video data: %s', e)
            st.write('You have exceeded your YouTube API quota. Please try again tomorrow.')
            return []

        except Exception as e:
            logger.error('An error occurred while fetching video data: %s', e)
            st.write('An unexpected error occurred. Please try again.')
            return []

    return video_data

# ...

# Create a database connection
def create_mongo_connection():
    try:
        client = pymongo.MongoClient(MONGO_DB_URL)
        return client
    except Exception as e:
        logger.error('Failed to connect to MongoDB: %s', e)
        return None

def close_mongo_connection(client):
    try:
        client.close()
    except Exception as e:
        logger.error('Error closing MongoDB connection: %s', e)

# ...

# Function to handle MySQL database operations
def execute_mysql_query(query):
    try:
        connect = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            auth_plugin="mysql_native_password")
        cursor = connect.cursor()
        cursor.execute(query)
        connect.commit()
        cursor.close()
        connect.close()
    except Exception as e:
        logger.error('MySQL query execution error: %s', e)

# ...

# Main function to run the Streamlit app
def main():
    # Your existing code for Streamlit UI

    if __name__ == '__main__':
        main()
