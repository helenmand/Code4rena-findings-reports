# Code4rena Findings Reports

This repository provides scripts for downloading Code4rena findings reports from GitHub using Selenium. It includes functionality for scraping both individual report data and repository titles, along with pre-downloaded markdown reports from 2021 to 2024.

## Repository Contents

### Scrape repository titles 
The script in `repository_title_scrapper.py` scrapes repository titles for Code4rena reports from GitHub, providing an overview of the available reports. This is done by collecting the titles of the repositories containing the word **findings**. The titles are stored in a `.txt` file.

### Download Reports 
The script in `report_scrapper.py` scrapes and downloads Code4rena findings reports directly from GitHub using Selenium, based on the results of the previous script. The reports are saved in markdown format.

### Analysis of the finding
A Jupyter notebook, `analysis.ipynb`, containing a bried analysis of the findings reports. 

## Setup and Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/Code4rena-scraper.git
cd Code4rena-scraper
```

### Install the required dependencies

Before running the scripts, you need to install the required Python libraries. You can do this using `pip`:

```bash
pip install -r requirements.txt
```
