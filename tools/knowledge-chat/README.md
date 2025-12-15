# AMODIT Knowledge Chat

An agentic chat application that navigates the project's file system to answer questions.

## Setup

1.  **Install dependencies**:
    ```bash
    npm install
    ```

2.  **Configure Environment**:
    Create a `.env.local` file in this directory:
    ```bash
    cp .env.example .env.local
    ```
    
    **For Azure OpenAI** (recommended if you have Azure subscription):
    ```env
    LLM_PROVIDER=openai
    AZURE_OPENAI_API_KEY=your-azure-api-key
    AZURE_OPENAI_ENDPOINT=https://your-resource-name.openai.azure.com
    AZURE_OPENAI_DEPLOYMENT_NAME=your-deployment-name
    AZURE_OPENAI_API_VERSION=2024-02-15-preview
    KNOWLEDGE_BASE_PATH=/path/to/your/knowledge/base
    ```
    
    **For Standard OpenAI**:
    ```env
    LLM_PROVIDER=openai
    OPENAI_API_KEY=sk-...
    KNOWLEDGE_BASE_PATH=/path/to/your/knowledge/base
    ```
    
    **For other providers** (Anthropic/Google):
    ```env
    LLM_PROVIDER=anthropic # or 'google'
    ANTHROPIC_API_KEY=sk-ant-...
    # or GOOGLE_GENERATIVE_AI_API_KEY=...
    KNOWLEDGE_BASE_PATH=/path/to/your/knowledge/base
    ```

3.  **Run Development Server**:
    ```bash
    npm run dev
    ```
    Open [http://localhost:3000](http://localhost:3000).

## Architecture

-   **Frontend**: Next.js App Router, TailwindCSS, Vercel AI SDK (UseChat).
-   **Backend**: `app/api/chat/route.ts` using Vercel AI SDK Core.
-   **Navigation**: The agent uses `list_files` and `read_file` tools to explore from the repository root, starting with `GEMINI.md`.

## Features

-   **Model Agnostic**: Switch between GPT-4o, Claude 3.5 Sonnet, and Gemini 1.5 Pro easily.
-   **Agentic Traversal**: No vector database. The AI reads files like a human developer.
-   **Secure**: File access is limited to the repository root.
