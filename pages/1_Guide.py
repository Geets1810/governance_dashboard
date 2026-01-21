import streamlit as st

st.set_page_config(
    page_title="Model Governance Guide",
    layout="centered"
)

st.title("📘 Model Governance Dashboard — Guide")

st.markdown("""
### What Is Model Governance?

Model governance ensures analytical/Statistical and AI/machine learning models remain accurate,
compliant, and appropriately reviewed throughout their lifecycle.

In companies like Fannie Mae and Freddie Mac these compliance rules have to be in alignment with Federal
standards (FHFA) to ensure all results produced, all decisions made based on the data are consistent over time.

In large organizations, governance teams oversee hundreds of models across domains
such as credit risk, forecasting, and fraud detection. The goal is **early risk
detection**, not post-failure analysis.
""")

st.markdown("""
### Purpose of This Dashboard

This dashboard is designed as a **decision-support tool** for governance and risk leaders to monitor compliance.

It helps answer three core questions:
1. Where is governance risk concentrating?
2. Which models require immediate attention?
3. Are monitoring and review processes keeping pace with model aging?
4. Are these reviews, issues assesing the risk before being closed?
5. Is evidence being provided, evaluated before activating the model again?
""")

st.markdown("""
### How to Read the Dashboard

**Overdue Review Trend**
Tracks models whose scheduled reviews are overdue. Rising trends suggest
governance capacity strain. (simulated data for 2025 may not work for other dates)

**Open vs Closed Reviews**
Compares review inflow versus completion. Persistent gaps indicate backlog
accumulation.(simulated data for 2025 may not work for other dates)

**Performance and Risk Views**
These should be interpreted together. Governance risk typically emerges when
performance degradation overlaps with delayed lifecycle actions.
This provide the details for models that are up for review, is this review overdue. If yes, ideally lead validator is alerted and review is escalated from top down.
If Validators are not assigned and the Model is overdue this also raises an alarm triggering series of next steps for Model Owner
and based on the risk tier the status is updated to inactive.
Once a Model is marked inactive the results produced from the model cannot be used for any decisions, analysis.
""")

st.markdown("""
### About the Data

The data used in this dashboard is **synthetic and anonymized**, created to simulate
real-world governance patterns rather than represent production metrics.

**Limitations**
- Absolute values are illustrative
- Regulatory thresholds are generalized
- Trends demonstrate structural behavior, not historical events
""")

st.markdown("""
*This dashboard reflects how governance teams reason about model risk, not the
reporting of any specific institution.*
""")
