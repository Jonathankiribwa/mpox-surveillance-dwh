import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from PIL import Image
import datetime

# --- Page Configuration ---
st.set_page_config(
    page_title="SeDW - Exanthem Surveillance Uganda",
    page_icon="🌍",
    layout="wide"
)

# --- Mock Semantic Backend Logic ---
def get_semantic_trust_score(metadata):
    """Simulates the Epistemic Trust Module (Layer 1 & 5)"""
    score = 0.5
    if metadata['location_verified']: score += 0.2
    if metadata['clinical_context']: score += 0.2
    if metadata['observer_role'] == "Health Worker": score += 0.1
    return min(score, 1.0)

# --- UI Header ---
st.title("🛡️ Semantic-Aware Data Warehouse (SeDW)")
st.subheader("Community-Based Surveillance for Exanthems in Uganda")

# --- Sidebar Navigation ---
page = st.sidebar.radio("Navigation", ["Surveillance Dashboard", "Live Data Capture", "Knowledge Graph View"])

# --- PAGE 1: Surveillance Dashboard ---
if page == "Surveillance Dashboard":
    st.markdown("### 📊 Epidemiological Intelligence")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Observations", "1,284", "+12% week")
    col2.metric("High-Trust Alerts", "42", "Action Required")
    col3.metric("OOD Robustness", "94.2%", "Model Confidence")

    # Mock Data for Chart
    chart_data = pd.DataFrame({
        'Date': pd.date_range(start='2026-03-01', periods=10),
        'Mpox': [5, 8, 12, 10, 15, 20, 18, 25, 30, 28],
        'Chickenpox': [20, 18, 22, 25, 15, 12, 10, 8, 5, 7]
    })
    fig = px.line(chart_data, x='Date', y=['Mpox', 'Chickenpox'], title="Trend Analysis: Confirmed Semantic Cases")
    st.plotly_chart(fig, use_container_width=True)

# --- PAGE 2: Live Data Capture (The "Citizen Science" Ingestion Layer) ---
elif page == "Live Data Capture":
    st.markdown("### 📸 Live Ingestion Layer")
    st.info("Ingesting multimodal data for semantic annotation (Layer 3 & 6).")

    with st.expander("Capture Image or Upload", expanded=True):
        source = st.radio("Choose Input Type:", ["Camera Capture", "File Upload"])
        img_file = None
        
        if source == "Camera Capture":
            img_file = st.camera_input("Scan Exanthem")
        else:
            img_file = st.file_uploader("Upload Image", type=['jpg', 'png', 'jpeg'])

    if img_file:
        st.success("Image successfully ingested into the buffer.")
        
        # Metadata Form (Ontology Enrichment)
        st.markdown("#### 📝 Clinical Context (Ontology Mapping)")
        col_a, col_b = st.columns(2)
        with col_a:
            role = st.selectbox("Observer Role", ["Citizen Scientist", "Community Health Worker", "Clinician"])
            symptoms = st.multiselect("Associated Signs", ["Fever", "Lymphadenopathy", "Headache", "Fatigue"])
        with col_b:
            location = st.text_input("Region/District", value="Kampala Central")
            duration = st.slider("Duration of Rash (Days)", 1, 21, 3)

        if st.button("Submit to SeDW Pipeline"):
            # Simulate the 8-Layer Process
            with st.status("Processing through 8-Layer Locator Framework...", expanded=True):
                st.write("L3: Ingesting Multimodal Data...")
                st.write("L7: Executing CNN Classification (MobileNetV2)...")
                st.write("L2: Mapping to ExanthemObservation Ontology...")
                
                # Semantic logic result
                trust = get_semantic_trust_score({
                    'location_verified': True,
                    'clinical_context': len(symptoms) > 0,
                    'observer_role': role
                })
                
                st.write(f"L5: Calculated Epistemic Trust Score: **{trust}**")
            
            st.success("Data successfully stored in the Knowledge Graph.")
            st.balloons()

# --- PAGE 3: Knowledge Graph View ---
elif page == "Knowledge Graph View":
    st.markdown("### 🕸️ Semantic Retrieval (SPARQL Results)")
    st.code("""
    PREFIX ex: <http://exanthem.org/ontology#>
    SELECT ?observation ?trust ?diagnosis
    WHERE {
        ?observation ex:hasTrustScore ?trust .
        ?observation ex:hasDiagnosis ?diagnosis .
        FILTER (?trust > 0.8)
    }
    """, language="sql")
    
    # Mock Results Table
    results = pd.DataFrame({
        "Observation ID": ["Obs_UG_001", "Obs_UG_004", "Obs_UG_012"],
        "Timestamp": ["2026-03-28", "2026-03-29", "2026-03-30"],
        "Trust Score": [0.92, 0.88, 0.95],
        "Classification": ["Mpox", "Mpox", "Varicella"]
    })
    st.table(results)