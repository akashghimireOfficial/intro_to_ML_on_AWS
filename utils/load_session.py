import boto3
import pandas as pd

def load_session(csv_dire='credential.csv'):
    credential=pd.read_csv(csv_dire)
    session = boto3.Session(
    aws_access_key_id=credential['Access key ID'].item(),
    aws_secret_access_key=credential['Secret access key'].item(),
    region_name=credential['region'].item()
    )
    return session

