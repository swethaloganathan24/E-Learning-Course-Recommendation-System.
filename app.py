import streamlit as st
import pandas as pd


st.set_page_config(
    page_title="Course Recommendation System",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)



def main():
    st.markdown(
        """
    <style>
        body {
            background-color: #0b1e34;
            color: white;
        }
        .st-bw {
            color: white;
        }
    </style>
    """,
        unsafe_allow_html=True,
    )

    st.title("Course Recommendation System")
    search_term = st.text_input("Search for a course")
    length = st.text_input("Enter the number of courses to display", 10)
    if st.button("Search") and search_term != "":
        if len(length) == 0:
            st.error("Please enter a valid number")
            return
        df = pd.read_csv("course_data_final.csv")
        df_filtered = df[df["Course Name"].str.contains(search_term, case=False, na=False)]
        df_filtered = df_filtered.sort_values(by="Average Score", ascending=False)
        df_filtered = df_filtered[["Course Name",  "Platform" ,"Average Rating", "Average Sentiment Score", "Number of Reviews"]]
        df_filtered = df_filtered[df_filtered["Number of Reviews"] > 10]
        df_filtered['Average Rating'] = df_filtered['Average Rating'].round(2)
        df_filtered['Average Sentiment Score'] = df_filtered['Average Sentiment Score'].round(2)
        df_filtered.index = range(1, len(df_filtered) + 1)
        df_filtered = df_filtered.head(int(length))
        st.dataframe(df_filtered)


if __name__ == "__main__":
    main()