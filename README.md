[![MseeP.ai Security Assessment Badge](https://mseep.net/pr/pride-archive-mcp-pride-archive-search-badge.png)](https://mseep.ai/app/pride-archive-mcp-pride-archive-search)

# 🧬 MCP PRIDE Archive Search Server

This project implements a **Model Context Protocol (MCP)**-compliant API server that exposes tools to search the [PRIDE Archive](https://www.ebi.ac.uk/pride/), a major repository for proteomics data. It allows AI models (such as Claude or other MCP-compatible LLMs) to interact with proteomics datasets programmatically using structured function calling.

---

## 🚀 Features

- ✅ MCP Server powered by `FastMCP`
- 🔍 PRIDE Archive Search Tool to query datasets by keyword, submission date, popularity, etc.
- 🤖 AI-friendly tools for biomedical and proteomics-related research
- ⚡ Supports both `http` (SSE) and `stdio` connection modes
- 🛠️ Easily extendable with additional tools

---

## 📦 Installation

Clone the repo and install dependencies:

```bash
git clone https://github.com/PRIDE-Archive/mcp_pride_archive_search.git
cd mcp_pride_archive_search
poetry install  # or pip install -r requirements.txt
```

## 👨‍💻 Usage

Start the MCP server with your preferred connection type (http or stdio):

```bash
python -m mcp_pride_archive_search --connection_type http --port 9999
```

Command-line Arguments

| Argument	          | Description	                        | Default |
|--------------------| -------------------------------------	|-----|
| --connection_type  |Type of connection: http or stdio      | 	http |
| --port	            |Port to run the server (for HTTP mode)	| 9999 |

## 🔧 Tool APIs
### search_archive_tool(...)

Fetches proteomics datasets from the PRIDE Archive database.

**Use this when:**
-  Searching for proteomics research data
- Mass spectrometry dataset queries
- Biomedical dataset exploration (e.g., cancer-related)
- Finding popular or specific proteomics projects


##  🤝 Integration with LLMs

This server works with any LLM that supports Model Context Protocol, including:

- Anthropic Claude
- Google Gemini
- Open-source MCP clients 
-   Custom RAG pipelines

## 🧠 Architecture Overview

```sql
+---------------------+       Tool Calls        +-----------------------------+
|  Claude / Gemini AI |  <--------------------> | MCP PRIDE API Server        |
+---------------------+                         | - search_archive_tool()     |
                                                | - server_status()           |
                                                +-----------------------------+
                                                           |
                                                           v
                                              +---------------------------+
                                              | PRIDE Archive REST API    |
                                              | (https://www.ebi.ac.uk    |
                                              |   /pride/ws/archive/      |
                                              |  v3/search/projects)      |
                                              +---------------------------+
```

## 📝 License

MIT License. See LICENSE for details.