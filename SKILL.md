---
name: ecommerce-email-from-brand-site
description: Create brand-faithful ecommerce emails by auditing a brand's website, existing email examples, on-site product and editorial content, and reusable email layout references, then producing staged strategy, copy, art direction, and optional HTML build artifacts. Use when Codex needs to develop or rebuild ecommerce lifecycle or campaign emails such as welcome, promo, launch, bestseller, bundle, editorial, or winback emails that should drive clicks and purchases without becoming generic or inventing unsupported offers.
---

# Ecommerce Email From Brand Site

Use this skill to build ecommerce emails as a system, not as isolated blocks of copy.

Create the work in stages. Do not jump to final HTML or final copy before the earlier artifacts exist.

## Email Types

Support at minimum:

- welcome
- promo / sale
- product launch
- bestseller / category push
- bundle / routine builder
- editorial / education
- winback / reactivation

If the user does not specify an email type, infer the most likely one from the request and state that choice in the strategy file.

## Workflow

1. Build source context.
2. Build or refresh `brand_audit.md`.
3. Create an email-purpose strategy file.
4. Draft copy for one chosen concept.
5. Create visual direction.
6. Build HTML only when requested.
7. Create mobile notes whenever HTML is built.

If a required earlier artifact is missing, create it before moving forward.

## Naming Convention

Use filenames based on the email type slug.

Examples:

- `welcome_email_strategy.md`
- `promo_email_strategy.md`
- `launch_email_strategy.md`
- `bundle_email_strategy.md`
- `editorial_email_strategy.md`

Do the same for copy, art direction, HTML, and mobile notes:

- `<email_type>_email_copy_v1.md`
- `<email_type>_email_art_direction.md`
- `<email_type>_email.html`
- `<email_type>_email_mobile_notes.md`

If the user already has a preferred filename, follow it.

## Build Source Context

Review the strongest available source material before writing strategy or copy:

- homepage or primary landing page
- about page
- collection or category pages
- PDPs
- blog, editorial, journal, or story pages
- existing email examples in the repo or provided assets
- any reusable brand copy such as banners, FAQs, value props, founder story, shipping notes, onboarding text, subscription notes, or campaign language
- any reusable email pattern library the user provided

Start with local context first. Search the repo for likely source files, content collections, CMS exports, design assets, and prior emails. Use rendered pages or a live site only when they are available and useful.

Prefer evidence over inference. Pull repeated phrases, CTA language, offer framing, merchandising logic, category logic, and product logic from actual source material.

## Use Layout References Intentionally

Treat external template libraries and Figma email systems as a pattern library, not as copy sources.

Extract:

- module inventory
- email archetypes
- hierarchy patterns
- CTA cadence
- image-to-copy balance
- product density
- footer and utility patterns

Do not copy a reference brand's tone, claims, or campaign framing into the target brand.

Use [layout-patterns.md](references/layout-patterns.md) to choose layouts that match the email goal.

## Stage 1: Brand And Site Audit

Create `brand_audit.md`.

Cover these sections:

- `Brand Voice Traits`
- `Repeated Messaging Themes`
- `Audience Cues`
- `CTA Language`
- `Offer Mechanics`
- `Visual Language Patterns`
- `Relevant Product Categories`
- `What To Avoid`
- `Open Questions Requiring Human Confirmation`

For each section, distinguish between:

- direct observations from source material
- cautious inferences that are likely but not explicit

Capture enough specificity that later stages can sound like the brand without repeating homepage copy verbatim.

In `What To Avoid`, call out generic ecommerce habits that would flatten the brand, such as exaggerated urgency, invented savings language, vague category claims, luxury clichés, founder-story overreach, or campaign tropes that do not match the site.

## Stage 2: Email Strategy

Create `<email_type>_email_strategy.md` using `brand_audit.md`.

Include:

- email type
- purpose of the email
- primary conversion goal
- secondary goals
- target audience state or moment
- recommended layout archetype
- recommended module structure
- three creative directions
- subject line options for each direction
- preview text options for each direction
- assumptions and confirmation flags

Each creative direction should have:

- a short name
- a one-paragraph rationale tied to the audit
- ideal audience state or moment
- likely strengths and risks
- recommended layout style

Recommended module structure should be written in send order, for example:

- preheader
- hero
- proof or value statement
- category or product block
- offer or urgency block
- CTA
- footer

## Stage 3: Draft One Chosen Concept

Create `<email_type>_email_copy_v1.md`.

Choose the strongest concept from the strategy unless the user has already picked one. State which concept was chosen and why.

Include:

- subject line options
- preview text options
- full email body copy
- module-by-module content hierarchy
- CTA copy
- optional plain-text fallback
- confirmation flags

Write copy that feels native to the brand. Keep product references, promises, urgency, benefits, and offer framing constrained to what the source material supports.

If a compliance, promotional, or operational detail is unclear, insert a clearly labeled note instead of inventing it.

## Stage 4: Visual Direction

Create `<email_type>_email_art_direction.md`.

Include:

- hero image concept
- supporting visual concepts
- image prompt drafts for generation when needed
- art direction notes for typography, composition, and styling
- notes on which visuals should use real product or site assets instead of generated imagery
- recommended module emphasis
- confirmation flags

Root the visual direction in the site's real design language. Reference actual patterns such as crop style, background treatment, density of copy, product framing, use of people, editorial pacing, iconography, texture, and CTA treatment.

Do not default to generic gradient blobs, empty luxury minimalism, or random lifestyle photography if the site does not support it.

## Conditional Visual Generation

Do not generate imagery by default.

Use real site, product, campaign, or brand assets first whenever acceptable for the email.

Default image mode should be:

1. keep strong existing imagery
2. upgrade weak imagery only when needed
3. generate only when required or explicitly requested

Treat this as the normal behavior unless the user says otherwise.

Do not interpret this as “always use raw website photography unchanged.”

If the available site images are technically weak, poorly cropped, low-resolution, visually flat, or not strong enough to carry the email module, improve the visual outcome while staying anchored to real brand products.

Only switch to generated visuals when at least one of these is true:

- the user explicitly asks for generated imagery
- a required visual does not exist in the available brand assets
- the requested concept needs a new on-brand composition that cannot be assembled from existing assets

When generated visuals are needed:

1. Start from the approved art direction, not from a blank prompt.
2. Convert the visual direction into a tighter image-generation brief before making the image.
3. Use `$imagegen` for the generation workflow.
4. If the requested workflow explicitly calls for Nano Banana, use Nano Banana through the image-generation path.
5. Keep the generation brief anchored to the brand's real typography direction, color palette, editorial tone, composition style, and product logic.
6. Preserve a note about what came from real assets vs what was newly generated.

## Image Decision Modes

Support these user-intent modes explicitly:

### Default Image Mode

Use this when the user does not specify otherwise.

Rule:

- keep existing site or brand imagery if it is already high quality, on-brand, and strong enough for the email's communication job
- do not replace acceptable imagery just because generation is available
- upgrade or generate only where the visual is weak, unclear, low quality, poorly cropped, missing text-safe space, or not persuasive enough

### Conservative Image Mode

If the user says things like:

- use existing imagery unless it is clearly weak
- do not generate unless necessary
- keep site images when they are good enough

Then:

- strongly prefer real site and brand assets
- generate only for obvious problem areas

### Mixed Image Mode

If the user says things like:

- audit each hero image and decide
- keep strong ones, replace weak ones
- only generate when current images are not good enough

Then:

- evaluate each major visual module one by one
- keep strong images as-is
- upgrade or generate only the weak ones
- document which images were kept and which were replaced

### Aggressive Upgrade Mode

If the user says things like:

- treat site images as references only
- upgrade all banners
- generate improved hero images for all email types

Then:

- use the site's visual direction as reference material
- generate or heavily upgrade most hero/banner modules

### Manual Override Mode

If the user says things like:

- do not generate unless I explicitly say so
- use only real photography

Then:

- never generate without direct user approval
- stay within real site and brand assets only

When the user's wording maps to one of these modes, state the chosen mode briefly in the strategy or art direction file when useful.

If the user does not specify a mode, use `Default Image Mode`.

## Editorial Banner Upgrade Rule

For hero banners, editorial feature images, launch banners, and other image-led modules, prefer this decision order:

1. Use a strong existing brand asset as-is when it already communicates clearly.
2. Recompose real brand/product assets into a stronger editorial banner concept when the raw site image is weak but the product itself should stay real.
3. Generate a new on-brand banner only when an existing asset or recomposed real-product concept still cannot communicate the idea well enough.

When recomposing or generating a stronger banner, keep the product real and recognizable.

That means:

- use the real SKU, packaging, or category identity
- preserve recognizable product colors, shapes, labels, and form factor
- upgrade the framing, composition, lighting, backdrop, and storytelling around it
- optimize the image for communication in-email, not for generic beauty-shot aesthetics

Use this banner-upgrade path especially for:

- welcome heroes
- launch heroes
- promo banners
- editorial feature banners
- winback reactivation heroes

Do not use it for:

- simple support cards where existing product packshots are already clear enough
- situations where the user explicitly wants untouched original photography

The prompt-enhancement step should tighten:

- use case
- asset type
- subject
- composition
- lighting and mood
- palette
- texture and material cues
- product prominence
- exact constraints
- avoid list

When deciding whether to apply the banner-upgrade path, judge the current image against these questions:

- Is it high enough resolution for email use?
- Does it communicate the email's idea in one glance?
- Is there enough text-safe space?
- Does it feel like a campaign asset rather than a random site crop?
- Is the composition strong enough to earn a click?

If the answer is mostly yes, keep the image.
If the answer is mixed, upgrade the composition.
If the answer is no, generate a stronger banner.

Do not send a vague one-line art idea directly to image generation if a stronger prompt can be crafted first.

## Stage 5: Build

Create:

- `<email_type>_email.html`
- `<email_type>_email_mobile_notes.md`

Only build HTML if the user asked for production-ready email HTML or if the request explicitly includes the build stage.

When building:

- create a desktop and mobile email structure
- keep content blocks editable and clearly labeled with comments
- include image placeholders and alt text placeholders
- preserve safe fallbacks for email clients
- keep copy modular so humans can swap sections easily
- choose a layout archetype that fits the email goal rather than defaulting to one hero plus one button

In `<email_type>_email_mobile_notes.md`, describe:

- stacking order
- spacing adjustments
- type size adjustments
- image crop guidance
- any modules that should be hidden, simplified, or shortened on mobile

If the repo already uses a preferred email stack, follow it. Otherwise default to robust table-based HTML with inline-friendly structure and conservative CSS.

## Conversion Rules

- Optimize for getting the reader from inbox to site with a clear next action.
- Choose a primary CTA path and keep the rest subordinate.
- Match module count to the email goal: fewer, stronger blocks for conversion-first emails; longer pacing only when the format supports it.
- Use urgency, savings, or incentive language only when verified by source material.
- Prefer merchandising logic over filler copy.
- Use layout references to improve clarity and clickability, not to import another brand's identity.

## Prompt-Crafting Rule For Generated Visuals

If an email needs generated imagery, treat prompt crafting as a separate sub-step.

Use [prompt-enhancement.md](references/prompt-enhancement.md) to turn the art direction into a production-ready generation brief.

The goal is not to make the prompt longer for its own sake. The goal is to make the visual output more faithful to:

- the brand
- the email's conversion job
- the chosen module's placement in the layout
- the actual product or merchandising story

For editorial banners specifically, also make the brief explicit about:

- what the banner must communicate in one glance
- where the text overlay or negative space needs to live
- whether the product should feel dominant, integrated, or supporting
- whether the mood should feel launch-driven, educational, promotional, or reactivation-focused

## Source Handling Rules

- Stay faithful to the site's real tone and product logic.
- Do not invent product claims, promotions, testimonials, legal language, certifications, or shipping promises.
- Flag anything that requires human confirmation.
- When uncertain, leave a note rather than guessing.
- Prefer quotes, paraphrases, and patterns grounded in source material over invented brand language.

## Output Quality Checks

Before finishing, verify:

- each stage artifact exists before the next stage depends on it
- the email angle matches the observed audience and product logic
- the layout archetype matches the email purpose
- CTAs resemble real site language
- any offer or incentive is explicitly supported by source material
- the copy is not generic enough to fit any ecommerce brand
- unresolved questions are visible and easy for a human to answer

## References

- Use [artifact-spec.md](references/artifact-spec.md) as the deliverables checklist.
- Use [layout-patterns.md](references/layout-patterns.md) to choose reusable email structures and modules.
- Use [prompt-enhancement.md](references/prompt-enhancement.md) when generated visuals are requested or required.
