import sys
from pathlib import Path
import csv

VERIFIT_COLUMNS = 'Date,Exercise,Category,Weight (kg),Reps,Comment'

def main():
    args = sys.argv
    if args[1].lower == 'help':
        print('ex usage: python convert.py [FitNotesBackupCSVFile] [OptionalVeriFitBackupFile]')
        return
    

    # input validation
    if not Path(args[1]).is_file():
        print(args[1], ' is not a file')

    if not args[1].endswith('.csv'):
        print(args[1], ' is not a csv file')
    
    # todo: add input validation for verifit backup file.
        
    # open fitNotes CSV file and read the data
    with open(args[1], 'r', encoding="utf-8") as fitNotesFile:
        csvReader = csv.reader(fitNotesFile)
        with open('newVeriFitBackup.txt', 'w', encoding="utf-8") as newFile:
            #newFile.write(VERIFIT_COLUMNS)
            for row in csvReader:
                print(row)

if __name__=="__main__":
    main()
