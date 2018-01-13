
# coding: utf-8

# M001183
# C001047
# M001180
# M001195
# J000297

# In[ ]:

import requests
import json
import pandas as pd


# ## set api header

# In[ ]:

headers = {
    'X-API-Key': 'qriXJypLHd8f9E5erjyak6EXamUwUa80sbVkf5Vy',
}


# In[ ]:

WVmembers = ['M001183', 'C001047', 'M001180', 'M001195', 'J000297']


# In[ ]:

def crunchdata(memberid):
    intro_bills = requests.get('https://api.propublica.org/congress/v1/members/' + memberid +'/bills/introduced.json', headers=headers)
    bill_list = json.loads(intro_bills.text)["results"]
    print(bill_list)



# In[ ]:

# crunchdata('M001183')


# In[ ]:

for name in WVmembers:
    crunchdata(name)


# In[ ]:
