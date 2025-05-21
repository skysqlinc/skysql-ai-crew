#### TODO ....

## Project purpose

## Setup instructions

## Use cases

## Demo GIF or screenshots (optional)

----
### Why use SkySQL DB Agents ? 

While it is possible to generate SQL given some schema description to a LLM or use APIs in frameworks, it is rather challenging to generate accurate SQL for real world DBs with high complexity. You need the correct context, allow humans to add missing semantic information(e.g. map common terms to columns), store some relevant context (Schema, categorical values, etc) in Vector stores and more. 
SkySQL DB Agents provides a No-Code UI to autonomously learn the DB context. It is also secure and reliable. 

### How do I create these DB Agents ? 
Here are the steps:
- Visit the SkySQL portal at app.skysql.com , sign up and click 'SkyAI Agents'. 
- We need a DB to work with. You could launch a SkySQL free Serverless DB. It will literally only take a second or two. Click 'Dashboard' --> Launch.
- OR, If you already have access to your DB (can only be MySQL or MariaDB), add a 'data source'. Enter the DB credentials (these are safely managed in SkySQL). 
- Click 'Agent --> Create' and type some goal/objectives for your DB agent. 
- SkySQL will discover the schema info, relationships, peek at the data and automatically select the appropriate tables and generate the context. 
- You can tweak this context (IMPORTANT, especially for complex DBs or tables) - select/deselect columns. Stick to no more than 10 tables. 
- Use the playground to test it out. Iteratively make the context for the tables and Agent better (i.e. edit the text)
- That is it. It is now accessible using the REST API  (tools to external Agents like Lanchain agents)


### Why integrate with AI frameworks

SkySQL provides "DB level" Agents. Your application may still need to work with disparate other sources, have its own orchestration across multiple agents and so on. 
Moreover, a high level agent often improves the quality of the responses. It will rewrite the user question to be more appropriate and synthesize good results. 

## Examples here

The Simple examples here provide a conversational agent that can interact with backend database agents to answer your queries, show SQL, and suggest next steps. You can use it as a web app (Streamlit) or from the command line.

