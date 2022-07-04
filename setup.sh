git clone https://github.com/PauliusU/PP2-numpy.git
cd PP2-numpy/
pip install --upgrade pipenv --user
pipenv install
cd drivers/
curl https://chromedriver.storage.googleapis.com/102.0.5005.61/chromedriver_win32.zip -L -o driver.zip
unzip driver.zip
cd ..
pipenv run python ./src/PP2-numpy/main.py
