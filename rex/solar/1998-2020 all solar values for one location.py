"""
This script will create a csv with all the solar values for one location for 1998-2020. Values come from the NSRDB. Pardon my lack of concision - I'm new here.
"""

import pandas as pd
from rex import NSRDBX

#Specify a path to the NSRDB file, starting with 1998
nsrdb_file = '/nrel/nsrdb/v3/nsrdb_1998.h5'
nrel = (39.741931, -105.169891)
with NSRDBX(nsrdb_file, hsds=True) as f:
    nrel_dni_1998 = f.get_lat_lon_df('dni', nrel)
    nrel_dhi_1998 = f.get_lat_lon_df('dhi', nrel)
    nrel_ghi_1998 = f.get_lat_lon_df('ghi', nrel)
    nrel_temp_1998 = f.get_lat_lon_df('air_temperature', nrel)

#Add the values of nrel_dhi_minus_date, nrel_ghi_minus_date, and nrel_temp_minus_date to nrel_dni
nrel_dni_1998['dhi'] = nrel_dhi_1998
nrel_dni_1998['ghi'] = nrel_ghi_1998
nrel_dni_1998['temp'] = nrel_temp_1998

#Do the same for 1999
nsrdb_file = '/nrel/nsrdb/v3/nsrdb_1999.h5'
nrel = (39.741931, -105.169891)
with NSRDBX(nsrdb_file, hsds=True) as f:
    nrel_dni_1999 = f.get_lat_lon_df('dni', nrel)
    nrel_dhi_1999 = f.get_lat_lon_df('dhi', nrel)
    nrel_ghi_1999 = f.get_lat_lon_df('ghi', nrel)
    nrel_temp_1999 = f.get_lat_lon_df('air_temperature', nrel)

#Add the values of nrel_dhi_minus_date, nrel_ghi_minus_date, and nrel_temp_minus_date to nrel_dni
nrel_dni_1999['dhi'] = nrel_dhi_1999
nrel_dni_1999['ghi'] = nrel_ghi_1999
nrel_dni_1999['temp'] = nrel_temp_1999

#2000
nsrdb_file = '/nrel/nsrdb/v3/nsrdb_2000.h5'
nrel = (39.741931, -105.169891)
with NSRDBX(nsrdb_file, hsds=True) as f:
    nrel_dni_2000 = f.get_lat_lon_df('dni', nrel)
    nrel_dhi_2000 = f.get_lat_lon_df('dhi', nrel)
    nrel_ghi_2000 = f.get_lat_lon_df('ghi', nrel)
    nrel_temp_2000 = f.get_lat_lon_df('air_temperature', nrel)

#Add the values of nrel_dhi_minus_date, nrel_ghi_minus_date, and nrel_temp_minus_date to nrel_dni
nrel_dni_2000['dhi'] = nrel_dhi_2000
nrel_dni_2000['ghi'] = nrel_ghi_2000
nrel_dni_2000['temp'] = nrel_temp_2000

#2001
nsrdb_file = '/nrel/nsrdb/v3/nsrdb_2001.h5'
nrel = (39.741931, -105.169891)
with NSRDBX(nsrdb_file, hsds=True) as f:
    nrel_dni_2001 = f.get_lat_lon_df('dni', nrel)
    nrel_dhi_2001 = f.get_lat_lon_df('dhi', nrel)
    nrel_ghi_2001 = f.get_lat_lon_df('ghi', nrel)
    nrel_temp_2001 = f.get_lat_lon_df('air_temperature', nrel)

#Add the values of nrel_dhi_minus_date, nrel_ghi_minus_date, and nrel_temp_minus_date to nrel_dni
nrel_dni_2001['dhi'] = nrel_dhi_2001
nrel_dni_2001['ghi'] = nrel_ghi_2001
nrel_dni_2001['temp'] = nrel_temp_2001

#2002
nsrdb_file = '/nrel/nsrdb/v3/nsrdb_2002.h5'
nrel = (39.741931, -105.169891)
with NSRDBX(nsrdb_file, hsds=True) as f:
    nrel_dni_2002 = f.get_lat_lon_df('dni', nrel)
    nrel_dhi_2002 = f.get_lat_lon_df('dhi', nrel)
    nrel_ghi_2002 = f.get_lat_lon_df('ghi', nrel)
    nrel_temp_2002 = f.get_lat_lon_df('air_temperature', nrel)

#Add the values of nrel_dhi_minus_date, nrel_ghi_minus_date, and nrel_temp_minus_date to nrel_dni
nrel_dni_2002['dhi'] = nrel_dhi_2002
nrel_dni_2002['ghi'] = nrel_ghi_2002
nrel_dni_2002['temp'] = nrel_temp_2002

#2003
nsrdb_file = '/nrel/nsrdb/v3/nsrdb_2003.h5'
nrel = (39.741931, -105.169891)
with NSRDBX(nsrdb_file, hsds=True) as f:
    nrel_dni_2003 = f.get_lat_lon_df('dni', nrel)
    nrel_dhi_2003 = f.get_lat_lon_df('dhi', nrel)
    nrel_ghi_2003 = f.get_lat_lon_df('ghi', nrel)
    nrel_temp_2003 = f.get_lat_lon_df('air_temperature', nrel)

#Add the values of nrel_dhi_minus_date, nrel_ghi_minus_date, and nrel_temp_minus_date to nrel_dni
nrel_dni_2003['dhi'] = nrel_dhi_2003
nrel_dni_2003['ghi'] = nrel_ghi_2003
nrel_dni_2003['temp'] = nrel_temp_2003

#2004
nsrdb_file = '/nrel/nsrdb/v3/nsrdb_2004.h5'
nrel = (39.741931, -105.169891)
with NSRDBX(nsrdb_file, hsds=True) as f:
    nrel_dni_2004 = f.get_lat_lon_df('dni', nrel)
    nrel_dhi_2004 = f.get_lat_lon_df('dhi', nrel)
    nrel_ghi_2004 = f.get_lat_lon_df('ghi', nrel)
    nrel_temp_2004 = f.get_lat_lon_df('air_temperature', nrel)

#Add the values of nrel_dhi_minus_date, nrel_ghi_minus_date, and nrel_temp_minus_date to nrel_dni
nrel_dni_2004['dhi'] = nrel_dhi_2004
nrel_dni_2004['ghi'] = nrel_ghi_2004
nrel_dni_2004['temp'] = nrel_temp_2004

#2005
nsrdb_file = '/nrel/nsrdb/v3/nsrdb_2005.h5'
nrel = (39.741931, -105.169891)
with NSRDBX(nsrdb_file, hsds=True) as f:
    nrel_dni_2005 = f.get_lat_lon_df('dni', nrel)
    nrel_dhi_2005 = f.get_lat_lon_df('dhi', nrel)
    nrel_ghi_2005 = f.get_lat_lon_df('ghi', nrel)
    nrel_temp_2005 = f.get_lat_lon_df('air_temperature', nrel)

#Add the values of nrel_dhi_minus_date, nrel_ghi_minus_date, and nrel_temp_minus_date to nrel_dni
nrel_dni_2005['dhi'] = nrel_dhi_2005
nrel_dni_2005['ghi'] = nrel_ghi_2005
nrel_dni_2005['temp'] = nrel_temp_2005

#2006
nsrdb_file = '/nrel/nsrdb/v3/nsrdb_2006.h5'
nrel = (39.741931, -105.169891)
with NSRDBX(nsrdb_file, hsds=True) as f:
    nrel_dni_2006 = f.get_lat_lon_df('dni', nrel)
    nrel_dhi_2006 = f.get_lat_lon_df('dhi', nrel)
    nrel_ghi_2006 = f.get_lat_lon_df('ghi', nrel)
    nrel_temp_2006 = f.get_lat_lon_df('air_temperature', nrel)

#Add the values of nrel_dhi_minus_date, nrel_ghi_minus_date, and nrel_temp_minus_date to nrel_dni
nrel_dni_2006['dhi'] = nrel_dhi_2006
nrel_dni_2006['ghi'] = nrel_ghi_2006
nrel_dni_2006['temp'] = nrel_temp_2006

#2007
nsrdb_file = '/nrel/nsrdb/v3/nsrdb_2007.h5'
nrel = (39.741931, -105.169891)
with NSRDBX(nsrdb_file, hsds=True) as f:
    nrel_dni_2007 = f.get_lat_lon_df('dni', nrel)
    nrel_dhi_2007 = f.get_lat_lon_df('dhi', nrel)
    nrel_ghi_2007 = f.get_lat_lon_df('ghi', nrel)
    nrel_temp_2007 = f.get_lat_lon_df('air_temperature', nrel)

#Add the values of nrel_dhi_minus_date, nrel_ghi_minus_date, and nrel_temp_minus_date to nrel_dni
nrel_dni_2007['dhi'] = nrel_dhi_2007
nrel_dni_2007['ghi'] = nrel_ghi_2007
nrel_dni_2007['temp'] = nrel_temp_2007

#2008
nsrdb_file = '/nrel/nsrdb/v3/nsrdb_2008.h5'
nrel = (39.741931, -105.169891)
with NSRDBX(nsrdb_file, hsds=True) as f:
    nrel_dni_2008 = f.get_lat_lon_df('dni', nrel)
    nrel_dhi_2008 = f.get_lat_lon_df('dhi', nrel)
    nrel_ghi_2008 = f.get_lat_lon_df('ghi', nrel)
    nrel_temp_2008 = f.get_lat_lon_df('air_temperature', nrel)

#Add the values of nrel_dhi_minus_date, nrel_ghi_minus_date, and nrel_temp_minus_date to nrel_dni
nrel_dni_2008['dhi'] = nrel_dhi_2008
nrel_dni_2008['ghi'] = nrel_ghi_2008
nrel_dni_2008['temp'] = nrel_temp_2008

#2009
nsrdb_file = '/nrel/nsrdb/v3/nsrdb_2009.h5'
nrel = (39.741931, -105.169891)
with NSRDBX(nsrdb_file, hsds=True) as f:
    nrel_dni_2009 = f.get_lat_lon_df('dni', nrel)
    nrel_dhi_2009 = f.get_lat_lon_df('dhi', nrel)
    nrel_ghi_2009 = f.get_lat_lon_df('ghi', nrel)
    nrel_temp_2009 = f.get_lat_lon_df('air_temperature', nrel)

#Add the values of nrel_dhi_minus_date, nrel_ghi_minus_date, and nrel_temp_minus_date to nrel_dni
nrel_dni_2009['dhi'] = nrel_dhi_2009
nrel_dni_2009['ghi'] = nrel_ghi_2009
nrel_dni_2009['temp'] = nrel_temp_2009

#2010
nsrdb_file = '/nrel/nsrdb/v3/nsrdb_2010.h5'
nrel = (39.741931, -105.169891)
with NSRDBX(nsrdb_file, hsds=True) as f:
    nrel_dni_2010 = f.get_lat_lon_df('dni', nrel)
    nrel_dhi_2010 = f.get_lat_lon_df('dhi', nrel)
    nrel_ghi_2010 = f.get_lat_lon_df('ghi', nrel)
    nrel_temp_2010 = f.get_lat_lon_df('air_temperature', nrel)

#Add the values of nrel_dhi_minus_date, nrel_ghi_minus_date, and nrel_temp_minus_date to nrel_dni
nrel_dni_2010['dhi'] = nrel_dhi_2010
nrel_dni_2010['ghi'] = nrel_ghi_2010
nrel_dni_2010['temp'] = nrel_temp_2010

#2011
nsrdb_file = '/nrel/nsrdb/v3/nsrdb_2011.h5'
nrel = (39.741931, -105.169891)
with NSRDBX(nsrdb_file, hsds=True) as f:
    nrel_dni_2011 = f.get_lat_lon_df('dni', nrel)
    nrel_dhi_2011 = f.get_lat_lon_df('dhi', nrel)
    nrel_ghi_2011 = f.get_lat_lon_df('ghi', nrel)
    nrel_temp_2011 = f.get_lat_lon_df('air_temperature', nrel)

#Add the values of nrel_dhi_minus_date, nrel_ghi_minus_date, and nrel_temp_minus_date to nrel_dni
nrel_dni_2011['dhi'] = nrel_dhi_2011
nrel_dni_2011['ghi'] = nrel_ghi_2011
nrel_dni_2011['temp'] = nrel_temp_2011

#2012
nsrdb_file = '/nrel/nsrdb/v3/nsrdb_2012.h5'
nrel = (39.741931, -105.169891)
with NSRDBX(nsrdb_file, hsds=True) as f:
    nrel_dni_2012 = f.get_lat_lon_df('dni', nrel)
    nrel_dhi_2012 = f.get_lat_lon_df('dhi', nrel)
    nrel_ghi_2012 = f.get_lat_lon_df('ghi', nrel)
    nrel_temp_2012 = f.get_lat_lon_df('air_temperature', nrel)

#Add the values of nrel_dhi_minus_date, nrel_ghi_minus_date, and nrel_temp_minus_date to nrel_dni
nrel_dni_2012['dhi'] = nrel_dhi_2012
nrel_dni_2012['ghi'] = nrel_ghi_2012
nrel_dni_2012['temp'] = nrel_temp_2012

#2013
nsrdb_file = '/nrel/nsrdb/v3/nsrdb_2013.h5'
nrel = (39.741931, -105.169891)
with NSRDBX(nsrdb_file, hsds=True) as f:
    nrel_dni_2013 = f.get_lat_lon_df('dni', nrel)
    nrel_dhi_2013 = f.get_lat_lon_df('dhi', nrel)
    nrel_ghi_2013 = f.get_lat_lon_df('ghi', nrel)
    nrel_temp_2013 = f.get_lat_lon_df('air_temperature', nrel)

#Add the values of nrel_dhi_minus_date, nrel_ghi_minus_date, and nrel_temp_minus_date to nrel_dni
nrel_dni_2013['dhi'] = nrel_dhi_2013
nrel_dni_2013['ghi'] = nrel_ghi_2013
nrel_dni_2013['temp'] = nrel_temp_2013

#2014
nsrdb_file = '/nrel/nsrdb/v3/nsrdb_2014.h5'
nrel = (39.741931, -105.169891)
with NSRDBX(nsrdb_file, hsds=True) as f:
    nrel_dni_2014 = f.get_lat_lon_df('dni', nrel)
    nrel_dhi_2014 = f.get_lat_lon_df('dhi', nrel)
    nrel_ghi_2014 = f.get_lat_lon_df('ghi', nrel)
    nrel_temp_2014 = f.get_lat_lon_df('air_temperature', nrel)

#Add the values of nrel_dhi_minus_date, nrel_ghi_minus_date, and nrel_temp_minus_date to nrel_dni
nrel_dni_2014['dhi'] = nrel_dhi_2014
nrel_dni_2014['ghi'] = nrel_ghi_2014
nrel_dni_2014['temp'] = nrel_temp_2014

#2015
nsrdb_file = '/nrel/nsrdb/v3/nsrdb_2015.h5'
nrel = (39.741931, -105.169891)
with NSRDBX(nsrdb_file, hsds=True) as f:
    nrel_dni_2015 = f.get_lat_lon_df('dni', nrel)
    nrel_dhi_2015 = f.get_lat_lon_df('dhi', nrel)
    nrel_ghi_2015 = f.get_lat_lon_df('ghi', nrel)
    nrel_temp_2015 = f.get_lat_lon_df('air_temperature', nrel)

#Add the values of nrel_dhi_minus_date, nrel_ghi_minus_date, and nrel_temp_minus_date to nrel_dni
nrel_dni_2015['dhi'] = nrel_dhi_2015
nrel_dni_2015['ghi'] = nrel_ghi_2015
nrel_dni_2015['temp'] = nrel_temp_2015

#2016
nsrdb_file = '/nrel/nsrdb/v3/nsrdb_2016.h5'
nrel = (39.741931, -105.169891)
with NSRDBX(nsrdb_file, hsds=True) as f:
    nrel_dni_2016 = f.get_lat_lon_df('dni', nrel)
    nrel_dhi_2016 = f.get_lat_lon_df('dhi', nrel)
    nrel_ghi_2016 = f.get_lat_lon_df('ghi', nrel)
    nrel_temp_2016 = f.get_lat_lon_df('air_temperature', nrel)

#Add the values of nrel_dhi_minus_date, nrel_ghi_minus_date, and nrel_temp_minus_date to nrel_dni
nrel_dni_2016['dhi'] = nrel_dhi_2016
nrel_dni_2016['ghi'] = nrel_ghi_2016
nrel_dni_2016['temp'] = nrel_temp_2016

#2017
nsrdb_file = '/nrel/nsrdb/v3/nsrdb_2017.h5'
nrel = (39.741931, -105.169891)
with NSRDBX(nsrdb_file, hsds=True) as f:
    nrel_dni_2017 = f.get_lat_lon_df('dni', nrel)
    nrel_dhi_2017 = f.get_lat_lon_df('dhi', nrel)
    nrel_ghi_2017 = f.get_lat_lon_df('ghi', nrel)
    nrel_temp_2017 = f.get_lat_lon_df('air_temperature', nrel)

#Add the values of nrel_dhi_minus_date, nrel_ghi_minus_date, and nrel_temp_minus_date to nrel_dni
nrel_dni_2017['dhi'] = nrel_dhi_2017
nrel_dni_2017['ghi'] = nrel_ghi_2017
nrel_dni_2017['temp'] = nrel_temp_2017

#2018
nsrdb_file = '/nrel/nsrdb/v3/nsrdb_2018.h5'
nrel = (39.741931, -105.169891)
with NSRDBX(nsrdb_file, hsds=True) as f:
    nrel_dni_2018 = f.get_lat_lon_df('dni', nrel)
    nrel_dhi_2018 = f.get_lat_lon_df('dhi', nrel)
    nrel_ghi_2018 = f.get_lat_lon_df('ghi', nrel)
    nrel_temp_2018 = f.get_lat_lon_df('air_temperature', nrel)

#Add the values of nrel_dhi_minus_date, nrel_ghi_minus_date, and nrel_temp_minus_date to nrel_dni
nrel_dni_2018['dhi'] = nrel_dhi_2018
nrel_dni_2018['ghi'] = nrel_ghi_2018
nrel_dni_2018['temp'] = nrel_temp_2018

#2019
nsrdb_file = '/nrel/nsrdb/v3/nsrdb_2019.h5'
nrel = (39.741931, -105.169891)
with NSRDBX(nsrdb_file, hsds=True) as f:
    nrel_dni_2019 = f.get_lat_lon_df('dni', nrel)
    nrel_dhi_2019 = f.get_lat_lon_df('dhi', nrel)
    nrel_ghi_2019 = f.get_lat_lon_df('ghi', nrel)
    nrel_temp_2019 = f.get_lat_lon_df('air_temperature', nrel)

#Add the values of nrel_dhi_minus_date, nrel_ghi_minus_date, and nrel_temp_minus_date to nrel_dni
nrel_dni_2019['dhi'] = nrel_dhi_2019
nrel_dni_2019['ghi'] = nrel_ghi_2019
nrel_dni_2019['temp'] = nrel_temp_2019

#2020
nsrdb_file = '/nrel/nsrdb/v3/nsrdb_2020.h5'
nrel = (39.741931, -105.169891)
with NSRDBX(nsrdb_file, hsds=True) as f:
    nrel_dni_2020 = f.get_lat_lon_df('dni', nrel)
    nrel_dhi_2020 = f.get_lat_lon_df('dhi', nrel)
    nrel_ghi_2020 = f.get_lat_lon_df('ghi', nrel)
    nrel_temp_2020 = f.get_lat_lon_df('air_temperature', nrel)

#Add the values of nrel_dhi_minus_date, nrel_ghi_minus_date, and nrel_temp_minus_date to nrel_dni
nrel_dni_2020['dhi'] = nrel_dhi_2020
nrel_dni_2020['ghi'] = nrel_ghi_2020
nrel_dni_2020['temp'] = nrel_temp_2020


#append all the nrel_dni_year values to nrel_dni_1998 and save to a csv
nrel_dni_1998 = nrel_dni_1998.append(nrel_dni_1999)
nrel_dni_1998 = nrel_dni_1998.append(nrel_dni_2000)
nrel_dni_1998 = nrel_dni_1998.append(nrel_dni_2001)
nrel_dni_1998 = nrel_dni_1998.append(nrel_dni_2002)
nrel_dni_1998 = nrel_dni_1998.append(nrel_dni_2003)
nrel_dni_1998 = nrel_dni_1998.append(nrel_dni_2004)
nrel_dni_1998 = nrel_dni_1998.append(nrel_dni_2005)
nrel_dni_1998 = nrel_dni_1998.append(nrel_dni_2006)
nrel_dni_1998 = nrel_dni_1998.append(nrel_dni_2007)
nrel_dni_1998 = nrel_dni_1998.append(nrel_dni_2008)
nrel_dni_1998 = nrel_dni_1998.append(nrel_dni_2009)
nrel_dni_1998 = nrel_dni_1998.append(nrel_dni_2010)
nrel_dni_1998 = nrel_dni_1998.append(nrel_dni_2011)
nrel_dni_1998 = nrel_dni_1998.append(nrel_dni_2012)
nrel_dni_1998 = nrel_dni_1998.append(nrel_dni_2013)
nrel_dni_1998 = nrel_dni_1998.append(nrel_dni_2014)
nrel_dni_1998 = nrel_dni_1998.append(nrel_dni_2015)
nrel_dni_1998 = nrel_dni_1998.append(nrel_dni_2016)
nrel_dni_1998 = nrel_dni_1998.append(nrel_dni_2017)
nrel_dni_1998 = nrel_dni_1998.append(nrel_dni_2018)
nrel_dni_1998 = nrel_dni_1998.append(nrel_dni_2019)
nrel_dni_1998 = nrel_dni_1998.append(nrel_dni_2020)

nrel_dni_1998.to_csv(r'C:\Users\Dominic\Desktop\Location_1_DNI_DHI_GHI_Temp.csv')
