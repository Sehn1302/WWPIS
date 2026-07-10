"""
WWPIS — Workplace Wellbeing & Productivity Intelligence System
UNCTAD Economic Data Analysis & Interactive Visualization Dashboard
"""
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(
    page_title="WWPIS — Economic Analytics",
    page_icon="📈",
    layout="wide"
)

@st.cache_data
def load_data():
  """Load and preprocess UNCTAD economic data."""
  try:
    df = pd.read_csv("UNCTAD_DE.csv", low_memory=False)
  except FileNotFoundError:
    st.warning("UNCTAD_DE.csv not found. Using sample data for demonstration.")
    np.random.seed(42)
    years = list(range(1990, 2024))
    df = pd.DataFrame({
      'TIME_PERIOD': np.repeat(years, 50),
      'OBS_VALUE': np.random.normal(100, 30, len(years) * 50) + np.linspace(0, 50, len(years) * 50).repeat(50),
      'INDICATOR_LABEL': np.random.choice(['GDP', 'Trade Balance', 'FDI Inflows', 'Employment Rate'], len(years) * 50)
    })
  df['OBS_VALUE'] = pd.to_numeric(df['OBS_VALUE'], errors='coerce')
  if 'TIME_PERIOD' in df.columns:
    df['TIME_PERIOD'] = pd.to_numeric(df['TIME_PERIOD'], errors='coerce')
  df = df.dropna(subset=['OBS_VALUE'])
  Q1, Q3 = df['OBS_VALUE'].quantile(0.25), df['OBS_VALUE'].quantile(0.75)
  IQR = Q3 - Q1
  df = df[(df['OBS_VALUE'] >= Q1 - 1.5 * IQR) & (df['OBS_VALUE'] <= Q3 + 1.5 * IQR)]
  return df

st.title("📈 WWPIS — Economic Intelligence Dashboard")
st.markdown("**UNCTAD Economic Data Analysis** — Germany | Built by [Sehan Balajee Pilli](https://github.com/Sehn1302)")

with st.sidebar:
  st.header("Controls")
  page = st.radio("Navigate", ["🏠 Overview", "📊 Trends", "📉 Distribution", "🔬 Analysis", "ℹ️ About"])

df = load_data()

if page == "🏠 Overview":
  col1, col2, col3, col4 = st.columns(4)
  col1.metric("Total Records", f"{len(df):,}")
  if 'TIME_PERIOD' in df.columns:
    col2.metric("Year Range", f"{int(df['TIME_PERIOD'].min())}–{int(df['TIME_PERIOD'].max())}")
  col3.metric("Mean Value", f"{df['OBS_VALUE'].mean():.2f}")
  col4.metric("Std Deviation", f"{df['OBS_VALUE'].std():.2f}")
  st.markdown("---")
  st.subheader("Data Preview")
  st.dataframe(df.head(20), use_container_width=True)
  st.subheader("Summary Statistics")
  st.dataframe(df.describe().round(2), use_container_width=True)

elif page == "📊 Trends":
  st.subheader("Economic Indicator Trends Over Time")
  if 'TIME_PERIOD' in df.columns:
    yearly = df.groupby('TIME_PERIOD')['OBS_VALUE'].agg(['mean', 'median', 'std']).reset_index()
    chart_type = st.selectbox("Chart Type", ["Line Chart", "Area Chart", "Bar Chart"])
    if chart_type == "Line Chart":
      st.line_chart(yearly.set_index('TIME_PERIOD')[['mean', 'median']])
    elif chart_type == "Area Chart":
      st.area_chart(yearly.set_index('TIME_PERIOD')['mean'])
    else:
      st.bar_chart(yearly.set_index('TIME_PERIOD')['mean'])
    st.dataframe(yearly.round(2), use_container_width=True)
  else:
    st.info("TIME_PERIOD column not available in current dataset.")

elif page == "📉 Distribution":
  st.subheader("Value Distribution Analysis")
  fig, ax = plt.subplots(figsize=(10, 5))
  ax.hist(df['OBS_VALUE'], bins=50, color='#6c63ff', edgecolor='white', alpha=0.8)
  ax.set_xlabel('OBS_VALUE')
  ax.set_ylabel('Frequency')
  ax.set_title('Distribution of Economic Indicator Values')
  st.pyplot(fig)
  col1, col2 = st.columns(2)
  col1.metric("Skewness", f"{df['OBS_VALUE'].skew():.3f}")
  col2.metric("Kurtosis", f"{df['OBS_VALUE'].kurtosis():.3f}")

elif page == "🔬 Analysis":
  st.subheader("Train-Test Split & Statistical Analysis")
  if 'TIME_PERIOD' in df.columns:
    agg = df.groupby('TIME_PERIOD')['OBS_VALUE'].mean().reset_index()
    X = agg[['TIME_PERIOD']].values
    y = agg['OBS_VALUE'].values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    col1, col2 = st.columns(2)
    col1.metric("Training Samples", len(X_train))
    col2.metric("Testing Samples", len(X_test))
    st.markdown("**Training Set Statistics**")
    st.write(f"Mean: {y_train.mean():.2f} | Std: {y_train.std():.2f}")
    st.markdown("**Test Set Statistics**")
    st.write(f"Mean: {y_test.mean():.2f} | Std: {y_test.std():.2f}")
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.scatter(X_train, y_train, alpha=0.6, label='Train', color='#6c63ff')
    ax.scatter(X_test, y_test, alpha=0.8, label='Test', color='#00d4aa', marker='x')
    ax.set_xlabel('Year')
    ax.set_ylabel('Mean OBS_VALUE')
    ax.legend()
    ax.set_title('Train-Test Split Visualization')
    st.pyplot(fig)

elif page == "ℹ️ About":
  st.markdown("""
  ### WWPIS — Workplace Wellbeing & Productivity Intelligence System
  
  AI-driven insights for workplace wellbeing, burnout detection, and productivity forecasting.
  Built for publishable visualizations and German/EU compliance context.
  
  **Data Source:** UNCTAD (United Nations Conference on Trade and Development)  
  **Focus:** German economic indicators
  
  **Pipeline:**
  1. Data loading & numeric conversion
  2. Null value removal
  3. IQR outlier detection & removal
  4. Exploratory data analysis
  5. Train-test split (80/20, random_state=42)
  6. Interactive visualization
  
  **Tech Stack:** Python · Pandas · Scikit-learn · Matplotlib · Streamlit
  
  **Author:** Sehan Balajee Pilli  
  MSc Business Development & AI · Steinbeis University, Berlin
  
  [GitHub](https://github.com/Sehn1302/WWPIS) · [LinkedIn](https://www.linkedin.com/in/sehanbalajee-771714194/)
  """)
