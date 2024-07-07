* There is a **GH Actions WF** that pushes the changes to - https://github.com/JAlcocerT?tab=packages

```sh
docker pull ghcr.io/jalcocert/phidata:yt-groq #https://github.com/users/JAlcocerT/packages/container/package/phidata
```

* Alternatively, you can build your own image:

```sh
docker build -t phidata:yt_summary_groq .
podman build -t phidata:yt_summary_groq .
```