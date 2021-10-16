# CSE 5520 Fall 2021

# Term Project Data Set Declaration

Due 11:59 Thur Oct 14th, 2021 

Name: Lynn Pepin ('Tristan Pepin')

Team Partner: none

Data Choices:

I have chosen the [MusicNet dataset](https://www.kaggle.com/imsparsh/musicnet-dataset)

## Describe the nature of data you tentatively decided to use:


The [MusicNet dataset](https://www.kaggle.com/imsparsh/musicnet-dataset) is a 23GB dataset of classical music that can be downloaded from Kaggle, containing labels for instrument, composer, note-onset times, and musical notes. The music is public domain and has an estimated ~4% error rate on the manual labels.

## Describe the sources of your data

Downloaded from Kaggle.

## Describe types of analyses you may want to perform

 - Mapping music by similarity (e.g. UMAP or some other algorithm?) and letting people explore a "graph" or spectrum of related songs
 - Exploration of music across different "properties" (e.g. axes from PCA)
 - Generation of music (e.g. by exploring the latent space of an auto-encoder.)
 
## Describe types of visualizations you may want to incorporate into Dash

Primarily, graph-based visualization interests me: Mapping this dataset to a spatial visualization. I also have ideas for doing this in up to 5 spatial dimensions, but am unsure how to implement that in Python.
