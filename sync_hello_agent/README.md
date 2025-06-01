# Sync Hello Agent

This project demonstrates a basic synchronous agent using the OpenAI Agents SDK.

## Purpose

The main purpose of this project is to provide a clear and simple example of how to create and run an agent that operates synchronously. In a synchronous model, tasks are executed sequentially, and the agent will wait for each operation to complete before moving on to the next. This is often simpler to understand and implement for basic agents that do not require concurrent processing.

## Key Features

- **Synchronous Operation:** The agent performs operations one at a time, in a blocking manner.
- **OpenAI Agents SDK:** Utilizes the core functionalities of the OpenAI Agents SDK for agent creation and management.
- **Basic Example:** Offers a straightforward "hello world" type example to illustrate the fundamental structure of a synchronous agent.

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
    cd path/to/sync_hello_agent # Replace with the actual path to the project
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

For more information on the overall repository structure and other examples, please refer to the main README file.
