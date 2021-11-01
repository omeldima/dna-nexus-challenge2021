import sys, getopt

class Converter:

    add_to_qual_score = 33
    current_string = []

    def __init__(self, path=""):
        if path != "":
            self.read_file(path)

    def read_file(self, path):
        all_binaries = self.get_binary_string(path)
        self.convert_binary(all_binaries)

    def convert_binary(self, all_binaries):
        self.current_string = [] 

        for nuc_qual in all_binaries:
            read_info = {
                "nucleotide": self.return_nucleotide(nuc_qual[:2]),
                "quality": self.retrieve_quality_score(nuc_qual[2:])
            }
            self.current_string.append(read_info)

    def print_FASTQ_output(self, read_length, printOutput=True):
        n = iter(self.current_string)
        l = int(read_length)

        read_num = 1
        printing = True
        result_output = ""
        while printing:

            read_sequence = ""
            quality_score = ""
            i = 0
            while i < l:
                nuc = next(n, None)

                if nuc is None: #end
                    printing = False
                    break

                read_sequence += nuc["nucleotide"]
                quality_score+= chr(nuc["quality"] + self.add_to_qual_score)

                i+=1
            
            if printing:
                result_output += self.results_print(read_num, read_sequence, quality_score)
                read_num += 1
        
        if printOutput:
            print(result_output, end='')
        else:
            return result_output

    def results_print(self, num, read_sequence, quality_score):
        result = ""
        result += f"@READ_{num}\n"
        result += read_sequence
        result += f"\n+READ_{num}\n"
        result += quality_score
        result += "\n"
        return result
            
    def return_nucleotide(self, data):
        if data == "00":
            return "A"
        elif data == "01":
            return "C"
        elif data == "10":
            return "G"
        elif data == "11":
            return "T"

    def retrieve_quality_score(self, data):
        return int(data, 2)

    def get_binary_string(self, path):
        
        all_binaries = []
        with open(path, "rb") as f:
            
            cont = f.read(1)
            while cont != b"":
                for b in cont:
                    all_binaries.append(self.convert_hex_input(b,8))
                cont = f.read(1)
            
        return all_binaries

    def convert_hex_input(self, x, n):
        return format(x, 'b').zfill(n)
