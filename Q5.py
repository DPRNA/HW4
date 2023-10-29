from documents import DocumentStore
from tf_idf_index import TfIdfIndex
from TfIdfInvertedIndex import TfIdfInvertedIndex
from query_process_AfterHW4 import QueryProcess
import timeit


# Load  document store and indexes
document_store = DocumentStore()
tfidf_index = TfIdfIndex()
tfidf_inverted_index = TfIdfInvertedIndex()


stopwords_file = "topwordsHW4.json"

# Instantiate  QueryProcess class with TfIdfIndex
query_process_tfidf = QueryProcess(document_store, tfidf_index, stopwords_file=stopwords_file)

# Instantiate  QueryProcess class with TfIdfInvertedIndex
query_process_tfidf_inverted = QueryProcess(document_store, tfidf_inverted_index, stopwords_file=stopwords_file)

# Instantiate  QueryProcess class with TfIdfInvertedIndex and  stopword list
query_process_tfidf_inverted_stopwords = QueryProcess(document_store, tfidf_inverted_index, stopwords_file=stopwords_file)

# Define  query and  number of results
query = 'credit card'
number_of_results = 10

# Measure  time taken by each call
time_tfidf = timeit.timeit(lambda: query_process_tfidf.search(query, number_of_results), number=100)
time_tfidf_inverted = timeit.timeit(lambda: query_process_tfidf_inverted.search(query, number_of_results), number=100)
time_tfidf_inverted_stopwords = timeit.timeit(lambda: query_process_tfidf_inverted_stopwords.search(query, number_of_results), number=100)

# Print  results
print("TfIdfIndex time:", time_tfidf)
print("TfIdfInvertedIndex time:", time_tfidf_inverted)
print("TfIdfInvertedIndex with stopwords time:", time_tfidf_inverted_stopwords)
