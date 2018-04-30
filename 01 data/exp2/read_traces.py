#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 11:52:41 2018

@author: hildeweerts
"""
import os
import pickle
import openml
import 

with open(os.getcwd() + '/hyperimp/01 data/exp2/acc_data.pickle', 'rb') as handle:
     data = pickle.load(handle)

traces = {}
i = 0
for run_id in data['run_id']:
    if i%100 == 0:
        print(i)
    try:
        trace = openml.runs.get_run_trace(int(run_id))
    except openml.exceptions.OpenMLServerException as e:
        print(run_id)
        print(e)
    val_scores = hyperimp.get_val_scores(trace)
    traces[run_id] = val_scores
    i += 1

#%%
with open('trace_data.pickle', 'wb') as handle:
    pickle.dump(traces, handle, protocol=pickle.HIGHEST_PROTOCOL)