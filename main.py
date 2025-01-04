import streamlit as st
from datetime import datetime
from src.scraper.scrape import WebScraper
from src.analyzer.analyzer import CompetitorAnalysis
from src.visualization.dashboard import Dashboard
from src.utils.helpers import export_analysis


def main():
    st.title("AI-Powered Competitive Analysis Tool")
    st.sidebar.header("Analysis Settings")

    # Initialize session state
    if 'competitor_data' not in st.session_state:
        st.session_state.competitor_data = {}

    # Input section
    url = st.text_input("Enter Competitor Website URL")
    competitor_name = st.text_input("Enter Competitor Name")

    scraper = WebScraper()
    analyzer = CompetitorAnalysis()

    if st.button("Analyze Competitor"):
        if url and competitor_name:
            st.write(f"Analyzing {competitor_name}...")

            # Scrape and analyze
            html_content = scraper.scrape_website(url)
            body_content = scraper.extract_body_content(html_content)
            cleaned_content = scraper.clean_body_content(body_content)

            # Store analysis results
            st.session_state.competitor_data[competitor_name] = {
                'url': url,
                'content': cleaned_content,
                'date_analyzed': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'sentiment': analyzer.analyze_sentiment(cleaned_content),
                'key_features': analyzer.extract_key_features(cleaned_content),
                'focus_areas': analyzer.identify_competitors_focus(cleaned_content)
            }

            st.success(f"Successfully analyzed {competitor_name}")

    # Render dashboard if there's data
    if st.session_state.competitor_data:
        st.header("Competitive Analysis Dashboard")

        dashboard = Dashboard()
        dashboard.render_sentiment_chart(st.session_state.competitor_data)
        dashboard.render_focus_areas_chart(st.session_state.competitor_data)
        dashboard.render_competitor_details(st.session_state.competitor_data)

        # Export functionality
        if st.button("Export Analysis"):
            export_data = export_analysis(st.session_state.competitor_data)
            st.download_button(
                label="Download Analysis Report",
                data=export_data,
                file_name="competitive_analysis.json",
                mime="application/json"
            )


if __name__ == "__main__":
    main()
