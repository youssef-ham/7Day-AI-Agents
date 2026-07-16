import os
from dotenv import load_dotenv
from groq import Groq
import search_tools

load_dotenv()


SYSTEM_PROMPT_TEMPLATE = """
You are a helpful assistant that answers questions about documentation.

Use the search results to answer the question.

Always include references by citing the filename of the source material you used.

Replace it with the full path to the GitHub repository:
https://github.com/{repo_owner}/{repo_name}/blob/main/
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

    prompt = f"""
{agent["system_prompt"]}

Question:
{question}

Search Results:
{docs}
"""

    response = (
        agent["client"]
        .chat
        .completions
        .create(
            model="openai/gpt-oss-120b",
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            temperature=0,
        )
    )

    return response.choices[0].message.content