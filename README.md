# PP2 NumPy

[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/PauliusU/balance_checker/blob/master/LICENSE)

Practical Project 2 (PP2) for Artificial Intelligence studies to
solidify **NumPy** basics by practicing. Project analyses U.S. national debt-to-GDP ratio in the last century (1929-2021)

<!-- TOC -->
* [PP2 NumPy](#pp2-numpy)
  * [Usage](#usage)
      * [Automatic launch](#automatic-launch)
      * [Manual launch](#manual-launch)
  * [Requirements](#requirements)
<!-- TOC -->

## Usage

#### Automatic launch
For Windows installation just **run automatic setup script** in Git Bash:
```bash
bash <(curl -s https://raw.githubusercontent.com/PauliusU/PP2-numpy/master/setup.sh)
```

#### Manual launch

1. Clone this repo:
```bash
git clone https://github.com/PauliusU/PP2-numpy.git
```

2. Navigate into project:
```bash
cd PP2-numpy/
```

3. Ensure pipenv is installed:
```bash
pip install --upgrade pipenv --user
```

4. Install dependencies:
```bash
pipenv install
```

5. Activate virtual environment:
```bash
pipenv shell
```

6. Navigate `drivers/` folder:
```bash
cd drivers/
```

7. Download [ChromeDriver](https://sites.google.com/chromium.org/driver/) (WebDriver for Chrome)
```bash
curl https://chromedriver.storage.googleapis.com/102.0.5005.61/chromedriver_win32.zip -L -o driver.zip
```

8. Unzip ChromeDriver
```bash
unzip driver.zip
```

9. Navigate back to project root folder:
```bash
cd ..
```

10. Run project:
```bash
python ./src/PP2-numpy/main.py
```

## Requirements

- [X] Scrape some data from the internet (does not need to be complex).
- [X] Initialize a numpy array from that data.
- [X] Perform some calculations over it (mean / average, sum, other simple descriptive statistics, and some array filtering must be included).
- [X] Please provide a complete working solution that has some documentation on how to run it and what it does (readme / collab).
- [X] Please provide the solution as either a GitHub repo or collab notebook with all the data necessary to just launch it.

** You can augment your previous PP1 if you want.