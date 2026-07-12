import streamlit as st
from datetime import datetime
from html import escape
import base64


st.set_page_config(page_title="YYGS Connect", page_icon="🌐", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@700;800&display=swap');
:root { --navy:#102a43; --blue:#1f5eff; --pale:#eef4ff; --ink:#172b4d; --muted:#66788a; }
.stApp { background:#f7f9fc; color:var(--ink); font-family:'DM Sans',sans-serif; }
[data-testid="stHeader"] { background:transparent; }
#MainMenu, footer { visibility:hidden; }
.block-container { max-width:1180px; padding-top:1.6rem; padding-bottom:5rem; }
h1,h2,h3 { font-family:'Manrope',sans-serif; color:var(--navy); letter-spacing:-.03em; }
.brand { font-family:'Manrope'; font-weight:800; font-size:1.35rem; color:var(--navy); }
.brand-dot { color:var(--blue); }
.eyebrow { color:var(--blue); font-size:.76rem; font-weight:700; letter-spacing:.12em; text-transform:uppercase; }
.hero { position:relative;overflow:hidden;padding:2.2rem;border-radius:24px;background:linear-gradient(125deg,#102a43 0%,#184e8e 60%,#2773dc 100%);color:white;box-shadow:0 18px 45px rgba(16,42,67,.16);transition:transform .25s ease,box-shadow .25s ease; }
.hero:hover { transform:translateY(-3px);box-shadow:0 25px 55px rgba(16,42,67,.22); }
.hero h1 { color:white; margin:.25rem 0 .55rem; font-size:2.25rem; }
.hero p { color:#dceaff; max-width:680px; margin:0; }
.card { background:white;border:1px solid #e7edf5;border-radius:18px;padding:1.15rem 1.25rem;margin-bottom:.8rem;box-shadow:0 5px 18px rgba(31,52,77,.045);transition:transform .2s ease,border-color .2s ease,box-shadow .2s ease; }
.card:hover { transform:translateY(-4px);border-color:#bfd1f2;box-shadow:0 13px 28px rgba(31,52,77,.10); }
.space-icon { width:48px;height:48px;border-radius:15px;display:flex;align-items:center;justify-content:center;font-size:.78rem;font-weight:800;letter-spacing:.05em;background:var(--pale);color:#2451a6; }
.muted { color:var(--muted); font-size:.88rem; }
.pill { display:inline-block; background:#eef4ff; color:#2451a6; border-radius:999px; padding:.3rem .65rem; font-size:.75rem; font-weight:700; margin:.15rem .18rem .15rem 0; }
.avatar { width:44px;height:44px;border-radius:50%;background:linear-gradient(135deg,#ffd9a0,#ff9f80);display:flex;align-items:center;justify-content:center;font-weight:800;color:#663820; }
.post-head { display:flex;gap:.75rem;align-items:center;margin-bottom:.8rem; }
.post-name { font-weight:700;color:var(--navy); }
.post-copy { font-size:1rem;line-height:1.55;margin:.45rem 0 1rem; }
.stat { font-size:.83rem;color:var(--muted); }
.progress-wrap { background:#e9eff7;border-radius:8px;height:7px;overflow:hidden; }
.progress-fill { background:linear-gradient(90deg,#1f5eff,#42a5ff);height:100%;border-radius:8px; }
.nav-wrap div[data-testid="stHorizontalBlock"] { gap:.35rem; }
div.stButton > button { border-radius:12px;font-weight:700;border:1px solid #dbe5f1;transition:transform .16s ease,box-shadow .16s ease; }
div.stButton > button:hover { transform:translateY(-2px);box-shadow:0 7px 15px rgba(31,94,255,.15); }
div.stButton > button:active { transform:translateY(1px) scale(.985); }
div.stButton > button[kind="primary"] { background:#1f5eff; border-color:#1f5eff; }
div[data-testid="stTextInput"] input, div[data-testid="stTextArea"] textarea { border-radius:12px; }
.login-shell { max-width:520px;margin:3vh auto 0; }
.login-logo { text-align:center;font-size:2rem;font-family:'Manrope';font-weight:800;color:var(--navy);margin-bottom:.4rem; }
.center-copy { text-align:center;color:var(--muted);margin-bottom:2rem; }
.choice-card { min-height:138px;border:1.5px solid #dce6f2;border-radius:18px;padding:1.1rem;background:white;transition:all .2s ease; }
.choice-card:hover { transform:translateY(-4px);border-color:#1f5eff;box-shadow:0 12px 25px rgba(31,94,255,.11); }
.step-dot { display:inline-block;width:8px;height:8px;border-radius:50%;background:#d4deec;margin-right:7px; }
.step-dot.active { width:26px;border-radius:10px;background:#1f5eff; }
.profile-preview { background:linear-gradient(145deg,#102a43,#245b9e);border-radius:24px;padding:1.7rem;color:white;box-shadow:0 18px 40px rgba(16,42,67,.18); }
.profile-preview h2 { color:white;margin:.7rem 0 .2rem; }
.comm-shell { background:#fff;border:1px solid #e3eaf3;border-radius:20px;padding:1rem;height:430px;overflow-y:auto;overflow-x:hidden;scroll-behavior:smooth;box-shadow:inset 0 1px 4px rgba(31,52,77,.04); }
.comm-shell::-webkit-scrollbar { width:7px; }
.comm-shell::-webkit-scrollbar-thumb { background:#cbd7e5;border-radius:10px; }
.person-row { display:flex;align-items:center;gap:.75rem;padding:.75rem;border-bottom:1px solid #edf1f6; }
.message-in,.message-out { display:block;width:fit-content;max-width:76%;padding:.72rem .9rem;border-radius:18px;margin:.55rem 0;line-height:1.42;overflow-wrap:anywhere;word-break:break-word;white-space:normal;clear:both; }
.message-in { background:#eef3f8;color:#172b4d;border-bottom-left-radius:5px; }
.message-out { background:#1687ff;color:white;border-bottom-right-radius:5px;margin-left:auto; }
.message-time { font-size:.7rem;opacity:.7;margin-top:.25rem; }
.unread { display:inline-block;background:#1f5eff;color:white;border-radius:999px;min-width:20px;text-align:center;font-size:.7rem;padding:.1rem .35rem; }
.mini-avatar { width:38px;height:38px;border-radius:50%;background:linear-gradient(135deg,#dbe8ff,#8eb5ff);display:flex;align-items:center;justify-content:center;color:#173c78;font-size:.72rem;font-weight:800;margin:.2rem auto; }
.thread-title { display:flex;align-items:center;gap:.7rem;margin-bottom:.35rem; }
.thread-title .mini-avatar { margin:0;flex:0 0 38px; }
.interest-focus { min-height:205px;border:1px solid #dce6f2;border-radius:24px;padding:2rem;background:linear-gradient(145deg,#fff,#f3f7ff);display:flex;flex-direction:column;justify-content:center;text-align:center;box-shadow:0 14px 32px rgba(31,52,77,.08); }
.st-key-bottom_nav { position:fixed;bottom:14px;left:50%;transform:translateX(-50%);width:min(720px,calc(100% - 24px));z-index:999;background:rgba(255,255,255,.94);backdrop-filter:blur(16px);border:1px solid #dfe7f1;border-radius:24px;padding:.45rem .6rem;box-shadow:0 14px 40px rgba(16,42,67,.2); }
.st-key-bottom_nav button { border:0!important;box-shadow:none!important;border-radius:17px!important; }
.photo-avatar { width:78px;height:78px;border-radius:50%;object-fit:cover;border:3px solid rgba(255,255,255,.7); }
@media(max-width:700px){.hero{padding:1.4rem}.hero h1{font-size:1.75rem}.block-container{padding-top:.7rem}.st-key-bottom_nav button{font-size:.72rem;padding:.5rem .2rem}}
</style>
""", unsafe_allow_html=True)


SPACES = [
    {"id": 1, "icon": "IST", "name": "IST 2026", "category": "Academic track", "members": 142, "description": "Ideas, workshops, and conversations for science and technology students."},
    {"id": 2, "icon": "SII", "name": "Session II", "category": "Official cohort", "members": 418, "description": "Your home base for announcements, introductions, and session-wide moments."},
    {"id": 3, "icon": "AI", "name": "AI & Society", "category": "Interest", "members": 86, "description": "Explore how artificial intelligence can serve people and communities."},
    {"id": 4, "icon": "ACT", "name": "Campus Sports", "category": "Social", "members": 119, "description": "Find a game, make a team, or invite people to play outside."},
    {"id": 5, "icon": "MUS", "name": "Music Makers", "category": "Creative", "members": 73, "description": "Musicians, singers, producers, and people who simply love music."},
    {"id": 6, "icon": "PS", "name": "Public Speaking", "category": "Skills", "members": 64, "description": "Practice speeches, share feedback, and become a more confident speaker."},
]

STARTER_POSTS = [
    {"id": 1, "initials": "AM", "author": "Amara Mensah", "meta": "IST 2026 · 18 min ago", "space": "AI & Society", "text": "Anyone interested in forming a small team for the responsible AI design challenge? I’m especially looking for someone who enjoys visual design!", "reactions": {"❤️": 8, "👏": 5, "💡": 12}, "comments": 4},
    {"id": 2, "initials": "LK", "author": "Leo Kim", "meta": "Session II · 42 min ago", "space": "Campus Sports", "text": "Spikeball at 12:30 on Old Campus! We have one set and need at least four more people. Beginners are very welcome ☀️", "reactions": {"👍": 14, "🎉": 6}, "comments": 7},
    {"id": 3, "initials": "SR", "author": "Sofia Rossi", "meta": "IST 2026 · 1 hr ago", "space": "IST 2026", "text": "What topic are you most excited to explore this summer? I’m curious about biomedical engineering and public health.", "reactions": {"❤️": 7, "💡": 9}, "comments": 11},
]


def init_state():
    defaults = {
        "logged_in": False, "onboarded": False, "page": "Home", "name": "Chase",
        "country": "United States", "track": "IST", "interests": ["Artificial Intelligence", "Entrepreneurship"],
        "bio": "Curious about technology, entrepreneurship, and meeting people who see problems differently.",
        "role": "Student", "profile_photo": None, "tos_agreed": False,
        "notifications": ["Amara sent you a new message", "AI ethics circle starts at 3:00 PM", "Sofia replied to your post"],
        "post_replies": {1: ["I’m interested in visual design—happy to help."], 2: ["I’ll be there!"], 3: []},
        "space_channel": "General", "archived_chats": set(),
        "events": [
            {"id": 1, "time": "12:30 PM", "title": "Spikeball", "location": "Old Campus", "going": 8, "joined": False},
            {"id": 2, "time": "3:00 PM", "title": "AI ethics circle", "location": "WLH 201", "going": 16, "joined": True},
            {"id": 3, "time": "7:30 PM", "title": "Open mic night", "location": "Common Room", "going": 31, "joined": False}],
        "onboarding_step": 1, "interest_index": 0, "joined": {1, 2, 3}, "posts": STARTER_POSTS.copy(), "reacted": set(),
        "active_space": "IST 2026", "active_chat": "Amara Mensah",
        "inbox": {
            "Amara Mensah": {"initials": "AM", "detail": "IST · Ghana", "unread": 2, "messages": [
                {"from": "them", "text": "Hi! I saw that you’re also interested in artificial intelligence.", "time": "2:14 PM"},
                {"from": "me", "text": "Yes—I’m especially interested in responsible AI and healthcare.", "time": "2:18 PM"},
                {"from": "them", "text": "That’s perfect. Would you want to join our design challenge team?", "time": "2:21 PM"}]},
            "Leo Kim": {"initials": "LK", "detail": "SGC · South Korea", "unread": 0, "messages": [
                {"from": "them", "text": "Are you coming to Spikeball this afternoon?", "time": "Yesterday"}]},
            "Sofia Rossi": {"initials": "SR", "detail": "IST · Italy", "unread": 0, "messages": [
                {"from": "me", "text": "Your biomedical engineering post was really interesting.", "time": "Monday"},
                {"from": "them", "text": "Thank you! Let’s talk after the workshop.", "time": "Monday"}]}
        }
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value
    for chat in st.session_state.inbox.values():
        chat.setdefault("muted", False)
        chat.setdefault("reported", False)
        chat.setdefault("last_activity", len(chat["messages"]))
        for message in chat["messages"]:
            message.setdefault("status", "Read" if message["from"] == "me" else "")


def avatar_html(initials, size=68):
    if st.session_state.profile_photo:
        return f'<img class="photo-avatar" style="width:{size}px;height:{size}px" src="{st.session_state.profile_photo}" alt="Profile photo">'
    return f'<div class="avatar" style="width:{size}px;height:{size}px;background:white;color:#1f5eff">{escape(initials)}</div>'


def login():
    st.markdown('<div class="login-shell"><div class="login-logo">YYGS Connect<span class="brand-dot">.</span></div><div class="center-copy">Meet your cohort before you meet on campus.</div></div>', unsafe_allow_html=True)
    left, mid, right = st.columns([1, 1.15, 1])
    with mid:
        with st.container(border=True):
            st.markdown("### Welcome to your community")
            st.caption("Sign in using the invitation code included with your admission.")
            name = st.text_input("Your name", placeholder="e.g. Chase Marshall")
            code = st.text_input("Invitation code", placeholder="Try YYGS-2026")
            st.text_input("Password", type="password", placeholder="••••••••")
            with st.expander("Community agreement and Terms of Service"):
                st.caption("Be respectful, protect others’ privacy, do not share access codes, and report unsafe behavior. YYGS Connect may remove content or accounts that violate these standards.")
            agreed = st.checkbox("I agree to the Terms of Service and community standards")
            if st.button("Continue", type="primary", use_container_width=True):
                if name and code == "YYGS-2026" and agreed:
                    st.session_state.name = name
                    st.session_state.tos_agreed = True
                    st.session_state.logged_in = True
                    st.rerun()
                elif not agreed:
                    st.warning("Please accept the community agreement before continuing.")
                elif code and code != "YYGS-2026":
                    st.error("That invitation code is not valid. Use YYGS-2026.")
                else:
                    st.warning("Enter your name and invitation code to continue.")
            st.caption("Prototype invitation code: YYGS-2026")


def onboarding():
    st.markdown('<div class="brand">YYGS Connect<span class="brand-dot">.</span></div>', unsafe_allow_html=True)
    step = st.session_state.onboarding_step
    st.markdown("".join(f'<span class="step-dot {"active" if i == step else ""}"></span>' for i in range(1, 5)), unsafe_allow_html=True)
    st.caption(f"PROFILE SETUP · STEP {step} OF 4")
    if step == 1:
        st.markdown("## Where are you joining us from?")
        st.write("Choose your home country to begin your profile and represent your corner of the global cohort.")
        countries = ["Argentina", "Australia", "Brazil", "Canada", "Chile", "China", "Colombia", "Egypt", "France", "Germany", "Ghana", "India", "Indonesia", "Italy", "Japan", "Kenya", "Mexico", "Morocco", "Netherlands", "Nigeria", "Pakistan", "Peru", "Philippines", "Poland", "Singapore", "South Africa", "South Korea", "Spain", "Sweden", "Thailand", "Turkey", "Ukraine", "United Kingdom", "United States", "Vietnam", "Other"]
        st.session_state.country = st.selectbox("Country or region", countries, index=countries.index(st.session_state.country))
        st.markdown('<div class="card"><div class="eyebrow">Your global cohort</div><h3>One campus. Dozens of perspectives.</h3><div class="muted">Location gives classmates an easy conversation starter and shows the reach of your session.</div></div>', unsafe_allow_html=True)
    elif step == 2:
        st.markdown("## Choose your academic track")
        st.write("Select a card to choose the lens you’ll use to explore complex global questions this summer.")
        tracks = {"IST": ("Innovations in Science & Technology", "Design, discovery, and the future of science."), "PLE": ("Politics, Law & Economics", "Institutions, markets, justice, and public life."), "SGC": ("Solving Global Challenges", "Collaborative responses to worldwide problems.")}
        for col, (code, details) in zip(st.columns(3), tracks.items()):
            with col:
                selected = st.session_state.track == code
                label = f"{code}\n\n{details[0]}\n\n{details[1]}"
                if st.button(label, key=f"track_{code}", use_container_width=True, type="primary" if selected else "secondary", help=f"Choose {details[0]}"):
                    st.session_state.track = code
                    st.rerun()
    elif step == 3:
        st.markdown("## Discover your interests")
        st.write("Move through one topic at a time. Save the ones you would genuinely want to discuss with another student.")
        options = ["Artificial Intelligence", "Biology", "Climate", "Debate", "Entrepreneurship", "Music", "Photography", "Public Speaking", "Sports", "Writing"]
        descriptions = {"Artificial Intelligence": "Technology, ethics, creativity, and how intelligent systems affect society.", "Biology": "Living systems, medicine, genetics, and discoveries that improve health.", "Climate": "Environmental solutions, sustainability, policy, and planetary health.", "Debate": "Reasoning clearly, hearing opposing views, and making a persuasive case.", "Entrepreneurship": "Turning an idea into something useful through design, leadership, and action.", "Music": "Performance, production, songwriting, and the cultures formed around sound.", "Photography": "Visual storytelling, observation, composition, and documenting the YYGS experience.", "Public Speaking": "Sharing ideas with confidence, presence, clarity, and purpose.", "Sports": "Teamwork, casual campus games, movement, and friendly competition.", "Writing": "Stories, journalism, poetry, reflection, and communicating complex ideas."}
        index = st.session_state.interest_index % len(options)
        interest = options[index]
        st.progress((index + 1) / len(options), text=f"Topic {index + 1} of {len(options)}")
        focus, selected_panel = st.columns([1.45, 1])
        with focus:
            st.markdown(f'<div class="interest-focus"><div class="eyebrow">TOPIC TO EXPLORE</div><h2>{interest}</h2><div class="muted">{descriptions[interest]}</div></div>', unsafe_allow_html=True)
            skip, save = st.columns(2)
            with skip:
                if st.button("Not for me", use_container_width=True):
                    st.session_state.interest_index = (index + 1) % len(options)
                    st.rerun()
            with save:
                is_saved = interest in st.session_state.interests
                if st.button("Remove interest" if is_saved else "Save interest", type="primary", use_container_width=True):
                    if is_saved: st.session_state.interests.remove(interest)
                    elif len(st.session_state.interests) < 5: st.session_state.interests.append(interest)
                    else: st.toast("You already saved five interests.")
                    st.session_state.interest_index = (index + 1) % len(options)
                    st.rerun()
        with selected_panel:
            st.markdown("#### Your saved interests")
            st.caption(f"{len(st.session_state.interests)} of 5 selected")
            if st.session_state.interests:
                for saved in st.session_state.interests:
                    st.markdown(f'<div class="card" style="padding:.7rem .9rem;margin-bottom:.45rem"><b>{saved}</b></div>', unsafe_allow_html=True)
                remove = st.selectbox("Remove an interest", ["Keep all"] + st.session_state.interests)
                if remove != "Keep all" and st.button("Remove selected", use_container_width=True):
                    st.session_state.interests.remove(remove)
                    st.rerun()
            else:
                st.info("Save a topic and it will appear here.")
    else:
        st.markdown("## This is how others will meet you")
        st.write("Add a quick introduction, review the live preview, or go back to change anything.")
        left, right = st.columns([1, 1.15])
        with left:
            photo = st.file_uploader("Profile photo", type=["png", "jpg", "jpeg"], help="Choose a square photo for the best crop.")
            if photo:
                st.session_state.profile_photo = f"data:{photo.type};base64,{base64.b64encode(photo.getvalue()).decode()}"
            st.session_state.bio = st.text_area("One or two sentence bio", value=st.session_state.bio, max_chars=220, height=120)
            st.caption("Share what you’re curious about and what you would enjoy doing at YYGS.")
        with right:
            initials = "".join(x[0] for x in st.session_state.name.split()[:2]).upper()
            chips = " ".join(f'<span class="pill">{x}</span>' for x in st.session_state.interests)
            st.markdown(f'<div class="profile-preview"><div class="eyebrow" style="color:#9fd0ff">LIVE PREVIEW</div><div style="margin-top:1rem">{avatar_html(initials)}</div><h2>{st.session_state.name}</h2><div style="color:#cfe2fa">{st.session_state.country} · {st.session_state.track} · Session II</div><p>{st.session_state.bio}</p><div>{chips}</div></div>', unsafe_allow_html=True)
    st.markdown("<div style='height:1rem'></div>", unsafe_allow_html=True)
    back, _, onward = st.columns([1, 3, 1])
    with back:
        if step > 1 and st.button("Back", use_container_width=True):
            st.session_state.onboarding_step -= 1
            st.rerun()
    with onward:
        if st.button("Enter YYGS Connect" if step == 4 else "Next", type="primary", use_container_width=True):
            if step == 4: st.session_state.onboarded = True
            else: st.session_state.onboarding_step += 1
            st.rerun()


def top_nav():
    brand, notice = st.columns([5, 1])
    with brand:
        st.markdown('<div class="brand">YYGS Connect<span class="brand-dot">.</span></div>', unsafe_allow_html=True)
    with notice:
        unread = len(st.session_state.notifications)
        with st.popover(f"Notifications ({unread})", use_container_width=True):
            st.markdown("#### Notifications")
            for item in st.session_state.notifications:
                st.markdown(f'<div class="card" style="padding:.65rem .8rem">{escape(item)}</div>', unsafe_allow_html=True)
            if unread and st.button("Mark all as read", use_container_width=True):
                st.session_state.notifications = []
                st.rerun()
    with st.container(key="bottom_nav"):
        cols = st.columns(5)
        for col, label in zip(cols, ["Home", "Community", "Messages", "Profile", "Log out"]):
            with col:
                page = "Communications" if label == "Messages" else label
                if st.button(label, use_container_width=True, type="primary" if st.session_state.page == page else "secondary"):
                    if label == "Log out":
                        st.session_state.logged_in = False
                    else:
                        st.session_state.page = page
                    st.rerun()
    st.markdown("<div style='height:1.2rem'></div>", unsafe_allow_html=True)


def space_card(space, show_join=True):
    st.markdown(f"""<div class="card"><div style="display:flex;gap:1rem;align-items:center">
    <div class="space-icon">{space['icon']}</div><div><div class="eyebrow">{space['category']}</div>
    <h3 style="font-size:1.05rem;margin:.1rem 0">{space['name']}</h3><span class="muted">{space['members']} members</span></div></div>
    <p class="muted" style="min-height:2.6rem">{space['description']}</p></div>""", unsafe_allow_html=True)
    if show_join:
        joined = space["id"] in st.session_state.joined
        if st.button("Open space" if joined else "Join space", key=f"join_{space['id']}", use_container_width=True, type="primary" if joined else "secondary"):
            if joined:
                st.session_state.active_space = space["name"]
                st.session_state.page = "Communications"
            else:
                st.session_state.joined.add(space["id"])
            st.rerun()
        if joined and st.button("Leave", key=f"leave_{space['id']}", use_container_width=True):
            st.session_state.joined.remove(space["id"])
            st.rerun()
    elif st.button("Open conversations", key=f"home_space_{space['id']}", use_container_width=True):
        st.session_state.active_space = space["name"]
        st.session_state.page = "Communications"
        st.rerun()


def home():
    name = st.session_state.name.split()[0]
    st.markdown(f"""<div class="hero"><div class="eyebrow" style="color:#83c5ff">Session II · {st.session_state.track}</div>
    <h1>Good afternoon, {name}</h1><p>Your YYGS community is waking up. See what people are talking about, find an activity, or say hello.</p></div>""", unsafe_allow_html=True)
    unread = sum(chat["unread"] for chat in st.session_state.inbox.values())
    joined_events = sum(1 for event in st.session_state.events if event["joined"])
    a, b, c = st.columns(3)
    for col, value, label in [(a, unread, "Unread messages"), (b, len(st.session_state.joined), "Your spaces"), (c, joined_events, "Events saved")]:
        with col: st.markdown(f'<div class="card"><div class="eyebrow">YOUR DAY</div><h2 style="margin:.3rem 0">{value}</h2><div class="muted">{label}</div></div>', unsafe_allow_html=True)
    st.markdown("### Coming up today")
    for col, event in zip(st.columns(3), st.session_state.events[:3]):
        with col:
            st.markdown(f'<div class="card"><div class="eyebrow">{event["time"]}</div><h3 style="font-size:1.05rem;margin:.5rem 0">{escape(event["title"])}</h3><div class="muted">{escape(event["location"])} · {event["going"]} going</div></div>', unsafe_allow_html=True)
            if st.button("Saved" if event["joined"] else "RSVP", key=f"rsvp_{event['id']}", type="primary" if event["joined"] else "secondary", use_container_width=True):
                event["joined"] = not event["joined"]
                event["going"] += 1 if event["joined"] else -1
                st.rerun()
    with st.expander("Create an activity"):
        with st.form("new_event", clear_on_submit=True):
            title = st.text_input("Activity name")
            event_time = st.text_input("Time", placeholder="4:30 PM")
            location = st.text_input("Location")
            create_event = st.form_submit_button("Create activity", type="primary")
        if create_event and title and event_time and location:
            st.session_state.events.append({"id": int(datetime.now().timestamp()), "time": event_time, "title": title, "location": location, "going": 1, "joined": True})
            st.session_state.notifications.append(f"Your activity “{title}” was created")
            st.rerun()
    st.markdown("### Your spaces")
    joined = [s for s in SPACES if s["id"] in st.session_state.joined]
    cols = st.columns(min(3, len(joined)))
    for col, space in zip(cols, joined):
        with col: space_card(space, show_join=False)
    st.markdown("### One conversation worth joining")
    st.caption("A focused recommendation based on your interests—not an endless feed.")
    matching = next((p for p in st.session_state.posts if p["space"] in [s["name"] for s in joined]), st.session_state.posts[0])
    render_post(matching)


def community():
    st.markdown("## Find your people")
    st.write("Explore spaces built around your cohort, interests, and the things you want to try.")
    query = st.text_input("Search spaces", placeholder="Try music, sports, AI…", label_visibility="collapsed")
    categories = st.radio("Filter", ["All", "Academic track", "Official cohort", "Interest", "Social", "Creative", "Skills"], horizontal=True, label_visibility="collapsed")
    results = [s for s in SPACES if (not query or query.lower() in (s["name"]+s["description"]).lower()) and (categories == "All" or s["category"] == categories)]
    for i in range(0, len(results), 3):
        cols = st.columns(3)
        for col, space in zip(cols, results[i:i+3]):
            with col: space_card(space)
    if not results: st.info("No spaces match that search yet. Try another word.")


def render_post(post):
    chips = " ".join([f'<span class="pill">{emoji} {count}</span>' for emoji, count in post["reactions"].items()])
    st.markdown(f"""<div class="card"><div class="post-head"><div class="avatar">{post['initials']}</div>
    <div><div class="post-name">{post['author']}</div><div class="muted">{post['meta']}</div></div>
    <span class="pill" style="margin-left:auto">{post['space']}</span></div><div class="post-copy">{post['text']}</div>
    <div>{chips} <span class="stat">&nbsp; {post['comments']} replies</span></div></div>""", unsafe_allow_html=True)
    cols = st.columns([1,1,1,5])
    for col, emoji in zip(cols[:3], ["❤️", "👏", "💡"]):
        with col:
            key = (post["id"], emoji)
            if st.button(emoji, key=f"react_{post['id']}_{emoji}", use_container_width=True):
                if key not in st.session_state.reacted:
                    post["reactions"][emoji] = post["reactions"].get(emoji, 0) + 1
                    st.session_state.reacted.add(key)
                st.rerun()
    replies = st.session_state.post_replies.setdefault(post["id"], [])
    with st.expander(f"Replies ({len(replies)})"):
        for reply in replies:
            st.markdown(f'<div class="card" style="padding:.65rem .8rem"><b>{escape(st.session_state.name if reply.startswith("You: ") else "Community member")}</b><br>{escape(reply.removeprefix("You: "))}</div>', unsafe_allow_html=True)
        with st.form(f"reply_{post['id']}", clear_on_submit=True):
            reply_text = st.text_input("Write a reply", label_visibility="collapsed", placeholder="Add to this conversation…")
            add_reply = st.form_submit_button("Reply")
        if add_reply and reply_text.strip():
            replies.append("You: " + reply_text.strip())
            post["comments"] = len(replies)
            st.session_state.notifications.append(f"Your reply was posted in {post['space']}")
            st.rerun()


def communications():
    st.markdown("## Communications")
    st.write("Talk with your communities or continue a private conversation—all in one place.")
    spaces_tab, inbox_tab = st.tabs(["Space conversations", "Private inbox"])

    with spaces_tab:
        joined_spaces = [s for s in SPACES if s["id"] in st.session_state.joined]
        joined_names = [s["name"] for s in joined_spaces]
        if joined_names and st.session_state.active_space not in joined_names:
            st.session_state.active_space = joined_names[0]
        selector, conversation = st.columns([1, 2.4])
        with selector:
            st.markdown("#### Your spaces")
            for space in joined_spaces:
                count = sum(1 for p in st.session_state.posts if p["space"] == space["name"])
                if st.button(f"{space['name']}  ·  {count}", key=f"open_space_{space['id']}", use_container_width=True, type="primary" if st.session_state.active_space == space["name"] else "secondary"):
                    st.session_state.active_space = space["name"]
                    st.rerun()
            st.markdown('<div class="card" style="margin-top:1rem"><div class="eyebrow">TODAY’S PROMPT</div><h3 style="font-size:1rem">What idea changed how you see the world?</h3><div class="muted">Use it to start a thoughtful conversation.</div></div>', unsafe_allow_html=True)
        with conversation:
            active = next((s for s in joined_spaces if s["name"] == st.session_state.active_space), None)
            if active:
                st.markdown(f"### {active['name']}")
                st.caption(f"{active['members']} members · {active['description']}")
                channels = ["General", "Announcements", "Questions", "Activities", "Resources"]
                st.session_state.space_channel = st.radio("Channel", channels, horizontal=True, label_visibility="collapsed")
                if st.session_state.space_channel == "Announcements":
                    st.info("Official announcements are read-only for students. Staff and moderators can publish here.")
                with st.expander("Create a post", expanded=False):
                    with st.form("space_post", clear_on_submit=True):
                        content = st.text_area("Message", placeholder="Ask a question, share an idea, or invite people to an activity…")
                        submitted = st.form_submit_button("Publish to this channel", type="primary", disabled=st.session_state.space_channel == "Announcements" and st.session_state.role == "Student")
                    if submitted and content.strip():
                        initials = "".join(x[0] for x in st.session_state.name.split()[:2]).upper()
                        st.session_state.posts.insert(0, {"id": int(datetime.now().timestamp()), "initials": initials, "author": st.session_state.name, "meta": f"{st.session_state.space_channel} · Just now", "space": active["name"], "text": content.strip(), "reactions": {}, "comments": 0})
                        st.rerun()
                space_posts = [p for p in st.session_state.posts if p["space"] == active["name"]]
                if space_posts:
                    for post in space_posts: render_post(post)
                else:
                    st.info("No posts here yet. Start the first conversation.")

    with inbox_tab:
        people, thread = st.columns([1, 2.25])
        with people:
            st.markdown("#### Inbox")
            search = st.text_input("Search conversations", placeholder="Search students", label_visibility="collapsed")
            matches = [(name, data) for name, data in st.session_state.inbox.items() if search.lower() in name.lower() and name not in st.session_state.archived_chats]
            matches.sort(key=lambda item: (item[1]["unread"] > 0, item[1]["last_activity"]), reverse=True)
            for name, data in matches:
                unread = f"  ({data['unread']} new)" if data["unread"] else ""
                avatar_col, person_col = st.columns([.32, 1.68], vertical_alignment="center")
                with avatar_col:
                    st.markdown(f'<div class="mini-avatar">{escape(data["initials"])}</div>', unsafe_allow_html=True)
                with person_col:
                    if st.button(f"{name}{unread}\n\n{data['detail']}", key=f"chat_{name}", use_container_width=True, type="primary" if st.session_state.active_chat == name else "secondary"):
                        st.session_state.active_chat = name
                        st.session_state.inbox[name]["unread"] = 0
                        st.rerun()
            with st.expander("Start a conversation"):
                new_person = st.selectbox("Find a student", ["Maya Patel", "Daniel Okafor", "Camila Torres"])
                if st.button("Open conversation", use_container_width=True):
                    if new_person not in st.session_state.inbox:
                        initials = "".join(x[0] for x in new_person.split()[:2]).upper()
                        st.session_state.inbox[new_person] = {"initials": initials, "detail": "Session II student", "unread": 0, "messages": []}
                    st.session_state.active_chat = new_person
                    st.rerun()
        with thread:
            person = st.session_state.active_chat
            chat = st.session_state.inbox[person]
            st.markdown(f'<div class="thread-title"><div class="mini-avatar">{escape(chat["initials"])}</div><div><h3 style="margin:0">{escape(person)}</h3><div class="muted">{escape(chat["detail"])} · Connected through YYGS</div></div></div>', unsafe_allow_html=True)
            with st.popover("Conversation options"):
                if st.button("Unmute" if chat["muted"] else "Mute", use_container_width=True):
                    chat["muted"] = not chat["muted"]
                    st.rerun()
                if st.button("Archive", use_container_width=True):
                    st.session_state.archived_chats.add(person)
                    remaining = [n for n in st.session_state.inbox if n not in st.session_state.archived_chats]
                    if remaining: st.session_state.active_chat = remaining[0]
                    st.rerun()
                if st.button("Report conversation", use_container_width=True):
                    chat["reported"] = True
                    st.toast("Report submitted for staff review.")
                if st.button("Delete conversation", use_container_width=True):
                    del st.session_state.inbox[person]
                    remaining = list(st.session_state.inbox)
                    if remaining: st.session_state.active_chat = remaining[0]
                    st.rerun()
            find_message = st.text_input("Search this conversation", placeholder="Search messages", label_visibility="collapsed")
            if chat["messages"]:
                message_html = []
                visible_messages = [m for m in chat["messages"] if find_message.lower() in m["text"].lower()]
                for message in visible_messages:
                    bubble = "message-out" if message["from"] == "me" else "message-in"
                    status = f" · {message.get('status', '')}" if message["from"] == "me" else ""
                    message_html.append(f'<div class="{bubble}">{escape(message["text"])}<div class="message-time">{escape(message["time"])}{status}</div></div>')
                st.markdown(f'<div class="comm-shell">{"".join(message_html)}</div>', unsafe_allow_html=True)
            else:
                st.markdown('<div class="comm-shell"><div class="muted" style="text-align:center;padding:5rem 1rem">No messages yet. Introduce yourself and mention how you found them.</div></div>', unsafe_allow_html=True)
            with st.form("private_message", clear_on_submit=True):
                message_text = st.text_input("Message", placeholder=f"Message {person}…", label_visibility="collapsed")
                sent = st.form_submit_button("Send message", type="primary")
            if sent and message_text.strip():
                chat["messages"].append({"from": "me", "text": message_text.strip(), "time": datetime.now().strftime("%I:%M %p").lstrip("0"), "status": "Delivered"})
                chat["last_activity"] = int(datetime.now().timestamp())
                st.rerun()


def profile():
    initials = "".join(x[0] for x in st.session_state.name.split()[:2]).upper()
    st.markdown(f"""<div class="hero" style="background:linear-gradient(125deg,#162c46,#2d5f9d)">
    {avatar_html(initials, 78)}
    <h1 style="margin-bottom:.15rem">{st.session_state.name}</h1><p>{st.session_state.country} &nbsp;·&nbsp; {st.session_state.track} &nbsp;·&nbsp; Session II &nbsp;·&nbsp; {st.session_state.role}</p></div>""", unsafe_allow_html=True)
    left, right = st.columns([1.6,1])
    with left:
        st.markdown("### About me")
        st.session_state.bio = st.text_area("Bio", st.session_state.bio, max_chars=220, label_visibility="collapsed")
        st.markdown("### Interests")
        st.markdown(" ".join(f'<span class="pill">{x}</span>' for x in st.session_state.interests), unsafe_allow_html=True)
        with st.expander("Edit profile details"):
            photo = st.file_uploader("Update profile photo", type=["png", "jpg", "jpeg"], key="profile_photo_upload")
            if photo:
                st.session_state.profile_photo = f"data:{photo.type};base64,{base64.b64encode(photo.getvalue()).decode()}"
            countries = ["Argentina", "Australia", "Brazil", "Canada", "Chile", "China", "Colombia", "Egypt", "France", "Germany", "Ghana", "India", "Indonesia", "Italy", "Japan", "Kenya", "Mexico", "Morocco", "Netherlands", "Nigeria", "Pakistan", "Peru", "Philippines", "Poland", "Singapore", "South Africa", "South Korea", "Spain", "Sweden", "Thailand", "Turkey", "Ukraine", "United Kingdom", "United States", "Vietnam", "Other"]
            tracks = ["IST", "PLE", "SGC"]
            st.session_state.country = st.selectbox("Country or region", countries, index=countries.index(st.session_state.country))
            st.session_state.track = st.radio("Academic track", tracks, index=tracks.index(st.session_state.track), horizontal=True)
            st.session_state.interests = st.multiselect("Interests", ["Artificial Intelligence", "Biology", "Climate", "Debate", "Entrepreneurship", "Music", "Photography", "Public Speaking", "Sports", "Writing"], default=st.session_state.interests, max_selections=5)
    with right:
        st.markdown("### Your YYGS journey")
        st.markdown(f'<div class="card"><b>{len(st.session_state.joined)} spaces joined</b><div class="muted">Keep exploring to find more people.</div><br><div class="progress-wrap"><div class="progress-fill" style="width:72%"></div></div><div class="muted" style="margin-top:.5rem">Profile 72% complete</div></div>', unsafe_allow_html=True)
        if st.button("Save profile", type="primary", use_container_width=True): st.toast("Profile saved!")
        st.markdown("### Program role")
        st.markdown(f'<div class="card"><div class="eyebrow">CURRENT ACCESS</div><h3>{st.session_state.role}</h3><div class="muted">Students can join spaces, message peers, create activities, and report content. Staff and moderators receive announcement and moderation controls.</div></div>', unsafe_allow_html=True)


init_state()
if not st.session_state.logged_in:
    login()
elif not st.session_state.onboarded:
    onboarding()
else:
    top_nav()
    {"Home": home, "Community": community, "Communications": communications, "Profile": profile}.get(st.session_state.page, home)()
