import csv
import os

def roundto(angle, precision=0.5):
  correction = 0.5 if angle>0 else -0.5
  return int(angle/precision+correction)*precision
  

os.chdir('/home/luxe/Tracking/program/')
with open('dataset_Erik.csv', 'rb') as csvfile:
  reader = csv.reader(csvfile, delimiter=',', quotechar='|')
  next(reader)
  for row in reader:
    if row[1] == '"1"' and row[2] == '"1"' and row[3] == '"6"':
      print int(roundto(float(row[6]),0.25))
