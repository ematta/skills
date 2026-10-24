---
name: job-description-review
description: Compare a job description with the user's resume, identify specialized domains and requirements, and assess role fit. Use this whenever the user shares a job posting or asks whether their resume fits a specific role, including when they provide a job URL. When qualified, write a tailored 250–300 word cover letter to the COVERLETTERS directory.
---

# Job Description Review

Use this skill to assess a specific job against the user's resume at
`@src/data/resume.json`. Keep the assessment grounded in the supplied posting
and resume. The goal is to help the user decide whether to pursue the role and,
when the resume supports it, provide a tailored cover letter.

## Workflow

1. Identify the company, role title, location, and job posting source. If the
   company is clear, name the conversation after it when the interface allows
   conversation renaming.
2. Read `@src/data/resume.json` and the complete job description. If the user
   supplied the posting text, use it directly. If they supplied a URL or ask
   you to find the posting, use Playwright MCP to open and read the page. Do not
   use fetch or other MCPs for this browser task. Close the browser when done,
   including when page access fails.
3. Extract the role's core responsibilities, required qualifications,
   preferred qualifications, and specialized domains. Separate requirements
   from preferences; do not treat a preferred qualification as mandatory.
4. Compare each important requirement with explicit resume evidence. Mark it
   as met, partially supported, not shown, or unclear. Cite the relevant resume
   experience or skills in plain language. Do not infer credentials, years of
   experience, or accomplishments that the resume does not state.
5. Give a qualification verdict based on the stated required qualifications.
   Explain the strongest matches and the most material gaps. If the posting or
   resume is incomplete, say what cannot be determined instead of overstating
   certainty.
6. If the resume supports that the user is qualified, write a tailored cover
   letter of 250–300 words and save it in `@COVERLETTERS`. Use a filename based
   on the company and role, with filesystem-safe characters. Refer only to
   experience and results supported by the resume. If the user is not
   qualified, do not create the letter; explain what evidence or experience is
   missing.

## Response format

### Role overview

- Company and title
- Specialized domains
- Main responsibilities and key requirements

### Resume match

Summarize the strongest evidence of fit, then list important requirements that
are partially supported, not shown, or unclear. Keep distinctions between
required and preferred qualifications visible.

### Qualification

State whether the user appears qualified based on the available evidence.
Give a short rationale and identify the main gaps or uncertainties.

### Next step

If qualified, state that a tailored cover letter was created and give its path.
If not qualified, give the most useful next step, such as addressing a
specific requirement or clarifying missing resume evidence.
