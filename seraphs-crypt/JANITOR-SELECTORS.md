# JanitorAI selector map

What can actually be targeted on a JanitorAI profile page, and how.

Observed from working community templates (Hime, `@yourhighness08`) rather than
official docs. None of this is documented by JanitorAI, so it can break on any
redeploy. Class *names* are facts about the platform, not anyone's design — the
techniques below are noted so the crypt can use them without copying anyone's
stylesheet.

## Two kinds of class name

**Semantic, stable — use these.** They read like names a developer chose, and
they survive redeploys:

| Selector | What it is |
|---|---|
| `.pp-uc-about-me` | the container your About Me paste lands in |
| `.pp-uc-avatar` | profile picture |
| `.pp-uc-title` | the username heading |
| `.pp-uc-background` | the bio card's background panel |
| `.profile-info-stack` | outer column holding the whole profile block |
| `.profile-info-hstack` | row holding avatar + name |
| `.profile-page-flex` | wrapper around bio *and* the bot card list |
| `.profile-background-effect-image` | the blurred backdrop image |

**Hashed, unstable — avoid.** Emotion/CSS-in-JS output like `.css-15w88gn`,
`.css-1q7rmf0`. The hash is regenerated whenever the site is rebuilt, so a rule
written against one works until it silently doesn't.

When there is no semantic class, match on a substring instead:

```css
[class*="contentWrapper"]   /* survives .css-1abc-contentWrapper-xyz */
[class*="wrapper"]
```

Only the hash changes; the readable part usually stays.

**Not real:** `.character-card__name`, `.character-card__wrapper` and the rest
of the `.character-card__*` family. JanitorAI does not ship those. Our
`profile-css.txt` is built almost entirely on them, which is why it appears to
do nothing — see PASTE-HERE.md.

## The trick worth knowing

```css
.pp-uc-about-me { display: contents; }
```

`display: contents` removes the About Me box from the layout while keeping its
children. Those children then become direct items of the profile grid above
them, so a paste can lay out the *whole page* — cover image, sidebar, dropdown
column, creators panel — instead of being trapped inside one bio card.

That is the mechanism behind every paid theme with a sidebar or a two-column
bio. Combine it with a grid on the parent:

```css
@media screen and (min-width: 768px) {
  .profile-info-stack:first-child {
    display: grid;
    grid-template-columns: minmax(300px, 900px) minmax(300px, 900px);
    grid-template-areas:
      "cover  cover"
      "left   right"
      ".      follow";
  }
}
```

Each child then claims its cell with `grid-area: cover`, and so on.

## Other techniques observed

**Replace the username with display type** — zero out the real text, draw your
own in a pseudo-element:

```css
.pp-uc-title { font-size: 0; }
.pp-uc-title::after { content: 'BELOVED ANGEL'; font-size: clamp(4rem, 6vw, 6rem); }
```

**Horizontal scroll row** — for THE WORLDS and the devotion groups:

```css
.row   { display: flex; gap: 20px; overflow-x: auto; }
.card  { width: 300px; flex-shrink: 0; scroll-snap-align: start; }
```

**Stack bio above the bot cards** — `.profile-page-flex { flex-direction: column; }`

**Unrestrict the bio card's width** — `.pp-uc-background { max-width: unset; }`

## Observed on live profiles

Things seen working on real pages (Hime's *Carnal Archive*, Neri's *Come in,
Angel*, *Noli Timere Messorem*, *Circus Troupe*) that go past the bio box:

**The site's own wordmark can be replaced.** Top-left reads "Carnal Archive" or
"Come in, Angel" instead of JanitorAI. Same `font-size: 0` + `::after { content }`
move as the username.

**So can the counts and placeholders.** "296 laments", "15 reaped souls",
"2360 together, under the snowfield" in place of the follower count; "search
lament…", "Do not fear the reaper" in place of the search placeholder. Anything
rendered as text can be zeroed and redrawn.

**Sticky bottom bar** — *Noli Timere* pins a strip along the foot of the page
carrying a label and the search field. `position: fixed; bottom: 0`.

**Frosted glass** — *Come in, Angel* floats near-transparent panels over a
full-bleed background with `backdrop-filter: blur()`, which suits a misty
palette far better than solid fills.

**Full-bleed background behind everything**, header included — not just behind
the bio. Our `profile-css-lean.txt` already does this on `body`.

**A portrait row overlapping the hero** — five character plates centred beneath
the display name, breaking the boundary between cover and content.

**Left sidebar** — *Circus Troupe* puts avatar, follow button, stats and a
stacked nav column down the left, cards to the right. Grid areas on
`.profile-info-stack`, same mechanism as above.

Every one of these is reachable from a single About Me paste.

## What survives the sanitizer

| | |
|---|---|
| `<style>` blocks in About Me | ✅ works — the bought themes ship four in one paste |
| `<details>` / `<summary>` | ✅ works — the crypt's seals rely on it |
| `::before` / `::after` with `content:` | ✅ works |
| `@media` queries | ✅ works |
| Inline `style=""` | ✅ always works |
| `<iframe>` | ❌ stripped — killed the SoundCloud player |
| `<script>` | ❌ stripped |

Because `<style>` works in About Me, the CSS Editor is optional. One paste into
About Me can carry both the styling and the content.

## Image hosting

GitHub Pages works (`belovedangel02.github.io/darts-of-doom/...`) and is what
the crypt uses. Community templates lean on `imgur.com` and `file.garden`.
Any of them is fine as long as the URL points straight at the image file.
