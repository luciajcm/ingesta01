import boto3

ficheroUpload = "data.csv"
nombreBucket = "gcr-output20252-01"

s3 = boto3.client('s3')
response = s3.upload_file(ficheroUpload, nombreBucket, ficheroUpload)
print(response)

print("Ingesta completada")