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

    # Define options as strings to avoid type errors
    options = ["N/A", "0", "1", "2", "3", "4", "5"]

    # Generate rating fields for each criterion
    for criterion in criteria:
        selected = st.selectbox(
            f"{criterion}:",
            options=options,
            format_func=lambda x: "Not Applicable" if x == "N/A" else x
        )
        # Store value as integer if not "N/A"
        ratings[criterion] = selected if selected == "N/A" else int(selected)

    st.write("---")

    # Submit button
    if st.button("Submit Evaluation"):
        st.write("### Candidate Evaluation Summary")

        # Display evaluation summary
        evaluation_summary = ""
        valid_scores = []

        # Build evaluation text
        for criterion, score in ratings.items():
            evaluation_summary += f"{criterion}: {score}\n"
            if score != "N/A":
                valid_scores.append(score)

        # Calculate average score
        if valid_scores:
            average_score = sum(valid_scores) / len(valid_scores)
        else:
            average_score = 0

        # Map average score to a descriptive rating
        rating_description = {
            (0, 1): "Poor",
            (1, 2): "Needs Improvement",
            (2, 3): "Fair",
            (3, 4): "Good",
            (4, 5): "Very Good",
            (5, 6): "Excellent"
        }
        overall_rating = next(
            (text for (low, high), text in rating_description.items() if low <= average_score < high),
            "No Rating"
        )

        # Append average score and overall rating to the summary
        evaluation_summary += f"\nAverage Score: {average_score:.2f}\n"
        evaluation_summary += f"Overall Rating: {overall_rating}\n"

        # Display summary in a textbox
        st.text_area("Evaluation Summary", value=evaluation_summary, height=400)

if __name__ == "__main__":
    main()
