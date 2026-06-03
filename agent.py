import os
import asyncio
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_ollama import ChatOllama
load_dotenv()

async def main():
    client = MultiServerMCPClient(
        {
            # "web_fetcher": {
            # "command": "uvx", 
            # "args": ["mcp-server-fetch"],
            # "transport": "stdio",
            # },
            "coin_flipper_server": {
                "command": "python3", 
                "args": [os.path.abspath("coin_server.py")],
                "transport": "stdio",
            },
            "file_server": {
                "command": "python3", 
                "args": [os.path.abspath("file_server.py")],
                "transport": "stdio",
            }
        }
    )
    
    mcp_tools = await client.get_tools()
    print(f"Available tools: {mcp_tools}")
    local_model = ChatOllama(model="qwen2.5:7b", temperature=0.7)
    async def run_agent(user_prompt: str, tools_list: list):
        agent = create_agent(
            model=local_model,
            tools=tools_list,
            system_prompt="You are a helpful assistant. Use your tools when necessary."
        )

        response = await agent.ainvoke({
            "messages": [{"role": "user", "content": user_prompt}]
        })
        return response["messages"]

    # prompt = "Flip a coin if heads Summarize the main content of this page: https://medium.com/@aivabea/tiniest-web-page-part-1-html-ba452600bcc1 else say you lose and give me the bug for each file in the directory"
    prompt= 'find the bugs in the  sample_code directory files. Write the fix as a comment at the start of the file. Use the tools provided where necessary.'
    print(f"Prompt: {prompt}\n")
    
    messages = await run_agent(user_prompt=prompt, tools_list=mcp_tools)
    print("Agent Response:", messages[-1].content)

if __name__ == "__main__":
    asyncio.run(main())
