# Google Trends Analysis: A Cultural and Geo-political Analysis of Queries Searched for in Google
In this project, we aim to study the rising search queries in github during the 
past 12 months in different countries. To this end, we first study the search 
queries people search for. We created a python dictionary mapping each unique 
query to the most relevant category. This dictionary is available at category_dictionaries.py. 
The categories we considered are the following:
```python
["Action/Fighting/Horror", "Adventure", "RPG", "Simulation", "Strategy", "Sports", "Puzzle", "Platformer", "Casual", "Family", "None"]
```
We then used the K-means clustering algorithm to cluster the queries into 3 to 8 clusters. 
Then these clustered were analyzed and the countries that appeared together in at least 4 
out of the 6 clusters were studied.

The results showed that these countries formed 4 big groups of countries. These groups show 
a similarity of interest that has correlation with similarity of culture in these countries 
as well as linguitstic similarity and how these countries rank in terms of democracy (the data for this was gathered from World Population Review).
The written result of this study is being writing and will be added to this repository in the future. 

In order to run the code, and interact with our code, you could use the following steps after
downloading the content of our repository:
1. Create a conda envrionment using the following command:

```bash
conda create --name <env name> python=3.8
```
2. Activate the environment using the following command:
```bash
conda activate <env name>
```
3. Install the required packages using the following command:
```bash
pip install -r requirements.txt
```

## Usage
You can then run the code using the following command:
```bash
python main.py
```

## Question & Contributing
If you have any questions, suggestions, and relevant ideas you would like to work on, 
please feel free to open an issue or connect to me on LinkedIn (available on my profile page on GitHub), and discuss it with us.