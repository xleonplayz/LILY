## Project Folder Structure

The Quantum Neural Network (QNN) project is organized into a structured directory to facilitate efficient development and ease of navigation. Below is an overview of the main components of the project's folder structure:

### docs
This directory contains all the documentation related to the project. It includes the system architecture (`Architecture.md`), detailed implementation notes (`ImplementationDetails.md`), and a user guide (`UserGuide.md`) for end-users.

### src
The source code of the project is housed here. It is further divided into several subdirectories:
- **data**: Contains scripts for data handling, including `load_data.py` for loading the dataset and `process_data.py` for preprocessing and data manipulation.
- **models**: This folder is split into two subfolders:
  - **qnn**: Contains the Quantum Neural Network model files, including `qnn_model.py` for the model definition, `qnn_training.py` for the training process, and `qnn_evaluation.py` for evaluating the model's performance.
  - **classical_nn**: Houses the classical neural network models for comparative purposes, with similar files for model definition, training, and evaluation.
- **tests**: Includes test scripts like `test_qnn.py` and `test_classical_nn.py` to ensure the reliability and accuracy of both quantum and classical models.
- **utils**: Consists of utility scripts and functions that support various aspects of the project, such as quantum-specific utilities (`quantum_utilities.py`), data handling (`data_utilities.py`), and general-purpose utilities (`general_utilities.py`).

### notebooks
Contains Jupyter notebooks like `Prototyping.ipynb` for experimental prototyping and `Demonstration.ipynb` for showcasing the project's capabilities.

### scripts
This directory includes various scripts for automated tasks such as `data_preparation.sh` for preparing the data, `model_training.sh` for training the models, and `model_evaluation.sh` for evaluating their performance.

### configs
Houses configuration files like `environment_variables.env` for setting up environmental variables and `model_parameters.json` for defining model parameters.
