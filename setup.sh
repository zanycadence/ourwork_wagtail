#! /bin/sh

# create virtual environment with a copy
# of python3, pip and local dependencies
virtualenv --python=python3 venv
source venv/bin/activate

pip install --upgrade pip

# Install any needed packages specified in requirements.txt
pip install -r requirements.txt
pip install gunicorn

# run django migrations
python manage.py migrate

# start app
./start.sh
