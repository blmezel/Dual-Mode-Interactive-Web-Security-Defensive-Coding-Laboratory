import os

def verify_sandbox_escape(user_input_path, base_sandbox_dir):
    # Yönerge Adım 5: Sandbox Escape ve Path Traversal Engelleme Mantığı
    resolved_path = os.path.realpath(user_input_path)
    if os.path.commonpath([base_sandbox_dir, resolved_path]) == os.path.realpath(base_sandbox_dir):
        return True # Güvenli erişim, sandbox içinde kalıyor
    raise PermissionError("HTTP 403: Sandbox Kaçış Girişimi Engellendi!")
