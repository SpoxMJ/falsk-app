#!/bin/bash

sudo docker-compose ps | grep aws_excercise_db_1

if [ $? = 0 ] ; then
  sudo docker-compose restart
else
  sudo docker-compose build
  sudo docker-compose up
fi