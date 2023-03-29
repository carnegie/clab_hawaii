**This is how you set up the Caltech HPC so that you can run pypsa:**  
**This protocol has been ammended so that it runs on the compute nodes, not login. Instructions for running quick jobs on the login node are at the bottom.**  

In the terminal  
Install miniconda3  
* wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh  
* sh ./Miniconda3-latest-Linux-x86_64.sh     

Install pypsa  
* pip install pypsa  

Then run commands  
* pip uninstall matplotlib  
* pip install matplotlib  
* pip install openpyx1 

Upload the clab_pypsa folder to your HPC directory  
Upload your input file with the correct path  
--> My input path is /home/dcovelli/clab_pypsa/inputs  
Upload the .sh file that runs run_pypsa.py  
--> You can make most of this through https://s3-us-west-2.amazonaws.com/imss-hpc/index.html or see my .sh file  
Then run commands   
* chmod +x filename.sh  
* sed -i -e 's/\r$//' filename.sh <--skip this step if you use Notepad++ to convert the .sh to unix format before uploading
* module load gurobi/10.0.0  <--make sure this is the last command you type before the sbatch command


You can now add your input to the queue  
* sbatch filename.sh  


**Method to run on the login node**  
In the terminal
Install miniconda3  

* wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh  
* sh ./Miniconda3-latest-Linux-x86_64.sh  
Install gurobi  

* pip install gurobipy  
Install gurobi license this part has worked but may not be the best solution. I don't know enough about Web License Service key vs regular key  

* grbgetkey type_key_here  
Install pypsa 

Then run commands  

* pip uninstall matplotlib  
* pip install matplotlib  
* pip install openpyx1  

* pip install pypsa  
Upload the clab_pypsa folder to your HPC directory  
Upload your input file with the correct path  
--> My input path is /home/dcovelli/clab_pypsa/inputs    
Upload the .sh file that runs run_pypsa.py  
--> You can make most of this through https://s3-us-west-2.amazonaws.com/imss-hpc/index.html or see my .sh file  
Then run commands  
* chmod +x filename.sh  
* sed -i -e 's/\r$//' filename.sh  
You can now run your input  

* ./ filename.sh  
