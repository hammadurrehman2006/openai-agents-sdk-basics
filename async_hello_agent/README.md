# Async Hello Agent

This project demonstrates a basic asynchronous agent using the OpenAI Agents SDK.

## Purpose

The main purpose of this project is to illustrate how to create and run an agent that operates asynchronously, allowing it to handle multiple tasks or I/O operations concurrently without blocking the main thread. This is particularly useful for agents that need to interact with external services or perform long-running operations while remaining responsive.

## Key Features

- **Asynchronous Operation:** The agent is built using `async` and `await` keywords, enabling non-blocking execution.
- **OpenAI Agents SDK:** Utilizes the core functionalities of the OpenAI Agents SDK for agent creation and management.
- **Basic Example:** Provides a simple "hello world" style example to showcase the fundamental structure of an asynchronous agent.

## Setup and Run with `uv`

[uv](https://github.com/astral-sh/uv) is a fast Python package installer and resolver, written in Rust.

1.  **Check for `uv` Installation**:
    Open your terminal and type `uv --version`. If it's installed, you'll see the version number. Otherwise, you need to install it.

2.  **Install `uv`** (if not already installed):
    You can install `uv` using pip, or by following the instructions on the [official `uv` installation guide](https://github.com/astral-sh/uv#installation).
    ```bash
    # Example using pip (ensure pip is available)
    pip install uv
    ```

3.  **Navigate to the Project Directory**:
    ```bash
    cd path/to/async_hello_agent # Replace with the actual path to the project
    ```

4.  **Create a Virtual Environment and Install Dependencies**:
    `uv` will create a virtual environment in the `.venv` directory and install dependencies specified in the `pyproject.toml` file (or `uv.lock` if present).
    ```bash
    uv venv  # Create the virtual environment
    uv sync  # Install dependencies from pyproject.toml
    ```
    If you prefer to activate the virtual environment explicitly before syncing (optional):
    ```bash
    uv venv
    source .venv/bin/activate  # On Linux/macOS
    # For Windows (Command Prompt): .venv\Scripts\activate.bat
    # For Windows (PowerShell): .venv\Scripts\Activate.ps1
    uv sync
    ```

5.  **Run the Agent**:
    Once the dependencies are installed and the virtual environment is active (if you activated it manually), run the agent using `uv`.
    ```bash
    uv run main.py
    ```

Refer to the main repository README for more details on the overall project structure and other related examples.
