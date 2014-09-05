import csv, sys, os, os.path
from datetime import datetime

station_activity = {}
turnstile_key = csv.reader(open('turnstile_key.csv', 'r'))

def get_turnstile_data(f):
	csv_file = csv.reader(open(f))
	for row in csv_file:
		

def main():
	for root, _, files in os.walk('data'):
		for f in files:
			get_turnstile_data(f)



if __name__ == '__main__':
    main()