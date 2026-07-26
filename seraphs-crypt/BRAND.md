# The Seraph's Crypt — Core Aesthetic & Creator Branding Directive

Reference note for any AI assistant or collaborator working on Beloved Angel's
JanitorAI profile, bots, or related pages. Keep this locked in.

## Identity & Lore
- **Creator name / meaning:** Beloved Angel 🪽
- **Community name:** Angels
- **Brand domain / profile title:** The Seraph's Crypt
- **Pronouns:** she / her
- **Literary touchstones:** Edgar Allan Poe (*Annabel Lee* macabre romanticism),
  contemporary gothic, high-tension dark romance, Ana Huang-style grounded intensity.

## Writing Style & Prose Guidelines
- **Classification:** Atmospheric Dark Romance with Grounded Character Realism.
- **Sensory depth & visceral grounding:** mood, spatial contrast, physical touch,
  tangible real-world elements (leather, grease, motorcycles, cold shadows shifting
  into sun-drenched/moonlit sanctuary) — never purple prose or dramatic monologues.
- **Character archetype (the anti-trope safe haven):** male leads are action-oriented
  safe havens — brooding, fiercely loyal, protective, morally grey — showing affection
  through physical grounding, actions, and unshakeable devotion, not toxic control or
  cheesy speeches.
- **Narrative architecture:** high-tension pacing, cinematic framing, structured and
  interactive choice/starter options.

Maintain this exact atmospheric tone, macabre-romantic edge, and sensory realism in
all prose, bot setups, dialogue, and author notes for this project. 🖤🪽🥀

## Visual Design Tokens
- **Canvas:** `rgb(0,0,0)` page, `rgb(5,5,5)`–`rgb(7,6,8)` panels, `rgb(18,12,21)` header bars
- **Ink:** `rgb(222,219,225)` display · `rgb(197,184,202)` headings/accents ·
  `rgb(140,135,145)` body · `rgb(76,71,81)` whisper text
- **Borders:** `1px solid rgba(197,184,202, 0.14–0.35)`
- **Type:** Georgia serif for headings (letter-spaced caps), Arial/Helvetica for body
- **Motifs:** ☾ ✦ ✧ ♡ 🪽 🕯️ 🥀 ⚰️ — sparingly, as punctuation not decoration

## Section Header Pattern (from reference profiles, translated dark)
Pill-shaped bar: `rgb(18,12,21)` background, lavender border, `border-radius: 40px`,
Georgia serif letter-spaced title on the left, 30px circular icon chip
(`rgb(48,42,54)`, ✦/☾/♡) on the right. Rounded `18px` dark panel below carries the
section content. Sections: About Me ☾ · Rules ✦ · My Creations ✧ · Status ✦ ·
Upcoming Work ✦ · What to Expect ✦ · Content Notes ♡ · Bot Requests ☾ ·
Guides ✧ · Friends ✦ · Extra ♡.

## Files
- `profile-bio.html` — inline-styles-only bio for the JanitorAI profile editor
  (copy from the outer `<div>` down; fill every `PASTE_..._HERE` placeholder).
- `index.html` — full profile CSS demo / selector map (site-chrome styling).

## Platform notes
- The little circular badges under a JanitorAI username are site-awarded profile
  badges and cannot be added via bio HTML; the bio uses a decorative emblem row
  (🪽 🕯️ 🥀 ⚰️ 🌙 🖤) to echo the look.
- JanitorAI bios strip `<style>` blocks and classes — inline `style=""` only.
- Image slots need direct image URLs (raw.githubusercontent.com or catbox).
