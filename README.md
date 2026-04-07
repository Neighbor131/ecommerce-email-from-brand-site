# Ecommerce Email From Brand Site

Build brand-faithful ecommerce emails from a real website, product catalog, editorial content, and email-layout references without drifting into generic copy or unsupported claims.

This skill is designed for staged work:

1. audit the brand
2. define the email strategy
3. write the copy
4. define the art direction
5. build HTML when needed

Supported email types:

- welcome
- promo / sale
- product launch
- bestseller / category push
- bundle / routine builder
- editorial / education
- winback / reactivation

## What This Package Includes

- `SKILL.md`
- `references/`
- `agents/openai.yaml`
- `scripts/gemini_email_banner.py`

## Image Behavior

The skill supports explicit image-decision modes:

- `Default Image Mode`
- `Conservative Image Mode`
- `Mixed Image Mode`
- `Aggressive Upgrade Mode`
- `Manual Override Mode`

Recommended default:

- keep strong existing imagery
- upgrade weak imagery only when needed
- generate only when required or explicitly requested

## Example Prompt

```text
Use $ecommerce-email-from-brand-site for https://www.example.com

Create an editorial email that drives readers from education into the product collection.

Use mixed image mode:
keep strong existing imagery, replace only weak visuals.

Deliver:
- brand_audit.md
- editorial_email_strategy.md
- editorial_email_copy_v1.md
- editorial_email_art_direction.md
- editorial_email.html

Stay faithful to the site’s real tone, product logic, and design direction.
Do not invent claims or promotions.
Flag anything that needs confirmation.
```

## Gemini Banner Generator

The included script can generate hero banners for:

- `welcome`
- `promo`
- `launch`
- `bestseller`
- `bundle`
- `editorial`
- `winback`

It can:

- save the banner into an email folder's `/assets/` directory
- optionally patch the HTML hero image source

## API Setup

Do not commit real API keys.

Use one of these approaches:

1. Export your key in the shell:

```bash
export GEMINI_API_KEY='your_key_here'
python3 scripts/gemini_email_banner.py editorial --patch-html
```

2. Copy `.env.example` to `.env.gemini` and add your own key there:

```bash
cp .env.example .env.gemini
```

Then edit:

```text
GEMINI_API_KEY='your_key_here'
```

## Install

Copy this folder into your Codex skills directory:

```bash
~/.codex/skills/ecommerce-email-from-brand-site
```

## Notes

- Use your own API keys.
- Review generated visuals manually before final send.
- Generated imagery should extend the brand system, not replace it.
