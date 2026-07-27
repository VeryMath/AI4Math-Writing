#!/usr/bin/env python3
"""Generate PNG preview cards for math-beamer starter templates."""

from __future__ import annotations

import argparse
import shutil
import subprocess
import tempfile
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
PACKS = ROOT / "templates" / "packs"
PREVIEWS = ROOT / "templates" / "previews"
CATALOG = ROOT / "templates" / "catalog.yaml"
GALLERY = ROOT / "templates" / "preview-gallery.md"


def run(command: list[str], cwd: Path) -> None:
    proc = subprocess.run(
        command,
        cwd=cwd,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        timeout=120,
    )
    if proc.returncode:
        tail = proc.stdout[-3000:]
        raise RuntimeError(f"{cwd.name} failed: {' '.join(command)}\n{tail}")


def compile_pack(pack: Path, build_root: Path) -> Path:
    meta = yaml.safe_load((pack / "template.yaml").read_text(encoding="utf-8"))
    engine = meta.get("engine", "pdflatex")
    out_dir = build_root / pack.name
    out_dir.mkdir(parents=True, exist_ok=True)
    command = [
        "latexmk",
        "-xelatex" if engine == "xelatex" else "-pdf",
        "-interaction=nonstopmode",
        "-halt-on-error",
        f"-outdir={out_dir}",
        "main.tex",
    ]
    run(command, pack)
    pdf = out_dir / "main.pdf"
    if not pdf.exists():
        raise RuntimeError(f"missing PDF for {pack.name}: {pdf}")
    return pdf


def render_page(pdf: Path, page_number: int, out_path: Path) -> None:
    prefix = out_path.with_suffix("")
    command = [
        "pdftoppm",
        "-png",
        "-singlefile",
        "-f",
        str(page_number),
        "-l",
        str(page_number),
        "-scale-to-x",
        "960",
        "-scale-to-y",
        "-1",
        str(pdf),
        str(prefix),
    ]
    proc = subprocess.run(command, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=60)
    generated = prefix.with_suffix(".png")
    if proc.returncode or not generated.exists():
        if page_number == 1:
            raise RuntimeError(f"pdftoppm failed for {pdf}\n{proc.stdout[-1000:]}")
        render_page(pdf, 1, out_path)
        return
    if generated != out_path:
        generated.replace(out_path)


def preview_images(pdf: Path, name: str) -> None:
    PREVIEWS.mkdir(parents=True, exist_ok=True)
    render_page(pdf, 1, PREVIEWS / f"{name}-cover.png")
    render_page(pdf, 2, PREVIEWS / f"{name}-content.png")


def update_catalog_preview_paths() -> None:
    catalog = yaml.safe_load(CATALOG.read_text(encoding="utf-8"))
    for template in catalog["templates"]:
        name = template["name"]
        template["preview"] = f"templates/previews/{name}-cover.png"
        template["content_preview"] = f"templates/previews/{name}-content.png"
    CATALOG.write_text(yaml.safe_dump(catalog, sort_keys=False, allow_unicode=True), encoding="utf-8")


def write_gallery() -> None:
    catalog = yaml.safe_load(CATALOG.read_text(encoding="utf-8"))
    lines = [
        "# Math Beamer Template Preview Gallery",
        "",
        "Use this gallery to choose a starter template before drafting a deck.",
        "Each row shows the title slide and the first content slide.",
        "",
        "| Template | Cover | Content | Best for |",
        "| --- | --- | --- | --- |",
    ]
    for template in catalog["templates"]:
        name = template["name"]
        best_for = ", ".join(str(item) for item in template.get("best_for", []))
        preview = template.get("preview", f"templates/previews/{name}.png")
        content_preview = template.get("content_preview", f"templates/previews/{name}-content.png")
        relative_preview = preview.removeprefix("templates/")
        relative_content = content_preview.removeprefix("templates/")
        lines.append(
            f"| `{name}` | ![{name} cover]({relative_preview}) | "
            f"![{name} content]({relative_content}) | {best_for} |"
        )
    lines.append("")
    lines.append("Regenerate with `python3 scripts/generate_template_previews.py` from the `math-beamer` package root.")
    GALLERY.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()

    for executable in ("latexmk", "pdftoppm"):
        if not shutil.which(executable):
            raise SystemExit(f"{executable} is required")

    with tempfile.TemporaryDirectory(prefix="math-beamer-previews-") as temp_name:
        build_root = Path(temp_name)
        for pack in sorted(path for path in PACKS.iterdir() if path.is_dir()):
            pdf = compile_pack(pack, build_root)
            preview_images(pdf, pack.name)

    update_catalog_preview_paths()
    write_gallery()
    print(f"Generated previews for {len(list(PACKS.iterdir()))} templates in {PREVIEWS.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
