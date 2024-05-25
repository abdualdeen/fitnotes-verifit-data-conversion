# FitNotes VeriFit Data Conversion Script

A python script that takes FitNotes backup file and converts it to a format that verifit can handle.

# Usage 

**WARNING** Make sure to backup VeriFit before attempting this as VeriFit erases the current data when you import.

The script lets your provide a path to the FitNotes file as well the VeriFit as it will merge the two so you don't lose data you already have on VeriFit. You can ignore the VeriFit file field if you only need to convert your data from FitNotes.

```
python convert.py [fitNotesFilePath] [veriFitFilePath]
```

A txt file will be output that can then be used to import into VeriFit. For the FitNotes file you must do a spreadsheet export.