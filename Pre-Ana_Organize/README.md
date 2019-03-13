### These scripts are provided as-is and nothing is guaranteed. A basic knowledge of python is assumed for editing the files

# BIDS Organization Scripts

These two python scripts are designed to:
    1. Create a BIDS directory tree that lines up with your traditional data storage method
    2. Transfer data from your existing file setup to the new BIDS setup

## Limitations

The directory script simply builds a file tree with the proper number of subjects given, not limitations
The move script works off of two assumptions:
    1. Your participant folders are labelled with only participant numbers (i.e. 17271)
    2. You want the BIDS folder right next to your data folder
The first can be corrected in the code with some experience in python, and
he second is hardly an inconvenience, as the folder can be moved later

### Prerequisites

The scripts are written to be run in Python 2.7.x
The modules used are included by default on many systems, but if errors are raised just install the needed modules

## Authors

* **Zachary Traylor** - *CNAPS Lab, LSU* - [CNAPS LSU](https://github.com/cnapslab)

# BIDS_organization
