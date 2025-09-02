import csv
import json
import os
from ollama import Client

client = Client()

# Severity scale mapping
SEVERITY_MAP = {
    "low": 2,
    "medium": 3,
    "high": 5
}

def analyze_hazard(description: str):
    """Send hazard description to Llama 3 and get structured analysis."""
    system_prompt = """
    You are a process safety hazard analysis assistant.
    Analyze hazards using frameworks like HAZOP, FMEA, ISO 31000.
    Respond strictly in JSON format with these fields:

    {
      "Hazard Description": "...",
      "Causes": ["...", "..."],
      "Consequences": ["...", "..."],
      "Likelihood": "Low/Medium/High",
      "Severity": "Low/Medium/High",
      "Mitigation / Control Measures": ["...", "..."],
      "Residual Risk": "Textual assessment",
      "Scientific Backing": "Which framework/guideline used",
      "Hazardous Element": "...",
      "Initiating Element": "...",
      "Pivotal Element": "..."
    }
    """

    response = client.chat(
        model="llama3",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": description}
        ]
    )

    return response['message']['content']


def save_results_to_csv(result: str, output_file="hazard_results.csv"):
    """Parse JSON-like response and save into CSV."""

    try:
        data = json.loads(result)
    except json.JSONDecodeError:
        print("⚠️ Model response not valid JSON. Saving raw text only.")
        data = {"Hazard Description": result}

    # Add severity score
    severity_label = data.get("Severity", "").lower()
    data["Severity Score"] = SEVERITY_MAP.get(severity_label, 0)

    # Ensure lists are saved as strings
    for key in ["Causes", "Consequences", "Mitigation / Control Measures"]:
        if isinstance(data.get(key), list):
            data[key] = "; ".join(data[key])

    # Define consistent CSV headers
    fieldnames = [
        "Hazard Description",
        "Causes",
        "Consequences",
        "Likelihood",
        "Severity",
        "Mitigation / Control Measures",
        "Residual Risk",
        "Scientific Backing",
        "Hazardous Element",
        "Initiating Element",
        "Pivotal Element",
        "Severity Score"
    ]

    file_exists = os.path.exists(output_file)

    with open(output_file, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        row = {key: data.get(key, "") for key in fieldnames}
        writer.writerow(row)

    abs_path = os.path.abspath(output_file)
    print(f"✅ Result saved to {abs_path}")


if __name__ == "__main__":
    user_input = input("Enter a hazard description: ")
    model_response = analyze_hazard(user_input)
    print("\n--- Model Response ---")
    print(model_response)
    save_results_to_csv(model_response)
