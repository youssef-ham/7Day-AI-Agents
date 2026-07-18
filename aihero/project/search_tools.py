class SearchTool:

    def __init__(self, index):
        self.index = index

    def search(self, query):

        results = self.index.search(
            query,
            num_results=3,
        )

        if not results:
            return "No relevant documents found."

        output = []

        for r in results:

            title = (
                r.get("title")
                or r.get("sidebarTitle")
                or r.get("name")
                or "Untitled"
            )

            output.append(
                f"""
Title:
{title}

Filename:
{r.get("filename")}

Content:
{r.get("content", "")[:500]}
"""
            )

        return "\n\n----------------\n\n".join(output)