#!/usr/bin/env python3
import argparse
import base64
import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path
from typing import Optional, Tuple


ROOT = Path(__file__).resolve().parent.parent
LOCAL_ENV_FILE = ROOT / ".env.gemini"


BANNER_JOBS = {
    "welcome": {
        "output": ROOT / "welcome" / "assets" / "welcome-hero-banner.png",
        "html": ROOT / "welcome" / "welcome_email.html",
        "alt": "Reuzel welcome banner with barber-built brand attitude",
        "prompt": (
            "Create a premium horizontal ecommerce email hero banner for Reuzel. "
            "Use the real Reuzel visual world: black, charcoal, cream, white, and restrained red accents. "
            "Keep a strong left-side text-safe area. On the right, show a barber-built founder-led or barbershop-led brand moment "
            "that feels campaign-ready, sharp, and credible instead of like a raw website photo. "
            "The image should communicate welcome, authority, and attitude in one glance. "
            "No fake packaging, no generic stock-grooming look, no purple tones, no clutter."
        ),
    },
    "promo": {
        "output": ROOT / "promo" / "assets" / "promo-hero-banner.png",
        "html": ROOT / "promo" / "promo_email.html",
        "alt": "Reuzel promo banner for building a lineup or bundle",
        "prompt": (
            "Create a premium horizontal ecommerce promo banner for Reuzel focused on building a lineup or bundle. "
            "Use real Reuzel products and preserve recognizable packaging. "
            "Show routine-building logic clearly: multiple products that belong together, arranged with strong visual hierarchy. "
            "Reserve the left side for headline space and put the products on the right. "
            "Make it feel bold, commercial, barber-built, and higher quality than a simple category crop."
        ),
    },
    "launch": {
        "output": ROOT / "launch" / "assets" / "launch-hero-banner.png",
        "html": ROOT / "launch" / "launch_email.html",
        "alt": "Reuzel launch banner featuring newly spotlighted pomade packaging",
        "prompt": (
            "Create a premium horizontal ecommerce launch banner for Reuzel featuring the real 3.38 oz pomade tins. "
            "Preserve real packaging identity and label readability. "
            "The image should communicate same trusted formula, new sharper presentation, and launch momentum. "
            "Reserve a strong left-side text-safe area and group the hero products on the right with polished studio lighting. "
            "No fake redesign, no generic beauty-campaign styling."
        ),
    },
    "bestseller": {
        "output": ROOT / "bestseller" / "assets" / "bestseller-hero-banner.png",
        "html": ROOT / "bestseller" / "bestseller_email.html",
        "alt": "Reuzel bestseller banner featuring proven favorites",
        "prompt": (
            "Create a premium horizontal ecommerce bestseller banner for Reuzel. "
            "Show a curated group of real Reuzel hero products with strong product hierarchy and clear text-safe space on the left. "
            "The image should communicate proven favorites, hard-working staples, and trusted starting points. "
            "Keep the mood barber-built, confident, and commercial. "
            "No clutter, no fake packaging, no weak category-tile feel."
        ),
    },
    "bundle": {
        "output": ROOT / "bundle" / "assets" / "bundle-hero-banner.png",
        "html": ROOT / "bundle" / "bundle_email.html",
        "alt": "Reuzel bundle banner showing a routine built from real products",
        "prompt": (
            "Create a premium horizontal ecommerce bundle banner for Reuzel. "
            "Use real Reuzel products arranged as a cohesive grooming routine rather than isolated items. "
            "Make the routine-building logic obvious at a glance and leave strong text-safe space on the left. "
            "The image should feel campaign-ready, practical, and product-led, with real packaging preserved."
        ),
    },
    "editorial": {
        "output": ROOT / "editorial" / "assets" / "editorial-hero-banner.png",
        "html": ROOT / "editorial" / "editorial_email.html",
        "alt": "Reuzel editorial banner showing multiple pomade options and barber-built guidance",
        "prompt": (
            "Create a premium horizontal editorial email hero banner for Reuzel about how to choose and use pomade without guessing. "
            "Show real Reuzel pomade tins with clearly recognizable labels and authentic pack shapes, using multiple finish and hold options. "
            "Reserve the left 40 percent as clean text-safe negative space. "
            "Group the real products on the right with one subtle grooming cue, such as a comb, hand, or hair texture. "
            "The image should instantly communicate that Reuzel has multiple pomade options and there is a smart way to choose. "
            "Use a dark charcoal barbershop-inspired backdrop, sharp commercial product photography, and restrained red accents. "
            "No fake packaging, no weak blog-photo look, no glossy fragrance-ad styling."
        ),
    },
    "winback": {
        "output": ROOT / "winback" / "assets" / "winback-hero-banner.png",
        "html": ROOT / "winback" / "winback_email.html",
        "alt": "Reuzel winback banner inviting customers back into their routine",
        "prompt": (
            "Create a premium horizontal ecommerce winback banner for Reuzel. "
            "Use real Reuzel products and make the image feel like a return-to-routine reminder rather than a generic category tile. "
            "Keep strong text-safe space on the left and a disciplined product grouping on the right. "
            "The mood should be confident, familiar, hard-working, and brand-faithful."
        ),
    },
}


def load_prompt(job_name: str, prompt_file: Optional[str], extra: Optional[str]) -> str:
    if prompt_file:
        prompt = Path(prompt_file).read_text(encoding="utf-8").strip()
    else:
        prompt = BANNER_JOBS[job_name]["prompt"]
    if extra:
        prompt = f"{prompt}\n\nAdditional constraints: {extra.strip()}"
    return prompt


def load_local_env_value(key: str) -> Optional[str]:
    if not LOCAL_ENV_FILE.exists():
        return None
    for raw_line in LOCAL_ENV_FILE.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        env_key, value = line.split("=", 1)
        if env_key.strip() != key:
            continue
        value = value.strip().strip("'").strip('"')
        return value or None
    return None


def call_gemini(api_key: str, model: str, prompt: str, image_size: str) -> Tuple[bytes, str]:
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"
    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {
            "imageConfig": {
                "aspectRatio": "16:9",
                "imageSize": image_size,
            }
        },
    }
    request = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "x-goog-api-key": api_key,
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=120) as response:
            data = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", "ignore")
        raise SystemExit(f"Gemini API error {exc.code}: {body}") from exc

    for candidate in data.get("candidates", []):
        content = candidate.get("content", {})
        for part in content.get("parts", []):
            inline = part.get("inlineData") or part.get("inline_data")
            if inline and inline.get("data"):
                mime = inline.get("mimeType") or inline.get("mime_type") or "image/png"
                return base64.b64decode(inline["data"]), mime
    raise SystemExit(f"No image returned by Gemini. Response keys: {list(data.keys())}")


def patch_html_image_src(html_path: Path, new_src: str, alt_text: str) -> None:
    html = html_path.read_text(encoding="utf-8")
    pattern = re.compile(r'(<img src=")([^"]+)(" width="640" alt=")([^"]+)(" style="display:block[^"]*border:0;">)')
    match = pattern.search(html)
    if not match:
        raise SystemExit(f"Could not locate hero image tag in {html_path}")
    html = pattern.sub(rf'\1{new_src}\3{alt_text}\5', html, count=1)
    html_path.write_text(html, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate Reuzel email hero banners with Gemini.")
    parser.add_argument("job", choices=sorted(BANNER_JOBS.keys()))
    parser.add_argument("--model", default="gemini-3.1-flash-image-preview")
    parser.add_argument("--image-size", default="2K", choices=["1K", "2K", "4K"])
    parser.add_argument("--prompt-file")
    parser.add_argument("--extra")
    parser.add_argument("--output")
    parser.add_argument("--patch-html", action="store_true")
    parser.add_argument("--html-src", help="Path or URL to write into the HTML img src. Defaults to the local output path.")
    args = parser.parse_args()

    api_key = os.environ.get("GEMINI_API_KEY") or load_local_env_value("GEMINI_API_KEY")
    if not api_key:
        raise SystemExit("Set GEMINI_API_KEY or create a local .env.gemini file next to the skill package.")

    job = BANNER_JOBS[args.job]
    output_path = Path(args.output) if args.output else job["output"]
    output_path.parent.mkdir(parents=True, exist_ok=True)

    prompt = load_prompt(args.job, args.prompt_file, args.extra)
    image_bytes, mime = call_gemini(api_key, args.model, prompt, args.image_size)

    suffix = ".png"
    if mime == "image/jpeg":
        suffix = ".jpg"
    if output_path.suffix.lower() not in {".png", ".jpg", ".jpeg", ".webp"}:
        output_path = output_path.with_suffix(suffix)

    output_path.write_bytes(image_bytes)
    print(f"Saved image to {output_path}")

    if args.patch_html:
        src_value = args.html_src or str(output_path)
        patch_html_image_src(job["html"], src_value, job["alt"])
        print(f"Patched HTML: {job['html']}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
