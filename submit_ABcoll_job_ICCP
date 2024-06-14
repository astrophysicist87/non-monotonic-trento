#!/bin/bash

# these values should correspond to available options in Trento
nucleusA=$1
nucleusB=$2
nEvents=$3

sbatch <<EOT
#!/bin/bash
#SBATCH -A qgp
#SBATCH -p qgp
#SBATCH -t 12:00:00
#SBATCH --nodes=1
#SBATCH --output="${nucleusA}${nucleusB}_job_%j.out"

./build/src/trento ${nucleusA} ${nucleusB} ${nEvents}

exit 0
EOT
