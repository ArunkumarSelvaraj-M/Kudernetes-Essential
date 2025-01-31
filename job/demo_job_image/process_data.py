# process_data.py

# Import necessary libraries
import pandas as pd
from google.cloud import storage

# Function to process data
def process_data():
    # Connect to cloud storage
    storage_client = storage.Client()
    bucket = storage_client.bucket('your-bucket-name')
    
    # Download dataset
    blob = bucket.blob('dataset.csv')
    blob.download_to_filename('dataset.csv')

    # Read dataset
    df = pd.read_csv('dataset.csv')

    # Perform data processing
    # (Example: Calculate summary statistics)
    summary_stats = df.describe()

    # Save processed data
    summary_stats.to_csv('summary_stats.csv')
    bucket.blob('summary_stats.csv').upload_from_filename('summary_stats.csv')

# Run data processing function
if __name__ == "__main__":
    process_data()

