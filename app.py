import streamlit as st
import pandas as pd
from datetime import datetime
import os

# Page Configuration
st.set_page_config(
    page_title="PUJA DJ KING - Pro Booking Manager", 
    page_icon="🎧", 
    layout="wide"
)

# Database file
DB_FILE = "puja_dj_bookings.csv"

def load_data():
    if os.path.exists(DB_FILE):
        return pd.read_csv(DB_FILE)
    else:
        return pd.DataFrame(columns=[
            "Customer Name", "Phone", "Event Dates", "Equipment Items", 
            "Advance Paid", "Total Amount", "Balance Due", "Status", "Remarks"
        ])

def save_data(df):
    df.to_csv(DB_FILE, index=False)

df = load_data()

# Header Branding
st.title("🎧 PUJA DJ KING 🎧")
st.markdown("### **Professional Sound System & Event Management System**")
st.markdown("---")

# Sidebar Navigation
st.sidebar.markdown("## 🎛️ Navigation Menu")
menu = st.sidebar.radio("Go to", ["📅 Check Availability", "➕ New Booking", "🔍 Search by Mobile No.", "📋 All Bookings List"])

# 1. Check Availability
if menu == "📅 Check Availability":
    st.header("🔍 Date Availability Check Karein")
    selected_date = st.date_input("Select Event Date", datetime.today())
    selected_date_str = selected_date.strftime("%Y-%m-%d")
    
    if not df.empty:
        matched_rows = df[df["Event Dates"].astype(str).str.contains(selected_date_str)]
        
        if not matched_rows.empty:
            st.error(f"❌ **Status:** {selected_date_str} ko sound system **ALREADY BOOKED** hai!")
            st.markdown("### 📋 Booking Details:")
            st.dataframe(matched_rows, use_container_width=True)
        else:
            st.success(f"✅ **Status:** {selected_date_str} bilkul **KHALI** hai! Aap booking le sakte hain.")
            
        st.markdown("---")
        st.subheader("📊 Business Summary")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Bookings", len(df))
        with col2:
            total_revenue = df["Total Amount"].sum() if "Total Amount" in df.columns else 0
            st.metric("Total Business Value", f"₹ {total_revenue}")
        with col3:
            total_advance = df["Advance Paid"].sum() if "Advance Paid" in df.columns else 0
            st.metric("Total Advance Received", f"₹ {total_advance}")
    else:
        st.info("Abhi tak system me koi booking darj nahi hai.")

# 2. New Booking
elif menu == "➕ New Booking":
    st.header("📝 Nayi Booking Darj Karein (Pro Form)")
    
    with st.form("booking_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        with col1:
            c_name = st.text_input("Customer Name (ग्राहक का नाम)")
            c_phone = st.text_input("Phone Number (मोबाइल नंबर)")
        with col2:
            status = st.selectbox("Booking Status", ["Confirmed", "Pending", "Completed"])
            remarks = st.text_input("Remarks / Notes (विशेष नोट या पता)")

        st.markdown("---")
        st.subheader("🎶 Sound Equipments & Items (Kya-kya lagana hai?)")
        
        equipments = st.multiselect(
            "Select Sound Items:",
            ["Double Base (JBL/Dual)", "Single Base", "Top Box (Double Horn)", "DJ Mixer & Player", "Generator", "Lighting / Fog Machine", "Mic Setup / Cordless", "Full Setup (Heavy)"]
        )
        custom_equipment = st.text_input("Other Items (Agar kuch aur alag se ho toh yahan likhein)")

        st.markdown("---")
        st.subheader("📅 Event Dates Selection")
        
        # Radio button to switch between Single and Double dates inside form
        num_dates = st.radio("Kitni tarikh ki booking hai?", ["Single Date", "Double / Multiple Dates"])
        
        event_dates_list = []
        if num_dates == "Single Date":
            single_date = st.date_input("Event Date", datetime.today())
            event_dates_list.append(single_date.strftime("%Y-%m-%d"))
        else:
            col_d1, col_d2 = st.columns(2)
            with col_d1:
                d1 = st.date_input("Pehli Date (First Date)", datetime.today())
            with col_d2:
                d2 = st.date_input("Doosri Date (Second Date)", datetime.today())
            event_dates_list = [d1.strftime("%Y-%m-%d"), d2.strftime("%Y-%m-%d")]

        st.markdown("---")
        col3, col4 = st.columns(2)
        with col3:
            advance_paid = st.number_input("Advance Payment (₹)", min_value=0.0, step=500.0)
        with col4:
            total_amount = st.number_input("Total Amount (₹)", min_value=0.0, step=500.0)

        submit = st.form_submit_button("💾 Save Booking")
        
        if submit:
            if c_name and c_phone:
                date_str_combined = ", ".join(event_dates_list)
                all_items_str = ", ".join(equipments)
                if custom_equipment:
                    all_items_str += f", {custom_equipment}"
                
                balance_due = total_amount - advance_paid

                new_row = {
                    "Customer Name": c_name,
                    "Phone": c_phone,
                    "Event Dates": date_str_combined,
                    "Equipment Items": all_items_str if all_items_str else "Standard Sound Setup",
                    "Advance Paid": advance_paid,
                    "Total Amount": total_amount,
                    "Balance Due": balance_due,
                    "Status": status,
                    "Remarks": remarks if remarks else "None"
                }
                df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
                save_data(df)
                st.success("🎉 Booking successfully save ho gayi hai!")
            else:
                st.error("Kripya Customer Name aur Phone Number zaroor bharein.")

# 3. Search by Mobile Number
elif menu == "🔍 Search by Mobile No.":
    st.header("🔍 Customer Search by Mobile Number")
    search_phone = st.text_input("Customer ka Mobile Number dalein:")
    
    if search_phone:
        if not df.empty:
            result_df = df[df["Phone"].astype(str).str.contains(search_phone)]
            if not result_df.empty:
                st.success(f"mil gaye {len(result_df)} booking(s) is number par:")
                st.dataframe(result_df, use_container_width=True)
            else:
                st.warning("Is mobile number par koi booking nahi mili.")
        else:
            st.info("Database khali hai.")

# 4. All Bookings List
elif menu == "📋 All Bookings List":
    st.header("📋 Sabhi Bookings ki List")
    
    if not df.empty:
        st.dataframe(df, use_container_width=True)
        
        st.markdown("---")
        st.subheader("❌ Booking Delete Karein")
        delete_index = st.number_input("Row Index Number Dalein Delete karne ke liye", min_value=0, max_value=max(0, len(df)-1), step=1)
        
        if st.button("Delete Selected Booking"):
            df = df.drop(delete_index).reset_index(drop=True)
            save_data(df)
            st.success("Booking hata di gayi hai! Page refresh karein.")
    else:
        st.info("Abhi tak koi booking record available nahi hai.")