#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.offline import iplot, plot
from plotly.subplots import make_subplots
import seaborn as sns


# In[2]:


#Importar los datos de mi computador
data = pd.read_csv('C:/Users/juang/OneDrive/Escritorio/datasets/netflix1.csv')
data.head(5)


# In[3]:


#información sobre las columnas en general
data.info()


# In[4]:


#Cantidad de valores duplicados en columnas
data.duplicated().value_counts()


# In[5]:


#Descripción estadistica de todos los datos
data.describe(include='all')


# In[6]:


#Tamaño del dataset
data.shape


# In[7]:


#Verificar si existen datos duplicados en la columna show_id
data["show_id"].duplicated().sum()


# In[8]:


#Cantidad de datos según el tipo
conteos_tipos = data['type'].value_counts().reset_index()


conteos_tipos.columns = ['Tipo', 'Conteo']


conteos_tipos.head()


# In[9]:


#Cantidad de datos repetidos
data.isnull().sum()


# In[10]:


data['country'].value_counts()


# In[11]:


#Años en los que se hicieron mayor cantidad de películas
film_making = data[data['type'] == 'Movie']['release_year'].value_counts().reset_index()

film_making.columns = ['Country', 'Quantity of Movies']

film_making.head(10)


# In[12]:


#Años en los que se hicieron menor cantidad de películas
film_making_low = film_making.sort_values(by='Quantity of Movies', ascending=True)

film_making_low.head(10)


# In[13]:


#Años en los que se hicieron mayor cantidad de producciones de televisión
tv_production = data[data['type'] == 'TV Show']['release_year'].value_counts().reset_index()

tv_production.columns = ['Country', 'Quantity of TV Production']

tv_production.head(10)


# In[14]:


#Años en los que se hicieron menor cantidad de producciones de televisión
tv_production_low = tv_production.sort_values(by='Quantity of TV Production', ascending=True)

tv_production_low.head(10)


# In[15]:


#Pelicula o TV Shows más antigua en Netflix 
old_serie = data['release_year'].min()
data[data['release_year'] == old_serie]


# In[16]:


#Pelicula o TV Shows más nueva en Netflix 
new_serie = data['release_year'].max()
data[data['release_year'] == new_serie]


# In[17]:


#Pelicula o TV Shows más antigua agregada
old_serie_added = data['date_added'].min()
data[data['date_added'] == old_serie_added]


# In[18]:


#Pelicula o TV Shows más nueva agregada
new_serie_added = data['date_added'].max()
data[data['date_added'] == new_serie_added]


# In[19]:


country = data.groupby('country')['type'].value_counts().rename('count').reset_index()
country = country.sort_values(by='count', ascending=False)
country


# In[20]:


#Paises con más peliculas
top_10_country_movies = country[(country['country'] != 'Not Given') & (country['type'] == 'Movie')].head(10)
top_10_country_movies


# In[21]:


#Paises con más TV Shows
top_10_country_tv = country[(country['country'] != 'Not Given') & (country['type'] == 'TV Show')].head(10)
top_10_country_tv


# In[22]:


#Director con más peliculas o TV Shows
director = data[data['director'] != 'Not Given'][['type','director']].value_counts().rename('count').reset_index()
director.sort_values(by='count', ascending=False)


# In[23]:


#Director con más peliculas
top_10_director_movies = director [director ['type'] == 'Movie'].head(10)
top_10_director_movies


# In[24]:


#Director con más TV Shows
top_10_director_tv = director [director ['type'] == 'TV Show'].head(10)
top_10_director_tv


# In[25]:


#Cantidad de datos únicos por categoría
unique_directors = data['director'].nunique()
unique_release_years = data['release_year'].nunique()
unique_types = data['type'].nunique()
unique_duration= data['duration'].nunique()
unique_country = data['country'].nunique()
unique_listedin = data['listed_in'].nunique()
result_table = pd.DataFrame({
    'Director': [unique_directors],
    'Release Year': [unique_release_years],
    'Type': [unique_types],
    'Duration' : [unique_duration],
    'Country' :[unique_country],
    'Genre': [unique_listedin]
}, index=['Amount of data'])


result_table.head()


# In[26]:


#Tipo de rating por tipo
rating = data.groupby(['rating', 'type']).size().reset_index(name='count')
rating = rating.sort_values(by='count', ascending=False)
rating


# In[27]:


#Mayor tipo de rating en peliculas
top_10_rating_movie = rating [rating ['type'] == 'Movie'].head(10)
top_10_rating_movie


# In[28]:


#Mayor tipo de rating en TV Shows
top_10_rating_tv = rating [rating ['type'] == 'TV Show'].head(10)
top_10_rating_tv


# In[29]:


#Mayor cantidad de generos
genre = data.groupby(['listed_in', 'type']).size().reset_index(name='count')
genre = genre.sort_values(by='count', ascending=False)
genre


# In[30]:


#Mayor cantidad de generos en películas
top_10_genre_movie = genre [genre ['type'] == 'Movie'].head(10)
top_10_genre_movie


# In[31]:


#Mayor cantidad de generos en TV Shows
top_10_genre_tv = genre [genre ['type'] == 'TV Show'].head(10)
top_10_genre_tv


# In[32]:


#Películas por titulo con mayor duración
data['duration_extracted'] = data['duration'].str.extract('(\d+)').astype(float)
result_table = data[data ['type'] == 'Movie'].sort_values(by='duration_extracted', ascending=False)
result_table_ = result_table[['type', 'title', 'duration']].head(10)
result_table_


# In[33]:


#TV Show por titulo con mayor duración
data['duration_extracted'] = data['duration'].str.extract('(\d+)').astype(float)
result_table = data[data ['type'] == 'TV Show'].sort_values(by='duration_extracted', ascending=False)
result_table[['type', 'title', 'duration']].head(10)


# In[34]:


#Generos más realizados por cada país
genre_country_count = data.groupby(['country', 'listed_in']).size().reset_index(name='count')
idx = genre_country_count.groupby(['country'])['count'].idxmax()
most_watched_genre_by_country = genre_country_count.loc[idx].sort_values(by='count', ascending=False).head(10)
most_watched_genre_by_country


# In[35]:


data.type.value_counts().plot(kind="pie",autopct="%0.0f%%",explode=[0,0.1],shadow=True,colors=['#8B0000', '#CD5C5C']);


# In[36]:


grouped_data = data.groupby('type').size().reset_index(name='count')


tv_shows = grouped_data[grouped_data['type'] == 'TV Show']
movies = grouped_data[grouped_data['type'] == 'Movie']


plt.figure(figsize=(8,6))
plt.bar(tv_shows['type'],tv_shows['count'],label='TV Show',color='#8B0000',alpha=0.7,edgecolor='black')
plt.bar(movies['type'],movies['count'],label='Movie',color='#CD5C5C',alpha=0.7,edgecolor='black')


plt.xlabel('Type')
plt.ylabel('Count')
plt.title('Counts of TV Shows and Movies')
plt.legend()


for i,count in enumerate(tv_shows['count']):
    plt.text(i,count,str(count),ha='center',va='bottom',fontsize=12,color='black')
    
for i,count in enumerate(movies['count']):
    plt.text(1+i,count,str(count),ha='center',va='bottom',fontsize=12,color='black') 


# In[37]:


released_year = data.release_year.value_counts()   
fig = px.area(released_year, x = released_year.index, y = released_year)
fig.update_xaxes(title_text='Year of release')
fig.update_yaxes(title_text='Quantity')

iplot(fig)


# In[38]:


sns.barplot(x=top_10_country_movies.reset_index()['country'], y=top_10_country_movies.reset_index()['count'])

# Configuración adicional del gráfico
plt.title('Movies by Country', fontsize=20, fontweight='bold')
plt.xlabel('Country', fontsize=16, fontweight='bold')
plt.ylabel('Quantity of Movies', fontsize=16, fontweight='bold')
sns.set(rc={'figure.figsize': (20, 10)})


plt.xticks(rotation=360, fontsize=16)  
plt.yticks(rotation=360, fontsize=16) 
plt.show()


# In[39]:


sns.barplot(x=top_10_country_tv.reset_index()['country'], y=top_10_country_tv.reset_index()['count'])

# Configuración adicional del gráfico
plt.title('TV Shows by Country', fontsize=20, fontweight='bold')
plt.xlabel('Country', fontsize=16, fontweight='bold')
plt.ylabel('Quantity of TV Shows', fontsize=16, fontweight='bold')
sns.set(rc={'figure.figsize': (20, 10)})


plt.xticks(rotation=360, fontsize=16)  
plt.yticks(rotation=360, fontsize=16) 
plt.show()


# In[40]:


movies = data.loc[data["type"] == "Movie", "rating"].value_counts()
tv_show = data.loc[data["type"] == "TV Show", "rating"].value_counts()


# In[41]:


movies_bar = go.Bar(x = movies.index, y = movies, name="Movie", marker=dict(color='#8B0000'))
tv_bar = go.Bar(x = tv_show.index, y = tv_show, name="Tv show", marker=dict(color='#CD5C5C'))


# In[42]:


fig = make_subplots(rows=1, cols=2, shared_yaxes=True)
fig.add_trace(movies_bar, row=1, col=1)
fig.add_trace(tv_bar, row=1, col=2)
fig.update_layout(height=500, width=900, title_text="Raiting by type of Show", legend_title_text = 'Type')
fig.update_xaxes(tickangle=90)
iplot(fig)


# In[43]:


directors = data["director"].value_counts()[1:6]
fig = px.bar(directors, 
       y =directors.index,
       x = directors,
       color=directors.index,
       text_auto=True,
       labels={"director": "Directory", "x": "Number of Movies & TV Shows"},
       orientation= "h",
      )

# Custom Format of numbers
fig.update_traces(
    textposition = "inside",
    outsidetextfont = {
        "family": "consolas",
         "size": 15,
    }
)
fig.update_yaxes(title_text="Directores")
fig.update_layout(showlegend=True,height=550, width=800, title_text="Top 5 Directors",legend_title_text="Directors")
iplot(fig)


# In[44]:


genre = data["listed_in"].value_counts()[1:6]
fig = px.bar(genre, 
       y =genre.index,
       x = genre,
       color=genre.index,
       text_auto=True,
       labels={"listed_in": "Directory", "x": "Number of Movies & TV Shows"},
       orientation= "h",
      )

# Custom Format of numbers
fig.update_traces(
    textposition = "outside",
    outsidetextfont = {
        "family": "consolas",
         "size": 15,
    }
)
fig.update_yaxes(title_text="Quantity")
fig.update_layout(showlegend=False,height=550, width=800, title_text="Top 5 Genre")
iplot(fig)

