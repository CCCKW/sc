import argparse
import os

def make_loom():
    pass

def parse_opt():
    parser = argparse.ArgumentParser()

    parser.add_argument('--repeat_gtf', default='/Bioinformatics-Core/caikangwen/common/mm10_rmsk.gtf', help='repeat_msk.gtf')
    parser.add_argument('--gtf', default='/Bioinformatics-Core/caikangwen/common/refdata-gex-mm10-2020-A/genes/genes.gtf', help='genes.gtf')
    parser.add_argument('--bam', default='/Bioinformatics-Core/caikangwen/data/test_workflow3/GS-2-3/GS-2-3_countResult/')
    parser.add_argument('--mode', default='10x',choices=['10x'], help='lan de xie le zi ji cha mo ren 10x')
    parser.add_argument('--output', default=None, help='zimian')
    opt = parser.parse_args()

    return opt

def main(opt):
    cmd = 'velocyto'
    if opt.mode == '10x':
        cmd += ' ' + 'run10x'
    elif False:
        pass

    cmd += ' -m ' + opt.repeat_gtf

    cmd += ' ' + opt.bam
    cmd += ' ' + opt.gtf
    if opt.output:
        cmd += ' ' + opt.output
    print(cmd)
    os.system(cmd)


if __name__ == "__main__":
    arg= parse_opt()

    main(arg)



# velocyto run10x -m /Bioinformatics-Core/caikangwen/common/mm10_rmsk.gtf mypath/sample01 /Bioinformatics-Core/caikangwen/common/refdata-gex-mm10-2020-A/genes/genes.htf
# velocyto run10x -m   /Bioinformatics-Core/caikangwen/data/test_workflow3/GS-2-3/GS-2-3_countResult
# velocyto run10x -m mm10_rmsk.gtf
# -id sample
# -@ 10
# --samtools-memory 8192
# -t uint32
# sample/cellranger/sample/outs/possorted_genome_bam.bam
# refdata-cellranger-mm10-3.0.0/genes/genes.gtf
# sample/