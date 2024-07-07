* There is a **GH Actions WF** that pushes the changes to - https://github.com/JAlcocerT?tab=packages

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

```sh
cd ./cookbook/llms/groq/video_summary
pip install -r requirements.txt #all at once
streamlit run app.py
```