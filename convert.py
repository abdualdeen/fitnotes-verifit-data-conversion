import sys
import argparse
from pathlib import Path
import csv

VERIFIT_COLUMNS = 'Date,Exercise,Category,Weight (kg),Reps,Comment\n'

def main():
    parser = argparse.ArgumentParser(prog='convert', description='Converts FitNotes backup to a format verifit can import.')
    parser.add_argument('fitNotesFilePath', help='FitNotes CSV backup file path.')
    parser.add_argument('veriFitFilePath', help='Verifit txt backup file path.', default=None, nargs='?')
    
    args = parser.parse_args()

    # input validation
    print(args.fitNotesFilePath)
    if not Path(args.fitNotesFilePath).is_file():
        print(args.fitNotesFilePath, ' is not a file')
        return

    if not args.fitNotesFilePath.endswith('.csv'):
        print(args.fitNotesFilePath, ' is not a csv file')
        return
    
    
    if args.veriFitFilePath is not None:
        if not Path(args.veriFitFilePath).is_file():
            print(args.veriFitFilePath, ' is not a file')
            return
            
        if not args.veriFitFilePath.endswith('.txt'):
            print(args.veriFitFilePath, ' is not a csv file')
            return
        
    # open fitNotes CSV file and read the data
    with open(args.fitNotesFilePath, 'r', encoding="utf-8") as fitNotesFile:
        next(fitNotesFile) # skip the header
        csvReader = csv.reader(fitNotesFile)
        with open('newVeriFitBackup.txt', 'w', encoding="utf-8") as newFile:
            # write the data from the FitNotes file to be in the format for VeriFit
            newFile.write(VERIFIT_COLUMNS)
            for row in csvReader:
                newRow = f"{row[0]},{row[1]},{row[2]},{row[3]},{row[5]},\n"
                #print(newRow)
                newFile.write(newRow)
            
    # merge the verifit backup data if it exists.    
    if args.veriFitFilePath is not None:
        with open(args.veriFitFilePath, 'r', encoding="utf-8") as veriFitFile:
            lines = veriFitFile.readlines()
            with open('newVeriFitBackup.txt', 'a', encoding="utf-8") as newFile:
                for line in lines:
                    newFile.write(line+'\n')
                    
    print("Operation Completed!")
            

if __name__=="__main__":
    main()
