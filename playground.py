# instead of making a team or multi agent in code like app.py, we can use playground to make it into a chatbot.
# multi agent or team will give results in the terminal.
# Whereas playground gives the result in --> phidata --> playground.
# This is Beta version though, yet looks good.

# import packages 
# import env variables
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools
from dotenv import load_dotenv
import uvicorn
import os
load_dotenv() 

# use API keys to access the model
from phi.playground import Playground, serve_playground_app
import phi.api
phi.api=os.getenv("PHI_API_KEY")


# create agent structure
# This agent is to search the web
web_agent = Agent(
    name="Web Agent",
    role="Search the web for information",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True,
)

# This agent is to get the financial data
finance_agent = Agent(
    name="Finance Agent - Harsha merge",
    role="Get financial data",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True)],
    instructions=["Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)

# Use the playground feature
app=Playground(agents=[finance_agent,web_agent]).get_app()

if __name__=="__main__":
    serve_playground_app("playground:app",reload=True)
# playground is filename and app is where the execution starts.
# run this to get local host.
# go to playground and select local host.
# Chatbot is made.
# ask the question in the Chatbot console.
