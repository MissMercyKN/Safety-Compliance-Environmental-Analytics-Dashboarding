
import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------------------------------------------------
# Workplace Safety Incident Intelligence Dashboard
# ---------------------------------------------------------
# This application provides interactive HSE analysis using
# workplace incident records. Users can filter incidents,
# review safety KPIs, identify risk patterns, and export data.
# ---------------------------------------------------------


@st.cache_data
def load_data():
    """
    Loads the OSHA safety dataset.

    Caching is used because the dataset does not change during
    dashboard interaction and repeated loading would reduce
    application efficiency.
    """
    df = pd.read_csv("data/OSHA_Safety_Incidents.csv")

    df["Event Date"] = pd.to_datetime(
        df["Event Date"],
        errors="coerce"
    )

    return df


df = load_data()

# -----------------------------
# Dashboard Header
# -----------------------------

st.title("Workplace Safety Incident Intelligence Dashboard")

st.write(
    "Interactive analysis of workplace incidents to identify "
    "safety trends, high-risk areas, and critical events."
)

# -----------------------------
# Data Preparation
# -----------------------------

df["Year"] = df["Event Date"].dt.year
df["Month"] = df["Event Date"].dt.month_name()
df["Day of Week"] = df["Event Date"].dt.day_name()

# Create severity score if severity information exists
if "Severity" in df.columns:
    severity_mapping = {
        "Fatality": 5,
        "Hospitalization": 4,
        "Severe Injury": 3,
        "Injury": 2
    }

    df["Severity Score"] = (
        df["Severity"]
        .map(severity_mapping)
        .fillna(1)
    )
else:
    df["Severity Score"] = 1


# -----------------------------
# Sidebar Filters
# -----------------------------

st.sidebar.header("Dashboard Filters")

filtered_df = df.copy()

if "State" in df.columns:
    locations = st.sidebar.multiselect(
        "Select Location",
        sorted(df["State"].dropna().unique()),
        default=list(df["State"].dropna().unique())
    )

    filtered_df = filtered_df[
        filtered_df["State"].isin(locations)
    ]


date_range = st.sidebar.date_input(
    "Select Date Range",
    [
        df["Event Date"].min(),
        df["Event Date"].max()
    ]
)

if len(date_range) == 2:
    filtered_df = filtered_df[
        (filtered_df["Event Date"] >= pd.to_datetime(date_range[0]))
        &
        (filtered_df["Event Date"] <= pd.to_datetime(date_range[1]))
    ]


if "Incident Type" in df.columns:
    incident_types = st.sidebar.multiselect(
        "Select Incident Type",
        sorted(df["Incident Type"].dropna().unique()),
        default=list(df["Incident Type"].dropna().unique())
    )

    filtered_df = filtered_df[
        filtered_df["Incident Type"].isin(incident_types)
    ]


# -----------------------------
# KPI Metrics
# -----------------------------

total_incidents = len(filtered_df)

average_severity = round(
    filtered_df["Severity Score"].mean(),
    2
)

critical_incidents = len(
    filtered_df[
        filtered_df["Severity Score"] >= 4
    ]
)

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Incidents",
    total_incidents
)

col2.metric(
    "Average Severity",
    average_severity
)

col3.metric(
    "Critical Incidents",
    critical_incidents
)


# -----------------------------
# Safety Alert Logic
# -----------------------------

critical_threshold = 100

if critical_incidents > critical_threshold:
    st.warning(
        "Critical incident levels have exceeded the safety threshold. "
        "Immediate safety review is recommended."
    )


# -----------------------------
# Visualisations
# -----------------------------

st.subheader("Incident Trend Over Time")

trend = (
    filtered_df
    .groupby(filtered_df["Event Date"].dt.to_period("M"))
    .size()
    .reset_index(name="Incidents")
)

trend["Event Date"] = trend["Event Date"].astype(str)

fig_trend = px.line(
    trend,
    x="Event Date",
    y="Incidents",
    markers=True,
    title="Monthly Workplace Incident Trend"
)

st.plotly_chart(fig_trend, use_container_width=True)


if "Incident Type" in filtered_df.columns:

    st.subheader("Incident Type Distribution")

    category = (
        filtered_df["Incident Type"]
        .value_counts()
        .reset_index()
    )

    category.columns = [
        "Incident Type",
        "Count"
    ]

    fig_bar = px.bar(
        category,
        x="Incident Type",
        y="Count",
        title="Incidents by Category"
    )

    st.plotly_chart(fig_bar, use_container_width=True)


# -----------------------------
# Heatmap
# -----------------------------

st.subheader("Incident Heatmap")

heatmap_data = (
    filtered_df
    .groupby(
        [
            "Day of Week",
            "Month"
        ]
    )
    .size()
    .reset_index(name="Incidents")
)

if not heatmap_data.empty:

    fig_heat = px.density_heatmap(
        heatmap_data,
        x="Month",
        y="Day of Week",
        z="Incidents",
        title="Incident Concentration by Day and Month"
    )

    st.plotly_chart(fig_heat, use_container_width=True)


# -----------------------------
# Export Filtered Data
# -----------------------------

st.subheader("Export Data")

csv = filtered_df.to_csv(index=False)

st.download_button(
    label="Download Filtered Safety Data CSV",
    data=csv,
    file_name="filtered_safety_incidents.csv",
    mime="text/csv"
)
