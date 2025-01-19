### Steps to Set Up and Run the Project

1. **Clone the GitHub Repository**  
   Open your terminal and run the following command to clone the repository:  
   ```bash
   git clone https://github.com/nivivirat/Final-Year-Project.git
   ```

2. **Check if Conda is Installed**  
   - Run the following command to verify if Conda is installed on your system:  
     ```bash
     conda --version
     ```
   - If Conda is installed, it will display the version.  
   - If Conda is not installed, follow this guide to install it:  
     [How to Install Conda](https://youtu.be/i0DCPOiNK4A?si=hTi2XsP6GjD3gNAf).

3. **Check for CUDA 11.6**  
   Ensure that CUDA 11.6 is installed on your system. Install it if necessary.

4. **Set Up the Conda Environment**  
   - Create a Conda environment using the provided dependencies file:  
     ```bash
     conda create --name ef_sat2rad --file ef-sat2rad/Preprocess/ef_sat2rad.txt
     ```
   - Activate the environment:  
     ```bash
     conda activate ef_sat2rad
     ```

5. **Run the Model**  
   - Navigate to the project directory:  
     ```bash
     cd ef-sat2rad
     ```
   - Execute the training script with the appropriate parameters:  
     ```bash
     python train_cuboid_sevir_invLinear.py --pretrained
     ```