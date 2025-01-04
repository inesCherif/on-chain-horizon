import streamlit as st
import plotly.express as px
import pandas as pd
from datetime import datetime
import json


class Dashboard:
    @staticmethod
    def render_sentiment_chart(competitor_data):
        sentiment_data = {
            'Competitor': [],
            'Sentiment Score': []
        }

        for comp, data in competitor_data.items():
            sentiment_data['Competitor'].append(comp)
            sentiment_data['Sentiment Score'].append(data['sentiment'])

        df_sentiment = pd.DataFrame(sentiment_data)
        fig_sentiment = px.bar(df_sentiment, x='Competitor', y='Sentiment Score',
                               title='Competitor Sentiment Analysis')
        st.plotly_chart(fig_sentiment)

    @staticmethod
    def render_focus_areas_chart(competitor_data):
        focus_data = {
            'Competitor': [],
            'Focus Area': [],
            'Score': []
        }

        for comp, data in competitor_data.items():
            for area, score in data['focus_areas'].items():
                focus_data['Competitor'].append(comp)
                focus_data['Focus Area'].append(area)
                focus_data['Score'].append(score)

        df_focus = pd.DataFrame(focus_data)
        fig_focus = px.bar(df_focus, x='Focus Area', y='Score', color='Competitor',
                           barmode='group', title='Competitor Focus Areas')
        st.plotly_chart(fig_focus)

    @staticmethod
    def render_competitor_details(competitor_data):
        for competitor, data in competitor_data.items():
            with st.expander(f"Detailed Analysis - {competitor}"):
                st.write(f"**URL:** {data['url']}")
                st.write(f"**Analysis Date:** {data['date_analyzed']}")

                st.write("**Top Keywords:**")
                key_features_df = pd.DataFrame(data['key_features'],
                                               columns=['Word', 'Frequency'])
                st.dataframe(key_features_df)

                st.write("**Raw Content:**")
                st.text_area("", data['content'], height=200)
