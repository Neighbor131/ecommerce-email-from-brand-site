# Prompt Enhancement

Use this file only when the email needs generated imagery.

This step exists to prevent weak visuals caused by thin prompts.

## Goal

Turn the approved art direction into a stronger image-generation brief before sending it to the image workflow.

## When To Use

Use this step when:

- the user explicitly wants generated visuals
- the needed brand visual does not exist
- a new campaign composition is required
- the available site image exists but does not communicate strongly enough for the email module

Do not use it when real brand assets already solve the need.

Before using this step, first make a decision:

- `Keep` when the existing asset is already strong enough
- `Upgrade` when the real asset is right in substance but weak in execution
- `Generate` when the needed image does not exist or the concept cannot be communicated clearly enough otherwise

This file applies only to `Upgrade` and `Generate`, not to `Keep`.

## Input

Start from:

- the chosen email type
- the approved concept
- the module where the visual will live
- the brand audit
- the art direction notes
- the real product asset or product details when the image must stay tied to a real SKU

## Output

Produce a concise structured image brief covering:

- `Use case`
- `Asset type`
- `Primary request`
- `Subject`
- `Scene/backdrop`
- `Style/medium`
- `Composition/framing`
- `Lighting/mood`
- `Color palette`
- `Materials/textures`
- `Product prominence`
- `Constraints`
- `Avoid`

For banners, also include:

- `Communication goal`
- `Text-safe negative space`
- `Overlay placement`

## Guidance

- Keep the prompt faithful to the brand's real design language.
- Tie the composition to the email module. A hero needs different framing than a supporting card.
- Keep product visibility and click-driving clarity in mind.
- Use exact product or category names when they matter.
- State what should not appear.
- Avoid generic “premium modern minimal” filler unless the brand actually supports it.
- If the goal is an upgraded editorial banner, improve the communication quality, not just the polish.
- Preserve recognizable product identity when the banner is supposed to feature a real SKU.
- Ask what the viewer should understand in one glance: product launch, value mechanic, routine story, education angle, or reactivation cue.

## Hand-Off Rule

After the prompt is tightened, pass it into `$imagegen`.

If the request explicitly says to use Nano Banana, treat that as the preferred generation path within the image workflow.

## Important Constraint

Generated imagery should extend the brand system, not replace it.

For product-led banners, generated imagery should extend the real product system, not turn the item into a fictional reinterpretation.

Always note:

- what was sourced from real brand assets
- what was generated
- what still needs human review
