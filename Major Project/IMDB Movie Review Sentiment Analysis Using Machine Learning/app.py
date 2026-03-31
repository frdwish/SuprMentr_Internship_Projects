from pathlib import Path

import joblib
import streamlit as st

from train_model import DATA_PATH, MODEL_PATH, SAMPLE_SIZE, clean_text, train_and_save_model


st.set_page_config(
    page_title="CineSense AI",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;700&family=DM+Sans:wght@400;500;700&display=swap');

    :root {
        --bg: #08111f;
        --panel: rgba(10, 22, 39, 0.78);
        --panel-strong: rgba(14, 30, 52, 0.95);
        --line: rgba(145, 187, 255, 0.18);
        --text: #f5f7fb;
        --muted: #9fb2cc;
        --positive: #34d399;
        --negative: #fb7185;
        --accent: #7dd3fc;
        --accent-strong: #38bdf8;
        --glow: rgba(56, 189, 248, 0.22);
    }

    .stApp {
        background:
            radial-gradient(circle at top left, rgba(56, 189, 248, 0.18), transparent 30%),
            radial-gradient(circle at top right, rgba(52, 211, 153, 0.12), transparent 28%),
            linear-gradient(145deg, #040914 0%, #08111f 45%, #0d1f35 100%);
        color: var(--text);
        font-family: "DM Sans", sans-serif;
    }

    .block-container {
        max-width: 1180px;
        padding-top: 2.2rem;
        padding-bottom: 2rem;
    }

    h1, h2, h3 {
        font-family: "Space Grotesk", sans-serif;
        letter-spacing: -0.03em;
        color: var(--text);
    }

    .hero-card,
    .panel-card,
    .stat-card,
    .sample-card,
    .result-card {
        background: var(--panel);
        backdrop-filter: blur(18px);
        border: 1px solid var(--line);
        border-radius: 24px;
        box-shadow: 0 20px 60px rgba(1, 8, 18, 0.35);
    }

    .hero-card {
        padding: 2rem;
        min-height: 100%;
        background:
            linear-gradient(135deg, rgba(125, 211, 252, 0.12), rgba(52, 211, 153, 0.08)),
            var(--panel);
    }

    .hero-kicker {
        display: inline-block;
        padding: 0.35rem 0.8rem;
        border-radius: 999px;
        background: rgba(125, 211, 252, 0.12);
        border: 1px solid rgba(125, 211, 252, 0.2);
        color: var(--accent);
        font-size: 0.82rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.08em;
    }

    .hero-title {
        font-size: clamp(2.2rem, 4vw, 4.3rem);
        line-height: 0.95;
        margin: 1rem 0 0.8rem;
    }

    .hero-copy {
        font-size: 1.05rem;
        line-height: 1.75;
        color: var(--muted);
        max-width: 44rem;
    }

    .info-chip-wrap {
        display: flex;
        flex-wrap: wrap;
        gap: 0.75rem;
        margin-top: 1.2rem;
    }

    .info-chip {
        padding: 0.8rem 1rem;
        border-radius: 18px;
        background: rgba(255, 255, 255, 0.04);
        border: 1px solid rgba(255, 255, 255, 0.08);
        color: var(--text);
        min-width: 11rem;
    }

    .info-chip-label {
        display: block;
        color: var(--muted);
        font-size: 0.78rem;
        margin-bottom: 0.25rem;
        text-transform: uppercase;
        letter-spacing: 0.07em;
    }

    .panel-card {
        padding: 1.4rem;
        min-height: 100%;
        background: var(--panel-strong);
    }

    .panel-title {
        font-size: 1.1rem;
        font-weight: 700;
        margin-bottom: 0.35rem;
    }

    .panel-copy {
        color: var(--muted);
        line-height: 1.6;
        font-size: 0.96rem;
    }

    .stat-card {
        padding: 1.15rem 1.2rem;
        margin-top: 0.7rem;
    }

    .stat-label {
        color: var(--muted);
        font-size: 0.8rem;
        text-transform: uppercase;
        letter-spacing: 0.08em;
    }

    .stat-value {
        font-family: "Space Grotesk", sans-serif;
        font-size: 1.75rem;
        margin-top: 0.35rem;
    }

    .input-shell {
        margin-top: 1.4rem;
        padding: 1.35rem;
        border-radius: 24px;
        background: rgba(7, 15, 29, 0.7);
        border: 1px solid var(--line);
    }

    .stTextArea textarea {
        background: rgba(255, 255, 255, 0.03) !important;
        color: var(--text) !important;
        border-radius: 18px !important;
        border: 1px solid rgba(157, 187, 255, 0.12) !important;
        min-height: 220px !important;
        font-size: 1rem !important;
        line-height: 1.7 !important;
        padding: 1rem 1rem 1.2rem !important;
    }

    .stTextArea label, .stButton button {
        font-family: "Space Grotesk", sans-serif;
    }

    .stButton button {
        width: 100%;
        border-radius: 16px;
        border: none;
        padding: 0.95rem 1rem;
        color: #03111f;
        font-weight: 700;
        background: linear-gradient(135deg, #7dd3fc, #34d399);
        box-shadow: 0 16px 35px var(--glow);
    }

    .stButton button:hover {
        filter: brightness(1.04);
    }

    .result-card {
        margin-top: 1.15rem;
        padding: 1.4rem;
    }

    .result-label {
        display: inline-block;
        padding: 0.45rem 0.9rem;
        border-radius: 999px;
        font-weight: 700;
        font-size: 0.9rem;
        margin-bottom: 1rem;
    }

    .positive-tag {
        background: rgba(52, 211, 153, 0.12);
        color: var(--positive);
        border: 1px solid rgba(52, 211, 153, 0.24);
    }

    .negative-tag {
        background: rgba(251, 113, 133, 0.12);
        color: var(--negative);
        border: 1px solid rgba(251, 113, 133, 0.24);
    }

    .result-heading {
        font-size: 1.7rem;
        margin-bottom: 0.3rem;
    }

    .result-copy {
        color: var(--muted);
        line-height: 1.6;
        margin-bottom: 1.1rem;
    }

    .confidence-row {
        margin-bottom: 0.9rem;
    }

    .confidence-meta {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 0.4rem;
        font-size: 0.95rem;
    }

    .confidence-bar {
        width: 100%;
        height: 11px;
        border-radius: 999px;
        background: rgba(255, 255, 255, 0.06);
        overflow: hidden;
    }

    .confidence-fill {
        height: 100%;
        border-radius: 999px;
    }

    .sample-card {
        padding: 1rem 1.1rem;
        min-height: 100%;
    }

    .sample-card h4 {
        margin: 0 0 0.6rem;
        font-size: 1rem;
        font-family: "Space Grotesk", sans-serif;
    }

    .sample-card p {
        color: var(--muted);
        line-height: 1.65;
        margin-bottom: 0;
    }

    .footer-note {
        color: var(--muted);
        text-align: center;
        margin-top: 1.4rem;
        font-size: 0.92rem;
    }

    @media (max-width: 900px) {
        .block-container {
            padding-top: 1.4rem;
        }

        .hero-card,
        .panel-card,
        .input-shell,
        .result-card {
            border-radius: 20px;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)


def load_or_train_model():
    if not Path(MODEL_PATH).exists():
        train_and_save_model()
    return joblib.load(MODEL_PATH)


def get_sentiment_summary(prediction: str) -> str:
    if prediction == "positive":
        return "This review leans positive, suggesting that the audience response is favorable."
    return "This review leans negative, suggesting that the audience response is unfavorable."


def render_confidence(label: str, score: float, color: str) -> None:
    st.markdown(
        f"""
        <div class="confidence-row">
            <div class="confidence-meta">
                <span>{label}</span>
                <strong>{score:.2%}</strong>
            </div>
            <div class="confidence-bar">
                <div class="confidence-fill" style="width: {score * 100:.1f}%; background: {color};"></div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


model = load_or_train_model()

left_col, right_col = st.columns([1.45, 0.95], gap="large")

with left_col:
    st.markdown(
        f"""
        <div class="hero-card">
            <span class="hero-kicker">AI Movie Review Analyzer</span>
            <h1 class="hero-title">CineSense AI</h1>
            <p class="hero-copy">
                A deployment-ready sentiment analysis app that classifies IMDB movie reviews
                as positive or negative using natural language processing and machine learning.
            </p>
            <div class="info-chip-wrap">
                <div class="info-chip">
                    <span class="info-chip-label">Dataset</span>
                    {DATA_PATH.name}
                </div>
                <div class="info-chip">
                    <span class="info-chip-label">Training Sample</span>
                    {SAMPLE_SIZE:,} reviews
                </div>
                <div class="info-chip">
                    <span class="info-chip-label">Model</span>
                    TF-IDF + Logistic Regression
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with right_col:
    st.markdown(
        """
        <div class="panel-card">
            <div class="panel-title">How It Works</div>
            <div class="panel-copy">
                The model cleans the review text, converts words into numeric features using
                TF-IDF, and predicts whether the opinion is positive or negative.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    metric_col_1, metric_col_2 = st.columns(2, gap="small")
    with metric_col_1:
        st.markdown(
            """
            <div class="stat-card">
                <div class="stat-label">Categories</div>
                <div class="stat-value">2</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with metric_col_2:
        st.markdown(
            """
            <div class="stat-card">
                <div class="stat-label">Use Case</div>
                <div class="stat-value">NLP</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.markdown('<div class="input-shell">', unsafe_allow_html=True)
st.subheader("Analyze a Review")

review_text = st.text_area(
    "Paste a movie review below",
    placeholder="Example: The film was visually stunning, emotionally powerful, and brilliantly acted.",
    label_visibility="collapsed",
)

button_col, helper_col = st.columns([0.34, 0.66], gap="medium")
with button_col:
    analyze_clicked = st.button("Analyze Sentiment")
with helper_col:
    st.markdown(
        """
        <div class="panel-copy" style="padding-top: 0.55rem;">
            Tip: longer, opinion-rich reviews usually produce more reliable predictions.
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("</div>", unsafe_allow_html=True)

if analyze_clicked:
    if not review_text.strip():
        st.warning("Please enter a movie review before analyzing.")
    else:
        cleaned_review = clean_text(review_text)
        prediction = model.predict([cleaned_review])[0]
        probabilities = model.predict_proba([cleaned_review])[0]
        scores = dict(zip(model.classes_, probabilities))
        tag_class = "positive-tag" if prediction == "positive" else "negative-tag"
        heading = "Positive Review" if prediction == "positive" else "Negative Review"

        st.markdown(
            f"""
            <div class="result-card">
                <span class="result-label {tag_class}">{prediction.title()}</span>
                <div class="result-heading">{heading}</div>
                <div class="result-copy">{get_sentiment_summary(prediction)}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        render_confidence("Positive confidence", scores["positive"], "linear-gradient(90deg, #38bdf8, #34d399)")
        render_confidence("Negative confidence", scores["negative"], "linear-gradient(90deg, #fb7185, #f97316)")

st.subheader("Demo Examples")
sample_col_1, sample_col_2, sample_col_3 = st.columns(3, gap="medium")

with sample_col_1:
    st.markdown(
        """
        <div class="sample-card">
            <h4>Positive Example</h4>
            <p>This movie was brilliantly acted, emotionally rich, and memorable from start to finish.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with sample_col_2:
    st.markdown(
        """
        <div class="sample-card">
            <h4>Negative Example</h4>
            <p>The plot was dull, the pacing was slow, and the ending felt completely disappointing.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with sample_col_3:
    st.markdown(
        """
        <div class="sample-card">
            <h4>Project Highlights</h4>
            <p>Built with Python, Streamlit, TF-IDF vectorization, and Logistic Regression on IMDB reviews.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

