FROM python:3.11

LABEL org.opencontainers.image.source https://github.com/JAlcocerT/phidata

# Install git
RUN apt-get update && apt-get install -y git

# Set up the working directory
#WORKDIR /app

# Clone the repository - https://github.com/phidatahq/phidata
RUN git clone --depth=1 https://github.com/JAlcocerT/phidata && \
    cd phidata && \
    git sparse-checkout init && \
    git sparse-checkout set cookbook/llms/groq/video_summary && \
    git pull origin main

WORKDIR /phidata

# Install Python requirements
RUN pip install -r /phidata/cookbook/llms/groq/video_summary/requirements.txt

#RUN sed -i 's/numpy==1\.26\.4/numpy==1.24.4/; s/pandas==2\.2\.2/pandas==2.0.2/' requirements.txt


# Set the entrypoint to a bash shell
CMD ["/bin/bash"]


#docker build -t phidata:yt_summary_groq .
#podman build -t phidata:yt_summary_groq .

#docker run -p 8501:8501 phidata:yt_summary_groq
#podman run -p 8501:8501 phidata:yt_summary_groq

# podman run -d --name=phidata_yt_groq -p 8502:8501 -e GROQ_API_KEY=your_api_key_here \
# phidata:yt_summary_groq tail -f /dev/null

# podman run -d --name=phidata_yt_groq -p 8502:8501 -e GROQ_API_KEY=your_api_key_here \
# phidata:yt_summary_groq streamlit run cookbook/llms/groq/video_summary/app.py