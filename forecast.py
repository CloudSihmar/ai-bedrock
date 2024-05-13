import boto3
import csv

# Initialize the AWS ForecastQuery client
client = boto3.client('forecastquery')

# Query the forecast
response = client.query_forecast(ForecastArn='arn:aws:forecast:ap-south-1:685421549691:forecast/my_forecast',  
                                  StartDate="2019-07-28T00:00:00", 
                                  EndDate="2019-08-26T00:00:00", 
                                  Filters={"item_id" : "2606"})

# Extract the predictions
predictions = response["Forecast"]["Predictions"]

# Specify the path for the CSV file
csv_file_path = 'predictions.csv'

# Write the predictions to a CSV file
with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Timestamp", "Value"])
    for percentile in ['p10', 'p50', 'p90']:
        for prediction in predictions[percentile]:
            timestamp = prediction["Timestamp"]
            value = prediction["Value"]
            writer.writerow([timestamp, value])

# Upload the CSV file to an S3 bucket
s3_client = boto3.client('s3')
bucket_name = 'sandy-0419044'
s3_client.upload_file(csv_file_path, bucket_name, 'predictions.csv')
