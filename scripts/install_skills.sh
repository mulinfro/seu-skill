#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
SRC_DIR="${REPO_ROOT}/skills"
DEST_ROOT="${HOME}/.codex/skills"
DEST_DIR="${DEST_ROOT}/seu-dev-flow"
TS="$(date +%Y%m%d_%H%M%S)"

if [[ ! -d "${SRC_DIR}" ]]; then
  echo "ERROR: skills directory not found: ${SRC_DIR}" >&2
  exit 1
fi

mkdir -p "${DEST_ROOT}"

if [[ -d "${DEST_DIR}" ]]; then
  BACKUP_DIR="${DEST_DIR}.bak_${TS}"
  echo "Existing install found. Backing up to: ${BACKUP_DIR}"
  mv "${DEST_DIR}" "${BACKUP_DIR}"
fi

mkdir -p "${DEST_DIR}"
cp -R "${SRC_DIR}/." "${DEST_DIR}/"

echo "Installed skills to: ${DEST_DIR}"
echo "Included files:"
find "${DEST_DIR}" -maxdepth 3 -type f | sort
echo
echo "Usage hint:"
echo "1) cd ${REPO_ROOT}"
echo "2) Start Codex CLI and ask it to read AGENTS.md + skills/README.md"
