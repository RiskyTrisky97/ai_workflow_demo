# AI Workflow Demo

This repository demonstrates a simple AI-assisted workflow simulation created by **Tristan Becker**, Co-Founder & Head of Systems & Client Implementation at **Chief AI Advisors**.

## Overview
The project simulates a compliance-first workflow for document-intensive or client-facing processes. It emphasizes:

- Structured execution
- Auditability and accountability
- Human oversight in AI-assisted systems
- Step-by-step process visibility

## Usage
1. Clone this repository:
```bash
git clone https://github.com/RiskyTrisky97/ai_workflow_demo.git

# Copy this into the editor
"""
AI Workflow Demo
Simulates a simple compliance-first workflow for document or client task tracking.

Author: Tristan Becker
Company: Chief AI Advisors
"""

# Sample workflow steps
workflow_steps = [
    "Receive client data",
    "Validate data completeness",
    "Log into CRM",
    "Upload documents",
    "Run automated quality checks",
    "Notify team of completion",
]

def run_workflow(steps):
    print("Starting AI-assisted workflow simulation...\n")
    for i, step in enumerate(steps, start=1):
        print(f"Step {i}: {step} ✅")
    print("\nWorkflow simulation complete. All steps executed with oversight.")

if __name__ == "__main__":
    run_workflow(workflow_steps)
