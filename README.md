# DNA Nexus challenge

Dima Omelchenko Mon Nov  1 15:20:36 CET 2021

## Description

This program converts hexidecimal input into FASTQ output. It converts hexidecimal values into binary strings and then creates an output where each byte represents one nucleotide position in the NGS reads. First two bits of each byte contatin an information about particurlar nucleotide and are represented by A,C,G,T strings, other 6 are converted into integer and subsequentually converted into ASCII (33+0-63) symbols which represent a qulaity score of each nucleotide. Program is written in Python 3. In order to run: 
## Usage
```bash
python3 nexus.py -p <path_to_input_file> -L <read_length>
```

## Additional

In order to write an output file use:
```bash
python3  nexus.py -p <path_to_input_file> -L <read_length> > outputfile
```
