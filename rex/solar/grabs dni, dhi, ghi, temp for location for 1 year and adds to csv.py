import pandas as pd
from rex import NSRDBX

nsrdb_file = '/nrel/nsrdb/v3/nsrdb_2018.h5'
nrel = (39.741931, -105.169891)
with NSRDBX(nsrdb_file, hsds=True) as f:
    nrel_dni = f.get_lat_lon_df('dni', nrel)
    nrel_dhi = f.get_lat_lon_df('dhi', nrel)
    nrel_ghi = f.get_lat_lon_df('ghi', nrel)
    nrel_temp = f.get_lat_lon_df('air_temperature', nrel)


#Add the values of nrel_dhi_minus_date, nrel_ghi_minus_date, and nrel_temp_minus_date to nrel_dni
nrel_dni['dhi'] = nrel_dhi
nrel_dni['ghi'] = nrel_ghi
nrel_dni['temp'] = nrel_temp

#save the value of nrel_dni, which now also includes dhi, ghi, and temp, to a csv
nrel_dni.to_csv(r'C:\Users\Dominic\Desktop\NREL_DNI.csv')
