#!/bin/bash

#Submit this script with: sbatch thefilename

#SBATCH --time=2:00:00   # walltime
#SBATCH --ntasks=16   # number of processor cores (i.e. tasks)
#SBATCH --nodes=1   # number of nodes
#SBATCH --mem-per-cpu=8G   # memory per CPU core
#SBATCH -J "two_generator_all_years"   # job name
#SBATCH --mail-user=dcovelli@caltech.edu   # email address
#SBATCH --mail-type=BEGIN
#SBATCH --mail-type=END
#SBATCH --mail-type=FAIL

echo "Starting at `date`"
echo "Running on hosts: $SLURM_NODELIST"
echo "Running on $SLURM_NNODES nodes."
echo "Running on $SLURM_NPROCS processors."
echo "Current working directory is `pwd`"

# LOAD MODULES, INSERT CODE, AND RUN YOUR PROGRAMS HERE
python run_pypsa.py -f two_generator_all_years.xlsx