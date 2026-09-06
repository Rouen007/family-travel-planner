# Universal Agent Guide (OpenAI Codex / ChatGPT / Copilot / Open-Source Harnesses)

This repository provides a standardized skill specification and templates for multi-generational family travel planning.

## System Prompt & Workflow
- Read `SKILL.md` for child age cohorts (0-2yo, 3-6yo, 7-12yo) and transportation engines (HSR vs EV/Gas Roadtrip).
- Read `templates/questionnaire.md` and `templates/departure_checklist_template.md` to guide user inputs and build stage-based leave-hotel/leave-car checklists.
- Apply age-graded dining matrices and hands-on non-heritage activity matching.
- For every hotel/vehicle transition, record must-bring, optional, and leave-behind items; never recommend leaving valuables, cameras, batteries, or heat-sensitive items in a hot vehicle.
- Execute `python3 scripts/cli.py all --input <markdown_file> --output-dir <dist_dir>` to compile Word docx, web SPA, and 2K long posters.
