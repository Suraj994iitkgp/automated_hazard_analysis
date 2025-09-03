# Automated Hazard Analyser Chatbot

**Hazard Analyser** is an AI-powered web tool for automatic hazard analysis of industrial incident reports, powered by a custom implementation of the LLaMA 3 model served locally via Ollama and sophisticated prompt engineering. It delivers detailed, structured risk assessments and documentation-ready reports directly through a chat interface. Additionally, for each of the query the results from the chatbot is stored automatically in a tabular format as .csv in the excel file for futher use cases.

---

## Key Features

- **Automatic Hazard Identification:** Extracts hazardous elements, initiating elements, and pivotal elements from descriptive incident reports.
- **Root Cause & Consequence Analysis:** Determines causes, consequences, and severity of incidents.
- **Risk Assessment:** Computes likelihood of occurrence, residual risk, and severity score for each hazard.
- **Recommendations:** Provides actionable recommendations to mitigate identified risks.
- **Prioritization:** Helps prioritize risks based on severity and likelihood for effective risk management.
- **Documentation:** Generates structured reports that can be directly used for industry documentation.

---

## Architecture & Technologies Used

Backend: Python 3, FastAPI (for web API and HTML/Jinja2 templating)

AI Model Serving: Ollama with LLaMA 3 (local large language model inference)

Prompt Engineering: Custom system prompts optimized for process safety risk analysis

Frontend: HTML/CSS, Jinja2 (dynamic server-side rendering)

Storage/Export: Results are persisted/exported to CSV for compliance and record-keeping

---

## How It Works

1. **Input:** User provides a descriptive incident report.
2. **Processing:** 
   - Ollama API uses **LLaMA 3** for natural language understanding.
   - Prompt engineering guides the model to extract specific elements like hazards, causes, consequences, and risk metrics.
3. **Output:** 
   - Hazardous elements, initiating and pivotal elements.
   - Causes, consequences, severity scores, likelihood, and residual risk.
   - Recommendations for risk mitigation.
4. **Reporting:** Generates structured output suitable for documentation, analysis, and decision-making.

---

## Use Cases

- Industrial risk assessment and management.
- Automated incident reporting and documentation.
- Prioritization of risks for safety planning.
- Prediction of potential hazards and preventive actions.

---

Example:
#from hazard_analyser import HazardAnalyser

# Initialize the analyser
#analyser = HazardAnalyser(api_key="YOUR_OLLAMA_API_KEY")

# Input a descriptive incident report
#report = """
#During routine maintenance, a worker slipped due to oil spillage on the floor, causing a minor injury.
"""

# Extract hazard analysis
#analysis = analyser.analyze(report)

#print(analysis)

Sample Output: 
#{
  "hazardous_element": "Oil spillage",
  "initiating_element": "Worker slipped",
  "pivotal_element": "Slippery floor",
  "causes": "Poor housekeeping, lack of signage",
  "consequences": "Minor injury to worker",
  "severity_score": 3,
  "likelihood_of_occurrence": 4,
  "residual_risk": 12,
  "recommendations": [
    "Clean oil spillage immediately",
    "Place warning signs",
    "Conduct regular floor inspections"
  ]
}#


## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/hazard_analyser.git
   cd hazard_analyser

## Project structure:

hazard_analyzer.py        # Handles AI analysis and CSV export
mainchat.py               # FastAPI app with chat endpoints
templates/chat.html       # Chat UI (Jinja2 rendered)
static/style.css          # Web styling
requirements.txt          # Dependencies
hazard_results.csv        # Output (auto-generated)

