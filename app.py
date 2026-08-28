import streamlit as st
import pandas as pd
import os
from datetime import datetime

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="PUJA DJ KING | Management",
    page_icon="🎧",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- PREMIUM STYLING (CSS) ---
st.markdown("""
    <style>
    /* Main Background & Text */
    .stApp {
        background-color: #0b0f19;
        color: #f3f4f6;
    }
    
    /* Header Card Style */
    .header-card {
        background: linear-gradient(135deg, #1f2937 0%, #111827 100%);
        padding: 25px;
        border-radius: 16px;
        border: 1px solid #374151;
        text-align: center;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.5);
        margin-bottom: 25px;
    }
    .header-title {
        color: #f59e0b;
        font-size: 2.2rem;
        font-weight: 800;
        letter-spacing: 1px;
        margin-bottom: 5px;
    }
    .header-subtitle {
        color: #9ca3af;
        font-size: 1rem;
        font-weight: 500;
    }

    /* Section Headers */
    h2, h3 {
        color: #f3f4f6 !important;
        font-weight: 700 !important;
    }

    /* Form & Input Fields Container */
    div.stForm {
        background-color: #111827;
        padding: 20px;
        border-radius: 14px;
        border: 1px solid #374151;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }

    /* Buttons Styling */
    .stButton > button {
        background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
        color: #0b0f19;
        font-weight: 700;
        border-radius: 10px;
        border: none;
        padding: 0.6rem 1.2rem;
        width: 100%;
        box-shadow: 0 4px 12px rgba(245, 158, 11, 0.3);
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        background: linear-gradient(135deg, #fbbf24 0%, #f59e0b 100%);
        box-shadow: 0 6px 16px rgba(245, 158, 11, 0.5);
        color: #000000;
    }

    /* Sidebar Styling & Professional Menu Look */
    section[data-testid="stSidebar"] {
        background-color: #030712;
        border-right: 1px solid #1f2937;
        padding-top: 20px;
    }
    section[data-testid="stSidebar"] .stMarkdown {
        color: #e5e7eb;
    }
    
    /* Custom Sidebar Radio Menu Styling */
    .stRadio div[role="radiogroup"] {
        background-color: #111827;
        padding: 10px;
        border-radius: 12px;
        border: 1px solid #374151;
    }
    .stRadio label {
        font-weight: 600 !important;
        color: #f3f4f6 !important;
        padding: 5px 0;
    }

    /* Dataframe Table Look */
    dataframe, table {
        border-radius: 10px !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- LOGIN SYSTEM ---
def check_login():
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False

    if not st.session_state.authenticated:
        st.markdown("""
            <div style="max-width: 420px; margin: 50px auto; background: linear-gradient(145deg, #111827, #1f2937); padding: 35px; border-radius: 20px; border: 1px solid #374151; text-align: center; box-shadow: 0 15px 30px rgba(0,0,0,0.7);">
                <div style="font-size: 3.5rem; margin-bottom: 10px;">🎛️🔊</div>
                <h2 style="color: #f59e0b; margin-bottom: 5px; font-weight: 800;">PUJA DJ KING</h2>
                <p style="color: #9ca3af; font-size: 0.95rem; margin-bottom: 0px; letter-spacing: 0.5px;">Professional Sound & Event Portal</p>
            </div>
        """, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            # Placeholder bilkul saaf kar diya hai taaki 1234 na dikhe
            pin = st.text_input("🔑 Enter Security PIN", type="password", placeholder="")
            if st.button("🔐 Login to Dashboard"):
                if pin == "1234":
                    st.session_state.authenticated = True
                    st.rerun()
                else:
                    st.error("❌ Galat PIN! Kripya sahi PIN dalein.")
        return False
    return True

if not check_login():
    st.stop()

# --- CSV FILE HANDLING ---
CSV_FILE = "puja_dj_bookings.csv"

def load_data():
    if os.path.exists(CSV_FILE):
        return pd.read_csv(CSV_FILE)
    else:
        return pd.DataFrame(columns=[
            "Customer Name", "Phone", "Event Dates", "Equipment", "Advance Paid", "Total Amount", "Remarks"
        ])

def save_data(df):
    df.to_csv(CSV_FILE, index=False)

df = load_data()

# --- HEADER SECTION ---
st.markdown("""
    <div class="header-card">
        <div class="header-title">🎧 PUJA DJ KING</div>
        <div class="header-subtitle">Professional Sound System & Event Management Dashboard</div>
    </div>
""", unsafe_allow_html=True)

# --- SIDEBAR MENU NAVIGATION ---
st.sidebar.markdown("### 🎛️ Control Panel")
menu = st.sidebar.radio("Select Option", ["➕ New Booking", "📋 View Bookings", "🔍 Search & Filter", "❌ Delete Booking"])

st.sidebar.markdown("---")
if st.sidebar.button("🔒 Logout"):
    st.session_state.authenticated = False
    st.rerun()

# Equipment Options
equipment_options = [
    "JBL Line Array Setup", 
    "Dual Bass Heavy Setup", 
    "Double Top Box Setup", 
    "Full Sound & Light Setup", 
    "Generator & Power Backup"
]

# --- 1. NEW BOOKING PAGE ---
if menu == "➕ New Booking":
    st.markdown("### 📝 Nayi Booking Darj Karein")
    
    with st.form("booking_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        
        with col1:
            customer_name = st.text_input("👤 Customer Name")
            phone = st.text_input("📞 Mobile Number")
            advance_paid = st.number_input("💵 Advance Amount (₹)", min_value=0, step=500)
            
        with col2:
            event_dates = st.date_input("📅 Event Date(s)", value=datetime.today())
            total_amount = st.number_input("💰 Total Amount (₹)", min_value=0, step=1000)
            
        selected_equipment = st.multiselect("🔊 Sound System / Equipment Select Karein", equipment_options)
        remarks = st.text_area("💬 Remarks / Notes (Location, Time, etc.)")
        
        submit_btn = st.form_submit_button("🚀 Save Booking")
        
        if submit_btn:
            if customer_name and phone:
                eq_str = ", ".join(selected_equipment)
                date_str = str(event_dates)
                
                new_row = pd.DataFrame({
                    "Customer Name": [customer_name],
                    "Phone": [phone],
                    "Event Dates": [date_str],
                    "Equipment": [eq_str],
                    "Advance Paid": [advance_paid],
                    "Total Amount": [total_amount],
                    "Remarks": [remarks]
                })
                
                df = pd.concat([df, new_row], ignore_index=True)
                save_data(df)
                st.success("🎉 Booking Safalpurvak Save Ho Gayi!")
            else:
                st.error("⚠️ Kripya Customer Name aur Mobile Number zaroor bharein!")

# --- 2. VIEW BOOKINGS PAGE ---
elif menu == "📋 View Bookings":
    st.markdown("### 📋 Sabhi Bookings ki List")
    
    if df.empty:
        st.info("📭 Abhi tak koi booking nahi hai.")
    else:
        st.dataframe(df, use_container_width=True)
        
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Download Bookings CSV",
            data=csv,
            file_name='puja_dj_bookings.csv',
            mime='text/csv',
        )

# --- 3. SEARCH & FILTER PAGE ---
elif menu == "🔍 Search & Filter":
    st.markdown("### 🔍 Booking Talashein (Search by Mobile / Name)")
    
    search_query = st.text_input("Mobile Number ya Naam enter karein:")
    
    if search_query:
        result_df = df[
            df['Phone'].astype(str).str.contains(search_query, case=False, na=False) |
            df['Customer Name'].astype(str).str.contains(search_query, case=False, na=False)
        ]
        
        if not result_df.empty:
            st.success(f"🎯 Total {len(result_df)} match mile hain:")
            st.dataframe(result_df, use_container_width=True)
        else:
            st.warning("❌ Is naam ya number se koi booking nahi mili.")
    else:
        st.info("👆 Upar search box me kisi customer ka mobile number ya naam type karein.")

# --- 4. DELETE BOOKING PAGE ---
elif menu == "❌ Delete Booking":
    st.markdown("### 🗑️ Booking Delete Karein")
    
    if df.empty:
        st.info("📭 Delete karne ke liye koi record nahi hai.")
    else:
        st.dataframe(df, use_container_width=True)
        
        row_idx = st.number_input("Kahin galti ho gayi? Upar table se Row Index number dalein jise delete karna hai:", min_value=0, max_value=max(0, len(df)-1), step=1)
        
        if st.button("❌ Selected Booking Delete Karein"):
            if len(df) > 0:
                df = df.drop(row_idx).reset_index(drop=True)
                save_data(df)
                st.success(f"🗑️ Row Index {row_idx} ko hata diya gaya hai!")
                st.rerun()
