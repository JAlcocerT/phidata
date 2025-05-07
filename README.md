<div align="center">
  <h1>PhiData Tests</h1>
</div>
<div align="center">
  <h3> Build Agents with memory, knowledge, tools and reasoning </h3>
</div>
<div align="center">
  <h3> Youtube Summarizer with Groq API </h3>
</div>


<div align="center">
  <!-- License Badge -->
  <a href="https://github.com/JAlcocerT/Streamlit-MultiChat?tab=GPL-3.0-1-ov-file" class="badge-link">
    <img alt="Code License GPLv3" src="https://img.shields.io/badge/License-GPLv3-blue.svg" class="badge-img"/>
  </a>

  <!-- GitHub Actions Workflow Badge -->
  <a href="https://github.com/JAlcocerT/Streamlit-MultiChat/actions/workflows/Streamlit_GHA_MultiArch.yml" class="badge-link">
    <img alt="GitHub Actions Workflow Status" src="https://github.com/JAlcocerT/Streamlit-MultiChat/actions/workflows/Streamlit_GHA_MultiArch.yml/badge.svg" class="badge-img"/>
  </a>

  <!-- Maintenance Status Badge -->
  <a href="https://GitHub.com/JAlcocerT/Streamlit-Multichat/graphs/commit-activity" class="badge-link">
    <img alt="Maintained? Yes" src="https://img.shields.io/badge/Maintained%3F-yes-green.svg" class="badge-img"/>
  </a>

  <!-- Python Version Badge (commented out but can be used if needed) -->
  <!--
  <a href="https://www.python.org/downloads/release/python-312" class="badge-link">
    <img alt="Python Version" src="https://img.shields.io/badge/python-3.12-blue.svg" class="badge-img"/>
  </a>
  -->

  <!-- Python Versions Groq Badge -->
  <a href="https://pypi.org/project/groq/" class="badge-link">
    <img alt="Supported Python Versions for Groq" src="https://img.shields.io/pypi/pyversions/groq.svg" class="badge-img"/>
  </a>

  <!-- HitCount Badge -->
  <!-- <a href="http://hits.dwyl.com/jalcocert/phidata" class="badge-link">
    <img src="https://hits.dwyl.com/jalcocert/phidata.svg?style=flat-square" alt="HitCount" class="badge-img"/>
  </a>
</div> -->




**Forked** from [PhiData](https://github.com/phidatahq/phidata) to...
    
* ...add systematical deployment method with [CI/CD](https://fossengineer.com/docker-github-actions-cicd/) & containers `./Z_DeployMe`    
    * Try the **YT Summaries** with [**Groq API**](https://console.groq.com/keys)
        * Groq Models - https://console.groq.com/docs/models
        * `./cookbook/llms/groq/video_summary/`
    * `./cookbook/agents/app.py`
* And to Try [manual astro Theme](https://github.com/TheOtterlord/manual) with Github CI/CD for the docs

* How to [deploy section](https://github.com/JAlcocerT/phidata/tree/main/Z_DeployMe) using the [GHCR Container Image](https://github.com/JAlcocerT/phidata/pkgs/container/phidata)

> **Extended explanation** at [this blog post](https://jalcocert.github.io/JAlcocerT/summarize-yt-videos/)

<!-- <div align="center" style="line-height: 1;">

  <a href="https://github.com/JAlcocerT/phidata/actions/workflows/Streamlit_GHA_MultiArch.yml" style="margin: 2px;">
    <img alt="GH Actions Workflow" src="https://github.com/JAlcocerT/phidata/actions/workflows/Streamlit_GHA_MultiArch.yml/badge.svg" style="display: inline-block; vertical-align: middle;"/>
  </a>

  <a href="https://pypi.org/project/groq/" style="margin: 2px;">
    <img alt="Python Versions Groq" src="https://img.shields.io/pypi/pyversions/groq.svg" style="display: inline-block; vertical-align: middle;"/>
  </a>

</div> -->

<!-- [![HitCount](https://hits.dwyl.com/jalcocert/phidata.svg?style=flat-square)](http://hits.dwyl.com/jalcocert/phidata) -->

<!-- [![Join the chat at https://gitter.im/{ORG-or-USERNAME}/{REPO-NAME}](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/dwyl/?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge) -->

## Venv Setup


```sh
python3 -m venv Z_PhiData_YT_Groq_venv

#Unix
source Z_PhiData_YT_Groq_venv/bin/activate
#.\Z_PhiData_YT_Groq_venv\Scripts\activate #Windows

cd ./cookbook/llms/groq/video_summary
pip install -r requirements.txt

source .env
#export GROQ_API_KEY="your-api-key-here"
#set GROQ_API_KEY=your-api-key-here
#$env:GROQ_API_KEY="your-api-key-here"
echo $GROQ_API_KEY


streamlit run app.py

# git add .
# git commit -m "some change to phidata yt groq"
# git push
```

See all models available with:

```sh
curl https://api.groq.com/openai/v1/models \
-H "Authorization: Bearer $GROQ_API_KEY"
```

Here’s a high-level walk-through of how the `cookbook/llms/groq/video_summary` example is wired together:

  1. What it is
      • A Streamlit-based demo that takes a YouTube URL, pulls down its transcript, and then uses Groq LLMs (via the Phidata “Assistant” API) to produce a two-stage New York-Times-style
write-up.
      • You log in (via `streamlit-authenticator`), pick your Groq model, set a “chunk” size, paste a video link and click Generate.
  2. Key Dependencies
      • streamlit + streamlit-authenticator (UI & login)
      • youtube-transcript-api (via Phidata’s `YouTubeTools`)
      • phidata (the Assistant abstraction)
      • groq (the Python client for Groq’s OpenAI-compatible API)
      • python-dotenv (to load your `GROQ_API_KEY`)
  3. Pipeline in `app.py`
        a. User logs in (hard-coded creds in `Z_Functions/Auth_functions.py`).
        b. Sidebar controls let you choose a model (`llama3-70b-8192`, `llama3-8b-8192`, etc.), set how many words per “chunk,” paste the YouTube URL and click Generate.
        c. Under the hood it calls

          youtube_tools = YouTubeTools(languages=[“en”])
          video_data     = youtube_tools.get_youtube_video_data(url)
          video_captions = youtube_tools.get_youtube_video_captions(url)

        so you see the embedded video + raw transcript.

        d. It splits the full transcript into N word-based chunks (based on your slider).
        e. For each chunk:
        • Instantiates a **chunk summarizer** via `get_chunk_summarizer(model)` (in `assistant.py`), which is a Phidata Assistant wrapping `phi.llm.groq.Groq(model=…)` plus system-style
instructions (“You are a Senior NYT Reporter tasked with summarizing…”).
        • Streams back each chunk’s summary in real-time using `assistant.run(...)`.
        f. Once all chunks are done it stitches them together and runs a **final summarizer** (`get_video_summarizer(model)`), again a Groq-backed Assistant with its own NYT-style prompt
and a `<report_format>` system message that tells it to output sections, headlines, key takeaways, date, etc.
        g. The final polished report is streamed back and rendered as Markdown in the app.
  4. How the Assistants are defined (`assistant.py`)
      • Both `get_chunk_summarizer` and `get_video_summarizer` return a `phi.assistant.Assistant` configured with:

  * `llm=Groq(model=…)`
  * `description`, a list of human instructions,
  * an injected `<report_format>` system prompt,
  * `markdown=True` and `debug_mode=True` for richer output and streaming.

  1. Supporting files
      • `groq_available_models.py` shows how to hit Groq’s `/openai/v1/models` endpoint to list your deployed LLMs.
      • `groq_sample_qq.py` is a minimal one-shot Q&A assistant example.
      • `requirements.txt` pins Streamlit, Phidata, Groq, youtube-transcript-api, etc.
      • `app_v2.py` is an alternate entry-point that does the same flow with a slightly different bootstrap (it calls `load_dotenv()`).
  2. What you learn from this demo
      • How to ingest and chunk large text (YouTube captions)
      • How to chain multiple LLM calls (chunk-level → aggregate-level)
      • How to stream partial results in a Streamlit UI
      • How to leverage Phidata’s Assistant abstraction on top of any OpenAI-compatible API (Groq here)
      • How to tame long transcripts by chunking against your model’s context window

> All in all, it’s a concise reference for building a **multi-step summarization pipeline**: YouTube → transcript → chunking → junior summaries → senior summary—using Phidata + Groq + Streamlit.


I’ve added a one-line top-of-file comment to each Python module involved in the `app_v3.py` run:

* **cookbook/llms/groq/video_summary/app_v2.py**
  “Streamlit front-end that orchestrates YouTube video summarization via Phidata + Groq”
* **cookbook/llms/groq/video_summary/assistant.py**
  “Defines Phidata Assistants for chunk-level and final video summarization using Groq LLMs”
* **cookbook/llms/groq/video_summary/Z_Functions/Auth_functions.py**
  “Provides Streamlit login/logout functionality using streamlit-authenticator”
* **phi/tools/youtube_tools.py**
  “Fetches YouTube video metadata and captions via youtube-transcript-api”
* Possibility to pass the latest groq models available via `.env`

**Thanks to:**

* https://pypi.org/project/youtube-transcript-api/
  * https://github.com/jdepoix/youtube-transcript-api

---

<h1 align="center">
  phidata
</h1>

<h3 align="center">
Build AI Assistants with memory, knowledge and tools
</h3>

![image](https://github.com/phidatahq/phidata/assets/22579644/295187f6-ac9d-41e0-abdb-38e3291ad1d1)

## What is phidata?

**Phidata is a framework for building Autonomous Assistants** (aka Agents) that have long-term memory, contextual knowledge and the ability to take actions using function calling.

Use phidata to turn any LLM into an AI Assistant that can:
- **Search the web** using DuckDuckGo, Google etc.
- **Analyze data** using SQL, DuckDb, etc.
- **Conduct research** and generate reports.
- **Answer questions** from PDFs, APIs, etc.
- **Write scripts** for movies, books, etc.
- **Summarize** articles, videos, etc.
- **Perform tasks** like sending emails, querying databases, etc.
- **And much more...**

## Why phidata?

**Problem:** We need to turn general-purpose LLMs into specialized assistants for our use-case.

**Solution:** Extend LLMs with memory, knowledge and tools:
- **Memory:** Stores **chat history** in a database and enables LLMs to have long-term conversations.
- **Knowledge:** Stores information in a vector database and provides LLMs with **business context**.
- **Tools:** Enable LLMs to **take actions** like pulling data from an API, sending emails or querying a database.

Memory & knowledge make LLMs **smarter** while tools make them **autonomous**.

## How it works

- **Step 1:** Create an `Assistant`
- **Step 2:** Add Tools (functions), Knowledge (vectordb) and Storage (database)
- **Step 3:** Serve using Streamlit, FastApi or Django to build your AI application


## Installation

```shell
pip install -U phidata
```

## Quickstart

### Assistant that can search the web

Create a file `assistant.py`

```python
from phi.assistant import Assistant
from phi.tools.duckduckgo import DuckDuckGo

assistant = Assistant(tools=[DuckDuckGo()], show_tool_calls=True)
assistant.print_response("Whats happening in France?", markdown=True)
```

Install libraries, export your `OPENAI_API_KEY` and run the `Assistant`

```shell
pip install openai duckduckgo-search

export OPENAI_API_KEY=sk-xxxx

python assistant.py
```

### Assistant that can query financial data

Create a file `finance_assistant.py`

```python
from phi.assistant import Assistant
from phi.llm.openai import OpenAIChat
from phi.tools.yfinance import YFinanceTools

assistant = Assistant(
    llm=OpenAIChat(model="gpt-4o"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True)],
    show_tool_calls=True,
    markdown=True,
)
assistant.print_response("What is the stock price of NVDA")
assistant.print_response("Write a comparison between NVDA and AMD, use all tools available.")
```

Install libraries and run the `Assistant`

```shell
pip install yfinance

python finance_assistant.py
```

## More information

- Read the docs at <a href="https://docs.phidata.com" target="_blank" rel="noopener noreferrer">docs.phidata.com</a>
- Chat with us on <a href="https://discord.gg/4MtYHHrgA8" target="_blank" rel="noopener noreferrer">discord</a>

## Examples

- [LLM OS](https://github.com/phidatahq/phidata/tree/main/cookbook/llm_os): Using LLMs as the CPU for an emerging Operating System.
- [Autonomous RAG](https://github.com/phidatahq/phidata/tree/main/cookbook/examples/auto_rag): Gives LLMs tools to search its knowledge, web or chat history.
- [Local RAG](https://github.com/phidatahq/phidata/tree/main/cookbook/llms/ollama/rag): Fully local RAG with Llama3 on Ollama and PgVector.
- [Investment Researcher](https://github.com/phidatahq/phidata/tree/main/cookbook/llms/groq/investment_researcher): Generate investment reports on stocks using Llama3 and Groq.
- [News Articles](https://github.com/phidatahq/phidata/tree/main/cookbook/llms/groq/news_articles): Write News Articles using Llama3 and Groq.
- [Video Summaries](https://github.com/phidatahq/phidata/tree/main/cookbook/llms/groq/video_summary): YouTube video summaries using Llama3 and Groq.
- [Research Assistant](https://github.com/phidatahq/phidata/tree/main/cookbook/llms/groq/research): Write research reports using Llama3 and Groq.

### Assistant that can write and run python code

<details>

<summary>Show code</summary>

The `PythonAssistant` can achieve tasks by writing and running python code.

- Create a file `python_assistant.py`

```python
from phi.assistant.python import PythonAssistant
from phi.file.local.csv import CsvFile

python_assistant = PythonAssistant(
    files=[
        CsvFile(
            path="https://phidata-public.s3.amazonaws.com/demo_data/IMDB-Movie-Data.csv",
            description="Contains information about movies from IMDB.",
        )
    ],
    pip_install=True,
    show_tool_calls=True,
)

python_assistant.print_response("What is the average rating of movies?", markdown=True)
```

- Install pandas and run the `python_assistant.py`

```shell
pip install pandas

python python_assistant.py
```

</details>

### Assistant that can analyze data using SQL

<details>

<summary>Show code</summary>

The `DuckDbAssistant` can perform data analysis using SQL.

- Create a file `data_assistant.py`

```python
import json
from phi.assistant.duckdb import DuckDbAssistant

duckdb_assistant = DuckDbAssistant(
    semantic_model=json.dumps({
        "tables": [
            {
                "name": "movies",
                "description": "Contains information about movies from IMDB.",
                "path": "https://phidata-public.s3.amazonaws.com/demo_data/IMDB-Movie-Data.csv",
            }
        ]
    }),
)

duckdb_assistant.print_response("What is the average rating of movies? Show me the SQL.", markdown=True)
```

- Install duckdb and run the `data_assistant.py` file

```shell
pip install duckdb

python data_assistant.py
```

</details>

### Assistant that can generate pydantic models

<details>

<summary>Show code</summary>

One of our favorite LLM features is generating structured data (i.e. a pydantic model) from text. Use this feature to extract features, generate movie scripts, produce fake data etc.

Let's create a Movie Assistant to write a `MovieScript` for us.

- Create a file `movie_assistant.py`

```python
from typing import List
from pydantic import BaseModel, Field
from rich.pretty import pprint
from phi.assistant import Assistant

class MovieScript(BaseModel):
    setting: str = Field(..., description="Provide a nice setting for a blockbuster movie.")
    ending: str = Field(..., description="Ending of the movie. If not available, provide a happy ending.")
    genre: str = Field(..., description="Genre of the movie. If not available, select action, thriller or romantic comedy.")
    name: str = Field(..., description="Give a name to this movie")
    characters: List[str] = Field(..., description="Name of characters for this movie.")
    storyline: str = Field(..., description="3 sentence storyline for the movie. Make it exciting!")

movie_assistant = Assistant(
    description="You help write movie scripts.",
    output_model=MovieScript,
)

pprint(movie_assistant.run("New York"))
```

- Run the `movie_assistant.py` file

```shell
python movie_assistant.py
```

- The output is an object of the `MovieScript` class, here's how it looks:

```shell
MovieScript(
│   setting='A bustling and vibrant New York City',
│   ending='The protagonist saves the city and reconciles with their estranged family.',
│   genre='action',
│   name='City Pulse',
│   characters=['Alex Mercer', 'Nina Castillo', 'Detective Mike Johnson'],
│   storyline='In the heart of New York City, a former cop turned vigilante, Alex Mercer, teams up with a street-smart activist, Nina Castillo, to take down a corrupt political figure who threatens to destroy the city. As they navigate through the intricate web of power and deception, they uncover shocking truths that push them to the brink of their abilities. With time running out, they must race against the clock to save New York and confront their own demons.'
)
```

</details>

### PDF Assistant with Knowledge & Storage

<details>

<summary>Show code</summary>

Lets create a PDF Assistant that can answer questions from a PDF. We'll use `PgVector` for knowledge and storage.

**Knowledge Base:** information that the Assistant can search to improve its responses (uses a vector db).

**Storage:** provides long term memory for Assistants (uses a database).

1. Run PgVector

Install [docker desktop](https://docs.docker.com/desktop/install/mac-install/) and run **PgVector** on port **5532** using:

```bash
docker run -d \
  -e POSTGRES_DB=ai \
  -e POSTGRES_USER=ai \
  -e POSTGRES_PASSWORD=ai \
  -e PGDATA=/var/lib/postgresql/data/pgdata \
  -v pgvolume:/var/lib/postgresql/data \
  -p 5532:5432 \
  --name pgvector \
  phidata/pgvector:16
```

2. Create PDF Assistant

- Create a file `pdf_assistant.py`

```python
import typer
from typing import Optional, List
from phi.assistant import Assistant
from phi.storage.assistant.postgres import PgAssistantStorage
from phi.knowledge.pdf import PDFUrlKnowledgeBase
from phi.vectordb.pgvector import PgVector2

db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"

knowledge_base = PDFUrlKnowledgeBase(
    urls=["https://phi-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
    vector_db=PgVector2(collection="recipes", db_url=db_url),
)
# Comment out after first run
knowledge_base.load()

storage = PgAssistantStorage(table_name="pdf_assistant", db_url=db_url)


def pdf_assistant(new: bool = False, user: str = "user"):
    run_id: Optional[str] = None

    if not new:
        existing_run_ids: List[str] = storage.get_all_run_ids(user)
        if len(existing_run_ids) > 0:
            run_id = existing_run_ids[0]

    assistant = Assistant(
        run_id=run_id,
        user_id=user,
        knowledge_base=knowledge_base,
        storage=storage,
        # Show tool calls in the response
        show_tool_calls=True,
        # Enable the assistant to search the knowledge base
        search_knowledge=True,
        # Enable the assistant to read the chat history
        read_chat_history=True,
    )
    if run_id is None:
        run_id = assistant.run_id
        print(f"Started Run: {run_id}\n")
    else:
        print(f"Continuing Run: {run_id}\n")

    # Runs the assistant as a cli app
    assistant.cli_app(markdown=True)


if __name__ == "__main__":
    typer.run(pdf_assistant)
```

3. Install libraries

```shell
pip install -U pgvector pypdf "psycopg[binary]" sqlalchemy
```

4. Run PDF Assistant

```shell
python pdf_assistant.py
```

- Ask a question:

```
How do I make pad thai?
```

- See how the Assistant searches the knowledge base and returns a response.

- Message `bye` to exit, start the assistant again using `python pdf_assistant.py` and ask:

```
What was my last message?
```

See how the assistant now maintains storage across sessions.

- Run the `pdf_assistant.py` file with the `--new` flag to start a new run.

```shell
python pdf_assistant.py --new
```

</details>

### Checkout the [cookbook](https://github.com/phidatahq/phidata/tree/main/cookbook) for more examples.

## Next Steps

1. Read the <a href="https://docs.phidata.com/basics" target="_blank" rel="noopener noreferrer">basics</a> to learn more about phidata.
2. Read about <a href="https://docs.phidata.com/assistants/introduction" target="_blank" rel="noopener noreferrer">Assistants</a> and how to customize them.
3. Checkout the <a href="https://docs.phidata.com/examples/cookbook" target="_blank" rel="noopener noreferrer">cookbook</a> for in-depth examples and code.

## Demos

Checkout the following AI Applications built using phidata:

- <a href="https://pdf.aidev.run/" target="_blank" rel="noopener noreferrer">PDF AI</a> that summarizes and answers questions from PDFs.
- <a href="https://arxiv.aidev.run/" target="_blank" rel="noopener noreferrer">ArXiv AI</a> that answers questions about ArXiv papers using the ArXiv API.
- <a href="https://hn.aidev.run/" target="_blank" rel="noopener noreferrer">HackerNews AI</a> summarize stories, users and shares what's new on HackerNews.

## Tutorials

### LLM OS with gpt-4o

[![Building the LLM OS with gpt-4o](https://img.youtube.com/vi/6g2KLvwHZlU/0.jpg)](https://www.youtube.com/watch?v=6g2KLvwHZlU "LLM OS")

### Autonomous RAG

[![Autonomous RAG](https://img.youtube.com/vi/fkBkNWivq-s/0.jpg)](https://www.youtube.com/watch?v=fkBkNWivq-s "Autonomous RAG")

### Local RAG with Llama3

[![Local RAG with Llama3](https://img.youtube.com/vi/-8NVHaKKNkM/0.jpg)](https://www.youtube.com/watch?v=-8NVHaKKNkM "Local RAG with Llama3")

### Llama3 Research Assistant powered by Groq

[![Llama3 Research Assistant powered by Groq](https://img.youtube.com/vi/Iv9dewmcFbs/0.jpg)](https://www.youtube.com/watch?v=Iv9dewmcFbs "Llama3 Research Assistant powered by Groq")

## Looking to build an AI product?

We've helped many companies build AI products, the general workflow is:

1. **Build an Assistant** with proprietary data to perform tasks specific to your product.
2. **Connect your product** to the Assistant via an API.
3. **Monitor and Improve** your AI product.

We also provide dedicated support and development, [book a call](https://cal.com/phidata/intro) to get started.

## Contributions

We're an open-source project and welcome contributions, please read the [contributing guide](https://github.com/phidatahq/phidata/blob/main/CONTRIBUTING.md) for more information.

## Request a feature

- If you have a feature request, please open an issue or make a pull request.
- If you have ideas on how we can improve, please create a discussion.

## Roadmap

Our roadmap is available <a href="https://github.com/orgs/phidatahq/projects/2/views/1" target="_blank" rel="noopener noreferrer">here</a>.
If you have a feature request, please open an issue/discussion.
