import streamlit as st
import pandas as pd
import os
from datetime import datetime, date

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="PUJA DJ KING | Management",
    page_icon="🎧",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- MODERN PREMIUM UI & STYLING ---
st.markdown("""
    <style>
    /* Main Theme & Background */
    .stApp {
        background: linear-gradient(180deg, #05070b 0%, #0c1017 100%);
        color: #f3f4f6;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    
    /* Top Header Card */
    .top-header-container {
        text-align: center;
        background: linear-gradient(135deg, #111827 0%, #1f2937 100%);
        padding: 16px 20px;
        border-radius: 20px;
        border: 1px solid rgba(245, 158, 11, 0.2);
        box-shadow: 0 12px 30px rgba(0, 0, 0, 0.6);
        margin-bottom: 15px;
    }
    .welcome-text {
        color: #9ca3af;
        font-size: 0.7rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 2px;
    }
    .brand-title {
        color: #f59e0b;
        font-size: 1.6rem;
        font-weight: 900;
        margin: 2px 0 0 0;
        letter-spacing: 0.5px;
        text-shadow: 0 2px 10px rgba(245, 158, 11, 0.3);
    }
    .brand-subtitle {
        color: #94a3b8;
        font-size: 0.75rem;
        font-weight: 500;
    }

    /* Section Headings */
    h2, h3, h4 {
        color: #f9fafb !important;
        font-weight: 700 !important;
        letter-spacing: -0.3px;
    }

    /* Form Design */
    div.stForm {
        background: rgba(17, 24, 39, 0.7);
        backdrop-filter: blur(10px);
        padding: 20px;
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.08);
        box-shadow: 0 8px 24px rgba(0,0,0,0.5);
    }

    /* Inputs & Selectboxes */
    .stTextInput input, .stNumberInput input, .stTextArea textarea, .stSelectbox div[data-baseweb="select"] {
        background-color: #0f172a !important;
        color: #f8fafc !important;
        border-radius: 12px !important;
        border: 1px solid #334155 !important;
    }
    .stTextInput input:focus, .stNumberInput input:focus {
        border-color: #f59e0b !important;
        box-shadow: 0 0 0 2px rgba(245, 158, 11, 0.2) !important;
    }

    /* Glossy Primary Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
        color: #05070b;
        font-weight: 800;
        border-radius: 14px;
        border: none;
        padding: 0.65rem 1.2rem;
        width: 100%;
        box-shadow: 0 6px 16px rgba(245, 158, 11, 0.35);
        transition: all 0.25s ease;
    }
    .stButton > button:hover {
        background: linear-gradient(135deg, #fbbf24 0%, #f59e0b 100%);
        box-shadow: 0 8px 20px rgba(245, 158, 11, 0.5);
        transform: translateY(-1px);
    }

    /* Metrics Grid Cards */
    .metrics-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 12px;
        margin-bottom: 20px;
    }
    .metric-card {
        background: linear-gradient(135deg, #111827 0%, #0d1117 100%);
        border: 1px solid #1f2937;
        padding: 16px 12px;
        border-radius: 16px;
        box-shadow: 0 6px 16px rgba(0,0,0,0.4);
        text-align: center;
    }
    .metric-title {
        color: #9ca3af;
        font-weight: 600;
        font-size: 0.75rem;
        margin-bottom: 6px;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    .metric-value {
        color: #f59e0b;
        font-weight: 900;
        font-size: 1.3rem;
    }
    
    /* Hide Default Sidebar to maximize mobile view */
    section[data-testid="stSidebar"] {
        display: none;
    }
    
    /* Footer */
    .footer-text {
        text-align: center;
        color: #64748b;
        font-size: 0.8rem;
        font-weight: 700;
        margin-top: 35px;
        margin-bottom: 20px;
        letter-spacing: 1.5px;
        text-transform: uppercase;
    }
    </style>
""", unsafe_allow_html=True)

# --- LOGIN SYSTEM ---
def check_login():
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False

    if not st.session_state.authenticated:
        st.markdown("<div style='height: 14vh;'></div>", unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 1.3, 1])
        with col2:
            st.markdown("""
                <div style="text-align: center; margin-bottom: 30px;">
                    <div style="font-size: 4.5rem; line-height: 1; filter: drop-shadow(0 6px 15px rgba(245,158,11,0.4));">🎧</div>
                    <h1 style="color: #f59e0b; font-weight: 900; font-size: 2.6rem; margin-top: 12px; margin-bottom: 0px;">PUJA DJ KING</h1>
                    <p style="color: #64748b; font-size: 0.85rem; letter-spacing: 3px; text-transform: uppercase; margin-top: 6px;">Secure Management Portal</p>
                </div>
            """, unsafe_allow_html=True)
            
            with st.form("login_form"):
                pin = st.text_input("PIN", type="password", placeholder="Enter 4-digit PIN", label_visibility="collapsed")
                st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)
                
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
EXPENSE_CSV_FILE = "puja_dj_expenses.csv"
CATEGORIES_CSV_FILE = "puja_dj_expense_categories.csv"
EQUIPMENT_CSV_FILE = "puja_dj_equipment_list.csv"

def load_data():
    if os.path.exists(CSV_FILE):
        df = pd.read_csv(CSV_FILE)
        expected_cols = ["Customer Name", "Phone", "Event Type", "Event Dates", "Equipment", "Advance Paid", "Total Amount", "Balance Due", "Status", "Remarks"]
        for col in expected_cols:
            if col not in df.columns:
                df[col] = "None"
        
        df["Total Amount"] = pd.to_numeric(df["Total Amount"], errors='coerce').fillna(0)
        df["Advance Paid"] = pd.to_numeric(df["Advance Paid"], errors='coerce').fillna(0)
        df["Balance Due"] = pd.to_numeric(df["Balance Due"], errors='coerce').fillna(0)
        df["Status"] = df["Status"].astype(str)
        df["Customer Name"] = df["Customer Name"].astype(str)
        df["Phone"] = df["Phone"].astype(str)
        df["Event Type"] = df["Event Type"].astype(str)
        return df
    else:
        return pd.DataFrame(columns=[
            "Customer Name", "Phone", "Event Type", "Event Dates", "Equipment", "Advance Paid", "Total Amount", "Balance Due", "Status", "Remarks"
        ])

def save_data(df):
    df.to_csv(CSV_FILE, index=False)

def load_expense_data():
    if os.path.exists(EXPENSE_CSV_FILE):
        df_exp = pd.read_csv(EXPENSE_CSV_FILE)
        expected_cols = ["Date", "Expense Category", "Amount", "Description"]
        for col in expected_cols:
            if col not in df_exp.columns:
                df_exp[col] = "None"
        df_exp["Amount"] = pd.to_numeric(df_exp["Amount"], errors='coerce').fillna(0)
        return df_exp
    else:
        return pd.DataFrame(columns=["Date", "Expense Category", "Amount", "Description"])

def save_expense_data(df_exp):
    df_exp.to_csv(EXPENSE_CSV_FILE, index=False)

def load_categories():
    default_categories = [
        "Labor Kharcha (Majdoori)", 
        "Petrol / Diesel", 
        "Repairing / Maintenance", 
        "Transport / Vehicle", 
        "Food & Snacks", 
        "Other Miscellaneous"
    ]
    if os.path.exists(CATEGORIES_CSV_FILE):
        try:
            df_cat = pd.read_csv(CATEGORIES_CSV_FILE)
            if "Category" in df_cat.columns:
                cats = df_cat["Category"].dropna().astype(str).tolist()
                for dc in default_categories:
                    if dc not in cats:
                        cats.append(dc)
                return cats
        except:
            pass
    return default_categories

def save_category(cat_name):
    cats = load_categories()
    if cat_name not in cats:
        cats.append(cat_name)
        save_all_categories(cats)

def save_all_categories(cats):
    df_cat = pd.DataFrame({"Category": cats})
    df_cat.to_csv(CATEGORIES_CSV_FILE, index=False)

def load_equipment():
    default_equipments = [
        "JBL Line Array", 
        "Dual Bass Heavy", 
        "Double Top Box", 
        "Full Sound & Light", 
        "Generator Backup"
    ]
    if os.path.exists(EQUIPMENT_CSV_FILE):
        try:
            df_eq = pd.read_csv(EQUIPMENT_CSV_FILE)
            if "Equipment" in df_eq.columns:
                eqs = df_eq["Equipment"].dropna().astype(str).tolist()
                for de in default_equipments:
                    if de not in eqs:
                        eqs.append(de)
                return eqs
        except:
            pass
    return default_equipments

def save_all_equipment(eqs):
    df_eq = pd.DataFrame({"Equipment": eqs})
    df_eq.to_csv(EQUIPMENT_CSV_FILE, index=False)

df = load_data()
df_expenses = load_expense_data()

# --- TOP HEADER SECTION ---
st.markdown("""
    <div class="top-header-container">
        <div class="welcome-text">Welcome Back</div>
        <div class="brand-title">🎧 PUJA DJ KING</div>
        <div class="brand-subtitle">Professional Sound System & Event Management</div>
    </div>
""", unsafe_allow_html=True)

# --- MODERN MOBILE-FRIENDLY TOP NAVIGATION TABS ---
menu_options = [
    "🏠 Dashboard",
    "➕ New Booking", 
    "📋 Bookings", 
    "📈 Ledger", 
    "💸 Expenses", 
    "🔍 Search", 
    "❌ Delete"
]

if "current_tab" not in st.session_state:
    st.session_state.current_tab = "🏠 Dashboard"

if "show_notifications" not in st.session_state:
    st.session_state.show_notifications = False

# Render custom selectbox style navigation on top for mobile ease
selected_menu = st.selectbox("📂 Control Panel Menu", menu_options, index=menu_options.index(st.session_state.current_tab), label_visibility="collapsed")

# Agar menu change kiya toh notification turant band ho jayega
if selected_menu != st.session_state.current_tab:
    st.session_state.current_tab = selected_menu
    st.session_state.show_notifications = False
    st.rerun()

st.markdown("<div style='margin-bottom: 10px;'></div>", unsafe_allow_html=True)

# Navigation row with Notification Bell and Logout buttons
col_nav1, col_nav2, col_nav3 = st.columns([2.5, 1.5, 1])

with col_nav2:
    # Notification Bell Toggle Button
    if st.session_state.show_notifications:
        bell_btn_label = "🔔 Hide Alerts"
    else:
        bell_btn_label = "🔔 View Alerts"
        
    if st.button(bell_btn_label):
        st.session_state.show_notifications = not st.session_state.show_notifications
        st.rerun()

with col_nav3:
    if st.button("🔒 Logout"):
        st.session_state.authenticated = False
        st.session_state.show_notifications = False
        st.rerun()

st.markdown("---")

# --- CONDITIONAL NOTIFICATIONS & ALERTS (Only shows when bell icon is clicked) ---
if st.session_state.show_notifications:
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
                main_date_str = event_date_str.split(" & ")[0].strip()
                ev_date = datetime.strptime(main_date_str, "%Y-%m-%d").date()
                diff_days = (ev_date - today_date).days
                if 0 <= diff_days <= 3:
                    upcoming_alerts.append(f"🚨 **{name}** ka event najdeek hai! Date: **{event_date_str}**")
            except:
                pass

    with st.container():
        st.markdown("""
            <div style="background-color: #111827; padding: 12px 15px; border-radius: 16px; border: 1px solid rgba(245, 158, 11, 0.3); margin-bottom: 15px;">
                <h4 style="color: #f59e0b; margin-top: 0; margin-bottom: 10px; font-size: 1rem;">🔔 Live Notifications & Alerts</h4>
            </div>
        """, unsafe_allow_html=True)
        cols_alert = st.columns(2)
        with cols_alert[0]:
            st.markdown("##### 💳 Pending Payments")
            if pending_alerts:
                for alert in pending_alerts:
                    st.error(alert)
            else:
                st.success("✅ Sabhi ka payment clear hai!")
        with cols_alert[1]:
            st.markdown("##### 📅 Upcoming Events")
            if upcoming_alerts:
                for alert in upcoming_alerts:
                    st.warning(alert)
            else:
                st.info("ℹ️ Aane wale 3 dino me koi event nahi hai.")
    st.markdown("---")

# --- ROUTING BASED ON TOP NAVIGATION SELECTION ---

if st.session_state.current_tab == "🏠 Dashboard":
    total_bookings = len(df) if not df.empty else 0
    total_revenue = df["Total Amount"].sum() if not df.empty else 0
    total_expense = df_expenses["Amount"].sum() if not df_expenses.empty else 0
    net_profit = total_revenue - total_expense

    st.markdown(f"""
        <div class="metrics-grid">
            <div class="metric-card">
                <div class="metric-title">📊 Total Bookings</div>
                <div class="metric-value">{total_bookings}</div>
            </div>
            <div class="metric-card">
                <div class="metric-title">💰 Total Revenue</div>
                <div class="metric-value">₹ {total_revenue:,.0f}</div>
            </div>
            <div class="metric-card">
                <div class="metric-title">💸 Total Expenses</div>
                <div class="metric-value" style="color: #f87171;">₹ {total_expense:,.0f}</div>
            </div>
            <div class="metric-card">
                <div class="metric-title">💎 Net Profit</div>
                <div class="metric-value" style="color: #34d399;">₹ {net_profit:,.0f}</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    col_nc1, col_nc2, col_nc3 = st.columns([1, 2, 1])
    with col_nc2:
        if st.button("➕ Nayi Booking Karein"):
            st.session_state.current_tab = "➕ New Booking"
            st.session_state.show_notifications = False
            st.rerun()
        
        st.markdown("<div style='height: 8px;'></div>", unsafe_allow_html=True)
        
        if st.button("💸 Kharcha Jodein"):
            st.session_state.current_tab = "💸 Expenses"
            st.session_state.show_notifications = False
            st.rerun()

# --- 1. NEW BOOKING PAGE ---
elif st.session_state.current_tab == "➕ New Booking":
    st.markdown("### 📝 Booking & Equipment Management")
    
    book_tab1, book_tab2 = st.tabs(["➕ Nayi Booking Darj Karein", "🔊 Sound System / Equipment Manage Karein"])

    with book_tab1:
        event_type = st.radio("🎯 Event Type Select Karein", ["Single Date", "Multiple Dates (2 Dates)"], horizontal=True)
        equipment_list = load_equipment()

        with st.form("booking_form", clear_on_submit=True):
            customer_name = st.text_input("👤 Customer Name")
            phone = st.text_input("📞 Mobile Number")
            total_amount = st.number_input("💰 Total Amount (₹)", min_value=0, step=1000)
            advance_paid = st.number_input("💵 Advance Amount (₹)", min_value=0, step=500)

            st.markdown("---")
            
            if event_type == "Single Date":
                single_date = st.date_input("📅 Event Date", value=datetime.today())
                date_str = str(single_date)
            else:
                col_d1, col_d2 = st.columns(2)
                with col_d1:
                    date_1 = st.date_input("📅 Event Date 1", value=datetime.today())
                with col_d2:
                    date_2 = st.date_input("📅 Event Date 2", value=datetime.today())
                date_str = f"{date_1} & {date_2}"

            selected_equipment = st.multiselect("🔊 Sound System / Equipment Select Karein", equipment_list)
            remarks = st.text_area("💬 Remarks / Notes (Location, Time, etc.)")
            
            submit_btn = st.form_submit_button("🚀 Save Booking")
            
            if submit_btn:
                if customer_name and phone:
                    eq_str = ", ".join(selected_equipment)
                    balance_due = float(total_amount) - float(advance_paid)
                    status = "Paid" if balance_due <= 0 else "Pending"
                    
                    new_row = pd.DataFrame({
                        "Customer Name": [str(customer_name)],
                        "Phone": [str(phone)],
                        "Event Type": [str(event_type)],
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
                    st.session_state.current_tab = "🏠 Dashboard"
                    st.rerun()
                else:
                    st.error("⚠️ Kripya Customer Name aur Mobile Number zaroor bharein!")

    with book_tab2:
        st.markdown("#### ⚙️ Sound System / Equipment Add, Edit & Delete")
        eq_list_current = load_equipment()
        
        new_eq_input = st.text_input("Equipment Naam Likhein (Jaise: JBL Bass, Mixer, etc.)")
        if st.button("💾 Equipment Save Karein"):
            if new_eq_input.strip():
                if new_eq_input.strip() not in eq_list_current:
                    eq_list_current.append(new_eq_input.strip())
                    save_all_equipment(eq_list_current)
                    st.success(f"✅ '{new_eq_input.strip()}' safalpurvak add ho gaya!")
                    st.rerun()
                else:
                    st.warning("⚠️ Yeh equipment pehle se list me hai.")
            else:
                st.warning("⚠️ Naam khali nahi ho sakta.")
                
        st.markdown("---")
        if eq_list_current:
            selected_eq_edit = st.selectbox("Equipment Select Karein:", eq_list_current)
            edited_eq_name = st.text_input("Naya Naam (Edit ke liye):", value=selected_eq_edit)
            
            col_sub_eq1, col_sub_eq2 = st.columns(2)
            with col_sub_eq1:
                if st.button("🔄 Update Equipment"):
                    if edited_eq_name.strip():
                        idx = eq_list_current.index(selected_eq_edit)
                        eq_list_current[idx] = edited_eq_name.strip()
                        save_all_equipment(eq_list_current)
                        st.success("✅ Equipment update ho gaya!")
                        st.rerun()
            with col_sub_eq2:
                if st.button("🗑️ Delete Equipment"):
                    if len(eq_list_current) > 1:
                        eq_list_current.remove(selected_eq_edit)
                        save_all_equipment(eq_list_current)
                        st.success("🗑️ Equipment hata diya gaya!")
                        st.rerun()
                    else:
                        st.error("⚠️ Kam se kam ek equipment hona zaroori hai.")

# --- 2. VIEW BOOKINGS PAGE ---
elif st.session_state.current_tab == "📋 Bookings":
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

# --- 3. LEDGER & PAYMENTS PAGE ---
elif st.session_state.current_tab == "📈 Ledger":
    st.markdown("### 📈 Customer Ledger & Payment Update")
    
    if df.empty:
        st.info("📭 Ledger ke liye koi data available nahi hai.")
    else:
        st.dataframe(df[["Customer Name", "Phone", "Event Type", "Event Dates", "Total Amount", "Advance Paid", "Balance Due", "Status"]], use_container_width=True)
        
        st.markdown("---")
        st.markdown("### 💳 Update Payment / Clear Due Amount")
        
        customer_list = df.index.astype(str) + " - " + df["Customer Name"].astype(str) + " (" + df["Phone"].astype(str) + ")"
        selected_row_label = st.selectbox("Kiska payment update karna hai select karein:", customer_list)
        
        if selected_row_label:
            idx = int(selected_row_label.split(" - ")[0])
            curr_row = df.loc[idx]
            
            st.info(f"👤 Customer: **{curr_row['Customer Name']}** | 💰 Total: ₹ {float(curr_row['Total Amount']):,.0f} | 💵 Paid: ₹ {float(curr_row['Advance Paid']):,.0f} | ⏳ Due: ₹ {float(curr_row['Balance Due']):,.0f}")
            
            additional_pay = st.number_input("💵 Kitna naya payment mila hai? (Enter Amount)", min_value=0, step=500, key="add_pay_input")
            
            col_btn1, col_btn2 = st.columns(2)
            with col_btn1:
                if st.button("📥 Update Partial Payment"):
                    if additional_pay > 0:
                        df.loc[idx, "Advance Paid"] = float(df.loc[idx, "Advance Paid"]) + float(additional_pay)
                        df.loc[idx, "Balance Due"] = float(df.loc[idx, "Total Amount"]) - float(df.loc[idx, "Advance Paid"])
                        if float(df.loc[idx, "Balance Due"]) <= 0:
                            df.loc[idx, "Balance Due"] = 0.0
                            df.loc[idx, "Status"] = "Paid"
                        else:
                            df.loc[idx, "Status"] = "Pending"
                        save_data(df)
                        st.success("✅ Payment Safalpurvak Update Ho Gaya!")
                        st.rerun()
                    else:
                        st.warning("⚠️ Kripya sahi amount enter karein.")
            
            with col_btn2:
                if st.button("✅ Mark as Fully Paid"):
                    df.loc[idx, "Advance Paid"] = float(df.loc[idx, "Total Amount"])
                    df.loc[idx, "Balance Due"] = 0.0
                    df.loc[idx, "Status"] = "Paid"
                    save_data(df)
                    st.success("🎉 Payment Poori Tarah Clear Ho Gaya!")
                    st.rerun()

        st.markdown("---")
        col_l1, col_l2 = st.columns(2)
        col_l1.warning(f"⏳ Total Balance Due: **₹ {df['Balance Due'].sum():,.0f}**")
        col_l2.success(f"✅ Total Collected: **₹ {df['Advance Paid'].sum():,.0f}**")

# --- 4. EXPENSE & LEDGER PAGE ---
elif st.session_state.current_tab == "💸 Expenses":
    st.markdown("### 💸 Kharcha Darj Karein & Profit-Loss Ledger")
    
    available_categories = load_categories()
    category_choices = available_categories + ["➕ Add New Category..."]

    exp_tab1, exp_tab2 = st.tabs(["💸 Naya Kharcha Jodein", "⚙️ Categories Manage Karein"])

    with exp_tab1:
        with st.form("expense_form", clear_on_submit=True):
            exp_date = st.date_input("📅 Kharche ki Date", value=datetime.today())
            selected_cat_option = st.selectbox("🏷️ Kharche ka Category", category_choices)
            new_custom_cat = st.text_input("✨ Naya Category Naam Likhein (Agar upar 'Add New' chuna ho):")
            exp_amount = st.number_input("💰 Kharcha Amount (₹)", min_value=0.0, step=100.0)
            exp_desc = st.text_input("💬 Description / Kis kaam ka kharcha tha?")
            
            save_exp_btn = st.form_submit_button("💾 Kharcha Save Karein")
            
            if save_exp_btn:
                final_category = selected_cat_option
                if selected_cat_option == "➕ Add New Category...":
                    if new_custom_cat.strip():
                        final_category = new_custom_cat.strip()
                    else:
                        final_category = "Other Miscellaneous"
                
                if exp_amount > 0:
                    save_category(final_category)
                    
                    new_exp_row = pd.DataFrame({
                        "Date": [str(exp_date)],
                        "Expense Category": [str(final_category)],
                        "Amount": [float(exp_amount)],
                        "Description": [str(exp_desc)]
                    })
                    df_expenses = pd.concat([df_expenses, new_exp_row], ignore_index=True)
                    save_expense_data(df_expenses)
                    st.success(f"✅ '{final_category}' ka kharcha safalpurvak save ho gaya!")
                    st.rerun()
                else:
                    st.warning("⚠️ Kripya valid amount enter karein.")

    with exp_tab2:
        if available_categories:
            selected_cat_to_edit = st.selectbox("Kiski category ko edit ya delete karna hai select karein:", available_categories, key="edit_cat_select")
            new_cat_name = st.text_input("✏️ Naya Naam (Badalne ke liye):", value=selected_cat_to_edit)
            
            col_ce1, col_ce2 = st.columns(2)
            with col_ce1:
                if st.button("🔄 Category Update Karein"):
                    if new_cat_name.strip():
                        idx = available_categories.index(selected_cat_to_edit)
                        available_categories[idx] = new_cat_name.strip()
                        save_all_categories(available_categories)
                        
                        if not df_expenses.empty:
                            df_expenses.loc[df_expenses["Expense Category"] == selected_cat_to_edit, "Expense Category"] = new_cat_name.strip()
                            save_expense_data(df_expenses)
                            
                        st.success("✅ Category update ho gayi!")
                        st.rerun()
                    else:
                        st.warning("⚠️ Naam khali nahi ho sakta.")
                        
            with col_ce2:
                if st.button("🗑️ Category Delete Karein"):
                    if len(available_categories) > 1:
                        available_categories.remove(selected_cat_to_edit)
                        save_all_categories(available_categories)
                        st.success("🗑️ Category hata di gayi hai!")
                        st.rerun()
                    else:
                        st.error("⚠️ Kam se kam ek category honi zaroori hai.")

    st.markdown("---")
    
    total_income = df["Total Amount"].sum() if not df.empty else 0
    total_expense = df_expenses["Amount"].sum() if not df_expenses.empty else 0
    net_savings = total_income - total_expense
    
    col_f1, col_f2, col_f3 = st.columns(3)
    col_f1.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">💰 Total Kamai</div>
            <div class="metric-value" style="color: #60a5fa;">₹ {total_income:,.0f}</div>
        </div>
    """, unsafe_allow_html=True)
    
    col_f2.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">💸 Total Kharcha</div>
            <div class="metric-value" style="color: #f87171;">₹ {total_expense:,.0f}</div>
        </div>
    """, unsafe_allow_html=True)
    
    col_f3.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">💎 Net Profit</div>
            <div class="metric-value" style="color: #34d399;">₹ {net_savings:,.0f}</div>
        </div>
    """, unsafe_allow_html=True)

    if not df_expenses.empty:
        st.markdown("#### 📉 Category-wise Kharcha Breakdown")
        cat_grouped = df_expenses.groupby("Expense Category")["Amount"].sum().reset_index()
        st.dataframe(cat_grouped, use_container_width=True)
        
        st.markdown("#### 📋 Sabhi Kharcho ki Detail List")
        st.dataframe(df_expenses, use_container_width=True)
        
        exp_del_idx = st.number_input("Kisi kharche ko hatane ke liye Row Index dalein:", min_value=0, max_value=max(0, len(df_expenses)-1), step=1, key="del_exp_idx")
        if st.button("🗑️ Kharcha Entry Delete Karein"):
            df_expenses = df_expenses.drop(exp_del_idx).reset_index(drop=True)
            save_expense_data(df_expenses)
            st.success("🗑️ Kharcha record hata diya gaya!")
            st.rerun()

# --- 5. SEARCH & FILTER PAGE ---
elif st.session_state.current_tab == "🔍 Search":
    st.markdown("### 🔍 Booking Talashein (Search by Mobile / Name)")
    
    search_query = st.text_input("Mobile Number ya Naam enter karein:")
    
    if search_query:
        result_df = df[
            df['Phone'].astype(str).str.contains(search_query, case=False, na=False) |
            df['Customer Name'].astype(str).str.contains(search_query, case=False, na=False)
        ]
        
        if not result_df.empty:
            st.success(f"🎯 Total {len(result_df)} match mile hain:")
            display_cols = ["Customer Name", "Phone", "Event Type", "Event Dates", "Equipment", "Advance Paid", "Total Amount", "Balance Due", "Status"]
            st.dataframe(result_df[display_cols], use_container_width=True)
        else:
            st.warning("❌ Is naam ya number se koi booking nahi mili.")
    else:
        st.info("👆 Upar search box me kisi customer ka mobile number ya naam type karein.")

# --- 6. DELETE BOOKING PAGE ---
elif st.session_state.current_tab == "❌ Delete":
    st.markdown("### 🗑️ Booking Delete Karein")
    
    if df.empty:
        st.info("📭 Delete karne ke liye koi record nahi hai.")
    else:
        display_cols = ["Customer Name", "Phone", "Event Type", "Event Dates", "Advance Paid", "Total Amount", "Balance Due", "Status"]
        st.dataframe(df[display_cols], use_container_width=True)
        
        row_idx = st.number_input("Table se Row Index number dalein jise delete karna hai:", min_value=0, max_value=max(0, len(df)-1), step=1)
        
        if st.button("❌ Selected Booking Delete Karein"):
            if len(df) > 0:
                df = df.drop(row_idx).reset_index(drop=True)
                save_data(df)
                st.success(f"🗑️ Row Index {row_idx} ko hata diya gaya hai!")
                st.rerun()

# --- FOOTER ---
st.markdown("---")
st.markdown('<div class="footer-text">Created by Dilip Singh</div>', unsafe_allow_html=True)
