# Turning YouTube Trends Into Insights: AWS Data Pipeline

In today’s data-driven world, the ability to extract value from raw data using modern tools is an essential skill and one I’ve been actively working to develop. Recently, I completed an end-to-end data engineering project using real-world YouTube trending video data. This experience helped me bring together multiple components of the data engineering lifecycle: ingestion, transformation, storage, querying and visualization.

## The Dataset: Real-World, Real Messy

I worked with the Trending YouTube Video Dataset from Kaggle, which contains trending video statistics from multiple countries. The data comes in CSV and JSON formats, with separate files for each region. It includes useful fields such as video titles, categories, tags, view counts, likes, and publish times. Like most real-world datasets, it wasn’t clean or analysis-ready. That made it the perfect candidate for an end-to-end pipeline.

## Building the ETL Pipeline with AWS

![alt text](https://github.com/devansh-pratap-singh/aws-based-youtube-data-pipeline/blob/main/AWS%20Architecture.jpg "AWS Architecture")

To manage the ETL process, I used Amazon Web Services (AWS). Here’s a breakdown of the components I used:

* Amazon S3 served as the data repository. I uploaded raw CSV/JSON files here and structured them into folders for different stages (raw, processed, analytics-ready).
* AWS Glue and Lambda were the heart of the transformation layer. I created a Lambda function to process the JSON files, then used Glue crawler to catalog the schema and finally built a Glue job using PySpark to clean and transform the data.
* AWS Athena allowed me to run SQL queries directly on the processed data in S3. I created views to segment data by region, category and engagement metrics like views, likes and dislikes.

This process gave me firsthand experience with serverless data engineering where I didn’t have to manage infrastructure but could still scale efficiently.

## Visualizing the Insights with Power BI

With the data processed and queried, I turned to Power BI to tell the story visually. I built an interactive dashboard that highlights:

* Top trending categories across countries
* Trends in viewership, likes and dislikes
* Engagement rates by video category

This dashboard made it easy to identify patterns like which categories trend more frequently, or how viewership pattern varies across regions. Check out the full dashboard [here](https://www.linkedin.com/posts/devanshpratapsingh_youtube-trends-analysis-activity-7340377666031710212-hWyU?utm_source=share&utm_medium=member_desktop&rcm=ACoAACjBy0ABaXaaeLrG9iJoE5OORTM6A3LLAv4 "Power BI Dashboard")

## Key Skills & Takeaways

This project was an incredible learning experience that helped me strengthen several core skills:

* Cloud-based ETL architecture using AWS Glue and S3
* Handling semi-structured data and working across file formats
* Data transformation with PySpark
* Query optimization and analysis using Athena
* Dashboard development with Power BI

More than anything, it taught me how to take a messy dataset and build a clear path to insights, something every data engineer needs to know how to do.

## What’s Next?

I plan to keep building more projects like this - diving deeper into orchestration tools (like Apache Airflow), CI/CD for data pipelines and exploring streaming data workflows.
