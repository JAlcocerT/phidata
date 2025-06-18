# YouTube Video Summary Application Documentation

## Overview

This documentation explains how the Streamlit application for YouTube video summarization works. The application uses Groq's LLM models to generate summaries of YouTube videos by processing their captions and metadata.

## How to Run the Application

```bash
# 1. Create a virtual environment
python3 -m venv ~/.venvs/groqvideosummary
# or on Windows
python -m venv groqvideosummary

# 2. Activate the virtual environment
source ~/.venvs/groqvideosummary/bin/activate
# or on Windows
groqvideosummary\Scripts\activate

# 3. Export your Groq API Key
export GROQ_API_KEY="YOUR_API_KEY"
# or on Windows CMD
set GROQ_API_KEY=YOUR_API_KEY
# or on Windows PowerShell
$env:GROQ_API_KEY="YOUR_API_KEY"

# 4. Install dependencies
pip install -r cookbook/llms/groq/video_summary/requirements.txt

# 5. Run the application
streamlit run cookbook/llms/groq/video_summary/app_v3.py
```

## Dependencies

The application requires the following main dependencies:

- **streamlit**: Web application framework
- **phidata**: AI application framework
- **groq**: Groq API client for accessing LLM models
- **youtube-transcript-api**: For fetching YouTube video captions
- **streamlit-authenticator**: For authentication functionality
- **python-dotenv**: For loading environment variables

Full dependencies are listed in the `requirements.txt` file.

## Environment Variables

The application uses the following environment variables:

- `GROQ_API_KEY`: API key for accessing Groq LLM models
- `AVAILABLE_LLM_MODELS` (optional): Comma-separated list of available Groq models

## File Structure

```
cookbook/llms/groq/video_summary/
├── app_v3.py                # Main application file
├── assistant.py             # Defines Groq assistants for summarization
├── Z_Functions/
│   └── Auth_functions.py    # Authentication functionality
├── requirements.txt         # Dependencies
├── requirements.in          # Input file for pip-compile
└── README.md                # Project documentation
```

## Core Components and Functions

### 1. Main Application (`app_v3.py`)

The main application file handles the Streamlit UI and orchestrates the video summarization process.

#### Key Functions:

- **`get_available_groq_models_from_env()`**: Reads available Groq models from environment variables
- **`main()`**: Main function that sets up the Streamlit UI and handles the video summarization workflow

#### Workflow:

1. User authentication via `Auth_functions.login()`
2. Selection of LLM model from available options
3. Input of YouTube video URL
4. Fetching video data and captions using `YouTubeTools`
5. Processing captions in chunks if necessary
6. Generating summaries for each chunk using `get_chunk_summarizer()`
7. Generating a final summary using `get_video_summarizer()`

### 2. Assistant Module (`assistant.py`)

Defines two assistant classes using the Groq LLM models:

#### Key Functions:

- **`get_chunk_summarizer(model, debug_mode)`**: Creates an assistant for summarizing individual chunks of video captions
- **`get_video_summarizer(model, debug_mode)`**: Creates an assistant for generating the final video summary based on chunk summaries

Both assistants use carefully crafted prompts to generate high-quality summaries in a New York Times reporter style.

### 3. Authentication (`Z_Functions/Auth_functions.py`)

Handles user authentication for the application.

#### Key Functions:

- **`login()`**: Authenticates users with predefined usernames and passwords

## Application Flow

1. **Authentication**: User logs in using credentials
2. **Configuration**: User selects LLM model and sets chunk size
3. **Input**: User provides YouTube video URL
4. **Video Processing**:
   - Fetch video metadata and captions
   - Split captions into manageable chunks if needed
5. **Chunk Summarization**:
   - For each chunk, generate a summary using `chunk_summarizer`
6. **Final Summary Generation**:
   - Combine chunk summaries and video metadata
   - Generate comprehensive final summary using `video_summarizer`
7. **Display**: Show the final summary to the user

## Technical Details

### Chunking Process

The application splits long video captions into chunks of a user-defined size (default: 4500 words) to avoid exceeding LLM context limits. Each chunk is processed separately, and the results are combined for the final summary.

### LLM Integration

The application uses the Groq API to access powerful language models like llama3-70b-8192, llama3-8b-8192, and mixtral-8x7b-32768. The model selection is configurable through the UI.

### YouTube Integration

The `YouTubeTools` class from the phidata library is used to fetch video metadata and captions from YouTube videos.

## User Interface

The Streamlit interface includes:

- Login form
- Sidebar with model selection and configuration options
- Video URL input field
- Summary generation button
- Status indicators for each processing step
- Final summary display

## Security Considerations

- Authentication is implemented using streamlit-authenticator
- API keys are loaded from environment variables
- Hardcoded credentials in the authentication module should be replaced with more secure methods in production

## Limitations

- Requires a valid Groq API key
- Performance depends on the selected LLM model
- May not work with all YouTube videos, especially those without captions
- Processing long videos may take significant time and resources
