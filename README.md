## Inspiration
I'm involved in a community service tutoring club at the University of Chicago called Phoenix Tutoring. We work with CPS students in the south-side Chicago community, and I've always found it really rewarding. Lately I've been trying to come up with a way to streamline our process with some technical infrastructure.

## What it does
Plug-and-Play Tutoring - Instant set up of a community service tutoring program at any college campus. Tutoring programs require a level of technical infrastructure, in particular:
- A mechanism for enrolling students
- A mechanism for undergrads/grads to apply to be tutors
- A mechanism to match tutors and students, once enrolled and admitted
- A calendar to track when tutoring sessions will occur

A good technical infrastructure would also include certain ‘luxuries’, including:
- Automated reminder emails to tutors and tutees based on the calendar
- A mechanism to collect basic analytics: most in-demand subjects, times, etc.
- A mechanism to collect feedback
- A mechanism to re-match tutors and tutees, on a semester to semester basis, based on said feedback

The idea of Plug-and-Play Tutoring/TutorPages is to provide a black box that requires only basic, surface-level inputs from the users and abstracts away all technical complexity, providing features like this as well as room to grow more and build up new capabilities.

## How we built it
For our Treehacks project, we're building a website allowing the user to showcase all tutors and students in their program. We're also putting together a matching algorithm to match tutors to students optimally by distances between n-dimensional preference vectors.

## Challenges we ran into
Creating dynamically updated websites has been challenging, as we're fairly new to web development.

## Accomplishments that we're proud of
While we've run into some technical challenges, we're proud to be working on a project with the intent to make community service easier and more streamlined across the country. We're optimistic about our approach for a matching algorithm and we're proud to have a coherent, condensed project.

## What we learned
Though we haven't moved forward with implementing our website with it, we've learned a lot about the Reflex API. We've also learned a lot about github pages, which we will be using. 

## What's next for TutorPages
Though in the 36hr format of Treehacks we of course can't perfectly implement every niche detail of a product like TutorPages, in the future we'll be continuing to work on it. As we've planned it out there's an ever-growing depth - for example, one key element we'd like to add is log-in and private access for different members of the organization, tutors, parents, students, admin, etc.

## The Matching Algorithm
Taking lists of lists of tutor and tutee information read in by text from our student enrollment/tutor application forms, we make Tutor and Tutee python objects. For a total offering of n subjects and k times, we provide helper functions to 1) take the distance formula on two n-dimensional vectors/points and 2) find overlaps out of lists of <= k times of availability. Using these helpers, we match every tutee to one tutor, with only tutors having the possibility of remaining unmatched. We do this as follows: after making sure the potential-match tutor and tutee are available at the same time, we optimize for similarity of subject preference vectors: tutors that are most comfortable tutoring a given subject are paired with students most in need of help with that subject. Finally, we produce Session objects from our matching dictionary, and store them. We should be left with a grouping of Session objects which can be queried for information about the tutor and tutee, the time, subjects being tutored, and so on.

Getting Started with TutorPages
=========================
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


Jekyll theme based on [Freelancer bootstrap theme ](http://startbootstrap.com/template-overviews/freelancer/)


---------
For more details, read the [documentation](http://jekyllrb.com/)
