# Filename: record-job.py
# Author: Nathaniel Tadesse
# Date: July 27 2022
# Description: Script to record a job application in CSV format.
#               If given an outut file, the script will append the CSV to the file,
#               otherwise it will print to stdout

from datetime import datetime
import argparse
import os

class JobApplication:
    """
    A class to represent a job application

    ...

    Attributes
    ----------
    company: str
        name of the company
    title: str
        title for the job
    job_id: str
        the id for the job description. Defaults to 'NA' to
        signal that an id is not provided in the job post
    date: datetime
        the date job was applied to. Defaults to the current day 
        script was called on 
    """

    def __init__(self, company, title, job_id):
        """
        Constructs all the necessary attributes for the job application object. 

        Parameters
        ----------
        company: str
            name of the company
        title: str
            title for the job
        job_id: str
            the id for the job description. Defaults to 'NA' to
            signal that an id is not provided in the job post
        """
        # Single quotes in variable will mess with SQL load data
        self.company = company.replace("'","")
        self.title = title.replace("'","")
        self.job_id = job_id.replace("'","").replace(" ", "")
        self.date = datetime.today().strftime('%B-%d-%Y')

    def get_job_app(self):
        return f'{job_application.date},{job_application.company},{job_application.title},{job_application.job_id}\n'

parser = argparse.ArgumentParser(description='Record a job application as a CSV')
parser.add_argument('--output-file', metavar='csv-file', type=argparse.FileType('a'),
        help='the csv output file path', required=False)
parser.add_argument('company', metavar='company-name', type=ascii, help='the name of the company')
parser.add_argument('title', metavar='job-title', type=ascii, help='the job title')
parser.add_argument('id', metavar='job-id', type=ascii, help='the id for the job', default='NA')

args = parser.parse_args()

job_application = JobApplication(args.company, args.title, args.id)


if (args.output_file):
    with args.output_file as csvFile:
        if os.stat(csvFile.name).st_size == 0:
            csvFile.write('Date, Company, Job Title, Job ID\n')
        csvFile.write(job_application.get_job_app())
else:
    print(job_application.get_job_app())
    
