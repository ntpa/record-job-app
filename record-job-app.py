# Filename: record-job.py
# Author: Nathaniel Tadesse
# Date: July 27 2022
# Description: 

import argparse

parser = argparse.ArgumentParser(description='Record a job application to a .csv file')
parser.add_argument('outputfile', metavar='csv-file', type=argparse.FileType('w', encoding='UTF-8'),
        help='the csv output file path')
parser.add_argument('company', metavar='company-name', type=ascii, help='the name of the company')
parser.add_argument('title', metavar='job-title', type=ascii, help='the job title')
parser.add_argument('id', metavar='job-id', type=ascii, help='the id for the job', default='NA')

args = parser.parse_args()

# Prime I/O Files
with open(args.outputfile.name) as file: 
    for line in file: 
        file.write(f'Date,{args.company.name},{args.title.name},{args.id.name}')
# Create csv line with company, title, id 

# append csv line to output file (append no truncation)
