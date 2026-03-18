import winreg
import subprocess

def is_cmd_disabled():
    try:
        # Open the registry key
        key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"Software\Policies\Microsoft\Windows\System",
            0,
            winreg.KEY_READ
        )
        value, _ = winreg.QueryValueEx(key, "DisableCMD")
        winreg.CloseKey(key)

        if value == 1:
            return True, "Command Prompt completely disabled."
        elif value == 2:
            return True, "Interactive Command Prompt disabled, scripts may still run."
        else:
            return False, "Command Prompt enabled."
    except FileNotFoundError:
        # Key doesn't exist → CMD not disabled
        return False, "Command Prompt enabled."
    except PermissionError:
        return None, "Permission denied when checking registry."
    except Exception as e:
        return None, f"Error checking CMD status: {e}"

def test_cmd_execution():
    try:
        subprocess.run(["cmd", "/c", "echo CMD test"], check=True, capture_output=True)
        return True, "CMD execution works."
    except subprocess.CalledProcessError:
        return False, "CMD execution failed."
    except FileNotFoundError:
        return False, "cmd.exe not found."
    except Exception as e:
        return False, f"Error executing CMD: {e}"

if __name__ == "__main__":
    disabled, message = is_cmd_disabled()
    print(f"[Registry Check] {message}")

    works, exec_message = test_cmd_execution()
    print(f"[Execution Test] {exec_message}")