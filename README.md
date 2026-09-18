# MeetScribe-Ai

AI-powered meeting documentation tool that converts meeting transcripts into structured, professional business documentation using Google's Gemini API.

MeetScribe is designed for consultants, business analysts, sales teams, and professionals who need to quickly transform meeting discussions into organized and actionable documentation.

---

## Features

* Convert meeting transcripts into professional business documentation
* Select multiple document types simultaneously
* Add or remove document types before generation
* Generate only the selected documentation
* Copy generated text directly from the application
* Download documentation as a Microsoft Word (`.docx`) file
* Convert Markdown-style `**bold text**` into actual bold formatting in Word
* Automatically name the downloaded Word file using the generated meeting title
* AI-powered transcript analysis using Google Gemini
* Prevents the AI from inventing information not present in the transcript
* Clean and simple Streamlit interface

---

## Supported Documents

MeetScribe can generate the following documentation:

1. **Meeting Notes / SOP**
2. **Minutes of Meeting (MoM)**
3. **Meeting Agenda**
4. **Action Items**
5. **Daily Progress**
6. **Questions & Follow-ups**

Multiple document types can be selected at the same time.

For example, users can select:

```text
Meeting Notes / SOP
Minutes of Meeting (MoM)
Action Items
Questions & Follow-ups
```

and MeetScribe will generate only those selected sections.

---

## How It Works

```text
Meeting Transcript
        │
        ▼
    MeetScribe
        │
        ▼
   Google Gemini
        │
        ▼
Transcript Analysis
        │
        ▼
Selected Documentation
        │
        ├───────────────┐
        ▼               ▼
Copyable Text      Word Document
                        │
                        ▼
              Meeting Title Filename
```

---

## Tech Stack

* **Python**
* **Streamlit** — User interface
* **Google Gemini API** — AI-powered documentation generation
* **Google GenAI SDK** — Gemini API integration
* **python-docx** — Microsoft Word document generation
* **python-dotenv** — Environment variable management

---

## Project Structure

```text
MeetScribe/
│
├── app.py
├── main.py
├── requirements.txt
├── README.md
├── .env
├── .env.example
├── .gitignore
│
└── prompts/
    └── master_prompt.txt
```

### File Description

| File                        | Description                                                                                 |
| --------------------------- | ------------------------------------------------------------------------------------------- |
| `app.py`                    | Streamlit interface, document selection, transcript input, output display and Word download |
| `main.py`                   | Gemini API integration and documentation generation                                         |
| `requirements.txt`          | Python dependencies                                                                         |
| `README.md`                 | Project documentation                                                                       |
| `.env`                      | Local Gemini API key                                                                        |
| `.env.example`              | Example environment configuration                                                           |
| `.gitignore`                | Prevents sensitive and unnecessary files from being committed                               |
| `prompts/master_prompt.txt` | Master prompt used to structure the generated documentation                                 |

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/meetscribe.git
cd meetscribe
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

#### Windows

```powershell
.\venv\Scripts\Activate.ps1
```

#### macOS / Linux

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

If required, the dependencies can also be installed manually:

```bash
pip install streamlit google-genai python-dotenv python-docx
```

---

## Environment Configuration

Create a `.env` file in the project root:

```text
GEMINI_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your Google Gemini API key.

### Important

Never upload your actual `.env` file or API key to GitHub.

The repository includes `.env.example` as a safe reference:

```text
GEMINI_API_KEY=your_api_key_here
```

---

## Running the Application

After activating the virtual environment, run:

```bash
streamlit run app.py
```

The application will open in your browser.

---

## Usage

### Step 1 — Select Documentation

Choose one or multiple document types from the selector.

Selected options can be removed if added by mistake.

### Step 2 — Add Transcript

Paste the meeting transcript into the transcript input field.

### Step 3 — Generate

Click:

**Generate**

MeetScribe sends the selected requirements and transcript to Gemini and generates the requested documentation.

### Step 4 — Review

The generated documentation appears directly in the application as copyable text.

### Step 5 — Download

Click:

**Download Microsoft Word Document**

The output is downloaded as a `.docx` file.

The filename automatically uses the generated meeting title.

For example:

```text
Meeting Title: Zygn ERP Product Demonstration
```

will generate:

```text
Zygn ERP Product Demonstration.docx
```

---

## Word Document Formatting

MeetScribe supports Markdown-style bold formatting.

For example, if the AI generates:

```text
**Meeting Objective**

The objective was to understand the client's requirements.
```

The copyable output retains:

```text
**Meeting Objective**
```

while the downloaded Word document converts it into actual Word formatting:

**Meeting Objective**

The `**` characters are therefore not displayed around bold text inside the Word document.

---

## Documentation Rules

MeetScribe's master prompt is designed to maintain factual accuracy and professional documentation standards.

The AI is instructed to:

* Use only information explicitly available in the transcript
* Never invent names, dates, deadlines, responsibilities, decisions, or facts
* Mark unavailable information as `Not specified`
* Never assume an owner for an action item
* Never create deadlines that were not mentioned
* Distinguish between discussions, decisions, suggestions, questions, and action items
* Remove greetings, filler words, repetition, and irrelevant conversation
* Correct obvious transcription errors when the intended meaning is clear
* Preserve important technical, business, product, and process terminology
* Keep the generated documentation concise and professional
* Produce copy-ready documentation

---

## Example Workflow

### Input

```text
The client discussed their current vendor management process.

They currently maintain vendor information manually.

The client asked whether the system supports WhatsApp integration.

The consultant explained that the platform supports WhatsApp integration.

The client also asked about purchase orders and wanted more clarification on the workflow.

The team agreed to discuss the purchase order workflow in the next meeting.
```

### Generated Documentation

```text
MEETING NOTES / SOP

Meeting Objective:
Understand the client's current vendor management process and discuss relevant system capabilities.

Key Discussion Points:
- Current vendor management process
- WhatsApp integration
- Purchase order workflow

Questions / Doubts:
- WhatsApp integration capabilities
- Purchase order workflow

Next Steps:
- Discuss the purchase order workflow in the next meeting.
```

The exact output varies depending on the transcript and document types selected.

---

## Security

MeetScribe uses environment variables to store the Gemini API key.

The `.gitignore` file prevents `.env` and other local files from being committed.

Never commit:

```text
.env
venv/
__pycache__/
*.pyc
```

---

## Future Improvements

Potential future enhancements include:

* Meeting transcript file upload
* PDF export
* Improved Word document formatting
* Meeting history
* Multiple meeting management
* Speaker identification
* Automatic transcript processing
* CRM integration
* Meeting platform integrations
* Cloud deployment
* Automated email delivery of meeting documentation

---

## Author

**Krish Gupta**

BCA | Data Analytics | AI | Python | SQL | Power BI

---

## License

This project is intended for educational, portfolio, and professional development purposes.

