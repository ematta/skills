# Skills

This repository collects independent skills. Each skill lives in its own
directory under `skills/` and is described by a `SKILL.md` file in that
directory.

## Install skills

Use the [`skills` CLI](https://github.com/vercel-labs/skills) through `npx`.
Run these commands from the project where you want the skills installed:

```sh
# Install both skills from this repository
npx skills add ematta/skills \
  --skill company-meeting-brief \
  --skill job-description-review

# Install just one skill
npx skills add ematta/skills --skill company-meeting-brief
```

By default, skills are installed for the current project. Add `-g` to install
them globally instead. After installation, run `npx skills update` to update
installed skills.

## Add a skill

1. Create a directory under `skills/` with a short, lowercase name.
2. Copy `skills/_template/SKILL.md` into the new directory.
3. Replace the placeholder metadata and instructions with the skill's purpose
   and workflow.

Keep each skill focused on one kind of task. Add supporting scripts or
references alongside its `SKILL.md` when they are needed.
