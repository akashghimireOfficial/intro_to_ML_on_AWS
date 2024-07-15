# Introduction to Machine Learning on AWS
This github repository contains exercise and other necessary information to complete the course [Intro to Machine Learning on AWS course from coursera](https://www.coursera.org/learn/machine-learning-on-aws). 

In this course we will learn how to utilize AWS services such as ``Amazon S3, AWS Rekognition, Amazon Comprehend, Amazon SageMaker``. I will be making notes on each of these services so anyone who goes through this repository would have a good understanding of above services. 

## Amazon Web Services (AWS)

Amazon Web Services (AWS) is a cloud computing platform by Amazon. It is one of the widely adopted cloud platform.  It provides a a broad set of on-demand services including machine learning. In this course we will also focus on aws machine learning related services. 




## AWS ML Services and Clients(NOT INCLUDED IN THE TURTORIAL)

Before starting this course it is better to have knowledge of how to use `AWS ML Services`. In order to utilize `AWS Services`, we will use `Boto3`, which is the AWS Software Development Kit (SDK) for Python. Boto3 allows Python developers to use AWS services. The `SDK` is a collection of software tools, libraries, documentation, code samples, and other resources that developers use to create applications for specific platforms or environments.

Using `Boto3`, we can initiate `clients` for different ML services such as `Rekognition`. A `client` here is an instance of an AWS service which can initiate different methods like `detect_labels()` (a Rekognition client method) which can be used similarly to APIs.



To install `boto3` run the following scripts:
```bash
pip install boto3
```
If you are not familiar with boto3, and using services using ``boto3``, you can look at basic turtorial for boto3 services (`s3`,`rekognition`,...) in this folder
[aws_services_basic_turtorial/](aws_services_basic_turtorial/)

