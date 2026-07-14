from minsearch import index


class SearchEngine:
    def __init__(self, index_path):
        self.index = index.Index(index_path)

    def search(self, query, top_k=5):
        results = self.index.search(query, top_k=top_k)
        return results
   
    def vector_search(self, query_vector, top_k=5):
        results = self.index.vector_search(query_vector, top_k=top_k)
        return results
   
   
    def hybrid_search(self, query, query_vector, top_k=5):
        results = self.index.hybrid_search(query, query_vector, top_k=top_k)
        return results