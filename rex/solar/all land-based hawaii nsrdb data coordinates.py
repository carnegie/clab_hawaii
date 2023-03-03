# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 16:15:08 2023

@author: Dominic


This code grabs DNI values from each of the coordinates the NSRDB contains for
the land of the state of Hawaii for one given time. From here, you can filter 
the coordinates in the csv to get only the coordinates of Oahu
"""

from rex import NSRDBX

nsrdb_file = '/nrel/nsrdb/v3/nsrdb_1999.h5'
state='Hawaii'
with NSRDBX(nsrdb_file, hsds=True) as f:
    date = '1999-07-04 18:00:00'
    dni_map = f.get_timestep_map('dni', date, region=state, region_col='state')

#save nrel_dni to csv to desktop
dni_map.to_csv(r'C:\Users\Dominic\Desktop\Hawaii_DNI_1999.csv')