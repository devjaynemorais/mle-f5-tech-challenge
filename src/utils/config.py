"""Carregamento de config/config.yaml."""

from pathlib import Path

import yaml

CONFIG_PATH = Path(__file__).resolve().parents[2] / "config" / "config.yaml"


def load_config(path: Path = CONFIG_PATH) -> dict:
    """Lê o YAML de configuração do projeto."""
    with path.open(encoding="utf-8") as fh:
        return yaml.safe_load(fh)
