#!/usr/bin/env python3
#-*- coding: utf-8 -*-


#import gitlab
import os
import sys
import getopt
import json
import requests

get_mr_title = False
project_id = ''

try:
   opts, args = getopt.getopt(sys.argv[1:],"hi:t:ti:p:b",["token=", "title", "project=", "branch="])

except getopt.GetoptError:
   print('test.py [-c | --commit] [-t | --token {token}]')
   sys.exit(2)
   
for opt, arg in opts:

    #print('[DEBUG] {0} {1}'.format(opt, arg))
    if opt == '-h':
        print('[commit.py] -i <inputfile> -o <outputfile>')
        sys.exit()
    elif opt in ("-t", "--token"):
       if arg is None:
         raise ValueError('Token switch was specified, however no token was supplied.')
       ci_job_token = arg
    elif opt in ("-ti", "--title"):
       get_mr_title = True
    elif opt in ("-p", "--project"):
       project_id = str(arg)
    elif opt in ("-b", "--branch"):
       git_branch = arg


# private token or personal token authentication
#gl = gitlab.Gitlab('https://gitlab.com', private_token=ci_job_token)


url = 'https://gitlab.com/api/v4/projects/' + project_id + '/merge_requests?state=opened&source_branch=' + git_branch

merge_requests = ""

try:

  if os.environ['CI_JOB_TOKEN'] is not None:

    headers = {'JOB_TOKEN': os.environ['CI_JOB_TOKEN']}

  if os.environ['CI_JOB_TOKEN'] == ci_job_token:

    headers = {'JOB_TOKEN': os.environ['CI_JOB_TOKEN']}

  merge_requests = requests.get(url, headers=headers, data='')
  merge_requests = merge_requests.json()
  
except:
    pass


if not isinstance(merge_requests, list):
  headers = {'PRIVATE-TOKEN': ci_job_token}

  merge_requests = requests.get(url, headers=headers, data='')

  merge_requests = merge_requests.json()


#print('\n\nmerge_requests=[-{0}-][]\n\n\n\n\n'.format(merge_requests))


#project_mrs = project.mergerequests.list()
#mrs = gl.mergerequests.list()


mr_title = 'failed to fetch Merge Request title'
mr_first_commit = ''
target_branch = ''

if isinstance(merge_requests, list):

  if len(merge_requests) > 0:

    for mr in merge_requests:

      if mr['source_branch'] == git_branch and str(mr['target_project_id']) == str(project_id) and str(mr['state']) == 'opened':
        mr_title = mr['title']

    if get_mr_title:

      print('{0}'.format(mr_title))

  else:

    print('ci: No Merge Request found, MR count "0"')

