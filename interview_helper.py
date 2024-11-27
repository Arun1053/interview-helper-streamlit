import streamlit as st

def main():
    st.title("Interview Evaluation Helper")
    st.write("Evaluate candidates based on various criteria using the scale below:")

    st.markdown("""
    ### Scoring Scale
    - **0:** Poor  
    - **1:** Needs Improvement  
    - **2:** Fair  
    - **3:** Good  
    - **4:** Very Good  
    - **5:** Excellent  
    - **N/A:** Not Applicable  
    """)

    st.write("---")

    # Define criteria
    criteria = [
        "Communication",
        "Programming (Python, OOP, multithreading)",
        "ML (Supervised/unsupervised/semi-supervised models)",
        "DL (ANN/CNN/RNN/LSTM)",
        "NLP",
        "Computer Vision (OpenCV, OCR)",
        "Gen AI (LLM, LLAMA, RAG)",
        "Frameworks (Django/Flask/Fast API)",
        "Database (MySql/Postgres/MongoDB/Redis)",
        "Deployment and Testing (CI-CD/MLOPS/docker/AWS/GCP)",
        "Version Control (GIT/bitbucket)",
        "Logical",
        "Libraries (Tensorflow/Pytorch/Pandas/Numpy/scikit/kafka)"
    ]

    # Initialize ratings dictionary
    ratings = {}

    # Generate rating fields for each criterion
    for criterion in criteria:
        ratings[criterion] = st.selectbox(
            f"{criterion}:",
            options=["N/A", 0, 1, 2, 3, 4, 5],
            format_func=lambda x: "Not Applicable" if x == "N/A" else x
        )

    st.write("---")

    # Submit button
    if st.button("Submit Evaluation"):
        st.write("### Candidate Evaluation Summary")

        # Display evaluation summary
        evaluation_summary = ""
        valid_scores = []
        for criterion, score in ratings.items():
            evaluation_summary += f"{criterion}: {score}\n"
            if score != "N/A":
                valid_scores.append(score)
        
        # Calculate average rating
        if valid_scores:
            average_score = sum(valid_scores) / len(valid_scores)
        else:
            average_score = 0

        # Map average score to rating description
        rating_description = {
            (0, 1): "Poor",
            (1, 2): "Needs Improvement",
            (2, 3): "Fair",
            (3, 4): "Good",
            (4, 5): "Very Good",
            (5, 6): "Excellent"
        }
        average_rating_text = next(
            (text for (low, high), text in rating_description.items() if low <= average_score < high),
            "No Rating"
        )

        # Display summary in a textbox
        st.text_area("Evaluation Summary", value=evaluation_summary, height=300)
        st.write(f"**Average Score (Excluding 'N/A'):** {average_score:.2f}")
        st.write(f"**Overall Rating:** {average_rating_text}")

if __name__ == "__main__":
    main()
