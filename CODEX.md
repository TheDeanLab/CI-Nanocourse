# CODEX Working Notes

## Slidev Markdown Formatting Rule
When a slide uses frontmatter/layout metadata, include a blank line after the closing `---` delimiter before the slide title.

Use this pattern:

```markdown
---
layout: image-right
image: /images/lecture-07/t07_from_s07.png
backgroundSize: contain
---

# Running Pytest
## Run tests from the command line with `pytest`
```

Do **not** place the title immediately after the closing delimiter.

Why this exists:
- Prevents recurring formatting drift in this deck.
- Keeps slide structure visually consistent.
- Makes frontmatter and slide content clearly separated.

## Editing Checklist for Slides
- Verify there is one blank line between closing frontmatter `---` and the first heading (`# ...`).
- Keep one `#` title and one `##` subtitle per slide.
- Preserve existing slide metadata keys (`layout`, `image`, `backgroundSize`, etc.).

## Text Density Limits
- Full-width text slides: keep total text to about 700 characters maximum.
- Half-width text slides (for example `layout: image-right`): keep total text to about 350 characters maximum.
- If a concept needs more text than the limit, split it across two slides.
