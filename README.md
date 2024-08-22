# Knowledge Assistant

This is a simple Python-based knowledge assistant that interacts with the OpenAI API to answer user questions. The application runs in a loop, allowing the user to ask multiple questions until they decide to exit.

## Features

- Asks the user to input a question.
- Provides answers using the OpenAI API.
- Allows continuous interaction until the user types 'exit' to quit the application.

## Prerequisites

- Python 3.7 or later
- A valid OpenAI API key

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <repository-url>
cd knowledge-assistant
```

### 2. Create and Activate a Virtual Environment

Create a virtual environment to manage dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install the Dependencies

Install the necessary Python packages using `pip`:

```bash
pip install -r requirements.txt
```

### 4. Set Up Your Environment Variables

Create a `.env` file in the root directory of the project. Use the `.env-example` file as a template and add your key:

```bash
cp .env-example .env
```

### 5. Run the Application

Start the knowledge assistant:

```bash
python3 main.py
```

## Usage

The application will prompt you to enter a question.
Type your question and press Enter to receive an answer.
To quit the application, type exit and press Enter.

## Example Interaction

```
You can type 'exit' to quit at any time.
Hello! I am your knowledge assistant. How can I help you today?
What is the capital of Brazil?
The capital of Brazil is Brasília.

Please enter your next question:
Who is the president of the United States?
The president of the United States is Joe Biden.

Please enter your next question:
exit
Ok, bye!
Exiting the application.
```
