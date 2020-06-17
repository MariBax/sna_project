# Anglicisms
HSE Magolego SNA project

### Data files
All data (initial and generated) can be found here 

https://drive.google.com/drive/folders/1F-pm_J-eKZAd7-PxnzZdCpKfAMlFs6Ke?usp=sharing

### Short guidline

* "json_parsing.ipynb": creation of posts_info dataset that contains AuthorID, OwnerID, CreatedDate, SearchQuery, AuthorType, OwnerType (type is 0 if group, type is 1 if user).
* "Groups and members.ipynb": extraction of members of groups from posts_info (max number of members is 1000 - vp api limit). 
* "analytics.ipynb": basic analysis of posts - word frequency, group activness, top words extraction and top groups extraction.
* "graph_analytics.ipynb": creation of graph that containes groups and their members, calculation of jaccard coefficient for all pairs of groups and extraction of the most similar groups and their info (name, description, anglicisms) to top_jaccard_groups dataset.


