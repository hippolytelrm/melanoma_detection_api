# Global env variables
ENV_NAME=melanoma

# Create conda env
conda create -n $ENV_NAME python=3.8.11
eval "$(conda shell.bash hook)"
conda activate $ENV_NAME

# Install packages in melanoma repo
pip install -e .
pip install -r requirements_M1.txt

