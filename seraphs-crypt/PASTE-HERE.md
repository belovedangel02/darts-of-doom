# Which file goes where

Read this before pasting anything into JanitorAI.

## The short answer

| Where you are pasting | File to use |
|---|---|
| **Settings → About Me** | `profile-complete-lean.txt` |
| CSS Editor (optional, only if you want a second copy of the site-wide styling) | `profile-css-lean.txt` |

That is the whole answer. Everything below explains why, and what the other
files are for.

## The rule that matters

**A `<style>` tag is HTML, not CSS.**

- **About Me** takes HTML. A `<style>` block inside it works — that is how the
  bought themes do it, four `<style>` blocks in one paste.
- **The CSS Editor** takes CSS only. Paste a file that begins with `<style>`
  into it and the very first line is a syntax error, so the browser throws the
  whole stylesheet away and *nothing* gets styled.

So a file starting with `<style>` belongs in About Me and nowhere else. A file
starting with `/*` belongs in the CSS Editor and nowhere else.

## Every file in this folder

| File | Starts with | Paste into |
|---|---|---|
| `profile-complete-lean.txt` | `<style>` | **About Me** — the one-paste file. Styling + bio in one block. |
| `profile-bio.html` | `<div>` | About Me, if you want the bio *without* any site-wide styling. |
| `profile-bio.txt` | `<div>` | Identical copy of `profile-bio.html`. Same thing, friendlier extension. |
| `profile-css-lean.txt` | `/*` | **CSS Editor** — the site-wide styling on its own. |
| `profile-complete.txt` | `<style>` | About Me. Works, but see the warning below. |
| `profile-css.txt` | `/*` | CSS Editor. Works, but see the warning below. |

## Warning about the two big files

`profile-css.txt` and the `<style>` block inside `profile-complete.txt` are
built on selectors like `.character-card__name` and `.character-card__wrapper`.

**JanitorAI does not use those class names.** They were invented. The real page
ships semantic classes like `.pp-uc-about-me` and `.profile-info-stack`, plus
hashed ones like `.css-15w88gn`. So most of those 600 lines match nothing on the
page and do nothing at all. They are not harmful, just inert — and they make the
paste four times larger for no gain.

The `-lean` files avoid this. They target things that genuinely exist:
`body`, `summary`, `input[placeholder*="earch"]`, and substring matches like
`[class*="wrapper"]` that survive a redeploy because only the hash changes.

See [`JANITOR-SELECTORS.md`](JANITOR-SELECTORS.md) for the real class names.

**Use the `-lean` files.** The big ones are kept for reference only.

## Before you publish

Search the file you are about to paste for `PASTE_` and replace every
placeholder with a real direct URL — character images, Carrd, guides, friends.
