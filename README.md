# Airflow ETL Data Pipeline
![Airflow](https://github.com/M0hamedIbrahim1/Airflow-Data-Pipeline/blob/main/images/AIRFLOW.png)

## Table of Contents
1. [Introduction](#introduction)
2. [Prerequisites](#prerequisites)
3. [Project Structure](#project-structure)
4. [Setup](#setup)
5. [Airflow DAG](#airflow-dag)
6. [Data Transformation](#data-transformation)
7. [Running the Pipeline](#running-the-pipeline)
8. [Logging and Monitoring](#logging-and-monitoring)



## Introduction
This project demonstrates an ETL (Extract, Transform, Load) data pipeline implemented using Apache Airflow. The pipeline loads data from an S3 bucket, applies data transformations using the Astro framework, and loads the transformed data into a Snowflake database.

## Prerequisites

- An AWS account to access the S3 bucket.
- A Snowflake account for the target Snowflake data warehouse.
- Access to an Apache Airflow environment : AWS Managed Apache Airflow (MWAA).

## Project Structure
The project structure is as follows:


## Setup
1. Clone this repository to your local machine.
2. Ensure that you have Apache Airflow or AWS Managed Apache Airflow (MWAA) set up.
3. Configure your Airflow connections:
   - Create an S3 connection (S3_CONN_ID) for accessing the S3 bucket.
   - Create a Snowflake connection (SNOWFLAKE_CONN_ID) for the Snowflake database.
4. Make necessary modifications to the DAG script to match your specific requirements, including the S3 file path, Snowflake credentials, and data transformations.

## Airflow DAG
![dag](https://github.com/M0hamedIbrahim1/Airflow-Data-Pipeline/blob/main/images/Screenshot_1.png)

The Airflow DAG (Directed Acyclic Graph) is defined in the Python script `Pipeline.py`. It performs the following tasks:
- Sets up a DAG with a unique `dag_id`.
- Schedules the DAG to run daily.
- Defines the data loading, transformation, and loading tasks.
- Uses the Astro framework for data transformation.
- Specifies conflict resolution when merging data into Snowflake.

## Data Transformation
Data transformations are defined using the Astro framework. Two transformation functions are used:
1. `filter_orders`: Filters rows in the input table where the "amount" column is greater than 150.
2. `join_orders_customers`: Joins two tables, filtered orders, and the customer table, using SQL.

## Running the Pipeline
1. Ensure your DAG script is uploaded and configured in your Airflow environment.
2. Trigger the DAG to start the ETL process.
3. Monitor the Airflow logs for any issues or failures.
4. Set up scheduling as per your requirements.

## Logging and Monitoring
To monitor the pipeline's progress and diagnose issues, you can:
- Monitor Airflow logs for task execution details.
- Configure alerts and notifications for failures.

Feel free to connect with me on LinkedIn

[![LinkedIn](https://img.shields.io/badge/Connect%20on-LinkedIn-blue?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/mohamed-ibrahim-513531202/)
