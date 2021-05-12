import requests
from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime, timedelta
#from django.http import JsonResponse
import json


# Create your views here.
def trending_lang(request):
    time_now = datetime.now()
    last_month = (time_now - timedelta(days=30)).strftime("%Y-%m-%d")
    url = "https://api.github.com/search/repositories?q=created:>{0}&sort=stars&order=desc&page=1&per_page=100".format(last_month)
    data=requests.get(url).json()

    languages = {element['language'] for element in data['items'] if element['language'] != None}
    response_object = {
		"languages_num" : len(languages),
		"incomplete_results": data['incomplete_results'],
		"languages" : []
	}
    for language in languages:
        language_repos = get_lagugage_repos(language, data['items'])
        
        response_object['languages'].append({
			"name" : language,
			"repositories_count" : len(language_repos),
			"repositories" : language_repos
		})
    return HttpResponse(json.dumps(response_object), content_type="application/json")


def	get_lagugage_repos(language, repositories):
	'''
		Parameters:
			repositories (string): repositories list
			language (string): languages name
		Return:
			list of repos for specific language
	'''
	repos = []
	for repo in repositories:
		if repo['language'] == language:
			# construct repo with information we need
			repo_info = {
				"repo_name" : repo['name'],
				"repo_url" : repo['html_url'],
				"stars_count" : repo['stargazers_count']
			}
			repos.append(repo_info)
	return repos