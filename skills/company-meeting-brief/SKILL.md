---
name: company-meeting-brief
description: Research a company and prepare a person for a meeting by explaining who the company is, what its products do, and the facts and questions worth knowing beforehand. Use this whenever the user shares company links or asks for a company briefing, interview preparation, or a pre-meeting research report. Gather and verify findings in a plan phase, then create a cited HTML report during the build phase.
---

# Company Meeting Brief

Prepare a useful, sourced briefing about a company before a meeting. The user
may provide the company name, one or more URLs, and meeting context in the
request or `$ARGUMENTS`. Follow a plan-then-build workflow so research can be
reviewed before it becomes a report.

## Plan phase: research first

1. Identify the company, the meeting purpose and audience if given, and every
   URL supplied by the user. Open and review each supplied URL. If a URL is
   inaccessible, record that instead of silently skipping it.
2. Gather the information needed for the meeting. Cover who the company is,
   what its products or services do, who they serve, its business and market
   context, and relevant recent developments. Include leadership, competitors,
   risks, or other facts when they matter to the meeting.
3. Use relevant available research tools to fill gaps and verify important
   claims. Prefer primary sources such as the company's product and leadership
   pages, regulatory filings, and official announcements. Use reliable
   independent sources for context. Distinguish a company's own claims from
   independently supported facts, and note when sources conflict or appear
   outdated.
4. Keep a source list and connect each material claim to its supporting URL.
   Record the access date for time-sensitive information. Do not invent facts
   or present an inference as confirmed information.
5. In the plan phase, present a concise research summary, the sources reviewed,
   any inaccessible links or unresolved questions, and a proposed report
   outline. Do not create the HTML report during this phase. When the research
   is ready, hand off for the build phase; if the user has not asked to build
   yet, wait for that instruction.

## Build phase: create the report

1. Check the root `interviews/` directory for existing reports and follow
   their useful patterns for naming, content, and presentation. If the
   directory or examples do not exist, create the directory and use the
   report structure below.
2. Create a standalone HTML file at
   `interviews/<company>-meeting-brief.html`. Use a filesystem-safe company
   slug. If a report with that name already exists, choose a distinct filename
   rather than overwriting it.
3. Include source links near the claims they support and a sources section
   with publisher, page title, URL, and access date where available. Make the
   report readable in a browser, with clear headings and responsive styling.
   Keep the structure simple and do not require external libraries or assets.
4. Tailor the level of detail to the meeting. Explain jargon, prioritize
   decision-useful facts, and separate confirmed facts, company statements,
   and reasoned inferences.
5. After saving, report the file path and briefly note the coverage and any
   material source limitations.

## Suggested report structure

- **At a glance:** who they are, their sector, location or reach, and a short
  summary of what the company does.
- **What the company does:** products and services, how they work, and who
  uses them.
- **Business and market context:** business model, customer segments, market
  position, and relevant competitors when supported by sources.
- **People and developments:** relevant leadership and recent news or
  announcements.
- **Meeting preparation:** useful context, likely discussion areas, and
  thoughtful questions tailored to the meeting purpose.
- **Sources:** linked references for factual claims.
