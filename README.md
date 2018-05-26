# Docker-and-Web-Services-using-AWS
Implementation of REST API on weather data using the following methods GET, GET with input parameter, POST, DELETE
# GET Method
Opens the csv file and reads the data and returns the all the dates present in the file in json. To run the GET method use the below link : ec2-52-14-133-222.us-east-2.compute.amazonaws.com:5000/historical
# GET Method with input parameter
This takes an input parameter 'date' in YYYYMMDD format and returns the corresponding TMAX and TMIN in json. To run the GET method with input parameters use the below link: ec2-52-14-133-222.us-east-2.compute.amazonaws.com:5000/historical/YYYYMMDD example: ec2-18-222-102-94.us-east-2.compute.amazonaws.com:5000/historical/20150101
# POST Method
This takes 3 input values 'DATE'(YYYYMMDD) , 'TMAX' , 'TMIN' and posts the new data in the csv file in the corresponding columns in json. To run the POST method we used the REST client (POSTMAN application) Request name - ec2-52-14-133-222.us-east-2.compute.amazonaws.com:5000/historical
Body(Example): "DATE" : "20130101" "TMAX" : "23.0" "TMIN" : "12.0"
# DELETE Method
It takes 'DATE' as input and deletes the corresponding row in the csv file and returns success. Request name - ec2-52-14-133-222.us-east-2.compute.amazonaws.com:5000/historical/YYYYMMDD example:ec2-52-14-133-222.us-east-2.compute.amazonaws.com:5000/historical/ Body: "DATE" : "20130101"
# WEATHER FORECASTING
used Yahoo weather API to forecast weather for the next 7 days GET Method - takes 'DATE' as input and forecasts the weather information for the coming 7 days. Request name - ec2-52-14-133-222.us-east-2.compute.amazonaws.com:5000/historical/20150202
we have implemented a an UI  with a dynamic approach that uses asynchronous java script requests to send the user inputted data to the REST API .
# Python FLASK
We have created to end ports in python: one for predicting the weather data uisng "daily.csv " file and an other using the Yahoo in python. you can run the code using the below link ec2-52-14-211-66.us-east-2.compute.amazonaws.com:5000/forecast/date/ ec2-52-14-211-66.us-east-2.compute.amazonaws.com:5000/API_forecast/
# UI Design
The web page displays a date picker where the user selects the date and provided with the submit button and API_forecast button. The submit button returns the values of the next 6 days from the day choosen using the data from the daily.csv file. The API_forecast button returns the weather data from the yahoo weather API from the current date in the system. The line Graph displays the pattern of the TMIN and TMAX for the predicted days.
# Hosting the web services in a docker
# Installing docker
$ sudo yum update -y $ sudo yum install -y docker $ sudo service docker start
Next, add ubuntu-user to the docker group so you can execute Docker commands without using sudo. Note that you’ll have to log out and log back in for the settings to take effect:
$ sudo usermod -a -G docker ubuntu
$ exit
# Created a directory "cloud" which holds the Dockerfile,app.py templates directory( forecast.html).
Created a Docker image by using the command
docker build -t weatherforecast
# Run the app, mapping your machine’s port 80 to the container’s published port 80 using -p:
docker run -p 80:80 -t weatherforecast
# To see the actives images running
docker ps
# To stop an image
docker stop <imageid>
# To destroy all the images and the containers
docker system prune
Create an account in cloud.docker.com
# Run docker tag image with your username, repository, and tag names so that the image uploads to your desired destination:
docker tag weatherforecast saisoudamini/cloudproject:final
# Upload your tagged image to the repository
docker push saisoudamini/cloudproject:final
# you can use docker run and run your app on any machine with this command:
docker run -p 80:80 saisoudamini/cloudproject:final
# Created a docker image file using the below commands
docker images --filter reference=weatherforecast
# To save and load the content
docker save -o weatherforcast.tar weatherforecast docker load -i weatherforcast.tar
# saved the tar file in Amazon S3.
You can download the file using the below link https://s3.us-east-2.amazonaws.com/weatherforecast-image/weatherforcast.tar
