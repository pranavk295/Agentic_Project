import langchainhub as hub
from langchain.agents import create_agent
from tools import tools
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

def run_agent(user_prompt: str, tools_list: list):
    agent = create_agent(
        model="google_genai:gemini-2.5-flash",
        tools=tools_list,
        system_prompt="You are a helpful assistant. Use your tools when necessary to answer questions accurately."
    )

    response = agent.invoke({
        "messages": [{"role": "user", "content": user_prompt}]
    })
    return response["messages"]
if __name__ == "__main__":
    test_prompt = "What comments can I write for each file in my codebase?"
    
    print(f"Asking Agent: '{test_prompt}'\n")
    
    final_answer = run_agent(test_prompt, tools)
    
    print(f"\nFinal Result: {final_answer}")
