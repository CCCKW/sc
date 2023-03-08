#!/bin/bash
#SBATCH --job-name=lung
#SBATCH --partition=debug
#SBATCH --output=test-%j.out
#SBATCH --error=test-%j.err
#SBATCH --ntasks 1
#SBATCH --cpus-per-task 32
python SC.py run --start aggr  --dataType fastq
