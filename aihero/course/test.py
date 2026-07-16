import asyncio
import ingest
import search_agent

repo_owner = "DataTalksClub"
repo_name = "faq"

def filter(doc):
    return "data-engineering" in doc["filename"]

index = ingest.index_data(repo_owner, repo_name, filter=filter)
agent = search_agent.init_agent(index, repo_owner, repo_name)


async def main():
    result = await agent.run("how do i run ollama locally?")
    print(result.output)


asyncio.run(main())