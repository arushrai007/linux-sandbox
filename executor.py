import subprocess
import uuid

def run_code(user_code, language):
    container_name = f"sandbox_{uuid.uuid4()}"

    try:
        if language == "python":
            cmd = [
                "python3", "-c", user_code
            ]

        elif language == "cpp":
            cmd = [
                "bash", "-c",
                "cat > main.cpp && g++ main.cpp -o main && ./main"
            ]

        elif language == "java":
            cmd = [
                "bash", "-c",
                "cat > Main.java && javac Main.java && java Main"
            ]

        else:
            return "Unsupported language"

        result = subprocess.run(
            [
                "docker", "run",
                "-i",
                "--rm",
                "--name", container_name,
                "--memory=200m",
                "--cpus=1",
                "--network=none",
                "sandbox-image"
            ] + cmd,
            input=user_code.encode(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=5
        )

        return result.stdout.decode() + result.stderr.decode()

    except subprocess.TimeoutExpired:
        return "Execution timed out!"
