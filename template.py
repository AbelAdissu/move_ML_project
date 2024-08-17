import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "moviedescription"

list_of_files = [
    # Core project structure
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",  # Data ingestion script
    f"src/{project_name}/components/feature_extraction.py",  # Image feature extraction script
    f"src/{project_name}/components/text_generation.py",  # Text generation model script
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/data_puller.py",  # Data pulling and preprocessing script
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",  # Configuration handling script
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/pipeline/train_pipeline.py",  # Training pipeline script
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/movie_entity.py",  # Entity script defining data structures
    f"src/{project_name}/constants/__init__.py",
    f"src/{project_name}/constants/constants.py",  # Script containing constant values

    # Project configuration and documentation
    "config/config.yaml",  # YAML configuration file
    "dvc.yaml",  # DVC pipeline file for data version control
    "params.yaml",  # Parameters file
    "requirements.txt",  # List of Python dependencies
    "setup.py",  # Setup script for the project
    "research/trials.ipynb",  # Jupyter notebook for research and experiments
    "templates/index.html",  # HTML template for any web UI
]

# Create the directories and files
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as file:
            pass  # Create an empty file
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")
