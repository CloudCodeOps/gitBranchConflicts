import boto3

# Create S3 client
s3 = boto3.client('s3')

# List buckets (tests connection)
response = s3.list_buckets()

print("Connected to S3 ✅")
print("Your Buckets:")

for bucket in response['Buckets']:
    print("-", bucket['Name'])
