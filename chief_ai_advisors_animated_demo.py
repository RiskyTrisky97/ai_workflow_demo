"""
Chief AI Advisors Animated Demo
Fun and professional simulation of AI-assisted workflows and services.
Author: Tristan Becker
Company: Chief AI Advisors
Website: https://chiefaiadvisors.com
Phone: +1 (555) 123-4567
Toll-Free: +1-833-313-7714
Email: chiefaiadvisors@gmail.com
"""
import time
import os

# ----------------------
# ASCII Animation Frames
# ----------------------

# Phase 1: Character builds up (body stays visible throughout)
build_frames = [
r"""
   (•_•)
   |    |
   /    \
""",
r"""
   (•_•)
   <)   )╯
   /    \
""",
r"""
   (•_•)
  ⌐■-■)
   <)   )╯
   /    \
""",
r"""
   (⌐■_■)
   <)   )╯
   /    \

   Ready for AI workflow!
""",
]

# Phase 2: Finger gun poses — body always present, one arm pointing
finger_gun_messages = [
    ("🚀 Launching AI solutions...",        r"""
   (⌐■_■)
   <)   )╯ 
   /    \
"""),
    ("📊 Data Analytics & Insights",         r"""
   (⌐■_■)
    /)  )>
   /    \
"""),
    ("⚖  Compliance & Reporting",            r"""
   (⌐■_■)
   <)   )╯ 
   /    \
"""),
    ("🌐 SEO & AEO Optimization",            r"""
   (⌐■_■)
    /)  )>
   /    \
"""),
    ("🤖 Custom AI Tools & Automation",      r"""
   (⌐■_■)
   <)   )╯ 
   /    \
"""),
    ("✅ Chief AI Advisors at work!",         r"""
   (⌐■_■)
    /)  )>
   /    \
"""),
]

# ----------------------
# Workflow Steps
# ----------------------
workflow_steps = [
    "Receive client data",
    "Validate data completeness",
    "Log into CRM",
    "Upload documents",
    "Run automated quality checks",
    "Notify team of completion",
    "Archive workflow log",
    "Send final report to stakeholders",
]

# ----------------------
# Helper Functions
# ----------------------
def clear():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def pause(prompt="Press Enter to continue..."):
    """Pause and wait for the user to press Enter."""
    input(f"\n{prompt}")

def animate_build(frames, delay=0.75):
    """Show the character building up frame by frame."""
    for frame in frames:
        clear()
        print("\n" + frame)
        time.sleep(delay)

def animate_finger_guns(gun_frames, delay=1.0):
    """Show the character doing finger guns with each service message."""
    for message, pose in gun_frames:
        clear()
        print("\n" + pose)
        print(f"   {message}")
        time.sleep(delay)

def run_workflow(steps):
    """Run the workflow step-by-step with simulated progress."""
    clear()
    print("\n" + "="*50)
    print("   🤖 AI-Assisted Workflow Simulation")
    print("="*50 + "\n")
    print("Starting AI-assisted workflow simulation...\n")
    for i, step in enumerate(steps, start=1):
        time.sleep(0.7)
        print(f"  Step {i}/{len(steps)}: {step} ✅")
    print("\n" + "-"*50)
    print("  All workflow steps executed with oversight.")
    print("-"*50 + "\n")
    pause("Press Enter to see the workflow summary...")

def summary(steps):
    """Print a summary of completed workflow steps."""
    clear()
    print("\n" + "="*50)
    print("   📋 Workflow Summary")
    print("="*50 + "\n")
    for i, step in enumerate(steps, start=1):
        print(f"  {i}. {step} ✔")
    print("\n" + "-"*50)
    print(f"  Total steps : {len(steps)}")
    print(f"  Status      : All completed successfully ✅")
    print("-"*50 + "\n")
    pause("Press Enter to view our services...")

def display_services():
    """Display all services offered by Chief AI Advisors."""
    clear()
    print("\n" + "="*55)
    print("   🌟  Chief AI Advisors — Our Services  🌟")
    print("="*55 + "\n")

    services = [
        ("🤖", "Custom AI Tools & Automation"),
        ("📊", "Data Analytics & Insights"),
        ("⚖ ", "Compliance & Reporting"),
        ("🌐", "SEO & AEO Optimization"),
        ("💼", "Workflow Optimization & Client Solutions"),
        ("🛠 ", "IT & AI Integrations"),
        ("📈", "Business Intelligence & Strategy"),
        ("🔒", "Data Security & Privacy Management"),
    ]

    for icon, service in services:
        print(f"  {icon}  {service}")
        time.sleep(0.4)

    print("\n" + "-"*55)
    print("  🌐  https://chiefaiadvisors.com")
    print("  📞  +1 (555) 123-4567  |  Toll-Free: +1-833-313-7714")
    print("  📧  chiefaiadvisors@gmail.com")
    print("-"*55 + "\n")
    pause("Press Enter to exit...")

# ----------------------
# Main Execution
# ----------------------
if __name__ == "__main__":
    # Step 1: Build up the character
    animate_build(build_frames, delay=0.75)

    # Step 2: Finger gun poses for each service/message
    animate_finger_guns(finger_gun_messages, delay=1.1)

    # Hold on the final pose before moving on
    clear()
    print(r"""
   (⌐■_■)
    /)  )>
   /    \

   💼 Chief AI Advisors — Let's get to work!
""")
    pause("Press Enter to start the workflow simulation...")

    # Step 3: Workflow simulation
    run_workflow(workflow_steps)

    # Step 4: Summary
    summary(workflow_steps)

    # Step 5: Services display (stays until Enter)
    display_services()

    # Exit message
    clear()
    print("\n🚀 AI workflow mode activated!")
    print("   Tristan Becker | Chief AI Advisors")
    print("   🌐 https://chiefaiadvisors.com")
    print("   📞 +1 (555) 123-4567  |  Toll-Free: +1-833-313-7714")
    print("   📧 chiefaiadvisors@gmail.com\n")
