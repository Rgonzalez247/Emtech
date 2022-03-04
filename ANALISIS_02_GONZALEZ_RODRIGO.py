#!/usr/bin/env python
# coding: utf-8

# In[1]:


# In[2]:

#Importar librerías
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np


# In[2]:


# In[3]:


#Importar datos
df = pd.read_csv('synergy_logistics_database.csv')
df


# In[3]:


# # Opción 1

# ## Importaciones

# In[4]:


dfi= df[df.direction == "Imports"] #Filtrar Importación


# In[4]:


# In[5]:


#Código para agrupar datos en un DataFrame el cual puede ser manipulable
rutas = dfi[['origin','destination']].value_counts() #Selecciono columnas a querer utilizar y contar las ocurrencias
rutas = pd.DataFrame(rutas) #Crear resultado anteriror en un DataFrame
rutas = rutas.reset_index() #Asignar un índice de inicio predeterminado, en lugar de utilizar una columna de datos como índice
rutas.columns = ['origin','destination','Count'] #Nombrar nuevas columnas
rutas.head(10) #Mostrar solo los primeros 10 resultados


# In[5]:


# In[7]:


# Filtrar sobre la base de datos original tomando como base la base de datos de rutas para poder sumar el valor total de los
#productos e identificar que ruta tiene mayor valor.
r1 = dfi[(dfi.origin == 'Singapore') & (dfi.destination == 'Thailand')]
print('r1:')
print(r1.total_value.sum())
r2 = dfi[(dfi.origin == 'Germany') & (dfi.destination == 'China')]
print('r2:')
print(r2.total_value.sum())
r3 = dfi[(dfi.origin == 'China') & (dfi.destination == 'Japan')]
print('r3:')
print(r3.total_value.sum())
r4 = dfi[(dfi.origin == 'Japan') & (dfi.destination == 'Mexico')]
print('r4:')
print(r4.total_value.sum())
r5 = dfi[(dfi.origin == 'China') & (dfi.destination == 'Thailand')]
print('r5:')
print(r5.total_value.sum())
r6 = dfi[(dfi.origin == 'Malaysia') & (dfi.destination == 'Thailand')]
print('r6:')
print(r6.total_value.sum())
r7 = dfi[(dfi.origin == 'Spain') & (dfi.destination == 'Germany')]
print('r7:')
print(r7.total_value.sum())
r8 = dfi[(dfi.origin == 'Mexico') & (dfi.destination == 'USA')]
print('r8:')
print(r8.total_value.sum())
r9 = dfi[(dfi.origin == 'China') & (dfi.destination == 'United Arab Emirates')]
print('r9:')
print(r9.total_value.sum())
r10 = dfi[(dfi.origin == 'Brazil') & (dfi.destination == 'China')]
print('r10:')
print(r10.total_value.sum())
print("")
print("Valor Total:")
vr = r1.total_value.sum()+r2.total_value.sum()+r3.total_value.sum()+r4.total_value.sum()+r5.total_value.sum()+r6.total_value.sum()+r7.total_value.sum()+r8.total_value.sum()+r9.total_value.sum()+r10.total_value.sum()
print(vr) #sumatoria total para comparar con las otras opciones


# In[6]:


# In[8]:


a = rutas.head(10)
print("Cantidad de uso de rutas del Top 10 rutas:")
print(a.Count.sum())


# In[7]:


# ## Exportación

# In[10]:


dfe= df[df.direction == "Exports"] #Filtrar Exportación


# In[8]:


# In[11]:


#Código para agrupar datos en un DataFrame el cual puede ser manipulable
rutas = dfe[['origin','destination']].value_counts() #Selecciono columnas a querer utilizar y contar las ocurrencias
rutas = pd.DataFrame(rutas) #Crear resultado anteriror en un DataFrame
rutas = rutas.reset_index() #Asignar un índice de inicio predeterminado, en lugar de utilizar una columna de datos como índice
rutas.columns = ['origin','destination','Count'] #Nombrar nuevas columnas
rutas.head(10) #Mostrar solo los primeros 10 resultados


# In[9]:


# In[12]:


r1 = dfe[(dfe.origin == 'South Korea') & (dfe.destination == 'Vietnam')]
print('r1:')
print(r1.total_value.sum())
r2 = dfe[(dfe.origin == 'Netherlands') & (dfe.destination == 'Belgium')]
print('r2:')
print(r2.total_value.sum())
r3 = dfe[(dfe.origin == 'USA') & (dfe.destination == 'Netherlands')]
print('r3:')
print(r3.total_value.sum())
r4 = dfe[(dfe.origin == 'China') & (dfe.destination == 'Mexico')]
print('r4:')
print(r4.total_value.sum())
r5 = dfe[(dfe.origin == 'Japan') & (dfe.destination == 'Brazil')]
print('r5:')
print(r5.total_value.sum())
r6 = dfe[(dfe.origin == 'Germany') & (dfe.destination == 'France')]
print('r6:')
print(r6.total_value.sum())
r7 = dfe[(dfe.origin == 'South Korea') & (dfe.destination == 'Japan')]
print('r7:')
print(r7.total_value.sum())
r8 = dfe[(dfe.origin == 'Australia') & (dfe.destination == 'Singapore')]
print('r8:')
print(r8.total_value.sum())
r9 = dfe[(dfe.origin == 'Canada') & (dfe.destination == 'Mexico')]
print('r9:')
print(r9.total_value.sum())
r10 = dfe[(dfe.origin == 'China') & (dfe.destination == 'Spain')]
print('r10:')
print(r10.total_value.sum())
print("")
print("Valor Total:")
vr = r1.total_value.sum()+r2.total_value.sum()+r3.total_value.sum()+r4.total_value.sum()+r5.total_value.sum()+r6.total_value.sum()+r7.total_value.sum()+r8.total_value.sum()+r9.total_value.sum()+r10.total_value.sum()
print(vr) #sumatoria total para comparar con las otras opciones


# In[10]:


# In[13]:


a = rutas.head(10)
print("Cantidad de uso de rutas del Top 10 rutas:")
print(a.Count.sum())


# In[11]:


# # Opcion 2

# ## Importación

# In[19]:


dfi2= df[df.direction == "Imports"] #Filtrar Importación


# In[12]:


# In[20]:


# Mismos códigos que los de la opción 1 pero ahora tomando en cuenta el medio de transporte nada más
transporte = dfi2['transport_mode'].value_counts()
transporte = pd.DataFrame(transporte)
transporte = transporte.reset_index()
transporte.columns = ['transport_mode','Count']
transporte.head(10)


# In[13]:


# In[21]:


t1 = dfi2[df.transport_mode == 'Sea']
print('Sea:')
print(t1.total_value.sum())
t2 = dfi2[df.transport_mode == 'Rail']
print('Rail:')
print(t2.total_value.sum())
t4 = dfi2[df.transport_mode == 'Road']
print('Road:')
print(t4.total_value.sum())
t3 = dfi2[df.transport_mode == 'Air']
print('Air:')
print(t3.total_value.sum())


# In[14]:


# In[23]:


print('Valor de los 3 medios de transporte más importantes:')
vt = t1.total_value.sum()+t2.total_value.sum()+t3.total_value.sum()
print(vt)


# In[15]:


# ## Exportación

# In[15]:


dfe2= df[df.direction == "Exports"] #Filtrar Importación


# In[16]:


# In[16]:


# Mismos códigos que los de la opción 1 pero ahora tomando en cuenta el medio de transporte nada más
transporte = dfe2['transport_mode'].value_counts()
transporte = pd.DataFrame(transporte)
transporte = transporte.reset_index()
transporte.columns = ['transport_mode','Count']
transporte.head(10)


# In[17]:


# In[17]:


t1 = dfe2[df.transport_mode == 'Sea']
print('Sea:')
print(t1.total_value.sum())
t2 = dfe2[df.transport_mode == 'Rail']
print('Rail:')
print(t2.total_value.sum())
t4 = dfe2[df.transport_mode == 'Road']
print('Road:')
print(t4.total_value.sum())
t3 = dfe2[df.transport_mode == 'Air']
print('Air:')
print(t3.total_value.sum())


# In[18]:


# In[18]:


print('Valor de los 3 medios de transporte más importantes:')
vt = t1.total_value.sum()+t2.total_value.sum()+t3.total_value.sum()
print(vt)


# In[19]:


# # Opción 3

# In[3]:


# Mismos códigos que los de la opción 1 y 2 pero ahora tomando en cuenta el origen nada más
valor = df.groupby(by = ['origin']).total_value.sum()
valor = pd.DataFrame(valor)
valor = valor.reset_index()
valor.columns = ['origin','Sum']
valor.sort_values(by='Sum',ascending=False)


# In[20]:


# In[4]:


#Sobre los resultados de la tabla anterior, dividir las cantidades de valor de productos entre el total para obtener porcentaje
#de representación
percentage = valor.Sum/valor.Sum.sum() #Obtener el porcentaje de cada fila entre el total de la suma de valores
percentage.sort_values(ascending = False)


# In[21]:


# In[6]:


sor = percentage.sort_values(ascending = False)
sor


# In[22]:


# In[12]:


sor2 = sor.head(9)
sum(sor2)


# In[23]:


# In[13]:


#Ordenar tabla en modo descendiente
val = valor.sort_values(by='Sum',ascending=False)
val


# In[24]:


# In[18]:


#Filtrar los 9 valores más altos, los cuales representan alrededor del 80% del valor total
val = val.head(9)
val


# In[25]:


# In[20]:


val.Sum.sum()

