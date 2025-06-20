* There is a **GH Actions WF** that pushes the changes to - https://github.com/JAlcocerT?tab=packages
* https://github.com/JAlcocerT/Docker/tree/main/AI_Gen/Project_YT_Groq

```sh
docker pull ghcr.io/jalcocert/phidata:yt-groq #https://github.com/users/JAlcocerT/packages/container/package/phidata
```

* Alternatively, you can build your own image:

```sh
docker build -t phidata:yt_summary_groq .
podman build -t phidata:yt_summary_groq .
```

---

* With Python Venv's

```sh
git clone https://github.com/JAlcocerT/phidata
python -m venv ytgroq #create the venv

ytgroq\Scripts\activate #activate venv (windows)
source ytgroq/bin/activate #(linux)
```


## YT+Groq

```sh
cd ./cookbook/llms/groq/video_summary
pip install -r requirements.txt #all at once
streamlit run app.py
```

## Agents with OpenAI GPT Models

It can read blog posts/pdf/Databases (duckDB compatible)

```sh
cd ./cookbook/agents
pip install -r requirements.txt #all at once
streamlit run app.py
#streamlit run cookbook/agents/app.py
```