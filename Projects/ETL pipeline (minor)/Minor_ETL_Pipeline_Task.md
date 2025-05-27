
# Minor ETL Pipeline Project – Internship Task

## 📌 Task Description

You are required to build a minor ETL pipeline during your internship. The objective is to take a file from your local machine, upload it to an AWS S3 bucket using a Python script, and then trigger a Lambda function on upload. The Lambda function should clean the file by:
- Dropping the first 5 rows  
- Removing any column named `UnwantedColumn` if it exists  

Finally, the Lambda should upload the cleaned file back to the S3 bucket with a prefix `cleaned_` added to the file name.

---

## 🗂️ Architecture Diagram

```
Local Machine
     |
     | (Python Script Upload)
     v
AWS S3 Bucket (Original File: Attrition.csv)
     |
     | (Trigger on Upload)
     v
AWS Lambda Function (Cleans the file)
     |
     | (Upload Cleaned File)
     v
AWS S3 Bucket (Cleaned File: cleaned_Attrition.csv)
```

---

## 📤 Python Script to Upload File to S3

```python
import boto3

# AWS credentials
aws_access_key = ''
aws_secret_key = ''
bucket_name = ''
region = 'ap-south-1'  # e.g., Mumbai region

# File details
local_file = 'Attrition.csv'
s3_file_name = 'Attrition.csv'  # Change if you want different name in S3

# Create boto3 client
s3 = boto3.client(
    's3',
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_key,
    region_name=region
)

# Upload file
try:
    s3.upload_file(local_file, bucket_name, s3_file_name)
    print("✅ File uploaded successfully to S3!")
except Exception as e:
    print(f"❌ Upload failed: {e}")
```

---

## 🧠 AWS Lambda Function Code for Cleaning

```python
import boto3
import pandas as pd
import io

def lambda_handler(event, context):
    s3 = boto3.client('s3')

    # Get bucket and file key from the event trigger
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    # Skip processing if file is already cleaned
    if key.startswith('cleaned_'):
        print(f"Ignoring already cleaned file: {key}")
        return {
            'statusCode': 200,
            'body': f"Ignored {key} as it is already cleaned."
        }

    try:
        # Read the file from S3
        obj = s3.get_object(Bucket=bucket, Key=key)
        df = pd.read_csv(io.BytesIO(obj['Body'].read()))

        # Drop the first 5 rows
        df = df.iloc[5:]

        # Drop 'UnwantedColumn' if it exists
        df.drop(columns=['UnwantedColumn'], errors='ignore', inplace=True)

        # Log shape for debugging
        print(f"Processed file: {key} → shape: {df.shape}")

        # Convert DataFrame back to CSV
        csv_buffer = io.StringIO()
        df.to_csv(csv_buffer, index=False)

        # Upload cleaned file with 'cleaned_' prefix
        cleaned_key = f"cleaned_{key}"
        s3.put_object(Bucket=bucket, Key=cleaned_key, Body=csv_buffer.getvalue())

        return {
            'statusCode': 200,
            'body': f"✅ Cleaned file uploaded as {cleaned_key}"
        }

    except Exception as e:
        print(f"❌ Error processing file {key}: {e}")
        return {
            'statusCode': 500,
            'body': f"❌ Lambda failed: {str(e)}"
        }
```

