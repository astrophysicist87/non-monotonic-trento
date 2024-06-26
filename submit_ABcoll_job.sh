#!/bin/bash

# these values should correspond to available options in Trento
nucleusA=$1
nucleusB=$2
nEvents=$3

sbatch <<EOT
#!/bin/bash
#SBATCH -t 48:00:00
#SBATCH --nodes=1
#SBATCH --output="${nucleusA}${nucleusB}_job_%j.out"

time ./build/src/trento ${nucleusA} ${nucleusB} ${nEvents}

exit 0
EOT
