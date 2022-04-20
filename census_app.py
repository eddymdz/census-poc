import time
import os                                                                                                                                                                        
from os.path import join, dirname                                                                                                                                                
from dotenv import load_dotenv
from census import Census
from us import states


dotenv_path = join(dirname(__file__), '.env')                                                                                                                                    
load_dotenv(dotenv_path)

c = Census(os.getenv('CENSUS_KEY'))

# States 
# https://www.nrcs.usda.gov/wps/portal/nrcs/detail/?cid=nrcs143_013696
print(states.lookup('34').abbr)

# Total Population
# Decennial Census SF1 (2010, 2000)
# https://www.census.gov/data/developers/data-sets/decennial-census.html
# https://api.census.gov/data/2010/dec/sf1/variables.html
# https://api.census.gov/data/2010/dec/sf1/geography.html
sf1_variables = ['P001001', 'P002002', 'P002003', 'P002004', 'P002005', 'P002006']
for sf1_variable in sf1_variables:
    result = c.sf1.get(sf1_variable, {'for': 'state:34'})
    print(result)
    time.sleep(5)

# HISPANIC OR LATINO BY SPECIFIC ORIGIN	
result = c.sf1.get('PCT011025', {'for': 'state:34'})
print(result)


# How to get state based on FIPS code
#print(states.lookup('21').abbr)

# print(c.acs1.tables())
