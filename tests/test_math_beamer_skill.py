from __future__ import annotations

import re
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "skills" / "math-beamer"
EXPECTED_TEMPLATES = {
    "algebra-number-theory-talk",
    "analysis-core-talk",
    "algorithm-talk",
    "backup-heavy-talk",
    "beamerposter-a0",
    "combinatorics-graph-talk",
    "control-systems-talk",
    "course-lecture-zh",
    "data-experiment-results",
    "dynamical-systems-talk",
    "geometry-topology-talk",
    "information-coding-crypto-talk",
    "logic-foundations-category-talk",
    "numerical-analysis-talk",
    "optimization-talk",
    "pde-analysis-talk",
    "probability-statistics-talk",
    "reading-group-paper",
    "seminar-minimal-en",
    "seminar-minimal-zh",
    "theorem-proof-talk",
    "thesis-defense",
    "workshop-tutorial",
}


class MathBeamerSkillTests(unittest.TestCase):
    def test_skill_entrypoint_names_domain_coverage(self) -> None:
        text = (PACKAGE / "SKILL.md").read_text(encoding="utf-8")
        for required in (
            "name: math-beamer",
            "pure mathematics",
            "optimization",
            "statistics",
            "geometry",
            "topology",
            "number theory",
            "combinatorics",
            "category theory",
            "control theory",
            "cryptography",
            "PDEs",
            "slide-source-ledger.md",
            "latexmk",
        ):
            with self.subTest(required=required):
                self.assertIn(required, text)

    def test_catalog_and_template_packs_match(self) -> None:
        catalog = (PACKAGE / "templates/catalog.yaml").read_text(encoding="utf-8")
        catalog_names = set(re.findall(r"^\s*- name: ([a-z0-9-]+)$", catalog, flags=re.MULTILINE))
        self.assertEqual(EXPECTED_TEMPLATES, catalog_names)

        packs_root = PACKAGE / "templates" / "packs"
        pack_names = {path.name for path in packs_root.iterdir() if path.is_dir()}
        self.assertEqual(EXPECTED_TEMPLATES, pack_names)
        for name in sorted(EXPECTED_TEMPLATES):
            with self.subTest(template=name):
                self.assertTrue((packs_root / name / "template.yaml").is_file())
                main = packs_root / name / "main.tex"
                self.assertTrue(main.is_file())
                self.assertGreater(main.stat().st_size, 400)

    def test_every_template_has_compiled_previews(self) -> None:
        catalog = (PACKAGE / "templates/catalog.yaml").read_text(encoding="utf-8")
        gallery = (PACKAGE / "templates/preview-gallery.md").read_text(encoding="utf-8")
        for name in sorted(EXPECTED_TEMPLATES):
            for suffix in ("cover", "content"):
                with self.subTest(template=name, preview=suffix):
                    relative = f"templates/previews/{name}-{suffix}.png"
                    path = PACKAGE / relative
                    self.assertTrue(path.is_file())
                    self.assertGreater(path.stat().st_size, 1000)
                    self.assertIn(relative, catalog)
                    self.assertIn(f"previews/{name}-{suffix}.png", gallery)

    def test_public_release_metadata(self) -> None:
        provenance = (PACKAGE / "PROVENANCE.yaml").read_text(encoding="utf-8")
        self.assertIn("Conan Xu", provenance)
        self.assertIn(
            "86507c9a966f6df28dc481b7ddc9879017a64078939e1d38c1f94f04508e765a",
            provenance,
        )
        self.assertIn("license: MIT", provenance)
        self.assertIn("MIT License", (PACKAGE / "LICENSE").read_text(encoding="utf-8"))
        self.assertIn("PyYAML", (PACKAGE / "requirements-preview.txt").read_text(encoding="utf-8"))

    def test_third_party_templates_are_indexed_not_vendored(self) -> None:
        text = (PACKAGE / "references/template-source-index.md").read_text(encoding="utf-8")
        self.assertIn("Pan Jianyu", text)
        self.assertIn("license", text)
        self.assertIn("ECNU logo rights", text)

    def test_preview_generator_exposes_help_without_rendering(self) -> None:
        result = subprocess.run(
            [sys.executable, str(PACKAGE / "scripts/generate_template_previews.py"), "--help"],
            capture_output=True,
            text=True,
            timeout=15,
        )
        self.assertEqual(0, result.returncode, result.stderr)
        self.assertIn("usage:", result.stdout)


if __name__ == "__main__":
    unittest.main()
