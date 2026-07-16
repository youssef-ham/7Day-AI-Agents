class SearchTool:
    def __init__(self, index):
        self.index = index

    def search(self, query):
        results = self.index.search(
            query,
            num_results=5,
        )

        if not results:
            return "No relevant documents found."

        output = []

        for r in results:
            output.append(
                f"""
Question:
{r.get('question', '')}

Content:
{r.get('content', '')}

Filename:
{r.get('filename', '')}
"""
            )

        return "\n\n---\n\n".join(output)