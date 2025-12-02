import streamlit as st
import feedparser

st.set_page_config(page_title="Cybersecurity Threat Dashboard", layout="wide")

st.title("🔐 Top 10 Cybersecurity Threat News Dashboard")

# --- 10 Cybersecurity RSS Feeds ---
rss_feeds = {
    "The Hacker News": "https://feeds.feedburner.com/TheHackersNews",
    "Krebs on Security": "https://krebsonsecurity.com/feed/",
    "Bleeping Computer": "https://www.bleepingcomputer.com/feed/",
    "Dark Reading": "https://www.darkreading.com/rss.xml",
    "Cybersecurity News – SecurityWeek": "https://www.securityweek.com/feed/",
    "Malware Traffic Analysis": "https://www.malware-traffic-analysis.net/blog-entries.rss",
    "ThreatPost": "https://threatpost.com/feed/",
    "CSO Online Security": "https://www.csoonline.com/index.rss",
    "CERT-In India Alerts": "https://www.cert-in.org.in/RSS_Feed.xml",
    "Trend Micro Security Blog": "https://feeds.trendmicro.com/TrendMicroResearch"
}

# --- Function to get top news ---
def get_top_news(url):
    feed = feedparser.parse(url)
    return feed.entries[:1]  # Take only Top 1 from each (total = 10)

# --- Display Dashboard in Boxes ---
col1, col2 = st.columns(2)

i = 0
for source, url in rss_feeds.items():
    news = get_top_news(url)
    for item in news:
        i += 1
        box = col1 if i % 2 == 1 else col2

        with box:
            st.markdown(
                f"""
                <div style='padding:15px;border-radius:10px;background:#f2f2f2;margin-bottom:20px;'>
                    <h3>{i}. {source}</h3>
                    <p><b>{item.title}</b></p>
                    <a href='{item.link}' target='_blank'>Read full article</a>
                </div>
                """,
                unsafe_allow_html=True
            )
