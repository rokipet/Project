from datetime import datetime
from pathlib import Path

OUTPUT_PATH = Path("MOVIE_PRESENTATION_GUIDE.md")

HEADER = """# Movie Rating Prediction Project

## Easy Presentation Plan
"""

SECTIONS = [
    {
        "title": "1. Warm Welcome (2 minutes)",
        "content": [
            "Greet the audience and thank them for the time.",
            "Ask a friendly question: *\"Who has ever spent way too long picking a movie?\"*",
            "Share a one-sentence story about scrolling through endless choices.",
            "Explain in plain words that the project learns what each viewer likes so picks feel personal.",
        ],
    },
    {
        "title": "2. The Problem in Simple Terms (3 minutes)",
        "content": [
            "People waste time choosing something to watch and often give up.",
            "Streaming apps usually show the same lists to everyone.",
            "It is hard to guess what any one person will enjoy without smart help.",
            "Our goal: predict each viewer's rating (1 to 5 stars) so we can show better picks.",
        ],
    },
    {
        "title": "3. Meet the Data (4 minutes)",
        "content": [
            "We use the public MovieLens dataset that has real movie ratings from thousands of people.",
            "Key pieces: a table of users, a table of movies, and a table of ratings with dates.",
            "Simple cleanup: drop duplicates, fix missing titles, and keep ratings between 0.5 and 5.",
            "Easy takeaway: there are many ratings, most movies sit in the 3-4 star range, and some genres are very popular.",
        ],
    },
    {
        "title": "4. Building Helpful Inputs (4 minutes)",
        "content": [
            "Start with simple numbers like each user's average rating and each movie's average score.",
            "Add a few extras: movie release year, main genres, and how recent the last rating was.",
            "Turn genres into flags (1 = likes comedy, 0 = does not) so the model can read them.",
            "Point out that these inputs give the model both taste (user) and movie facts.",
        ],
    },
    {
        "title": "5. How the Model Works (5 minutes)",
        "content": [
            "We use a common recommendation idea called matrix factorization—think of it as matching taste profiles.",
            "Training goal: the model learns two short lists of numbers, one for each user and one for each movie.",
            "When we combine the lists we get a predicted rating; closer to the real rating is better.",
            "We check success with RMSE (lower is better) and compare to simple averages to show the win.",
        ],
    },
    {
        "title": "6. Show and Tell (5 minutes)",
        "content": [
            "Walk through a quick demo notebook or screenshots if live demos are risky.",
            "Pick a sample viewer and highlight how their top movie list changes as tastes shift.",
            "Use one clear chart that shows similar movies sitting close together.",
            "Summarize in a sentence what the audience should notice from the demo.",
        ],
    },
    {
        "title": "7. Why It Matters (4 minutes)",
        "content": [
            "Better picks mean people watch faster and stay engaged longer.",
            "Happier viewers lead to lower churn and more word-of-mouth.",
            "Marketing teams can send smarter notifications based on learned tastes.",
            "Suggest an easy pilot: run an A/B test with the new rankings for a small group.",
        ],
    },
    {
        "title": "8. Honest Limits & Next Steps (3 minutes)",
        "content": [
            "Cold start: brand-new users and brand-new movies need extra info to get started.",
            "We watch for fairness so we do not trap people in one narrow genre.",
            "Next ideas: mix in movie summaries, trailers, or friend activity to boost accuracy.",
            "Plan ahead for real-time updates so new ratings refresh the list quickly.",
        ],
    },
    {
        "title": "9. Ready for Questions (2 minutes)",
        "content": [
            "Prepare simple answers about data privacy: ratings are anonymous and stored securely.",
            "Have a short explanation of how the model picks movies (taste profile + movie profile).",
            "Know the basic deployment story: nightly training, an API for the app, and dashboard tracking.",
        ],
    },
    {
        "title": "10. Close with Confidence (2 minutes)",
        "content": [
            "Repeat the core promise: no more endless scrolling—viewers see movies they will likely love.",
            "Invite the audience to try the pilot or share a team who could benefit first.",
            "Share where to find the code, the slides, and a contact for follow-up.",
            "End with a short, upbeat line that echoes your opening story.",
        ],
    },
]

SUPPORTING_MATERIAL = {
    "Speaking Tips": [
        "Use everyday language—pretend you are explaining the idea to a friend over coffee.",
        "Pause after each chart and tell the audience the one thing they should notice.",
        "Invite quick reactions during the talk so it feels like a conversation.",
        "Keep energy high with smiles and eye contact; the topic is about enjoying movies!",
    ],
    "Slide Suggestions": [
        "Opening slide: project name, friendly movie-themed image, and the big promise.",
        "Problem slide: one bold stat about time wasted searching for something to watch.",
        "Data slide: simple table or icons showing how many users, movies, and ratings.",
        "Model slide: visual of two puzzle pieces coming together (user profile + movie profile).",
        "Results slide: side-by-side comparison of old vs. new recommendations in plain numbers.",
        "Backup slide: glossary with short definitions (RMSE, matrix factorization, cold start).",
    ],
    "Rehearsal Checklist": [
        "Time each section to stay within the 30-minute plan.",
        "Practice the demo on the same device you will present with.",
        "Save backup images or GIFs in case the demo will not load.",
        "Print or save a one-page cheat sheet with key numbers and stories.",
    ],
}

FOOTER = """\n---\nGenerated on {date}. Customize the plan, swap in your own stories, and have fun sharing the project!\n"""


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
    print(f"Easy presentation guide written to {OUTPUT_PATH.resolve()}")


if __name__ == "__main__":
    main()
