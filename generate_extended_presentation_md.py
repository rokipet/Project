from datetime import datetime
from pathlib import Path

OUTPUT_PATH = Path("MOVIE_PRESENTATION_GUIDE.md")

HEADER = """# Movie Rating Prediction Project

## Presentation Guide (Extended Edition)
"""

SECTIONS = [
    {
        "title": "1. Welcome & Hook (2 minutes)",
        "content": [
            "Open with a question: *\"How many of you have decided what to watch based on a recommendation?\"*",
            "Share a quick story about scrolling endlessly through movie options.",
            "Explain that the project helps predict how much someone will like a movie, so recommendations feel personal." ,
            "Preview the roadmap: problem, data, model, demo, and impact."
        ],
    },
    {
        "title": "2. Problem Statement (3 minutes)",
        "content": [
            "Describe the challenge: streaming platforms struggle to highlight the right movie for each viewer.",
            "Quantify the frustration with a statistic or anecdote about time spent searching for content.",
            "Explain that predicting movie ratings lets us rank options by likely enjoyment.",
            "Connect the problem to audience pain points: wasted time and missed great movies."
        ],
    },
    {
        "title": "3. Data Deep Dive (5 minutes)",
        "content": [
            "Introduce the MovieLens dataset with millions of user ratings.",
            "Highlight key tables: users, movies, and ratings with timestamps.",
            "Explain basic cleaning: removing duplicates, handling missing fields, and normalizing titles.",
            "Share insights from exploration: rating distributions, popular genres, and user activity levels.",
            "Use visuals such as histograms of ratings and heatmaps of genre preference.",
        ],
    },
    {
        "title": "4. Feature Engineering (4 minutes)",
        "content": [
            "Summarize baseline features: user averages, movie averages, and global bias.",
            "Explain additional signals: genre embeddings, release year, and recency of ratings.",
            "Discuss how you encoded categorical data (e.g., one-hot genres, embeddings).",
            "Emphasize the goal: represent both user taste and movie characteristics for the model."
        ],
    },
    {
        "title": "5. Modeling Approach (6 minutes)",
        "content": [
            "Walk through the chosen algorithm: matrix factorization with bias terms.",
            "Explain training: alternating least squares or gradient descent with regularization.",
            "Highlight evaluation metrics: RMSE and MAE on validation folds.",
            "Compare with baselines: simple average vs. collaborative filtering gains.",
            "Mention hyperparameter tuning and cross-validation setup.",
        ],
    },
    {
        "title": "6. Demo & Visualization (5 minutes)",
        "content": [
            "Show a live notebook or pre-recorded demo of recommending top movies for a sample user.",
            "Highlight ranking changes when user preferences shift (e.g., likes thrillers vs. comedies).",
            "Include a visualization of latent factors to explain how similar movies cluster.",
            "Share before/after scenario: what recommendations looked like pre-model vs. post-model.",
        ],
    },
    {
        "title": "7. Impact & Business Value (4 minutes)",
        "content": [
            "Translate accuracy improvements into user engagement metrics (e.g., increased watch time).",
            "Outline how better recommendations reduce churn and improve satisfaction.",
            "Discuss personalization: tailoring marketing campaigns, homepage carousels, and notifications.",
            "Mention possible A/B tests to validate the recommendation lift.",
        ],
    },
    {
        "title": "8. Limitations & Future Work (3 minutes)",
        "content": [
            "Call out data sparsity issues for new users or niche movies (cold start).",
            "Note ethical considerations: avoiding feedback loops and filter bubbles.",
            "Propose enhancements: hybrid models with content metadata or NLP on movie plots.",
            "Suggest scaling to real-time recommendations with streaming data pipelines.",
        ],
    },
    {
        "title": "9. Q&A Preparation (2 minutes)",
        "content": [
            "Prepare answers about data privacy and compliance (GDPR, anonymization).",
            "Anticipate questions on explainability: how to surface reasons for recommendations.",
            "Practice speaking to infrastructure: deployment stack, APIs, and monitoring.",
        ],
    },
    {
        "title": "10. Closing & Call-to-Action (2 minutes)",
        "content": [
            "Reiterate the core message: personalized recommendations delight users and boost engagement.",
            "Invite stakeholders to pilot the model with a small user segment.",
            "Provide follow-up resources: GitHub repo, dashboards, and documentation links.",
            "End with a memorable statement tying back to the opening story.",
        ],
    },
]

SUPPORTING_MATERIAL = {
    "Speaking Tips": [
        "Use simple analogies such as \"matching movie taste buds\" when describing the model.",
        "Pause after visuals to let the audience absorb the takeaway.",
        "Engage with questions throughout rather than waiting until the end.",
        "Keep your tone enthusiastic—this is about helping people find stories they love!",
    ],
    "Slide Suggestions": [
        "Title slide with a movie reel background and presentation goals.",
        "Data overview slide with infographics summarizing users, movies, and ratings counts.",
        "Model architecture slide illustrating user and movie latent factors.",
        "Results slide with metric improvements in bold numbers.",
        "Appendix slides for backup: evaluation metrics, sample user profiles, and glossary.",
    ],
    "Rehearsal Checklist": [
        "Time each section to stay within the 30-minute window.",
        "Test the demo on the presentation device beforehand.",
        "Prepare fallback screenshots in case the demo environment fails.",
        "Print a one-page summary for quick reference during Q&A.",
    ],
}

FOOTER = """\n---\nGenerated on {date}. Feel free to customize sections, add your own visuals, and adapt the timing to your speaking style.\n"""

def format_section(section: dict) -> str:
    lines = [f"## {section['title']}\n"]
    for bullet in section["content"]:
        lines.append(f"- {bullet}\n")
    lines.append("\n")
    return "".join(lines)


def format_supporting_material(supporting: dict) -> str:
    blocks = ["# Supporting Materials\n\n"]
    for title, items in supporting.items():
        blocks.append(f"## {title}\n")
        for item in items:
            blocks.append(f"- {item}\n")
        blocks.append("\n")
    return "".join(blocks)


def build_document() -> str:
    sections_text = "".join(format_section(section) for section in SECTIONS)
    supporting_text = format_supporting_material(SUPPORTING_MATERIAL)
    date_str = datetime.now().strftime("%B %d, %Y")
    return f"{HEADER}{sections_text}{supporting_text}{FOOTER.format(date=date_str)}"


def main() -> None:
    document = build_document()
    OUTPUT_PATH.write_text(document, encoding="utf-8")
    print(f"Extended presentation guide written to {OUTPUT_PATH.resolve()}")


if __name__ == "__main__":
    main()
