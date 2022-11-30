# Project 4 - Fangting Ma

[![Python application test with Github Actions](https://github.com/nogibjj/Fangting_P4/actions/workflows/main.yml/badge.svg)](https://github.com/nogibjj/Fangting_P4/actions/workflows/main.yml)

## INTRODUCTION

It is my 706 Project 4. I created Microservices in Fast API using AWS ECR and App Runner and pushed it onto my Github. It basically implements three APIs, one for introduction page, one for querying some interesting facts happened in a given year, and one for querying covid-19 statistics for the given date.

## IMPLEMENTATION

I created this new repo on github for my project 4, and worked on it in a cloud development environment, Cloud9. 
I created two Microservices, both of which can return JSON payloads.
I performed Continuous Integration with Github Actions.
I created a docker container for it, and pushed the docker image to ECR.
I created App Runner Service for automatically deploying the most updated version.
