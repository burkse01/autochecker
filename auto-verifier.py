import requests
import beautifulsoup4
import pandas

url = 'https://www.sis.hawaii.edu/uhdad/avail.classes?i=MAN&t=202330&s=ACM'
exceldoc = ''

#Parse the sheets
changes_sheet = pandas.read_excel(exceldoc, sheet_name='changes', header=3, skiprows=829)

#get only changes which are not verified but have been entered and are valid for the auto verifier

#Sort each change to be verified by subject

#get URL of subject

#Check each element by crn and verify its correctness

#Update google sheet
