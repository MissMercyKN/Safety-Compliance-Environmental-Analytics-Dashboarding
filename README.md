Workplace Safety Incident Intelligence Dashboard

Project Overview

The Workplace Safety Incident Intelligence Dashboard is an interactive Health, Safety, and Environment (HSE) analytics application developed using OSHA workplace incident data.

The purpose of the dashboard is to transform workplace incident records into meaningful safety insights. It helps safety teams identify incident patterns, monitor severity levels, recognise high-risk areas, and support preventive safety decisions.

The dashboard is developed using Python and Streamlit and provides interactive filtering, visual analysis, safety alerts, and data export functionality.

Business Problem

Organisations collect large amounts of workplace safety information, but reviewing raw incident records manually makes it difficult to identify trends and emerging risks.

This project addresses that challenge by creating a visual safety monitoring tool that allows users to:

Track workplace incident trends over time

Identify frequent incident categories

Analyse locations with higher incident occurrence

Monitor critical safety events

Support faster safety intervention decisions

Dataset Description

The project uses the OSHA Severe Injury Reports dataset.

The dataset contains workplace incident records including information such as:

Incident date

Workplace location

Incident category

Injury outcomes

Severity indicators

Company and industry information

The dataset was selected because it provides realistic workplace safety information and supports the required HSE dashboard functions.

Project Objectives

The main objectives are:

Develop an interactive safety incident dashboard.

Analyse workplace incident patterns.

Provide key safety performance indicators.

Identify critical safety risks through automated alerts.

Allow users to export filtered safety records.

Dashboard Features

Interactive Filters

Users can filter safety incidents using:

Location/site

Date range

Incident type

All dashboard charts and metrics update dynamically based on selected filters.

Key Performance Indicators

The dashboard displays:

Total Incidents

Shows the total number of workplace incidents included in the selected filter range.

Average Severity

Provides an overall indication of incident seriousness.

Critical Incidents

Highlights incidents requiring immediate safety attention.

Visualisations

Incident Trend Analysis

A time-series chart displays incident patterns over time and helps identify increases or decreases in safety events.

Incident Category Analysis

A categorical chart shows which incident types occur most frequently.

Safety Heatmap

A heatmap identifies periods with higher incident concentration using time-based patterns such as day and month.

Safety Alert Logic

The dashboard includes automated warning logic.

When the number of critical incidents exceeds a predefined threshold, the application displays a warning message recommending safety review and corrective action.

Data Export

Users can download filtered incident records as a CSV file for further analysis or reporting.

Technical Implementation

Programming Language

Python

Main Libraries

Pandas: Data cleaning and analysis

Plotly: Interactive visualisation

Streamlit: Dashboard development

NumPy: Data processing support

Project Structure

HSE_Safety_Dashboard_Project/

│
├── data/
│   └── OSHA_Safety_Incidents.csv
│
├── notebooks/
│   └── HSE_Safety_Dashboard_Project.ipynb
│
├── app/
│   └── app_safety_dashboard.py
│
├── reports/
│   └── Week7_Safety_Alert_Name.pdf
│
├── README.md
│
└── requirements.txt

Installation Instructions

Clone the repository:

git clone <repository-link>

Navigate to the project folder:

cd HSE_Safety_Dashboard_Project

Install required packages:

pip install -r requirements.txt

Running the Streamlit Dashboard

Run the application using:

streamlit run app_safety_dashboard.py

The dashboard will open in the browser.

Dashboard Design Decisions

The dashboard was designed around practical HSE management needs.

The main design decisions include:

Using interactive filters to allow targeted safety investigations.

Using KPI indicators to provide rapid safety status checks.

Using trend analysis to identify changing risk patterns.

Using automated alerts to highlight critical conditions.

Providing data export functionality for additional reporting.

Safety Alert Development

The safety alert document converts dashboard findings into workplace communication.

The alert focuses on:

Identified safety concern

Risk impact

Immediate corrective actions

Employee responsibilities

Contact information

This ensures analytical findings can be translated into practical safety improvements.

Future Improvements

Future versions of the dashboard could include:

Real-time incident reporting integration

Predictive safety risk modelling

Geographic incident mapping

Employee safety behaviour analysis

Integration with organisational HSE management systems

Author

HSE Safety Analytics Project
