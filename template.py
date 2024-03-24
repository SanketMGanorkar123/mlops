import os
import logging

def create_files(list_of_files):
    for filepath in list_of_files:
        filepath = os.path.abspath(filepath)
        filedir, filename = os.path.split(filepath)

        # Ensure the directory structure exists
        if filedir != "":
            os.makedirs(filedir, exist_ok=True)
            logging.info(f"Created directory: {filedir} for file: {filename}")

        # Create an empty file if it doesn't exist or is empty
        if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
            with open(filepath, "w") as f:
                logging.info(f"Created file: {filename}")

if __name__ == "__main__":
    # List of files and directories to create
    list_of_files = [
        ".github/workflows/.gitkeep",
        "src/__init__.py",
        "src/components/__init__.py",
        "src/components/data_injection.py",
        "src/components/data_transformation.py",
        "src/components/model_trainer.py",
        "src/components/model_evaluation.py",
        "src/pipeline/__init__.py",
        "src/pipeline/training_pipeline.py",
        "src/pipeline/prediction_pipeline.py",
        "src/utils/__init__.py",
        "src/utils/utils.py",
        "src/logger/logging.py",
        "src/exception/exception.py",
        "tests/unit/__init__.py",
        "tests/integration/__init__.py",
        "init_setup.sh",
        "requirements.txt",
        "requirements_dev.txt",
        "set_up.py",
        "setup.cfg",
        "pyproject.toml",
        "tox.ini",
        "experiment/experiments.ipynb"  
    ]

    # Set up logging
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

    # Create files
    create_files(list_of_files)
