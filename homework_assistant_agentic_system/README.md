# Homework Assistant Agentic System

This project implements a basic agentic system designed to assist with homework tasks, utilizing the OpenAI Agents SDK.

## Purpose

The primary goal of this project is to showcase how multiple agents can collaborate or be orchestrated to solve more complex problems, such as assisting a student with their homework. It demonstrates concepts like task decomposition, agent communication (if applicable in the design), and the integration of different agent capabilities.

## Key Features

- **Agentic System:** Implies the use of one or more agents working together.
- **OpenAI Agents SDK:** Built upon the OpenAI Agents SDK, leveraging its tools for creating and managing agents.
- **Homework Assistance:** The conceptual use-case involves providing support for homework-related queries or tasks. This might include agents specialized in different subjects or problem-solving steps.
- **Modular Design:** (Assumed) The system is likely designed in a modular way to allow for the easy addition or modification of agents and their functionalities.

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
    cd path/to/homework_assistant_agentic_system # Replace with the actual path to the project
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

5.  **Run the Agent System**:
    Once the dependencies are installed and the virtual environment is active (if you activated it manually), run the agent system using `uv`.
    ```bash
    uv run main.py
    ```

Please see the main repository README for an overview of all projects and further context.
