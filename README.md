Getting Started with TutorPages
=========================

Jekyll theme based on [Freelancer bootstrap theme ](http://startbootstrap.com/template-overviews/freelancer/)
## Useful Links
 - Tutor Signup form: https://bit.ly/tutorPagestutor
## How to use
 - Fork the repo
 - Replace `your-email@domain.com` in `_config.yml` with your email address. Refer to [formspree](http://formspree.io/) for more information.
 - Clone the repo onto your local machine
 - Download the results of your tutor signup form (see above), and replace the current tutorsignup.xlsx form in your local repo. Open and run the tutorUpload.py file on your local machine
 - 
# Setting Up a Virtual Environment and Installing Required Packages

## Step 1: Install Conda

If you haven't installed Conda yet, you can download and install Miniconda or Anaconda from the official website: [Miniconda](https://docs.conda.io/en/latest/miniconda.html) | [Anaconda](https://www.anaconda.com/products/distribution).

## Step 2: Create a Virtual Environment

Open a terminal or command prompt and create a new virtual environment using Conda. Replace `<env_name>` with your desired environment name.

```bash
conda create --name <env_name> python=3.8
```

Activate the virtual environment:

- On Windows:
  ```bash
  conda activate <env_name>
  ```

- On macOS and Linux:
  ```bash
  source activate <env_name>
  ```

## Step 3: Install Required Packages

Navigate to the directory containing your `requirements.txt` file. Then, use pip to install the required packages:

```bash
pip install -r requirements.txt
```

Replace `requirements.txt` with the actual name of your requirements file if it's different.

## Step 4: Verify Installation

To verify that the packages were installed correctly, you can check the list of installed packages in your virtual environment:

```bash
pip list
```

## Step 5: Deactivate the Virtual Environment

Once you're done working in the virtual environment, you can deactivate it:

```bash
conda deactivate
```

---------
For more details, read the [documentation](http://jekyllrb.com/)
