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

# --- PREMIUM STYLING & AUTO-HIDE SIDEBAR SCRIPT ---
st.markdown("""
    <style>
    /* Main Background & Text */
    .stApp {
        background-color: #0b0f19;
        color: #f3f4f6;
    }
    
    /* Top Header Layout (Centered PUJA DJ KING) */
    .top-header-container {
        text-align: center;
        background: linear-gradient(135deg, #1f2937 0%, #111827 100%);
        padding: 15px 20px;
        border-radius: 14px;
        border: 1px solid #374151;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.5);
        margin-bottom: 15px;
    }
    .welcome-text {
        color: #9ca3af;
        font-size: 0.85rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    .brand-title {
        color: #f59e0b;
        font-size: 1.6rem;
        font-weight: 800;
        margin: 0;
    }

    /* Section Headers */
    h2, h3 {
        color: #f3f4f6 !important;
        font-weight: 700 !important;
    }

    /* Form & Input Fields Container */
    div.stForm {
        background-color: #111827;
        padding: 15px;
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

    /* SIDEBAR & PREMIUM MENU STYLING */
    section[data-testid="stSidebar"] {
        background-color: #030712;
        border-right: 1px solid #1f2937;
        padding-top: 20px;
    }
    
    /* Radio Menu Container */
    .stRadio div[role="radiogroup"] {
        background-color: #111827;
        padding: 12px;
        border-radius: 14px;
        border: 1px solid #374151;
        box-shadow: 0 4px 12px rgba(0,0,0,0.4);
    }
    
    /* Radio Option Cards Style */
    .stRadio label {
        background-color: #1f2937 !important;
        color: #f3f4f6 !important;
        padding: 10px 15px !important;
        border-radius: 10px !important;
        margin-bottom: 8px !important;
        font-weight: 600 !important;
        border: 1px solid #374151 !important;
        transition: all 0.3s ease-in-out !important;
        cursor: pointer;
    }
    .stRadio label:hover {
        background: linear-gradient(135deg, #374151, #4b5563) !important;
        border-color: #f59e0b !important;
        color: #f59e0b !important;
        transform: translateX(4px);
    }

    /* Custom Metric Cards Grid Styling */
    .metrics-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 10px;
        margin-bottom: 15px;
    }
    .metric-card {
        background-color: #111827;
        border: 1px solid #374151;
        padding: 12px;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.3);
        text-align: center;
    }
    .metric-title {
        color: #9ca3af;
        font-weight: 600;
        font-size: 0.8rem;
        margin-bottom: 4px;
    }
    .metric-value {
        color: #f59e0b;
        font-weight: 800;
        font-size: 1.25rem;
    }
    
    /* Footer Styling */
    .footer-text {
        text-align: center;
        color: #9ca3af;
        font-size: 0.85rem;
        font-weight: 600;
        margin-top: 30px;
        margin-bottom: 20px;
        letter-spacing: 1px;
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
        
        st.markdown("<div style='height: 12vh;'></div>", unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 1.2, 1])
        with col2:
            st.markdown("""
                <div style="text-align: center; margin-bottom: 25px;">
                    <div style="font-size: 4rem; line-height: 1;">🎧</div>
                    <h1 style="color: #f59e0b; font-weight: 900; font-size: 2.8rem; margin-top: 10px; margin-bottom: 0px;">PUJA DJ KING</h1>
                    <p style="color: #94a3b8; font-size: 1.1rem; letter-spacing: 2px; text-transform: uppercase;">Secure Portal</p>
                </div>
            """, unsafe_allow_html=True)
            
            with st.form("login_form"):
                st.markdown("<p style='color: #cbd5e1; font-weight: 600; margin-bottom: 5px;'>Security PIN Required</p>", unsafe_allow_html=True)
                pin = st.text_input("PIN", type="password", placeholder="", label_visibility="collapsed")
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

# --- SIDEBAR NAVIGATION SETUP ---
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
    "💸 Expense & Ledger", 
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

# --- TOP HEADER SECTION (Centered Branding) ---
st.markdown("""
    <div class="top-header-container">
        <div class="welcome-text">Welcome to</div>
        <div class="brand-title">🎧 PUJA DJ KING</div>
        <div style="color: #9ca3af; font-size: 0.8rem; margin-top: 4px;">Professional Sound System & Event Management</div>
    </div>
""", unsafe_allow_html=True)

# --- SMART ALERTS & NOTIFICATIONS ---
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
                upcoming_alerts.append(f"🚨 **{name}** ka event bilkul najdeek hai! Date: **{event_date_str}**")
        except:
            pass

if st.session_state.get("show_alerts", False):
    st.markdown("<div style='margin-top: 10px;'></div>", unsafe_allow_html=True)
    with st.container():
        st.markdown("""
            <div style="background-color: #111827; padding: 15px; border-radius: 12px; border: 1px solid #f59e0b; margin-bottom: 15px;">
                <h4 style="color: #f59e0b; margin-top: 0;">🔔 Live Notifications & Alerts</h4>
            </div>
        """, unsafe_allow_html=True)
        cols_alert = st.columns(2)
        with cols_alert[0]:
            st.markdown("#### 💳 Pending Payments")
            if pending_alerts:
                for alert in pending_alerts:
                    st.error(alert)
            else:
                st.success("✅ Sabhi ka payment clear hai!")
        with cols_alert[1]:
            st.markdown("#### 📅 Upcoming Events")
            if upcoming_alerts:
                for alert in upcoming_alerts:
                    st.warning(alert)
            else:
                st.info("ℹ️ Aane wale 3 dino me koi event nahi hai.")

st.markdown("<div style='margin-bottom: 10px;'></div>", unsafe_allow_html=True)

# --- ROUTING BASED ON MENU SELECTION ---

if st.session_state.menu_selection == "🏠 Home / Dashboard":
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
                <div class="metric-value" style="color: #ef4444;">₹ {total_expense:,.0f}</div>
            </div>
            <div class="metric-card">
                <div class="metric-title">💎 Net Profit (Bachat)</div>
                <div class="metric-value" style="color: #10b981;">₹ {net_profit:,.0f}</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<div style='margin-bottom: 25px;'></div>", unsafe_allow_html=True)
    
    st.markdown("<h3 style='text-align: center;'>⚡ Quick Navigation</h3>", unsafe_allow_html=True)
    
    col_nc1, col_nc2, col_nc3 = st.columns([1, 2.5, 0.8])
    with col_nc2:
        if st.button("➕ Create New Booking"):
            st.session_state.menu_selection = "➕ New Booking"
            st.rerun()
        
        st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)
        
        if st.button("💸 Add Expense / Kharcha"):
            st.session_state.menu_selection = "💸 Expense & Ledger"
            st.rerun()
            
    with col_nc3:
        st.markdown("<div style='height: 15px;'></div>", unsafe_allow_html=True)
        if st.button("🔔", help="Click to View Live Alerts"):
            st.session_state.show_alerts = not st.session_state.get("show_alerts", False)
            st.rerun()

# --- 1. NEW BOOKING PAGE (WITH EQUIPMENT MANAGER TAB) ---
elif st.session_state.menu_selection == "➕ New Booking":
    st.markdown("### 📝 Booking & Equipment Management")
    
    book_tab1, book_tab2 = st.tabs(["➕ Nayi Booking Darj Karein", "🔊 Sound System / Equipment Manage Karein"])

    with book_tab1:
        event_type = st.radio("🎯 Event Type Select Karein", ["Single Date", "Multiple Dates (2 Dates)"], horizontal=True)
        equipment_list = load_equipment()

        with st.form("booking_form", clear_on_submit=True):
            col1, col2 = st.columns(2)
            
            with col1:
                customer_name = st.text_input("👤 Customer Name")
                phone = st.text_input("📞 Mobile Number")
                
            with col2:
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
                    st.session_state.menu_selection = "🏠 Home / Dashboard"
                    st.rerun()
                else:
                    st.error("⚠️ Kripya Customer Name aur Mobile Number zaroor bharein!")

    with book_tab2:
        st.markdown("#### ⚙️ Sound System / Equipment Add, Edit & Delete")
        eq_list_current = load_equipment()
        
        col_eq1, col_eq2 = st.columns(2)
        with col_eq1:
            st.markdown("##### ➕ Naya Equipment Jodein")
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
                    
        with col_eq2:
            st.markdown("##### ✏️ Edit / Delete Existing Equipment")
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
elif st.session_state.menu_selection == "📋 View Bookings":
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
elif st.session_state.menu_selection == "📈 Ledger & Payments":
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
            
            st.info(f"👤 Customer: **{curr_row['Customer Name']}** | 💰 Total: ₹ {float(curr_row['Total Amount']):,.0f} | 💵 Already Paid: ₹ {float(curr_row['Advance Paid']):,.0f} | ⏳ Current Balance Due: ₹ {float(curr_row['Balance Due']):,.0f}")
            
            col_u1, col_u2 = st.columns(2)
            with col_u1:
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
                if st.button("✅ Mark as Fully Paid (Clear All Due)"):
                    df.loc[idx, "Advance Paid"] = float(df.loc[idx, "Total Amount"])
                    df.loc[idx, "Balance Due"] = 0.0
                    df.loc[idx, "Status"] = "Paid"
                    save_data(df)
                    st.success("🎉 Payment Poori Tarah Clear (Paid) Ho Gaya!")
                    st.rerun()

        st.markdown("---")
        col_l1, col_l2, col_l3 = st.columns(3)
        col_l1.info(f"📋 Total Accounts: **{len(df)}**")
        col_l2.warning(f"⏳ Total Balance Due in Market: **₹ {df['Balance Due'].sum():,.0f}**")
        col_l3.success(f"✅ Total Collected Amount: **₹ {df['Advance Paid'].sum():,.0f}**")

# --- 4. EXPENSE & LEDGER PAGE (WITH CLEAR FORM ON SUBMIT) ---
elif st.session_state.menu_selection == "💸 Expense & Ledger":
    st.markdown("### 💸 Kharcha Darj Karein & Profit-Loss Ledger Dekhein")
    
    available_categories = load_categories()
    category_choices = available_categories + ["➕ Add New Category..."]

    exp_tab1, exp_tab2 = st.tabs(["💸 Naya Kharcha Jodein", "⚙️ Expense Categories Manage Karein (Edit/Delete)"])

    with exp_tab1:
        st.markdown("#### 📝 Expense Entry Form")
        
        with st.form("expense_form", clear_on_submit=True):
            col_e1, col_e2 = st.columns(2)
            with col_e1:
                exp_date = st.date_input("📅 Kharche ki Date", value=datetime.today())
                selected_cat_option = st.selectbox("🏷️ Kharche ka Category", category_choices)
                
                new_custom_cat = st.text_input("✨ Naya Category Naam Likhein (Agar upar 'Add New' chuna ho):")

            with col_e2:
                exp_amount = st.number_input("💰 Kharcha Amount (₹)", min_value=0.0, step=100.0)
                exp_desc = st.text_input("💬 Description / Kis kaam ka kharcha tha?")
                st.markdown("<div style='height: 28px;'></div>", unsafe_allow_html=True)
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
        st.markdown("#### ⚙️ Manage Categories (Edit / Delete)")
        if available_categories:
            selected_cat_to_edit = st.selectbox("Kiski category ko edit ya delete karna hai select karein:", available_categories, key="edit_cat_select")
            
            col_ce1, col_ce2 = st.columns(2)
            with col_ce1:
                new_cat_name = st.text_input("✏️ Naya Naam (Badalne ke liye):", value=selected_cat_to_edit)
                if st.button("🔄 Category Update / Edit Karein"):
                    if new_cat_name.strip():
                        idx = available_categories.index(selected_cat_to_edit)
                        available_categories[idx] = new_cat_name.strip()
                        save_all_categories(available_categories)
                        
                        if not df_expenses.empty:
                            df_expenses.loc[df_expenses["Expense Category"] == selected_cat_to_edit, "Expense Category"] = new_cat_name.strip()
                            save_expense_data(df_expenses)
                            
                        st.success(f"✅ Category successfully update ho kar '{new_cat_name.strip()}' ho gayi!")
                        st.rerun()
                    else:
                        st.warning("⚠️ Naam khali nahi ho sakta.")
                        
            with col_ce2:
                st.markdown("<div style='height: 28px;'></div>", unsafe_allow_html=True)
                if st.button("🗑️ Yeh Category Delete Karein"):
                    if len(available_categories) > 1:
                        available_categories.remove(selected_cat_to_edit)
                        save_all_categories(available_categories)
                        st.success(f"🗑️ Category '{selected_cat_to_edit}' ko hata diya gaya hai!")
                        st.rerun()
                    else:
                        st.error("⚠️ Kam se kam ek category honi zaroori hai.")
        else:
            st.info("Koi custom category available nahi hai.")

    st.markdown("---")
    
    # Financial Summary
    st.markdown("### 📊 Professional Financial Summary (P&L Ledger)")
    
    total_income = df["Total Amount"].sum() if not df.empty else 0
    total_expense = df_expenses["Amount"].sum() if not df_expenses.empty else 0
    net_savings = total_income - total_expense
    
    col_f1, col_f2, col_f3 = st.columns(3)
    col_f1.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">💰 Total Kamai (Revenue)</div>
            <div class="metric-value" style="color: #3b82f6;">₹ {total_income:,.0f}</div>
        </div>
    """, unsafe_allow_html=True)
    
    col_f2.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">💸 Total Kharcha (Expenses)</div>
            <div class="metric-value" style="color: #ef4444;">₹ {total_expense:,.0f}</div>
        </div>
    """, unsafe_allow_html=True)
    
    col_f3.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">💎 Shuddh Bachat (Net Profit)</div>
            <div class="metric-value" style="color: #10b981;">₹ {net_savings:,.0f}</div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<div style='margin-top: 20px;'></div>", unsafe_allow_html=True)
    
    if not df_expenses.empty:
        st.markdown("#### 📉 Category-wise Kharcha Breakdown")
        cat_grouped = df_expenses.groupby("Expense Category")["Amount"].sum().reset_index()
        st.dataframe(cat_grouped, use_container_width=True)
        
        st.markdown("#### 📋 Sabhi Kharcho ki Detail List")
        st.dataframe(df_expenses, use_container_width=True)
        
        exp_del_idx = st.number_input("Kisi kharche ki entry ko hatana ho toh uska Row Index dalein:", min_value=0, max_value=max(0, len(df_expenses)-1), step=1, key="del_exp_idx")
        if st.button("🗑️ Selected Kharcha Entry Delete Karein"):
            df_expenses = df_expenses.drop(exp_del_idx).reset_index(drop=True)
            save_expense_data(df_expenses)
            st.success("🗑️ Kharcha record hata diya gaya hai!")
            st.rerun()
    else:
        st.info("ℹ️ Abhi tak koi kharcha darj nahi kiya gaya hai.")

# --- 5. SEARCH & FILTER PAGE ---
elif st.session_state.menu_selection == "🔍 Search & Filter":
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
elif st.session_state.menu_selection == "❌ Delete Booking":
    st.markdown("### 🗑️ Booking Delete Karein")
    
    if df.empty:
        st.info("📭 Delete karne ke liye koi record nahi hai.")
    else:
        display_cols = ["Customer Name", "Phone", "Event Type", "Event Dates", "Advance Paid", "Total Amount", "Balance Due", "Status"]
        st.dataframe(df[display_cols], use_container_width=True)
        
        row_idx = st.number_input("Kahin galti ho gayi? Upar table se Row Index number dalein jise delete karna hai:", min_value=0, max_value=max(0, len(df)-1), step=1)
        
        if st.button("❌ Selected Booking Delete Karein"):
            if len(df) > 0:
                df = df.drop(row_idx).reset_index(drop=True)
                save_data(df)
                st.success(f"🗑️ Row Index {row_idx} ko hata diya gaya hai!")
                st.rerun()

# --- FOOTER ---
st.markdown("---")
st.markdown('<div class="footer-text">Created by Dilip Singh</div>', unsafe_allow_html=True)
