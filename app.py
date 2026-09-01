import streamlit as st
import pandas as pd
import os
import uuid
from datetime import datetime, date
import urllib.parse

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
        margin-bottom: 12px;
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
    
    /* Hide Default Sidebar */
    section[data-testid="stSidebar"] {
        display: none;
    }
    
    /* Footer */
    .footer-text {
        text-align: center;
        color: #64748b;
        font-size: 0.8rem;
        font-weight: 700;
        margin-top: 15px;
        margin-bottom: 10px;
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

# --- FILE & DIRECTORY HANDLING ---
CSV_FILE = "puja_dj_bookings.csv"
EXPENSE_CSV_FILE = "puja_dj_expenses.csv"
CATEGORIES_CSV_FILE = "puja_dj_expense_categories.csv"
EQUIPMENT_CSV_FILE = "puja_dj_equipment_list.csv"
GALLERY_CSV_FILE = "puja_dj_gallery.csv"
MEDIA_FOLDER = "gallery_media"

if not os.path.exists(MEDIA_FOLDER):
    os.makedirs(MEDIA_FOLDER)

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

def load_gallery_data():
    if os.path.exists(GALLERY_CSV_FILE):
        df_gal = pd.read_csv(GALLERY_CSV_FILE)
        expected_cols = ["ID", "Type", "Category", "Title", "Source", "Date_Added"]
        for col in expected_cols:
            if col not in df_gal.columns:
                if col == "Category":
                    df_gal[col] = "General Events"
                else:
                    df_gal[col] = ""
        return df_gal
    else:
        return pd.DataFrame(columns=["ID", "Type", "Category", "Title", "Source", "Date_Added"])

def save_gallery_data(df_gal):
    df_gal.to_csv(GALLERY_CSV_FILE, index=False)

df = load_data()
df_expenses = load_expense_data()
df_gallery = load_gallery_data()

if "current_tab" not in st.session_state:
    st.session_state.current_tab = "🏠 Dashboard"

if "show_notifications" not in st.session_state:
    st.session_state.show_notifications = False

# --- TOP HEADER SECTION ---
st.markdown("""
    <div class="top-header-container">
        <div class="welcome-text">Welcome Back</div>
        <div class="brand-title">🎧 PUJA DJ KING</div>
        <div class="brand-subtitle">Professional Sound System & Event Management</div>
    </div>
""", unsafe_allow_html=True)

# --- TOP NAVIGATION TABS ---
menu_options = [
    "🏠 Dashboard",
    "➕ New Booking", 
    "📋 Bookings", 
    "📈 Ledger", 
    "💸 Expenses", 
    "🖼️ Gallery",
    "🔍 Search", 
    "❌ Delete"
]

selected_menu = st.selectbox("📂 Control Panel Menu", menu_options, index=menu_options.index(st.session_state.current_tab) if st.session_state.current_tab in menu_options else 0, label_visibility="collapsed")

if selected_menu != st.session_state.current_tab:
    st.session_state.current_tab = selected_menu
    st.session_state.show_notifications = False
    st.rerun()

st.markdown("<div style='margin-bottom: 10px;'></div>", unsafe_allow_html=True)

# --- CONDITIONAL NOTIFICATIONS & ALERTS ---
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

# --- SHARED GALLERY RENDER FUNCTION (Mobile Upload Bug Fixed) ---
def render_gallery_section():
    global df_gallery
    
    selected_media_type = st.radio(
        "🎯 Kya dekhna chahte hain?", 
        ["Photo 📷", "Video 🎥"], 
        horizontal=True, 
        key="shared_media_type_select"
    )
    
    type_str = "Photo" if "Photo" in selected_media_type else "Video"
    type_filtered_df = df_gallery[df_gallery["Type"] == type_str]
    
    st.markdown("---")
    
    action_tabs = st.tabs([
        "👁️ View Gallery", 
        "➕ Add Media", 
        "✏️ Modify Media", 
        "🗑️ Delete Media"
    ])
    
    # --- SUB-TAB 1: VIEW CATEGORY-WISE MEDIA ---
    with action_tabs[0]:
        if type_filtered_df.empty:
            st.warning(f"Is category ({type_str}) me abhi koi media uplabdh nahi hai.")
        else:
            available_cats = type_filtered_df["Category"].dropna().unique().tolist()
            selected_category = st.selectbox(
                f"📂 {type_str} ki Category Select Karein:", 
                available_cats, 
                key=f"shared_cat_select_{type_str}"
            )
            
            final_filtered_df = type_filtered_df[type_filtered_df["Category"] == selected_category]
            st.markdown(f"#### 📁 Showing {type_str}s under: **{selected_category}** ({len(final_filtered_df)} items)")
            
            if final_filtered_df.empty:
                st.info("Is category me koi items nahi hain.")
            else:
                cols = st.columns(2)
                for i, (_, row) in enumerate(final_filtered_df.iterrows()):
                    with cols[i % 2]:
                        st.markdown(f"##### {row['Title']}")
                        st.caption(f"📅 Added: {row['Date_Added']} | Category: {row['Category']}")
                        
                        source = row["Source"]
                        if row["Type"] == "Photo":
                            if os.path.exists(source):
                                st.image(source, use_container_width=True)
                            else:
                                st.error("❌ Photo File nahi mili.")
                        elif row["Type"] == "Video":
                            if source.startswith("http://") or source.startswith("https://"):
                                embed_url = source
                                if "youtube.com/watch?v=" in source:
                                    video_id = source.split("watch?v=")[1].split("&")[0]
                                    embed_url = f"https://www.youtube.com/embed/{video_id}"
                                elif "youtu.be/" in source:
                                    video_id = source.split("youtu.be/")[1].split("?")[0]
                                    embed_url = f"https://www.youtube.com/embed/{video_id}"
                                elif "youtube.com/shorts/" in source:
                                    video_id = source.split("shorts/")[1].split("?")[0]
                                    embed_url = f"https://www.youtube.com/embed/{video_id}"
                                    
                                st.markdown(f"""
                                    <iframe width="100%" height="250" src="{embed_url}" 
                                    title="YouTube video player" frameborder="0" 
                                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
                                    allowfullscreen style="border-radius: 12px;"></iframe>
                                """, unsafe_allow_html=True)
                            elif os.path.exists(source):
                                st.video(source)
                            else:
                                st.error("❌ Video file ya link invalid hai.")
                        
                        with st.expander(f"📤 WhatsApp par Share Karein ({row['Title']})"):
                            wa_phone = st.text_input("WhatsApp Mobile Number (e.g., 919876543210):", key=f"shared_wa_phone_{row['ID']}")
                            share_msg = f"🎧 *PUJA DJ KING* \nCheck out our {row['Type']}: *{row['Title']}* ({row['Category']})\nLink/Details: {source}"
                            
                            if st.button("💬 Send to WhatsApp", key=f"shared_wa_btn_{row['ID']}"):
                                if wa_phone.strip():
                                    encoded_msg = urllib.parse.quote(share_msg)
                                    wa_url = f"https://api.whatsapp.com/send?phone={wa_phone.strip()}&text={encoded_msg}"
                                    st.markdown(f'''
                                        <a href="{wa_url}" target="_blank">
                                            <button style="background-color: #25D366; color: white; padding: 10px 20px; border: none; border-radius: 10px; font-weight: bold; width: 100%; cursor: pointer;">
                                                👉 Click Here to Open WhatsApp & Send Message
                                            </button>
                                        </a>
                                    ''', unsafe_allow_html=True)
                                else:
                                    st.warning("⚠️ Kripya valid WhatsApp mobile number enter karein.")
                        st.markdown("---")

    # --- SUB-TAB 2: ADD MEDIA (Mobile Friendly without st.form) ---
    with action_tabs[1]:
        default_photo_cats = ["Stage Setup", "Birthday Party", "Wedding Ceremony", "Live Concert", "Other Photos"]
        default_video_cats = ["DJ Remix Reels", "Stage Performance", "Full Party Video", "Other Videos"]
        
        cat_options = default_photo_cats if type_str == "Photo" else default_video_cats
        
        st.markdown(f"#### ➕ Add New {type_str}")
        media_title = st.text_input("🖼️ Title / Description Likhein:", key="mob_media_title")
        selected_cat = st.selectbox("📂 Category Select Karein:", cat_options, key="mob_sel_cat")
        custom_cat = st.text_input("✨ Ya Naya Category Naam Likhein (Optional):", key="mob_custom_cat")
        
        uploaded_file = None
        video_url = ""
        
        if type_str == "Photo":
            uploaded_file = st.file_uploader("📷 Photo File Upload Karein (JPG, PNG)", type=["jpg", "jpeg", "png"], key="mob_photo_up")
        else:
            v_choice = st.radio("Video Source:", ["YouTube / Web Link 🔗", "Upload Video File 📁"], horizontal=True, key="mob_v_choice")
            if v_choice == "YouTube / Web Link 🔗":
                video_url = st.text_input("🔗 YouTube / Shorts URL:", placeholder="https://www.youtube.com/watch?v=...", key="mob_v_url")
            else:
                uploaded_file = st.file_uploader("🎥 Video File Upload Karein (MP4)", type=["mp4", "mov"], key="mob_v_file")
        
        st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)
        submit_media = st.button("💾 Media Save Karein", key="mob_save_media_btn")
        
        if submit_media:
            final_category = custom_cat.strip() if custom_cat.strip() else selected_cat
            file_id = uuid.uuid4().hex[:8]
            saved_source = ""
            
            if type_str == "Photo":
                if uploaded_file is not None and media_title.strip() != "":
                    ext = uploaded_file.name.split(".")[-1]
                    saved_source = os.path.join(MEDIA_FOLDER, f"photo_{file_id}.{ext}")
                    with open(saved_source, "wb") as f:
                        f.write(uploaded_file.getbuffer())
                else:
                    st.warning("⚠️ Kripya Title aur Photo file dono select karein.")
            else:
                if video_url.strip() and media_title.strip():
                    saved_source = video_url.strip()
                elif uploaded_file is not None and media_title.strip() != "":
                    ext = uploaded_file.name.split(".")[-1]
                    saved_source = os.path.join(MEDIA_FOLDER, f"video_{file_id}.{ext}")
                    with open(saved_source, "wb") as f:
                        f.write(uploaded_file.getbuffer())
                else:
                    st.warning("⚠️ Kripya Title aur Video (Link ya File) dono dein.")
            
            if media_title.strip() and saved_source:
                new_media_row = pd.DataFrame({
                    "ID": [file_id],
                    "Type": [type_str],
                    "Category": [final_category],
                    "Title": [media_title.strip()],
                    "Source": [saved_source],
                    "Date_Added": [str(date.today())]
                })
                df_gallery = pd.concat([df_gallery, new_media_row], ignore_index=True)
                save_gallery_data(df_gallery)
                st.success("✅ Media Safalpurvak Add Ho Gaya!")
                st.rerun()

    # --- SUB-TAB 3: MODIFY MEDIA ---
    with action_tabs[2]:
        st.markdown(f"#### ✏️ Modify Existing {type_str}")
        if type_filtered_df.empty:
            st.info("📭 Modify karne ke liye koi media nahi hai.")
        else:
            media_options = type_filtered_df["ID"].astype(str) + " - " + type_filtered_df["Title"].astype(str) + " (" + type_filtered_df["Category"].astype(str) + ")"
            selected_media_mod = st.selectbox("Badalne ke liye Media Select Karein:", media_options, key=f"shared_mod_select_{type_str}")
            
            if selected_media_mod:
                mod_id = selected_media_mod.split(" - ")[0]
                row_idx = df_gallery[df_gallery["ID"] == mod_id].index[0]
                current_media = df_gallery.loc[row_idx]
                
                updated_title = st.text_input("✏️ Title Edit Karein:", value=current_media["Title"], key=f"shared_mod_title_{type_str}")
                updated_cat = st.text_input("📂 Category Edit Karein:", value=current_media["Category"], key=f"shared_mod_cat_{type_str}")
                
                if current_media["Type"] == "Video" and (current_media["Source"].startswith("http://") or current_media["Source"].startswith("https://")):
                    updated_source = st.text_input("🔗 Video URL Edit Karein:", value=current_media["Source"], key=f"shared_mod_src_{type_str}")
                else:
                    updated_source = current_media["Source"]
                    st.info(f"📁 Local File Path: `{current_media['Source']}`")
                
                if st.button("🔄 Update Media Info", key=f"shared_mod_btn_{type_str}"):
                    if updated_title.strip() and updated_cat.strip():
                        df_gallery.loc[row_idx, "Title"] = updated_title.strip()
                        df_gallery.loc[row_idx, "Category"] = updated_cat.strip()
                        df_gallery.loc[row_idx, "Source"] = updated_source.strip()
                        save_gallery_data(df_gallery)
                        st.success("✅ Media Information Modify Ho Gayi!")
                        st.rerun()
                    else:
                        st.warning("⚠️ Fields khali nahi ho sakte.")

    # --- SUB-TAB 4: DELETE MEDIA ---
    with action_tabs[3]:
        st.markdown(f"#### 🗑️ Delete {type_str}")
        if type_filtered_df.empty:
            st.info("📭 Delete karne ke liye koi media nahi hai.")
        else:
            media_options_del = type_filtered_df["ID"].astype(str) + " - " + type_filtered_df["Title"].astype(str) + " (" + type_filtered_df["Category"].astype(str) + ")"
            selected_media_del = st.selectbox("Delete karne ke liye Select Karein:", media_options_del, key=f"shared_del_select_{type_str}")
            
            if st.button("❌ Selected Item Delete Karein", key=f"shared_del_btn_{type_str}"):
                del_id = selected_media_del.split(" - ")[0]
                row_idx = df_gallery[df_gallery["ID"] == del_id].index[0]
                source_path = df_gallery.loc[row_idx, "Source"]
                
                if not source_path.startswith("http://") and not source_path.startswith("https://") and os.path.exists(source_path):
                    try:
                        os.remove(source_path)
                    except:
                        pass
                
                df_gallery = df_gallery.drop(row_idx).reset_index(drop=True)
                save_gallery_data(df_gallery)
                st.success("🗑️ Media Item Gallery se hata diya gaya hai!")
                st.rerun()

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

    st.markdown("---")
    st.markdown("### 🖼️ Gallery")
    render_gallery_section()

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

# --- 5. DEDICATED GALLERY TAB ---
elif st.session_state.current_tab == "🖼️ Gallery":
    st.markdown("### 🖼️ Gallery Management")
    render_gallery_section()

# --- 6. SEARCH & FILTER PAGE ---
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

# --- 7. DELETE BOOKING PAGE ---
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
col_footer_left, col_footer_center = st.columns([1, 3])

with col_footer_left:
    bell_label = "🔔" if not st.session_state.show_notifications else "❌"
    if st.button(bell_label, help="View Alerts / Notifications"):
        st.session_state.show_notifications = not st.session_state.show_notifications
        st.rerun()

with col_footer_center:
    st.markdown('<div class="footer-text">Created by Dilip Singh</div>', unsafe_allow_html=True)
