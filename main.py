from seqbio.calculation.SeqCal import gcContent,countBasesDict
from seqbio.seqMan.dnaconvert import dna2rna,dna2protein,reverseComplementSeq
from seqbio.pattern.SeqPattern import enzTargetsScan 

def argparserLocal():
    from argparse import ArgumentParser
    parser=ArgumentParser(prog='myseq',description='Work with sequence')
    
    subparsers = parser.add_subparsers(
        title='commands',description='Please chose command below:',
        dest='command'    
    )
    subparsers.required = True
    cgc_command = subparsers.add_parser('gcContent',help='Calculate GC content')
    cgc_command.add_argument("-s","--seq",type=str,default=None,
                            help="Provide sequence")

    cbs_command = subparsers.add_parser('countBases',help='Count number of each base')
    cbs_command.add_argument("-s","--seq",type=str,default=None,
                            help="Provide sequence")
    cbs_command.add_argument("-r","--revcomp" ,action='store_true',default=None,
                            help="Convert DNA to reverse-complementary")
    
    trc_command = subparsers.add_parser('transcription',help='Convert DNA>RNA')
    trc_command.add_argument("-s","--seq",type=str,default=None,
                            help="Provide sequence")
    trc_command.add_argument("-r","--revcomp",action='store_true',
                            help="Convert DNA to reverse-complementary")
 
    trs_command = subparsers.add_parser('translation',help='Convert DNA>Protein')
    trs_command.add_argument("-s","--seq",type=str,default=None,
                            help="Provide sequence")
    trs_command.add_argument("-r","--revcomp",action='store_true',default=None,
                            help="Convert DNA to reverse-complementary")
    
    renz_command = subparsers.add_parser('enzTargetsScan',help='Find Restriction Enzyme')
    renz_command.add_argument("-s","--seq",type=str,default=None,
                            help="Provide sequence")
    renz_command.add_argument("-e","--enz",type=str,default=None,
                            help="Enzyme Name")
    renz_command.add_argument("-r","--revcomp",action='store_true',
                            help="Convert DNA to reverse-complementary")
    #print(parser.print_help())
    return parser
def main():
    parser = argparserLocal()
    args=parser.parse_args()
    args.seq=args.seq.upper()
    if args.command == 'gcContent':
        print("Input",args.seq)
        print("GC content =",gcContent(args.seq))
        
    elif args.command == 'countBases':
        if args.revcomp == None:    
            print("Input",args.seq)
            print("countBases =",countBasesDict(args.seq))
        elif args.revcomp == True:
            print("Input",args.seq)
            print("countBases =",countBasesDict(reverseComplementSeq(args.seq)))    
    elif args.command == 'transcription':
        if args.revcomp == False:
            print("Input",args.seq)
            print("Transcription =",dna2rna(args.seq))
        elif args.revcomp == True:
            print("Input",args.seq)
            print("Transcription =",dna2rna(reverseComplementSeq(args.seq.upper())))  
    
    elif args.command == 'translation':
        print(" reach translate")
        print(args.revcomp)
        if args.revcomp == None:
            print("Input",args.seq)
            print("Translation =",dna2protein(args.seq))
        elif args.revcomp == True:
            print("Input",args.seq)
            print("Translation =",dna2protein(reverseComplementSeq(args.seq)))  
    elif args.command == 'enzTargetsScan':
        if args.revcomp == False:
            print("Input",args.seq)
            print(enzTargetsScan(args.seq,args.enz))
        elif args.revcomp == True:
            print("Input",args.seq)
            print("Ecori site=",enzTargetsScan(reverseComplementSeq(args.seq),args.enz))  
    

    


