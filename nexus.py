#!/usr/bin/python
from automation import *
from converter import *

def main(argv):
    path_to_input_file, read_length = Automation.get_args(argv)

    print('Path to input file: ', path_to_input_file)
    print('Read length (L number): ', read_length)
    
    fastq_converter = Converter(path_to_input_file)
    fastq_converter.print_FASTQ_output(read_length)

if __name__ == "__main__":
    main(sys.argv[1:]) 
