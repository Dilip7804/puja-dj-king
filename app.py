import streamlit as st
import pandas as pd
import os
from datetime import datetime, date

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="PUJA DJ KING | Management",
    page_icon="🎧",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- PREMIUM STYLING ---
st.markdown("""
    <style>
    .stApp {
        background-color: #0b0f19;
        color: #f3f4f6;
    }
    
    .top-header-box {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background: linear-gradient(135deg, #1f2937 0%, #111827 100%);
        padding: 12px 15px;
        border-radius: 12px;
        border: 1px solid #374151;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.4);
        margin-bottom: 10px;
    }
    .welcome-text {
        color: #9ca3af;
        font-size: 0.7rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    .brand-title {
        color: #f59e0b;
        font-size: 1.25rem;
        font-weight: 800;
        margin: 0;
    }

    h2, h3 {
        color: #f3f4f6 !important;
        font-weight: 700 !important;
    }

    div.stForm {
        background-color: #111827;
        padding: 12px;
        border-radius: 12px;
        border: 1px solid #374151;
    }

    .stButton > button {
        background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
        color: #0b0f19;
        font-weight: 700;
        border-radius: 8px;
        border: none;
        padding: 0.5rem 1rem;
        width: 100%;
        box-shadow: 0 4px 10px rgba(245, 158, 11, 0.3);
    }
    .stButton > button:hover {
        background: linear-gradient(135deg, #fbbf24 0%, #f59e0b 100%);
        color: #000000;
    }

    section[data-testid="stSidebar"] {
        background-color: #030712;
        border-right: 1px solid #1f2937;
        padding-top: 10px;
    }
    
    .stRadio div[role="radiogroup"] {
        background-color: #111827;
        padding: 8px;
        border-radius: 12px;
        border: 1px solid #374151;
    }
    
    .stRadio label {
        background-color: #1f2937 !important;
        color: #f3f4f6 !important;
        padding: 8px 12px !important;
        border-radius: 8px !important;
        margin-bottom: 6px !important;
        font-weight: 600 !important;
        border: 1px solid #374151 !important;
        cursor: pointer;
    }

    .metrics-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 8px;
        margin-bottom: 10px;
    }
    .metric-card {
        background-color: #111827;
        border: 1px solid #374151;
        padding: 10px;
        border-radius: 10px;
        text-align: center;
    }
    .metric-title {
        color: #9ca3af;
        font-weight: 600;
        font-size: 0.75rem;
        margin-bottom: 2px;
    }
    .metric-value {
        color: #f59e0b;
        font-weight: 800;
        font-size: 1.1rem;
    }
    
    .footer-text {
        text-align: center;
        color: #f3f4f6;
        font-size: 0.9rem;
        margin-top: 25px;
        margin-bottom: 15px;
        font-weight: 800;
    }
    </style>
""", unsafe_allow_html=True)

# --- LOGIN SYSTEM ---
def check_login():
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False

    if not st.session_state.authenticated:
        st.markdown("""
            <style>
            [data-testid="stSidebar"] {display: none;}
            .stApp { background: radial-gradient(circle at center, #1e293b 0%, #020617 100%); }
            </style>
        """, unsafe_allow_html=True)
        
        st.markdown("<div style='height: 15vh;'></div>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([0.1, 1, 0.1])
        with col2:
            st.markdown("""
                <div style="text-align: center; margin-bottom: 20px;">
                    <div style="font-size: 3.5rem; line-height: 1;">🎧</div>
                    <h1 style="color: #f59e0b; font-weight: 900; font-size: 2.2rem; margin-top: 10px; margin-bottom: 0px;">PUJA DJ KING</h1>
                    <p style="color: #94a3b8; font-size: 0.9rem; letter-spacing: 2px; text-transform: uppercase;">Secure Portal</p>
                </div>
            """, unsafe_allow_html=True)
            
            with st.form("login_form"):
                pin = st.text_input("Security PIN", type="password", placeholder="Enter PIN", label_visibility="collapsed")
                if st.form_submit_button("Secure Login 🚀"):
                    if pin == "1234":
                        st.session_state.authenticated = True
                        st.rerun()
                    else:
                        st.error("❌ Galat PIN! Kripya dobara try karein.")
        return False
    return True

if not check_login():
    st.stop()

# --- CSV FILE HANDLING ---
CSV_FILE = "puja_dj_bookings.csv"

def load_data():
    if os.path.exists(CSV_FILE):
        df = pd.read_csv(CSV_FILE)
        expected_cols = ["Customer Name", "Phone", "Event Dates", "Equipment", "Advance Paid", "Total Amount", "Balance Due", "Status", "Remarks"]
        for col in expected_cols:
            if col not in df.columns:
                df[col] = "None"
        df["Total Amount"] = pd.to_numeric(df["Total Amount"], errors='coerce').fillna(0)
        df["Advance Paid"] = pd.to_numeric(df["Advance Paid"], errors='coerce').fillna(0)
        df["Balance Due"] = pd.to_numeric(df["Balance Due"], errors='coerce').fillna(0)
        return df
    else:
        return pd.DataFrame(columns=[
            "Customer Name", "Phone", "Event Dates", "Equipment", "Advance Paid", "Total Amount", "Balance Due", "Status", "Remarks"
        ])

def save_data(df):
    df.to_csv(CSV_FILE, index=False)

df = load_data()

# --- SIDEBAR NAVIGATION ---
st.sidebar.markdown("### 🎛️ Control Panel")

if "menu_selection" not in st.session_state:
    st.session_state.menu_selection = "🏠 Home / Dashboard"

if "show_alerts" not in st.session_state:
    st.session_state.show_alerts = False

options = [
    "🏠 Home / Dashboard",
    "➕ New Booking", 
    "📋 View Bookings", 
    "📈 Ledger & Payments", 
    "🔍 Search & Filter", 
    "❌ Delete Booking"
]

selected_menu = st.sidebar.radio("Select Option", options, index=options.index(st.session_state.menu_selection), label_visibility="collapsed")

if selected_menu != st.session_state.menu_selection:
    st.session_state.menu_selection = selected_menu
    st.rerun()

st.sidebar.markdown("---")
if st.sidebar.button("🔒 Logout"):
    st.session_state.authenticated = False
    st.rerun()

# --- TOP HEADER BOX WITH BELL BUTTON ---
col_head1, col_head2 = st.columns([5, 1])
with col_head1:
    st.markdown("""
        <div class="top-header-box" style="margin-bottom: 0px;">
            <div>
                <div class="welcome-text">Welcome</div>
                <div class="brand-title">🎧 PUJA DJ KING</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

with col_head2:
    st.markdown("<div style='height: 4px;'></div>", unsafe_allow_html=True)
    if st.button("🔔", help="Live Notifications"):
        st.session_state.show_alerts = not st.session_state.show_alerts
        st.rerun()

# --- SMART ALERTS PANEL ---
pending_alerts = []
upcoming_alerts = []
if not df.empty:
    today_date = date.today()
    for idx, row in df.iterrows():
        name = str(row["Customer Name"])
        phone = str(row["Phone"])
        balance = float(row["Balance Due"])
        event_date_str = str(row["Event Dates"])
        
        if balance > 0:
            pending_alerts.append(f"⚠️ **{name}** ({phone}) ka **₹ {balance:,.0f}** balance baaki hai!")
            
        try:
            ev_date = datetime.strptime(event_date_str.strip(), "%Y-%m-%d").date()
            diff_days = (ev_date - today_date).days
            if 0 <= diff_days <= 3:
                upcoming_alerts.append(f"🚨 **{name}** ka event najdeek hai! Date: **{event_date_str}**")
        except:
            pass

if st.session_state.get("show_alerts", False):
    with st.container():
        st.markdown("""
            <div style="background-color: #111827; padding: 10px; border-radius: 10px; border: 1px solid #f59e0b; margin-top: 8px; margin-bottom: 10px;">
                <h4 style="color: #f59e0b; margin-top: 0; font-size: 0.9rem;">🔔 Live Notifications & Alerts</h4>
            </div>
        """, unsafe_allow_html=True)
        if pending_alerts:
            for alert in pending_alerts[:3]:
                st.error(alert)
        if upcoming_alerts:
            for alert in upcoming_alerts[:3]:
                st.warning(alert)
        if not pending_alerts and not upcoming_alerts:
            st.success("✅ Sabhi ka payment clear hai aur koi paas me event nahi hai.")

# --- EQUIPMENT OPTIONS ---
equipment_options = [
    "JBL Line Array", 
    "Dual Bass Heavy", 
    "Double Top Box", 
    "Full Sound & Light", 
    "Generator Backup"
]

# --- ROUTING BASED ON MENU SELECTION ---

if st.session_state.menu_selection == "🏠 Home / Dashboard":
    if not df.empty:
        total_bookings = len(df)
        total_revenue = df["Total Amount"].sum()
        total_advance = df["Advance Paid"].sum()
        total_pending = df["Balance Due"].sum()
    else:
        total_bookings = 0
        total_revenue = 0
        total_advance = 0
        total_pending = 0

    st.markdown("<div style='margin-top: 10px;'></div>", unsafe_allow_html=True)
    st.markdown(f"""
        <div class="metrics-grid">
            <div class="metric-card">
                <div class="metric-title">📊 Total Bookings</div>
                <div class="metric-value">{total_bookings}</div>
            </div>
            <div class="metric-card">
                <div class="metric-title">💰 Total Business</div>
                <div class="metric-value">₹ {total_revenue:,.0f}</div>
            </div>
            <div class="metric-card">
                <div class="metric-title">💵 Advance Received</div>
                <div class="metric-value">₹ {total_advance:,.0f}</div>
            </div>
            <div class="metric-card">
                <div class="metric-title">⏳ Pending Balance</div>
                <div class="metric-value">₹ {total_pending:,.0f}</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

elif st.session_state.menu_selection == "➕ New Booking":
    st.markdown("### 📝 Nayi Booking Darj Karein")
    with st.form("booking_form", clear_on_submit=True):
        customer_name = st.text_input("👤 Customer Name")
        phone = st.text_input("📞 Mobile Number")
        event_dates = st.date_input("📅 Event Date", value=datetime.today())
        total_amount = st.number_input("💰 Total Amount (₹)", min_value=0, step=1000)
        advance_paid = st.number_input("💵 Advance Amount (₹)", min_value=0, step=500)
            
        selected_equipment = st.multiselect("🔊 Sound System Select Karein", equipment_options)
        remarks = st.text_area("💬 Remarks / Notes")
        
        if st.form_submit_button("🚀 Save Booking"):
            if customer_name and phone:
                eq_str = ", ".join(selected_equipment)
                date_str = str(event_dates)
                balance_due = float(total_amount) - float(advance_paid)
                status = "Paid" if balance_due <= 0 else "Pending"
                
                new_row = pd.DataFrame({
                    "Customer Name": [str(customer_name)],
                    "Phone": [str(phone)],
                    "Event Dates": [date_str],
                    "Equipment": [eq_str],
                    "Advance Paid": [float(advance_paid)],
                    "Total Amount": [float(total_amount)],
                    "Balance Due": [float(balance_due)],
                    "Status": [str(status)],
                    "Remarks": [str(remarks)]
                })
                df = pd.concat([df, new_row], ignore_index=True)
                save_data(df)
                st.success("🎉 Booking Safalpurvak Save Ho Gayi!")
                st.session_state.menu_selection = "🏠 Home / Dashboard"
                st.rerun()
            else:
                st.error("⚠️ Kripya Customer Name aur Mobile Number zaroor bharein!")

elif st.session_state.menu_selection == "📋 View Bookings":
    st.markdown("### 📋 Sabhi Bookings ki List")
    if df.empty:
        st.info("📭 Abhi tak koi booking nahi hai.")
    else:
        st.dataframe(df, use_container_width=True)
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Download CSV", csv, 'puja_dj_bookings.csv', 'text/csv')

elif st.session_state.menu_selection == "📈 Ledger & Payments":
    st.markdown("### 📈 Payment Update")
    if df.empty:
        st.info("📭 Koi data available nahi hai.")
    else:
        st.dataframe(df[["Customer Name", "Phone", "Total Amount", "Advance Paid", "Balance Due", "Status"]], use_container_width=True)
        st.markdown("---")
        customer_list = df.index.astype(str) + " - " + df["Customer Name"].astype(str) + " (" + df["Phone"].astype(str) + ")"
        selected_row_label = st.selectbox("Customer Select Karein:", customer_list)
        
        if selected_row_label:
            idx = int(selected_row_label.split(" - ")[0])
            curr_row = df.loc[idx]
            st.info(f"👤 **{curr_row['Customer Name']}** | Due: ₹ {float(curr_row['Balance Due']):,.0f}")
            additional_pay = st.number_input("💵 Kitna naya payment mila?", min_value=0, step=500)
            
            col_b1, col_b2 = st.columns(2)
            with col_b1:
                if st.button("📥 Update Payment"):
                    if additional_pay > 0:
                        df.loc[idx, "Advance Paid"] = float(df.loc[idx, "Advance Paid"]) + float(additional_pay)
                        df.loc[idx, "Balance Due"] = max(0.0, float(df.loc[idx, "Total Amount"]) - float(df.loc[idx, "Advance Paid"]))
                        df.loc[idx, "Status"] = "Paid" if df.loc[idx, "Balance Due"] <= 0 else "Pending"
                        save_data(df)
                        st.success("✅ Payment Update Ho Gaya!")
                        st.rerun()
            with col_b2:
                if st.button("✅ Fully Paid"):
                    df.loc[idx, "Advance Paid"] = float(df.loc[idx, "Total Amount"])
                    df.loc[idx, "Balance Due"] = 0.0
                    df.loc[idx, "Status"] = "Paid"
                    save_data(df)
                    st.success("🎉 Clear Ho Gaya!")
                    st.rerun()

elif st.session_state.menu_selection == "🔍 Search & Filter":
    st.markdown("### 🔍 Booking Talashein")
    search_query = st.text_input("Mobile Number ya Naam dalein:")
    if search_query:
        result_df = df[
            df['Phone'].astype(str).str.contains(search_query, case=False, na=False) |
            df['Customer Name'].astype(str).str.contains(search_query, case=False, na=False)
        ]
        if not result_df.empty:
            st.dataframe(result_df, use_container_width=True)
        else:
            st.warning("❌ Koi booking nahi mili.")

elif st.session_state.menu_selection == "❌ Delete Booking":
    st.markdown("### 🗑️ Booking Delete Karein")
    if df.empty:
        st.info("📭 Koi record nahi hai.")
    else:
        st.dataframe(df, use_container_width=True)
        row_idx = st.number_input("Row Index dalein:", min_value=0, max_value=max(0, len(df)-1), step=1)
        if st.button("❌ Delete Karein"):
            if len(df) > 0:
                df = df.drop(row_idx).reset_index(drop=True)
                save_data(df)
                st.success("🗑️ Hata di gayi hai!")
                st.rerun()

# --- FOOTER ---
st.markdown('<div class="footer-text">Created by Dilip Singh</div>', unsafe_allow_html=True)
