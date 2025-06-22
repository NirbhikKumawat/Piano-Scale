#! /usr/bin/env python3
import argparse
import sys


valid_commands=['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
c_scale=['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
def rotate_array(array,n):
    n=n%len(array)
    temp=array[:n]
    array[:len(array)-n-1]=array[n:]
    array[len(array)-n-1:]=temp
    return array
def sargam(scale):
    return [scale[0],scale[2],scale[4],scale[5],scale[7],scale[9],scale[11],scale[0]]
c_sharp_scale=['C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C']
d_scale=['D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#']
d_sharp_scale=['D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D']
e_scale=['E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#']
f_scale=['F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E']
f_sharp_scale=['F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F']
g_scale=['G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#']
g_sharp_scale=['G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G']
a_scale=['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
a_sharp_scale=['A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A']
b_scale=['B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#']
arg_mappings = {'C':c_scale,'C#':c_sharp_scale,'D':d_scale,'D#':d_sharp_scale,'E':e_scale,'F':f_scale,'F#':f_sharp_scale,'G':g_scale,'G#':g_sharp_scale,'A':a_scale,'A#':a_sharp_scale,'B':b_scale}
def change_scale(input_file,output_file,in_scale,out_scale):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            for word in line.split():
                for i in range(12):
                    if word == in_scale[i]:
                        outfile.write(out_scale[i])
                        outfile.write(' ')
                        break
                else:
                    outfile.write(word)
                    outfile.write(' ')
            outfile.write('\n')
def main():
    parser = argparse.ArgumentParser(description='Converts music notes between different scales\n.This is created by NirbhikTheNice')
    def percent_arg(value):
     if value in arg_mappings:
       return arg_mappings[value]
     raise argparse.ArgumentTypeError(
            f"Invalid Scale Entered"
        )
    parser.add_argument('inputfile', type=str, help='The file containing notes in original scale')
    parser.add_argument('-o','--outputfile',default='/dev/tty', type=str, help='The file where you want the notes in different scale')
    parser.add_argument('initialscale',type=percent_arg, help='The original scale')
    parser.add_argument('finalscale',type=percent_arg, help='The scale you want')
   
    parser.add_argument('-v', '--verbose', action='store_true', help='Show verbose output')
    
    args = parser.parse_args()
    
   
    change_scale(args.inputfile,args.outputfile,args.initialscale,args.finalscale)
    
    
    if args.verbose:
        print(f"Changed the scale of notes in file {inputfile} from {initialscale} to {finalscale}. Output stored in {outputfile}")
    else:
        print(f"Completed")

if __name__ == '__main__':
    main()
