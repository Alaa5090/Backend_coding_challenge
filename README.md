<h1  align="center">backend-coding-challenge</h1>
backend web app to list the languages used by the 100 trending public repos on GitHub


Alaa Abdraboo ([alaa5090](https://github.com/Alaa5090))

[![code license](https://img.shields.io/badge/code%20license-MIT-blue.svg?longCache=true&style=for-the-badge)](https://choosealicense.com/licenses/mit/)

Code in this repository is provided under the terms of the [MIT license](https://choosealicense.com/licenses/mit/).

## Table of Contents <!-- omit in toc -->

- [About the challenge](#about-the-challenge)
- [Technologies used](Technologies-used)
- [Quick Start](#Quick-Start)
  - [Requirements](#requirements)
  - [Install](#Install)
- [End Points](#Entry-points)


## About the challenge

[Gemography backend-coding-challenge](https://github.com/gemography/backend-coding-challenge/blob/master/README.md) is about creating REST microservice that list the languages used by the 100 trending public repos on GitHub.
- For every language, you need to calculate the attributes below 👇:
    Number of repos using this language
    The list of repos using the language



## Done
-For every language calculate the attributes below 👇:
    Number of repos using this language  (done)
    The list of repos using the language (done)

## Technologies used

	- Django			: python web framework
	- python Requests 	: for using requests capabilities
	

## Quick Start

### Requirements
	- Web browser (chrome)
    - python installed
### Install
1. create a virtual environment
    `py -m venv project-name`
2. activate the environment
    `project-name\Scripts\activate.bat`
3. install Django & requests
    `py -m pip install Django`
    `pip install requests`
4. clone the project
	`git clone https://github.com/Alaa5090/Backend_coding_challenge.git`
5. cd into project directory
	`cd trending_languages`
6. run 
    `python manage.py runserver`

Now, Starting development server at http://127.0.0.1:8000/

## End point
| Entry point   | description|
|-------------  |-----------|
|/trending_lang | list all languages in 100 trending github repos.

