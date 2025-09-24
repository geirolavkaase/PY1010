#!/usr/bin/env python
# coding: utf-8

# <h1>Årlige kostnader for EL-bil vs bensinbil</h1>

# Geir Olav Kaase, 23.09.25

# Dette skriptet beregner de årlige kostnader for bruk av en typisk elbil og en typisk bensinbil 
# under følgende antakelser som gitt i oppgave teksten: 

# In[32]:


print("Under følgende antakelser beregnes den årlige kostnaden for EL-bil og bensinbil:")


# <h3>Felles antakelser:</h3>

# In[33]:


km = 10000    # [km] årlig kjørt distanse 
print("Årlig kjørelengde:", km, "[km]")
f_av = 8.38  # [kr/dag] trafikkforsikringsavgift 
print("Trafikkforsikringsavgift:", f_av, "[kr/dag]")


# <h3>Antakelser for EL-bil:</h3>

# In[34]:


f_el = 5000  # [kr/år] forsikringskostnad per år
print("Bilforsikring ELbil:", f_el, "[kr/år]")
wltp = 0.2   # [kWh/km] strømforbruk per km
print("Strømforbruk ELbil:", wltp, "[kWh/km]")
el_p = 2     # [kr/kWh] strømpris 
print("Strømpris:", el_p, "[kr/kWh]")
bom_el = 0.1 # [kr/km] kostnad for bompasseringer 
print("Bomavgift Elbil:", bom_el, "[kr/km]")


# <h3>Antakelser for bensinbil:</h3>

# In[35]:


f_b = 7500  # [kr/år] forsikringskostnad per år
print("Bilforsikring bensinbil:", f_b, "[kr/år]")
b_km = 1    # [kr/km] drivstoffkostnad per km
print("Drivstoffkostnad:", b_km, "[kr/km]")
bom_b = 0.3 # [kr/km] kostnad for bompasseringer
print("Bomavgift bensinbil:", bom_b, "[kr/km]")


# <h3>Beregning av årlig kostnad for ELbil:</h3>

# In[36]:


EL_ko = f_el + (el_p*wltp + bom_el)*km + f_av*365 # [kr/år]
print("Årlig kostnad for ELbil:", EL_ko, "[kr/år]")


# <h3>Beregning av årlig kostnad for bensinbil:</h3>

# In[37]:


BEN_ko = f_b + (b_km + bom_b)*km + f_av*365 # [kr/år]
print("Årlig kostnad for bensinbil:", BEN_ko, "[kr/år]")


# <h3>Differanse i årlige kostnader:</h3>
# <h4>(uttrykt som årlig tilleggskostnad for bensinbil)</h4>

# In[38]:


Diff = BEN_ko - EL_ko # [kr/år]
print("Årlig tilleggskostnad for bensinbil:", Diff, "[kr/år]")

