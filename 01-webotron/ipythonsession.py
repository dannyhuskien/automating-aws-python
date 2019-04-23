# coding: utf-8
impot boto3
import boto3
session = boto3.Session(profile_name='pythonAutomation')
s3 = session.resource('s3')
