
# Set page config
st.set_page_config(page_title="Life Dashboard", layout="wide")

# Custom background via markdown (optional)
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://images.unsplash.com/photo-1503264116251-35a269479413");
    background-size: cover;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# Sidebar Navigation
with st.sidebar:
    selected = option_menu(
        menu_title="Life Dashboard",
        options=["Pomodoro Timer", "Expense Tracker", "To-Do List", "Medicine Tracker", "Sleep Tracker"],
        icons=["clock", "cash-coin", "list-task", "capsule", "moon-stars"],
        menu_icon="house",
        default_index=0,
    )

# --- Pomodoro Timer ---
if selected == "Pomodoro Timer":
    st.title("🍅 Pomodoro Timer")

    work_time = st.number_input("Work Duration (minutes):", min_value=1, value=25)
    break_time = st.number_input("Break Duration (minutes):", min_value=1, value=5)

    if 'pomodoro_running' not in st.session_state:
        st.session_state.pomodoro_running = False

    def digital_clock():
        now = datetime.now().strftime("%H:%M:%S")
        st.markdown(f"### 🕒 {now}")

    digital_clock()

    if st.button("Start Pomodoro"):
        st.session_state.pomodoro_running = True
        total_time = work_time * 60
        st.success("Work session started!")

        start_time = time.time()
        progress_bar = st.progress(0)
        status_text = st.empty()

        while time.time() - start_time < total_time:
            elapsed = time.time() - start_time
            remaining = int(total_time - elapsed)
            minutes, seconds = divmod(remaining, 60)
            status_text.markdown(f"**Time Remaining:** {minutes:02d}:{seconds:02d}")
            progress_bar.progress(int((elapsed / total_time) * 100))
            digital_clock()
            time.sleep(1)
        st.success("Work session completed! Take a break now. ⏳")

# --- Expense Tracker ---
elif selected == "Expense Tracker":
    st.title("💰 Expense Tracker")

    if 'expenses' not in st.session_state:
        st.session_state.expenses = []

    with st.form("expense_form"):
        date = st.date_input("Date")
        category = st.text_input("Category")
        amount = st.number_input("Amount", min_value=0.0, format="%.2f")
        submitted = st.form_submit_button("Add Expense")
        if submitted:
            st.session_state.expenses.append({"date": date, "category": category, "amount": amount})
            st.success("Expense added!")

    if st.session_state.expenses:
        st.subheader("Expenses")
        for exp in st.session_state.expenses:
            st.write(f"{exp['date']} | {exp['category']} | ₹{exp['amount']:.2f}")

# --- To-Do List ---
elif selected == "To-Do List":
    st.title("📝 To-Do List")

    if 'tasks' not in st.session_state:
        st.session_state.tasks = []

    new_task = st.text_input("Add New Task")
    if st.button("Add Task"):
        if new_task:
            st.session_state.tasks.append({"task": new_task, "done": False})
            st.success("Task added!")

    st.subheader("Tasks:")
    for i, task in enumerate(st.session_state.tasks):
        col1, col2 = st.columns([0.85, 0.15])
        with col1:
            st.write(task["task"])
        with col2:
            if st.checkbox("Done", key=f"task_{i}"):
                st.session_state.tasks[i]["done"] = True

# --- Medicine Tracker ---
elif selected == "Medicine Tracker":
    st.title("💊 Daily Medicine Tracker")

    if 'medicines' not in st.session_state:
        st.session_state.medicines = []

    with st.form("medicine_form"):
        med_name = st.text_input("Medicine Name")
        med_time = st.time_input("Time to take")
        med_submit = st.form_submit_button("Add Medicine")
        if med_submit:
            st.session_state.medicines.append({"name": med_name, "time": med_time, "taken": False})
            st.success("Medicine added!")

    if st.session_state.medicines:
        st.subheader("Today's Medicines:")
        for i, med in enumerate(st.session_state.medicines):
            col1, col2, col3 = st.columns([0.5, 0.3, 0.2])
            with col1:
                st.write(f"{med['name']}")
            with col2:
                st.write(f"{med['time'].strftime('%H:%M')}")
            with col3:
                if st.checkbox("Taken", key=f"med_{i}"):
                    st.session_state.medicines[i]["taken"] = True

# --- Sleep Tracker ---
elif selected == "Sleep Tracker":
    st.title("🌙 Sleep Tracker")

    if 'sleep_log' not in st.session_state:
        st.session_state.sleep_log = []

    with st.form("sleep_form"):
        sleep_date = st.date_input("Date")
        sleep_time = st.time_input("Sleep Time")
        wake_time = st.time_input("Wake Up Time")
        sleep_submit = st.form_submit_button("Log Sleep")
        if sleep_submit:
            duration = (datetime.combine(datetime.today(), wake_time) - datetime.combine(datetime.today(), sleep_time)).seconds / 3600
            if duration < 0:
                duration += 24
            st.session_state.sleep_log.append({"date": sleep_date, "sleep": sleep_time, "wake": wake_time, "duration": duration})
            st.success(f"Sleep logged ({duration:.2f} hours)")

    if st.session_state.sleep_log:
        st.subheader("Sleep Records:")
        for log in st.session_state.sleep_log:
            st.write(f"{log['date']} | Sleep: {log['sleep'].strftime('%H:%M')} | Wake: {log['wake'].strftime('%H:%M')} | {log['duration']:.2f} hours")

