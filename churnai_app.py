import streamlit as st
import time

# ─── Page Config ───
st.set_page_config(page_title="ChurnAI Neural Engine", page_icon="🧠", layout="wide")

# ─── Dark Cyberpunk CSS ───
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Space+Grotesk:wght@400;500;600;700&display=swap');

/* Global dark background */
.stApp {
    background: #0a0e1a;
    background-image: radial-gradient(circle at 1px 1px, rgba(56,189,248,0.04) 1px, transparent 0);
    background-size: 32px 32px;
    color: #e2e8f0;
    font-family: 'Inter', sans-serif;
}
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, rgba(8,12,24,0.98), rgba(5,8,18,0.99));
    border-right: 1px solid rgba(56,189,248,0.08);
}
[data-testid="stSidebar"] * { color: #94a3b8 !important; }
[data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3,
[data-testid="stSidebar"] .sidebar-title { color: #cbd5e1 !important; }

/* Hide default header/footer */
header[data-testid="stHeader"] { background: transparent; }
footer { display: none; }

/* Glass card */
.glass-card {
    background: linear-gradient(135deg, rgba(15,23,42,0.7), rgba(15,23,42,0.4));
    backdrop-filter: blur(24px);
    border: 1px solid rgba(56,189,248,0.1);
    border-radius: 16px;
    padding: 28px;
    margin-bottom: 16px;
    position: relative;
}
.glass-card::before {
    content: '';
    position: absolute;
    inset: 0;
    border-radius: 16px;
    padding: 1px;
    background: linear-gradient(135deg, rgba(56,189,248,0.2), rgba(139,92,246,0.2));
    -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
    -webkit-mask-composite: xor;
    mask-composite: exclude;
    pointer-events: none;
}

/* Section header */
.section-icon {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 36px; height: 36px;
    border-radius: 12px;
    background: rgba(56,189,248,0.12);
    margin-right: 12px;
    vertical-align: middle;
}
.section-icon-accent { background: rgba(139,92,246,0.12); }
.section-header {
    font-family: 'Space Grotesk', sans-serif;
    font-weight: 600;
    font-size: 1.1rem;
    color: #e2e8f0;
    display: flex;
    align-items: center;
    margin-bottom: 4px;
}
.section-sub {
    font-size: 0.7rem;
    color: #64748b;
    margin-left: 48px;
    margin-bottom: 18px;
}

/* Badge */
.badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 6px 16px;
    border-radius: 9999px;
    background: rgba(56,189,248,0.08);
    border: 1px solid rgba(56,189,248,0.15);
    font-size: 0.7rem;
    font-weight: 500;
    color: #38bdf8;
    letter-spacing: 0.05em;
    margin-bottom: 12px;
}
.badge-dot {
    width: 6px; height: 6px;
    border-radius: 50%;
    background: #38bdf8;
    animation: pulse-dot 2s ease-in-out infinite;
}

/* Title */
.glow-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 2.8rem;
    font-weight: 700;
    color: #e2e8f0;
    text-align: center;
    line-height: 1.1;
}
.glow-title span {
    color: #38bdf8;
    text-shadow: 0 0 30px rgba(56,189,248,0.6), 0 0 80px rgba(56,189,248,0.25);
}
.subtitle {
    text-align: center;
    color: #64748b;
    font-size: 0.88rem;
    max-width: 540px;
    margin: 10px auto 0;
    line-height: 1.6;
}

/* Metric boxes */
.metric-box {
    background: linear-gradient(135deg, rgba(56,189,248,0.08), rgba(56,189,248,0.03));
    border: 1px solid rgba(56,189,248,0.1);
    border-radius: 14px;
    padding: 20px;
    text-align: center;
}
.metric-box-accent {
    background: linear-gradient(135deg, rgba(139,92,246,0.08), rgba(139,92,246,0.03));
    border: 1px solid rgba(139,92,246,0.1);
}
.metric-value {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 2.2rem;
    font-weight: 700;
    color: #38bdf8;
    text-shadow: 0 0 20px rgba(56,189,248,0.5);
}
.metric-value-accent { color: #a78bfa; text-shadow: none; }
.metric-label {
    font-size: 0.65rem;
    color: #64748b;
    margin-top: 6px;
    text-transform: uppercase;
    letter-spacing: 0.1em;
}

/* Risk alert */
.risk-alert {
    background: rgba(239,68,68,0.08);
    border: 1px solid rgba(239,68,68,0.15);
    border-radius: 14px;
    padding: 16px 20px;
    display: flex;
    align-items: center;
    gap: 14px;
}
.risk-icon {
    width: 34px; height: 34px;
    border-radius: 10px;
    background: rgba(239,68,68,0.12);
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    font-size: 1rem;
}

/* Recommendation */
.recommendation {
    background: rgba(56,189,248,0.04);
    border: 1px solid rgba(56,189,248,0.08);
    border-radius: 14px;
    padding: 14px 18px;
    font-size: 0.8rem;
    color: #94a3b8;
}

/* Param row */
.param-row {
    background: rgba(30,41,59,0.4);
    border-radius: 14px;
    padding: 16px 20px;
    margin-bottom: 8px;
    transition: background 0.2s;
}
.param-row:hover { background: rgba(30,41,59,0.6); }
.param-label {
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 0.85rem;
    color: #94a3b8;
    font-weight: 500;
}
.param-value {
    font-family: 'Space Grotesk', sans-serif;
    font-weight: 700;
    color: #38bdf8;
    font-size: 0.9rem;
}

/* Skill card */
.skill-card {
    border-radius: 16px;
    padding: 22px;
    border: 1px solid rgba(56,189,248,0.06);
    transition: all 0.4s;
    cursor: default;
}
.skill-card:hover {
    box-shadow: 0 0 24px rgba(56,189,248,0.25), 0 0 80px rgba(56,189,248,0.08);
    transform: translateY(-2px);
}
.skill-icon {
    width: 34px; height: 34px;
    border-radius: 10px;
    background: rgba(15,23,42,0.6);
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 10px;
    font-size: 1rem;
}
.skill-label { font-size: 0.9rem; font-weight: 600; color: #e2e8f0; }
.skill-desc { font-size: 0.75rem; color: #64748b; margin-top: 4px; }

/* Status bar */
.status-bar {
    background: linear-gradient(90deg, rgba(56,189,248,0.06), rgba(139,92,246,0.06));
    border: 1px solid rgba(56,189,248,0.08);
    border-radius: 14px;
    padding: 10px 16px;
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 0.7rem;
    color: #64748b;
    font-weight: 500;
}

/* Model info dots */
.model-item {
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 0.8rem;
    color: #64748b;
    margin-bottom: 4px;
}
.model-dot {
    width: 4px; height: 4px;
    border-radius: 50%;
    background: rgba(56,189,248,0.5);
}

/* Awaiting state */
.await-icon {
    width: 80px; height: 80px;
    border-radius: 16px;
    background: linear-gradient(135deg, rgba(56,189,248,0.15), rgba(139,92,246,0.15));
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 0 auto 20px;
    font-size: 2rem;
    animation: float 4s ease-in-out infinite;
}

/* Override Streamlit widgets for dark theme */
.stSlider label, .stSelectbox label, .stNumberInput label { color: #94a3b8 !important; font-size: 0.85rem !important; }
.stSlider [data-testid="stTickBarMin"], .stSlider [data-testid="stTickBarMax"] { color: #475569 !important; }
div[data-baseweb="select"] { background: rgba(30,41,59,0.6) !important; border-color: rgba(56,189,248,0.15) !important; }
.stNumberInput input { background: rgba(30,41,59,0.6) !important; border-color: rgba(56,189,248,0.15) !important; color: #e2e8f0 !important; }
button[kind="primary"] {
    background: linear-gradient(135deg, #0ea5e9, #38bdf8) !important;
    box-shadow: 0 0 24px rgba(56,189,248,0.4), 0 0 80px rgba(56,189,248,0.15) !important;
    border: none !important;
    font-weight: 600 !important;
}
button[kind="secondary"] {
    background: transparent !important;
    border: 1px solid rgba(56,189,248,0.2) !important;
    color: #94a3b8 !important;
}
button[kind="secondary"]:hover {
    box-shadow: 0 0 20px rgba(56,189,248,0.25) !important;
}

/* Animations */
@keyframes float {
    0%, 100% { transform: translateY(0px); }
    50% { transform: translateY(-8px); }
}
@keyframes pulse-dot {
    0%, 100% { opacity: 0.4; }
    50% { opacity: 1; }
}
</style>
""", unsafe_allow_html=True)


# ─── Sidebar ───
with st.sidebar:
    st.markdown("""
    <div style="display:flex;align-items:center;gap:12px;margin-bottom:24px;">
        <div style="width:36px;height:36px;border-radius:12px;background:rgba(56,189,248,0.12);display:flex;align-items:center;justify-content:center;font-size:1.1rem;">🧠</div>
        <div>
            <div style="font-family:'Space Grotesk';font-weight:600;color:#cbd5e1;font-size:0.95rem;">ChurnAI</div>
            <div style="font-size:0.65rem;color:#475569;">Neural Engine</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("🧠 **AI Assistant**")
    live_support = st.toggle("Enable Live Support", value=False)

    st.markdown("---")
    st.markdown("⚙️ **System Settings**")
    neural_sync = st.checkbox("Neural Sync Active", value=True)
    high_precision = st.checkbox("High Precision Mode", value=True)

    st.markdown("---")
    st.markdown("⚡ **Model Info**")
    for m in ["Logistic Regression", "Decision Trees", "ROC-AUC Evaluation"]:
        st.markdown(f'<div class="model-item"><div class="model-dot"></div>{m}</div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div class="status-bar">
        <div style="width:8px;height:8px;border-radius:50%;background:#38bdf8;animation:pulse-dot 2s ease-in-out infinite;"></div>
        All systems operational
    </div>
    """, unsafe_allow_html=True)


# ─── Header Badge ───
st.markdown('<div style="text-align:center;padding-top:16px;">', unsafe_allow_html=True)
st.markdown('<div class="badge"><div class="badge-dot"></div>POWERED BY NEURAL NETWORKS</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ─── Title ───
st.markdown('<p class="glow-title">Churn<span>AI</span> Neural Engine</p>', unsafe_allow_html=True)
st.markdown(
    '<p class="subtitle">Predict which customers are likely to stop using a service '
    'based on their historical behavior using advanced classification models.</p>',
    unsafe_allow_html=True,
)
st.write("")
st.write("")

# ─── Main Grid ───
col_params, col_analysis = st.columns(2, gap="large")

# ── Customer Parameters ──
with col_params:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-header"><div class="section-icon">📋</div>Customer Parameters</div>'
        '<div class="section-sub">Configure input features</div>',
        unsafe_allow_html=True,
    )

    st.markdown('<div class="param-row">', unsafe_allow_html=True)
    tenure = st.slider("📅 Tenure (Months)", 0, 72, 24)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="param-row">', unsafe_allow_html=True)
    monthly = st.slider("💰 Monthly Charges ($)", 0, 150, 65)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="param-row">', unsafe_allow_html=True)
    contract = st.selectbox("📄 Contract Type", ["Month-to-Month", "One Year", "Two Year"])
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="param-row">', unsafe_allow_html=True)
    total = st.number_input("💵 Total Charges ($)", value=1560, step=100)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# ── Analysis Panel ──
with col_analysis:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-header"><div class="section-icon section-icon-accent">📊</div>Intelligence Analysis</div>'
        '<div class="section-sub">ML-powered predictions</div>',
        unsafe_allow_html=True,
    )

    if "analyzed" not in st.session_state:
        st.session_state.analyzed = False

    if not st.session_state.analyzed:
        st.markdown("""
        <div style="text-align:center;padding:20px 0;">
            <div class="await-icon">📈</div>
            <p style="color:#94a3b8;font-size:0.95rem;margin-bottom:4px;">Awaiting Neural Data Input</p>
            <p style="color:#475569;font-size:0.8rem;">Configure parameters and run prediction</p>
        </div>
        """, unsafe_allow_html=True)

        c1, c2, c3 = st.columns([1, 2, 1])
        with c2:
            if st.button("✨ Run Prediction", use_container_width=True, type="primary"):
                with st.spinner("Processing neural pathways..."):
                    time.sleep(2)
                st.session_state.analyzed = True
                st.rerun()
    else:
        # Risk alert
        st.markdown("""
        <div class="risk-alert">
            <div class="risk-icon">⚠️</div>
            <div>
                <div style="font-weight:600;color:#e2e8f0;font-size:0.9rem;">High Churn Risk</div>
                <div style="font-size:0.78rem;color:#64748b;">78% probability of churning within 30 days</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.write("")

        # Metrics
        m1, m2 = st.columns(2)
        with m1:
            st.markdown("""
            <div class="metric-box">
                <div class="metric-value">78%</div>
                <div class="metric-label">Churn Probability</div>
            </div>
            """, unsafe_allow_html=True)
        with m2:
            st.markdown("""
            <div class="metric-box metric-box-accent">
                <div class="metric-value metric-value-accent">0.85</div>
                <div class="metric-label">ROC-AUC Score</div>
            </div>
            """, unsafe_allow_html=True)

        st.write("")

        # Risk factors
        st.markdown("""
        <div style="background:rgba(30,41,59,0.4);border-radius:14px;padding:18px 22px;">
            <p style="font-size:0.7rem;font-weight:600;color:#e2e8f0;text-transform:uppercase;letter-spacing:0.1em;margin-bottom:14px;">Key Risk Factors</p>
        """, unsafe_allow_html=True)

        risk_factors = [
            ("Month-to-month contract", 92, "#ef4444"),
            ("Low tenure (< 24 months)", 76, "#f59e0b"),
            ("High monthly charges", 64, "#38bdf8"),
        ]
        for label, impact, color in risk_factors:
            c1, c2, c3 = st.columns([3, 4, 1])
            with c1:
                st.caption(label)
            with c2:
                st.progress(impact / 100)
            with c3:
                st.markdown(f'<span style="color:{color};font-weight:700;font-size:0.85rem;">{impact}%</span>', unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

        st.write("")
        st.markdown("""
        <div class="recommendation">
            ✅ <strong style="color:#e2e8f0;">Recommendation:</strong> Offer a discounted annual plan to retain this customer.
        </div>
        """, unsafe_allow_html=True)

        st.write("")
        if st.button("🔄 Reset Analysis", use_container_width=True, type="secondary"):
            st.session_state.analyzed = False
            st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

# ─── Skills Grid ───
st.write("")
st.markdown(
    '<div class="section-header"><div class="section-icon">🎯</div>Concepts & Skills</div>'
    '<div class="section-sub">Core ML competencies</div>',
    unsafe_allow_html=True,
)

skills = [
    ("🗄️", "Data Preprocessing", "Cleaning & transformation", "rgba(56,189,248,0.1)", "rgba(56,189,248,0.03)"),
    ("🔍", "Exploratory Analysis", "EDA & pattern discovery", "rgba(139,92,246,0.1)", "rgba(139,92,246,0.03)"),
    ("🔀", "Feature Selection", "Key variable identification", "rgba(56,189,248,0.1)", "rgba(139,92,246,0.05)"),
    ("✨", "Classification Models", "Logistic Reg & Decision Trees", "rgba(139,92,246,0.1)", "rgba(56,189,248,0.05)"),
    ("📊", "Model Evaluation", "Accuracy & ROC-AUC metrics", "rgba(56,189,248,0.1)", "rgba(56,189,248,0.03)"),
    ("🎯", "Churn Reduction", "Actionable retention insights", "rgba(139,92,246,0.1)", "rgba(139,92,246,0.03)"),
]

cols = st.columns(3)
for i, (icon, label, desc, c1, c2) in enumerate(skills):
    with cols[i % 3]:
        st.markdown(f"""
        <div class="skill-card" style="background:linear-gradient(135deg,{c1},{c2});">
            <div class="skill-icon">{icon}</div>
            <div class="skill-label">{label}</div>
            <div class="skill-desc">{desc}</div>
        </div>
        """, unsafe_allow_html=True)
        
st.write("")
