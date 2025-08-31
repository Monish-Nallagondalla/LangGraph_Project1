# 🤖 LangGraph AgenticAI

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.42.0-red.svg)](https://streamlit.io/)
[![LangGraph](https://img.shields.io/badge/LangGraph-latest-green.svg)](https://github.com/langchain-ai/langgraph)

A powerful, modular Agentic AI application built with LangGraph and Streamlit, enabling stateful conversational AI experiences with multiple use cases including basic chatbots, tool-integrated assistants, and AI news summarization.

## 🌟 Features

- **Modular Architecture**: Clean separation of concerns with dedicated modules for graphs, nodes, state management, tools, and UI.
- **Multiple Use Cases**: Support for Basic Chatbot, Chatbot with Tools, and AI News summarization.
- **Stateful Conversations**: Persistent state management using LangGraph's state graph.
- **Tool Integration**: Seamless integration with external tools like Tavily for web search.
- **Streamlit UI**: Intuitive web interface for easy interaction and configuration.
- **Groq LLM Support**: Powered by Groq's fast inference models (Mixtral, Llama3, Gemma).
- **News Summarization**: Automated AI news fetching and summarization with markdown export.
- **Configurable**: Easy configuration through INI files for models, options, and settings.

## 🏗️ Architecture

The project follows a modular architecture:

```
src/langgraphagenticai/
├── graph/
│   └── graph_builder.py      # Graph construction and compilation
├── nodes/
│   ├── basic_chatbot_node.py # Basic chatbot logic
│   ├── chatbot_with_Tool_node.py # Tool-integrated chatbot
│   └── ai_news_node.py       # AI news processing
├── state/
│   └── state.py              # State definitions
├── tools/
│   └── search_tool.py        # Tool definitions (Tavily search)
├── LLMS/
│   └── groqllm.py            # Groq LLM configuration
├── ui/
│   ├── uiconfigfile.ini      # UI configuration
│   ├── uiconfigfile.py       # Config parser
│   └── streamlitui/
│       ├── loadui.py         # Streamlit UI loader
│       └── display_result.py # Result display logic
└── main.py                   # Application entry point
```

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- Groq API Key ([Get one here](https://console.groq.com/keys))
- Tavily API Key ([Get one here](https://app.tavily.com/home)) (for search and news features)

### Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Monish-Nallagondalla/LangGraph_Project1.git
   cd LangGraph_Project1
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up API keys:**
   - Obtain your Groq API key from [console.groq.com](https://console.groq.com/keys)
   - Obtain your Tavily API key from [app.tavily.com](https://app.tavily.com/home)

## 📖 Usage

### Running the Application

1. **Start the Streamlit app:**
   ```bash
   streamlit run app.py
   ```

2. **Access the application:**
   Open your browser and navigate to `http://localhost:8501`

### Configuration

Use the sidebar to configure:

- **LLM Selection**: Choose Groq as the LLM provider
- **Model Selection**: Select from available Groq models (Mixtral-8x7B, Llama3-8B, Llama3-70B, Gemma-7B)
- **API Keys**: Enter your Groq and Tavily API keys
- **Use Case**: Select the desired functionality

## 🎯 Use Cases

### 1. Basic Chatbot
- Simple conversational AI using Groq LLM
- No external tools required
- Ideal for general Q&A and conversation

### 2. Chatbot with Tool
- Enhanced chatbot with web search capabilities
- Uses Tavily for real-time information retrieval
- Supports tool calling for complex queries

### 3. AI News
- Automated AI news fetching and summarization
- Supports daily, weekly, and monthly timeframes
- Generates markdown summaries with source links
- Downloads available for offline viewing

## 🔧 Configuration

The application uses `src/langgraphagenticai/ui/uiconfigfile.ini` for configuration:

```ini
[DEFAULT]
PAGE_TITLE = LangGraph: Build Stateful Agentic AI graph
LLM_OPTIONS = Groq
USECASE_OPTIONS = Basic Chatbot, Chatbot with Tool, AI News
GROQ_MODEL_OPTIONS = mixtral-8x7b-32768, llama3-8b-8192, llama3-70b-8192, gemma-7b-it
```

## 📦 Dependencies

Key dependencies include:

- `langchain` & `langchain_core`: Core LangChain functionality
- `langgraph`: Graph-based AI workflows
- `langchain_groq`: Groq LLM integration
- `langchain_community`: Community tools and integrations
- `streamlit`: Web UI framework
- `tavily-python`: Web search and news API
- `faiss-cpu`: Vector storage (for future extensions)

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [LangGraph](https://github.com/langchain-ai/langgraph) for the graph-based AI framework
- [Groq](https://groq.com/) for fast LLM inference
- [Tavily](https://tavily.com/) for web search capabilities
- [Streamlit](https://streamlit.io/) for the UI framework

## 📞 Support

If you have any questions or need help, please open an issue on GitHub.

---

**Note**: This project is currently in development. Features and APIs may change.
