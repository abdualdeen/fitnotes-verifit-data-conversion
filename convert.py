import sys
import argparse
from pathlib import Path
import csv

VERIFIT_COLUMNS = 'Date,Exercise,Category,Weight (kg),Reps,Comment'

def main():
    args = sys.argv
    if args[1].lower == 'help':
        print('ex usage: python convert.py [FitNotesBackupCSVFile] [OptionalVeriFitBackupFile]')
        return
    
    if args[1] is None:
        print('Error: did not provide a file to convert.') 

    # input validation
    if not Path(args[1]).is_file():
        print(args[1], ' is not a file')

    if not args[1].endswith('.csv'):
        print(args[1], ' is not a csv file')
    
    
    if args[2] is not None:
        if not Path(args[2]).is_file():
            print(args[2], ' is not a file')
            
        if not args[2].endswith('.txt'):
            print(args[2], ' is not a csv file')
        
    # open fitNotes CSV file and read the data
    with open(args[1], 'r', encoding="utf-8") as fitNotesFile:
        csvReader = csv.reader(fitNotesFile)
        with open('newVeriFitBackup.txt', 'w', encoding="utf-8") as newFile:
            # write the data from the FitNotes file to be in the format for VeriFit
            newFile.write(VERIFIT_COLUMNS)
            for row in csvReader:
                newRow = f"{row[0]},{row[1]},{row[2]},{row[3]},{row[5]}"
                #print(newRow)
                newFile.write(newRow)
            
    # merge the verifit backup data if it exists.    
    if args[2] is not None:
        with open(args[2], 'r', encoding="utf-8") as veriFitFile:
            lines = veriFitFile.readlines()
            with open('newVeriFitBackup.txt', 'a', encoding="utf-8") as newFile:
                for line in lines:
                    newFile.write(line)
                    
    print("Operation Completed!")
            

if __name__=="__main__":
    main()
