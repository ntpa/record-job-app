# record-job-app

Record a job application in CSV format for standalone use, database use or for your favorite spreadsheet application.

### Requirements

- [Python 3.0](https://www.python.org/download/releases/3.0/+)

### Usage

```python
python3 record-job-app.py [-h] [--output-file csv-file] company-name job-title job-id
```

### Overview
Run the script above in your terminal of choice. The script takes an optional output file parameter, that when given
will append the job application in CSV format. Otherwise it will print the result out to standard output.

Below is an example of a table definition if you wish to copy the CSV data into a database(**potential streamlined support for this in the future**).

> The below assumes PostgreSQL ('text' datatype is Postgre specific)

```sql
CREATE TABLE jobapps (
date date NOT NULL,
company text NOT NULL,
job_title text NOT NULL,
job_id text
);
```

As always, if you wish to contribute, or recommend implementations please do not hesitate to reach out!
