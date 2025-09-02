# Hazard Analyser

**Hazard Analyser** is an AI-powered tool designed to automatically analyze incident reports and generate comprehensive hazard assessments. Leveraging the **Ollama API** with the **LLaMA 3 model** and advanced **prompt engineering**, this tool identifies key elements of industrial hazards and calculates risk metrics to aid decision-making and documentation.

---

## Key Features

- **Automatic Hazard Identification:** Extracts hazardous elements, initiating elements, and pivotal elements from descriptive incident reports.
- **Root Cause & Consequence Analysis:** Determines causes, consequences, and severity of incidents.
- **Risk Assessment:** Computes likelihood of occurrence, residual risk, and severity score for each hazard.
- **Recommendations:** Provides actionable recommendations to mitigate identified risks.
- **Prioritization:** Helps prioritize risks based on severity and likelihood for effective risk management.
- **Documentation:** Generates structured reports that can be directly used for industry documentation.

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

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/hazard_analyser.git
   cd hazard_analyser
