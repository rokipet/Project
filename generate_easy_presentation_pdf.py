import textwrap

# Content for the PDF
sections = [
    {"text": "Movie Rating Prediction Project", "size": 24, "font": "F1", "spacing": 32},
    {"text": "Easy Presentation Guide", "size": 18, "font": "F1", "spacing": 28},
    {"text": " " , "size": 12, "font": "F2", "spacing": 18},
    {"text": "1. Start with a quick hook (30 seconds)", "size": 16, "font": "F1", "spacing": 26},
    {"text": "Open with a question: \"How many times have you watched a movie you didn't love?\"", "size": 12, "font": "F2", "spacing": 18},
    {"text": "Promise the outcome: our model predicts ratings before you press play.", "size": 12, "font": "F2", "spacing": 18},
    {"text": " ", "size": 12, "font": "F2", "spacing": 18},
    {"text": "2. Share the simple story (2 minutes)", "size": 16, "font": "F1", "spacing": 26},
    {"text": "Slide 1 – The problem: people rate 100k movies but most pairs are unknown.", "size": 12, "font": "F2", "spacing": 18},
    {"text": "Slide 2 – Our solution: a three-step pipeline that groups users, makes rules, and finds hidden tastes.", "size": 12, "font": "F2", "spacing": 18},
    {"text": "Slide 3 – Visual cue: reuse the K-Means clusters graphic and label each cluster with a persona.", "size": 12, "font": "F2", "spacing": 18},
    {"text": " ", "size": 12, "font": "F2", "spacing": 18},
    {"text": "3. Explain each method with analogies (3 minutes)", "size": 16, "font": "F1", "spacing": 26},
    {"text": "K-Means → Study groups: show a table with \"Movie Lovers\" through \"Critics\" and their habits.", "size": 12, "font": "F2", "spacing": 18},
    {"text": "Decision Tree → Flowchart: walk top to bottom, highlighting how we branch on movie popularity and generosity.", "size": 12, "font": "F2", "spacing": 18},
    {"text": "Matrix Factorization → Hidden tastes: compare to Spotify uncovering your secret playlist vibe.", "size": 12, "font": "F2", "spacing": 18},
    {"text": "Tip: keep each explanation under 40 seconds and point to the matching slide icon.", "size": 12, "font": "F3", "spacing": 18},
    {"text": " ", "size": 12, "font": "F2", "spacing": 18},
    {"text": "4. Highlight results and impact (1 minute)", "size": 16, "font": "F1", "spacing": 26},
    {"text": "Share the rating accuracy snapshot and the insight that users are generous (average 3.5 stars).", "size": 12, "font": "F2", "spacing": 18},
    {"text": "Connect back to the hook: we help people skip mediocre movies and surface hidden gems.", "size": 12, "font": "F2", "spacing": 18},
    {"text": " ", "size": 12, "font": "F2", "spacing": 18},
    {"text": "5. Close with engagement (30 seconds)", "size": 16, "font": "F1", "spacing": 26},
    {"text": "Ask for a volunteer's favorite genre and describe how the model would tailor picks for them.", "size": 12, "font": "F2", "spacing": 18},
    {"text": "Invite questions: \"Want to know which part of the pipeline matters most?\"", "size": 12, "font": "F2", "spacing": 18},
    {"text": " ", "size": 12, "font": "F2", "spacing": 18},
    {"text": "Presenter checklist", "size": 16, "font": "F1", "spacing": 24},
    {"text": "✓ Practice with the simple slide deck (PRESENTATION_SIMPLE.md).", "size": 12, "font": "F2", "spacing": 18},
    {"text": "✓ Keep each phase under one minute to stay within a 7-minute talk.", "size": 12, "font": "F2", "spacing": 18},
    {"text": "✓ Use stories: \"Imagine Netflix texting you your rating before you watch.\"", "size": 12, "font": "F2", "spacing": 18},
    {"text": "✓ Bring up the data chart (01_data_exploration.png) when discussing generosity of ratings.", "size": 12, "font": "F2", "spacing": 18},
    {"text": "✓ End by restating the value: smarter movie nights with personalized predictions.", "size": 12, "font": "F2", "spacing": 18},
]


def escape_pdf_text(text: str) -> str:
    return text.replace("\\", r"\\\\").replace("(", r"\\(").replace(")", r"\\)")


content_lines = []
y = 760

for item in sections:
    text = item["text"]
    size = item["size"]
    font = item["font"]
    spacing = item["spacing"]

    if not text.strip():
        y -= spacing
        continue

    wrapped = textwrap.wrap(text, width=90 if size <= 12 else 70)
    for idx, line in enumerate(wrapped):
        safe_text = escape_pdf_text(line)
        content_lines.append("BT")
        content_lines.append(f"/{font} {size} Tf")
        content_lines.append(f"72 {y} Td")
        content_lines.append(f"({safe_text}) Tj")
        content_lines.append("ET")
        y -= spacing if size <= 12 else spacing
        # Reduce extra space after wrapped lines except last
        if idx < len(wrapped) - 1:
            y += spacing - 14
    y -= 6

content_stream = "\n".join(content_lines)
content_bytes = content_stream.encode("utf-8")

objects = []
objects.append("1 0 obj << /Type /Catalog /Pages 2 0 R >> endobj\n")
objects.append("2 0 obj << /Type /Pages /Kids [3 0 R] /Count 1 >> endobj\n")
objects.append("3 0 obj << /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Contents 4 0 R /Resources << /Font << /F1 5 0 R /F2 6 0 R /F3 7 0 R >> >> >> endobj\n")
objects.append(f"4 0 obj << /Length {len(content_bytes)} >> stream\n".encode("utf-8") + content_bytes + b"\nendstream\nendobj\n")
objects.append("5 0 obj << /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold >> endobj\n")
objects.append("6 0 obj << /Type /Font /Subtype /Type1 /BaseFont /Helvetica >> endobj\n")
objects.append("7 0 obj << /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Oblique >> endobj\n")

# Build PDF
pdf_parts = [b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n"]
xref_positions = []
current_position = len(pdf_parts[0])

for obj in objects:
    if isinstance(obj, bytes):
        data = obj
    else:
        data = obj.encode("utf-8")
    xref_positions.append(current_position)
    pdf_parts.append(data)
    current_position += len(data)

xref_start = current_position
xref_entries = [b"0000000000 65535 f \n"]
for pos in xref_positions:
    xref_entries.append(f"{pos:010d} 00000 n \n".encode("ascii"))

pdf_parts.append(b"xref\n")
pdf_parts.append(f"0 {len(xref_entries)}\n".encode("ascii"))
pdf_parts.extend(xref_entries)

pdf_parts.append(b"trailer << /Size {size} /Root 1 0 R >>\n".replace(b"{size}", str(len(xref_entries)).encode("ascii")))
pdf_parts.append(b"startxref\n")
pdf_parts.append(f"{xref_start}\n".encode("ascii"))
pdf_parts.append(b"%%EOF\n")

with open("MOVIE_PRESENTATION_GUIDE.pdf", "wb") as f:
    for part in pdf_parts:
        f.write(part)

print("Created MOVIE_PRESENTATION_GUIDE.pdf")
