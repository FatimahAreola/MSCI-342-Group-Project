# use python container image
From python:3.6-stretch

# set the working directory of the image filesystem 
WORKDIR /app

# copy current directory to the working directory 
ADD . /app

# Install the python dependencies
RUN pip install -r requirements.txt

# start the uWSGI
CMD ["uwsgi", "app.ini"]
