# Video Summaries powered by Groq

> Note: Fork and clone this repository if needed

### 1. Create a virtual environment

```shell
python3 -m venv ~/.venvs/groqvideosummary
python -m venv groqvideosummary #create the venv in windows

groqvideosummary\Scripts\activate #activate venv (windows)
source groqvideosummary/bin/activate #(linux)
```

### 2. Export your Groq API Key

* Linux - export GROQ_API_KEY="YOUR_API_KEY"
* CMD - set GROQ_API_KEY=YOUR_API_KEY
* PS - $env:GROQ_API_KEY="YOUR_API_KEY"

```shell
export GROQ_API_KEY=***
```

### 3. Install libraries

```shell
#pip install -r requirements.txt
pip install -r cookbook/llms/groq/video_summary/requirements.txt
```

### 4. Run Streamlit App

```shell
#streamlit run app.py
streamlit run cookbook/llms/groq/video_summary/app.py
```

- Open [localhost:8501](http://localhost:8501) to view your Video Summary App

### 5. Message on [discord](https://discord.gg/4MtYHHrgA8) if you have any questions

### 6. Star ⭐️ the project if you like it.