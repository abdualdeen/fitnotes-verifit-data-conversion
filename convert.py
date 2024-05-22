import sys
import argparse
from pathlib import Path
import csv

VERIFIT_COLUMNS = 'Date,Exercise,Category,Weight (kg),Reps,Comment'

def main():
    parser = argparse.ArgumentParser(prog='convert', description='Converts FitNotes backup to a format verifit can import.')
    parser.add_argument('fitNotesFilePath', help='FitNotes CSV backup file path.')
    parser.add_argument('veriFitFilePath', help='Verifit txt backup file path.', default=None, nargs='?')
    
    args = parser.parse_args()

    # input validation
    if not Path(args[1]).is_file():
        print(args[1], ' is not a file')
        return

    if not args[1].endswith('.csv'):
        print(args[1], ' is not a csv file')
        return
    
    
    if args[2] is not None:
        if not Path(args[2]).is_file():
            print(args[2], ' is not a file')
            return
            
        if not args[2].endswith('.txt'):
            print(args[2], ' is not a csv file')
            return
        
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
