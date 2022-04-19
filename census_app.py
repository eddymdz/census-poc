from census import Census
from us import states

c = Census("key")

# States 
# https://www.nrcs.usda.gov/wps/portal/nrcs/detail/?cid=nrcs143_013696

# Age
# Decennial Census SF1 (2010, 2000)
# https://www.census.gov/data/developers/data-sets/decennial-census.html
# https://api.census.gov/data/2010/dec/sf1/variables.html
# https://api.census.gov/data/2010/dec/sf1/geography.html
male_35_39_years = c.sf1.get('P002003', {'for': 'state:34'})
print(states.lookup('34').abbr)
print(male_35_39_years)


# Gender
# https://api.census.gov/data/2016/acs/acs5/variables.html
#male_5to9_years = c.acs5.get('B01001_004E', {'for': 'state:34'})
#print(male_5to9_years)                                                                                                                                                            



# How to get state based on FIPS code
#print(states.lookup('21').abbr)

# print(c.acs1.tables())
