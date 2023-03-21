This is how you set up the Caltech HPC so that you can run pypsa:

In the terminal  
Install miniconda3  
* wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh  
* sh ./Miniconda3-latest-Linux-x86_64.sh   

Install gurobi  
* pip install gurobipy  

Install gurobi license *this part has worked but may not be the best solution. I don't know enough about Web License Service key vs regular key*  
* grbgetkey type_key_here  

Install pypsa  
* pip install pypsa  

Upload the clab_pypsa folder to your HPC directory  
Upload your input file with the correct path  
--> My input path is /home/dcovelli/clab_pypsa  
Upload the .sh file that runs run_pypsa.py  
--> You can make most of this through https://s3-us-west-2.amazonaws.com/imss-hpc/index.html or see my .sh file  
Then run commands  
* pip uninstall matplotlib  
* pip install matplotlib  
* pip install openpyx1  
* chmod +x filename.sh  
* sed -i -e 's/\r$//' filename.sh  

You can now run your input  
* ./ filename.sh  
