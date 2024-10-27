# Textual Data Analysis and Big Data Analysis Project in INA Course

## Part I: Analysis of Textual Data

In this Project, the focus is on exploring the Gensim library for textual data analysis.

### Step 1: Reading News from File

Write a function called `read_isna_content` that reads the news text from the provided file. The function should take the file path as input and return a string containing the text of all ISNA news.

### Step 2: Normalization

Write a function called `normalize_isna_content` to normalize the news text. The function should take a string as input and return a normalized string. For example, it can replace "y" with "ي" to account for different character encodings.

### Step 3: Segmenting Corpus into Sentences

Write a function called `segment_corpus_isna` to segment the normalized corpus into sentences. The function should take a string (the output of Step 2) as input and return a list of sentences.

### Step 4: Cutting Sentences into Words

Write a function called `prepare_final_isna` to split each sentence into a list of words. The input to this function is the output of Step 3, and the output should be a two-dimensional list representing the words of each sentence.

### Step 5: Model Training

Train a word embedding model using the gensim library. Compare the Continuous Bag-of-Words (CBOW) and Skip-gram models and choose one for training. Use the two-dimensional list from Step 4 as input to the `Word2Vec` class in gensim, along with the appropriate parameters. Explain the model parameters and their selection criteria in your report.

### Step 6: Using the Model

With the trained word embedding model, find the five words that are closest to the word "Iran".

### Step 7: Model Evaluation

Propose a method for evaluating the trained word embedding model and implement it. Explain your evaluation method in the report.

Helpful links: [Gensim Documentation](https://radimrehurek.com/gensim/)

## Part II: Spark

The purpose of this part is to become familiar with structural network analysis using Spark in the context of big data.

### Part I

To familiarize yourself with the PySpark library and Spark platform, write a program that lists the top 10 products and the bottom 10 products based on the number of user feedbacks and average scores. Extract these lists into two separate CSV files, one for the top 10 products and one for the bottom 10 products. Consider the number of feedbacks, average scores, and prices for each product. Download the feedback dataset from the provided link.

### Part II

In this part, using the given data file that contains user-user communication within a social network, the following features should be calculated and reported. Note that in this dataset, the nodes represent users, and the edges represent friendship links between them. Save the calculated values for each node in a CSV file with the appropriate format:

1. Calculate the in-degree and out-degree of nodes.
2. Calculate the average degrees of each node's neighbors.
3. Calculate the diameter of the graph.
4. Calculate the closeness centrality for all nodes.
5. Calculate the PageRank for all nodes.
6. Calculate the local clustering coefficient for all nodes.
7. Obtain the connected components and strongly connected components.

