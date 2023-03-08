#SBATCH --job-name=cellranger
#SBATCH --partition=debug
#SBATCH --output=test-%j.out
#SBATCH --error=test-%j.err
#SBATCH --ntasks 4
#SBATCH --cpus-per-task 12

workflow=/home/tmp/monkey_test

sample=ABC

fastqdir=abc

gtf=/Bioinformatics-Core/caikangwen/common/refdata-gex-GRCh38-2020-A

outdir="$workflow""/""$sample""_countResult"


echo $outdir

cd $workflow 

cellranger count \
	--id=$outdir \
	--sample=$sample \
	--transcriptome=$gtf \
	--fastqs=$fastqdir
