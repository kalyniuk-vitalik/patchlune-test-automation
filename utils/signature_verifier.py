import json
import subprocess
from pathlib import Path

def get_signature(path):
    path = str(Path(path).resolve())
    ps = [
        "powershell", "-NoProfile", "-NonInteractive", "-Command",
        f"Get-AuthenticodeSignature -FilePath '{path}' | ConvertTo-Json -Depth 5"
    ]
    proc = subprocess.run(ps, capture_output=True, text=True)
    if proc.returncode != 0:
        raise RuntimeError(f"PowerShell error: {proc.stderr.strip()}")

    data = json.loads(proc.stdout)

    status = data.get("Status")
    description = data.get("StatusMessage")
    signer = (data.get("SignerCertificate") or {}).get("Subject")

    return {
        "status": status,
        "status_message": description,
        "signer_subject": signer,
    }

