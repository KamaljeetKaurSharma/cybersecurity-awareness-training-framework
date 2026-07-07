#!/usr/bin/env python3
"""
Phishing Simulation Tracker
Demonstrates basic security automation for tracking enterprise cybersecurity awareness metrics.
"""

import json
from datetime import datetime

# Simulated database of company departments
departments = ["Engineering", "HR", "Finance", "Sales", "Operations"]

def log_simulation_event(employee_id, department, action):
    """
    Logs a simulated phishing click event to assess high-risk units.
    """
    if department not in departments:
        print(f"Error: Department '{department}' not recognized.")
        return None

    event = {
        "timestamp": datetime.now().isoformat(),
        "employee_id": employee_id,
        "department": department,
        "action_taken": action, # e.g., "Ignored", "Reported", "Clicked"
        "risk_score_impact": 10 if action == "Clicked" else 0
    }
    
    print(f"[SECURITY ALERT] Event logged for Dept: {department} | Action: {action}")
    return event

if __name__ == "__main__":
    print("Initializing Phishing Simulation Analysis Engine...\n")
    
    # Simulate data logging
    log1 = log_simulation_event("EMP104", "Finance", "Clicked")
    log2 = log_simulation_event("EMP202", "Engineering", "Reported")
    
    # Save log snippet to a dummy file to demonstrate file handling
    with open("sim_results.json", "w") as f:
        json.dump([log1, log2], f, indent=4)
