# Preparing and Displaying Data with Python

This repository showcases a collection of Python projects I’ve worked on over the past several months, focusing on data preparation, analysis, and visualization. It includes hands-on work with libraries such as Pandas, NumPy, Matplotlib, and Seaborn.

## 📌 About This Repository

These projects were originally part of a larger monolithic repository that housed multiple folders, each representing different learning goals or challenges I took on over time.

To better organize my work, I attempted to extract one specific folder—`making-a-bubble-plot`—into its own standalone repository using the following Git command:

```bash
git filter-repo --subdirectory-filter making-a-bubble-plot

While my goal was simply to isolate that folder, I didn’t realize at the time that this command would rewrite the entire commit history of the repository. As a result, all files now appear as if they were added or modified at the same point in time, even though they were created and developed over the course of many months.

💡 Lesson Learned

Although this wasn’t the outcome I intended, the experience taught me a valuable lesson about the power of Git history rewriting and the importance of understanding the impact of such commands before using them. I’m keeping the repository and this note as part of my learning journey.

🧠 What You'll Find Here

Clean and well-documented Python scripts
Visualizations using Matplotlib and Seaborn
Examples of data cleaning and transformation
Exploratory data analysis (EDA) workflows
A focus on writing readable, maintainable code
🚀 What's Next

I’ll continue expanding and refining this work as I grow my skills, with a focus on real-world data projects, improving my use of version control, and building tools that communicate insights effectively.

Thanks for checking out the project!

— Vonschell

# Install Python

Check to see if you already have Python installed on your system by running:

On a Mac:
`python3 --version`

On Windows:
`python --version`

If you already have Python installed, check to be sure it’s Python 3.8 or up. (For example, 3.11 is great!) We suggest waiting on 3.12 to give any dependencies time to be updated.

If you are using a Windows machine, it is possible that you don’t have Python installed. You’ll need to pause here for a moment and proceed to install it. See this document for more [information](https://docs.google.com/document/d/14diNu_g6uhouBscRt8zIezolANTRQA6HobKRP4Lgu5Q/copy).

# Setting up to run scripts to work with Python.

The scripts will be run in a virtual environment. Start by creating a virtual environment. Navigate to to the class folder in the command line and run:

On a Mac:
`python3 -m venv venv`

On Windows:
`python -m venv venv`

You can also create individual virtual environments for each lesson. Directions are in the READMEs in the lesson folders.

<br>
After creating the virtual environment, you need to activate it:

On a Mac:
`source venv/bin/activate`

On Windows:
`source venv/Scripts/activate`

<br>
Once the virtual environment is activated, the beginning of your terminal prompt should display (venv).

<br>
Install the modules by running (in both a Mac and Windows):

`pip install matplotlib numpy requests pandas seaborn beautifulsoup4 statsmodels`

You'll see a venv folder has been added to the directory with all of the installed dependencies.

<br>

With the virtual environment running and the modules installed, you can navigate to the folder for the lesson and run your code.

The scripts in this class can by run with these commands:

On a Mac:
`python3 <filename>`

On Windows:
`python <filename>`

For instance, to run the code in the main.py file the command would be:

On a Mac:
`python3 main.py`

On Windows:
`python main.py`

And to run the solution code:

On a Mac:
`python3 solution.py`

On Windows:
`python solution.py`

<br>

To navigate back to the class folder, run `cd ..` to move up a level. You can then cd into the lesson's folder.

When finished, close the virtual environment by running:

`deactivate`

<br>

Each of the folders has been named for the lesson. So some of the folder names are verrrry long! To make navigating the folders in the command line easier be sure to use the tab key. Start with `cd` and a space. Then type the first few letters of the lesson's folder and hit the tab key. The remainder of the name should appear. If there's more than one option, continue to tab until the right folder appears.

During the class you'll run the same commands repeatedly. In the command line you can scroll through the list of commands you've previously run using the up and down arrow keys in the bottom right of your keyboard. So much faster!

<br>
