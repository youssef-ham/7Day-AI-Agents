import os

from dotenv import load_dotenv
from groq import Groq

import search_tools

load_dotenv()

SYSTEM_PROMPT_TEMPLATE = """
You are a helpful assistant that answers questions about LangChain documentation.

Use ONLY the search results to answer the user's question.

If the answer is not present in the search results, say that you couldn't find it.

At the end of every answer add:

References

For each document you used include:

Filename:
<filename>

GitHub:
https://github.com/{repo_owner}/{repo_name}/blob/main/<filename>

Never generate fake citations like:
【1】
【2】
[1]
[2]
Only use the filenames provided in the search results.
"""

def init_agent(index, repo_owner, repo_name):
    client = Groq(
        api_key=os.getenv("GROQ_API_KEY")
    )

    search_tool = search_tools.SearchTool(index)

    system_prompt = SYSTEM_PROMPT_TEMPLATE.format(
        repo_owner=repo_owner,
        repo_name=repo_name,
    )

    return {
        "client": client,
        "search_tool": search_tool,
        "system_prompt": system_prompt,
    }


def ask_agent(agent, question):

    docs = agent["search_tool"].search(question)

    print("=" * 80)
    print("Search Results Size:", len(docs))
    print("=" * 80)

    prompt = f"""
{agent["system_prompt"]}

Question:
{question}

Search Results:
{docs}
"""

    print("=" * 80)
    print("Prompt Size:", len(prompt))
    print("=" * 80)

    response = (
        agent["client"]
        .chat
        .completions
        .create(
            model="openai/gpt-oss-120b",
            temperature=0,
            max_tokens=1024,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )
    )

    return response.choices[0].message.content