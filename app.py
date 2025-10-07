import streamlit as st

# --- Page Configuration ---
st.set_page_config(
    page_title="Kevin Go's Portfolio",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- Hide Streamlit's default menu/footer with custom CSS ---
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# --- Custom CSS for font, cards, headings, tabs, etc. ---
custom_css = """
    <style>
    body, html, .card, .stMarkdown, .stText, .stApp {
        font-family: 'Calibri', Arial, sans-serif !important;
    }
    body {
        background: #181818 !important;
        color: #f5f6fa;
    }
    .card {
        background: #22272e;
        border-radius: 1rem;
        padding: 2.5rem 2.5rem 2rem 2.5rem;
        margin-bottom: 2.5rem;
        box-shadow: 0 4px 16px 0 #0003;
        color: #f5f6fa;
        font-size: 1.13rem;
        letter-spacing: 0.04em;
    }
    .card h3 {
        margin-top: 0;
        font-size: 2rem;
        color: #ffb86c;
        font-weight: bold;
        letter-spacing: 0.03em;
        margin-bottom: 0.6em;
        font-family: 'Calibri', Arial, sans-serif !important;
    }
    .section-heading {
        color: #8be9fd;
        font-size: 1.15rem;
        font-weight: bold;
        margin-top: 1.2em;
        margin-bottom: 0.4em;
        font-family: 'Calibri', Arial, sans-serif !important;
        letter-spacing: 0.01em;
    }
    .stack-list {
        display: grid;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 0.5em 1.2em;
        list-style: none;
        padding-left: 0;
        margin-bottom: 1em;
        margin-top: 0.3em;
    }
    .stack-list li {
        background: #23272e;
        border-radius: 6px;
        padding: 0.35em 0.7em;
        font-size: 1.07rem;
        color: #ffb86c;
        font-weight: 500;
        display: inline-block;
        margin-bottom: 0.35em;
        text-align: left;
    }
    .card ul {
        margin-left: 1.2em;
        margin-bottom: 1em;
    }
    .card li:not(.stack-list li) {
        margin-bottom: 0.5em;
        line-height: 1.7;
    }
    .card a, .card a:visited {
        color: #8be9fd;
        text-decoration: underline;
        font-size: 1.05rem;
    }
    .emoji {
        font-size: 2.1rem;
        margin-right: 0.5em;
        vertical-align: middle;
    }
    hr {
        border: 1px solid #444;
        margin-top: 2.5rem;
        margin-bottom: 1.5rem;
    }
    /* --- Custom Tabs --- */
    .stTabs [data-baseweb="tab-list"] {
        justify-content: flex-end;
        background: #181818;
        border-bottom: 2px solid #22272e;
        margin-bottom: 1.8em;
    }
    .stTabs [data-baseweb="tab"] {
        color: #8be9fd;
        background: #181818;
        padding: 0.8em 2.2em 0.8em 2.2em;
        border-radius: 0.5em 0.5em 0 0;
        margin-right: 0.2em;
        font-size: 1.18rem;
        font-family: 'Calibri', Arial, sans-serif !important;
        font-weight: 600;
        border: none;
        transition: background 0.25s, color 0.25s;
    }
    .stTabs [data-baseweb="tab"]:hover {
        background: #23272e;
        color: #ffb86c;
    }
    .stTabs [aria-selected="true"] {
        color: #181818 !important;
        background: linear-gradient(90deg, #ffb86c 60%, #8be9fd 100%);
        font-weight: bold;
        border-bottom: 2px solid #181818 !important;
    }
    @media (max-width: 900px) {
        .card { padding: 1.2rem; }
        .card h3 { font-size: 1.45rem; }
        .section-heading { font-size: 1rem; }
        .stack-list { grid-template-columns: repeat(2, minmax(0, 1fr)); }
        .stTabs [data-baseweb="tab"] { font-size: 1rem; }
    }
    </style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# --- Tabs at top right ---
tabs = st.tabs(["About", "Projects"])

with tabs[0]:
    st.markdown(
        """
        <h1 style="color:#ffb86c; font-size:2.6rem; margin-bottom:0; font-family: 'Calibri', Arial, sans-serif;">💼 Nachiketa's Portfolio</h1>
        <p style="color:#f5f6fa; font-size:1.25rem; margin:1.2em 0 2.5em 0; font-family: 'Calibri', Arial, sans-serif;">
            <b style="font-size:1.15rem;">About Me</b>
            <br><br>
            I am a passionate developer enthusiastic about building robust APIs and backend systems. My journey began with .NET and C#, where I learned the principles of clean architecture, modularity, and system design. After gaining hands-on experience creating and consuming APIs with .NET, I transitioned to Python to broaden my perspective and learn how different technologies approach similar backend problems.
            <br><br>
            Throughout this transition, I explored the nuances between C# and Python development — from dependency injection and async programming, to differences in ORM usage and web frameworks. This has made me more versatile and deepened my understanding of design patterns and best practices.
            <br><br>
            <b>Current Role:</b> I work as a Python developer, primarily writing automation scripts for IBM Maximo. One of my key achievements was designing and deploying an enhancement to automate the end-to-end workflow of asset management triggered by work order creation. This solution is now running in our production environment, saving manual effort and reducing operational errors.
            <br><br>
            My keen interest in system design and automation motivates me to keep learning. I enjoy designing, building, and documenting APIs and backend services, and I’m always eager to explore new technologies and frameworks.
        </p>
        """,
        unsafe_allow_html=True,
    )

with tabs[1]:
    # --- Project Data ---
    projects = [
        {
            "emoji": "🌦️",
            "title": "Blogging Site Using Flask",
            "stack": ["Python", "Flask", "SQLAlchemy", "SQLite", "JWT", "Docker", "Jinja 2", "Materialize UI"],
            "features": [
                "Authentication and Authorization using JWT",
                "Simple Registration and Login Page",
                "Users can follow and unfollow each other",
                "Users can see other users' blogs if they follow each other",
                "Users can edit their profile",
                "Forgot Password and password reset via provided email",
                "Created Blueprints for modular code",
                "Deployed using Docker",
                "Responsive design using Materialize CSS framework",
                "ORM using SQLAlchemy with SQLite database",
                "Jinja 2 templating engine",
            ],
            "link": '<a href="https://github.com/nachiketa345/MICROBLOG-USING-FLASK" target="_blank">View code on GitHub</a>'
        },
        {
            "emoji": "📝",
            "title": "Banking API with Python and FastAPI",
            "stack": ["FastAPI", "Python", "OAuth2PasswordBearer", "JWT (python-jose)", "Passlib bcrypt", "SQLAlchemy", "PostgreSQL", "Pydantic", "Swagger/OpenAPI", "Uvicorn", "Docker", ],
            "features": [
                "Modular backend API with clean separation of concerns (backend/, routers/, models/, schemas/, db.py, auth.py)",
                "Authentication using OAuth2PasswordBearer and JWTs (python-jose) with secure password hashing (passlib bcrypt)",
                "Helper utilities for creating/verifying tokens and obtaining the current user",
                "Persistence via SQLAlchemy (declarative Base, engine, SessionLocal) connected to PostgreSQL (psycopg2); endpoints use dependency injection for DB sessions",
                "Input validation with Pydantic schemas; automatic OpenAPI/Swagger docs available for testing",
                "Consistent HTTPException-based error handling and logging-ready patterns",
                "Purpose: a learning-focused reference implementation showing authentication, authorization, validation, async endpoints, and ORM-backed persistence — useful as a starter user-management or auth microservice for demos and portfolios"
            ],
            "link": '<a href="https://github.com/nachiketa345/api" target="_blank">View code on GitHub</a>'
        },
        {
            "emoji": "📃",
            "title": "Portfolio Website",
            "stack": ["Streamlit", "Python"],
            "features": [
                "Clean, responsive design",
                "Easy to update projects and descriptions"
            ],
            "link": ''
        },
    ]

    # --- Display Projects as Cards ---
    for proj in projects:
        stack_html = (
            f'<div class="section-heading">Stack</div><ul class="stack-list">'
            + "".join([f"<li>{tech}</li>" for tech in proj["stack"]])
            + "</ul>" if proj["stack"] else ""
        )

        features_html = (
            f'<div class="section-heading">Features</div><ul>'
            + "".join([f"<li>{feat}</li>" for feat in proj["features"]])
            + "</ul>"
        )

        link_html = f'<div style="margin-top:1.1em;">{proj["link"]}</div>' if proj["link"] else ""

        st.markdown(
            f"""
            <div class="card">
                <h3>{proj["emoji"]} {proj["title"]}</h3>
                {stack_html}
                {features_html}
                {link_html}
            </div>
            """,
            unsafe_allow_html=True,
        )

    # --- Contact / Footer ---
    st.markdown(
        """
        <hr>
        <div style="padding-top:1rem; font-family:'Calibri', Arial, sans-serif;">
            <b style="color:#8be9fd;">Want to know more?</b>
            <a href="mailto:your.email@example.com" style="color:#8be9fd; margin-left:0.8em;">Contact me</a> |
            <a href="https://linkedin.com/in/yourprofile" style="color:#8be9fd; margin-left:0.8em;">LinkedIn</a>
        </div>
        """,
        unsafe_allow_html=True,
    )