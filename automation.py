
import sys, getopt

class Automation:

    HELP_MESSAGE = 'nexus.py -p <path_to_file> -L <frag_length>'

    @staticmethod
    def get_args(argv):
        path_to_input_file = ''
        read_length = ''

        try:
            opts, args = getopt.getopt(argv,"hp:L:")
        except getopt.GetoptError:
            print(Automation.HELP_MESSAGE)
            sys.exit(2)
        if(len(opts) != 2):
            print(Automation.HELP_MESSAGE)
            sys.exit(2)
        for opt, arg in opts:
            if opt == '-h':
                print(Automation.HELP_MESSAGE)
                sys.exit()
            elif opt in ("-p"): 
                path_to_file = arg
            elif opt in ("-L"): 
                read_length = arg

        return path_to_file, read_length

    def read_file(path):
        with open(path, 'r') as hexinput:
            inputfile = hexinput.read()

        return inputfile
