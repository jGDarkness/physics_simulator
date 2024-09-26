import subprocess
import json
import os
import sys

def test_install_requirements():
    # Get the path to the main project directory
    project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    
    # Path to requirements.txt
    requirements_path = os.path.join(project_dir, 'requirements.txt')
    
    # Run pip install command
    process = subprocess.Popen(
        ['pip', 'install', '-r', requirements_path],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True,
        bufsize=1
    )
    
    # Capture output
    stdout_output = []
    stderr_output = []

    # Print and capture stdout
    for line in process.stdout:
        print(line, end='')
        sys.stdout.flush()
        stdout_output.append(line)

    # Print and capture stderr
    for line in process.stderr:
        print(line, end='', file=sys.stderr)
        sys.stderr.flush()
        stderr_output.append(line)

    # Wait for the process to complete
    process.wait()

    # Prepare results
    results = {
        'stdout': ''.join(stdout_output),
        'stderr': ''.join(stderr_output),
        'returncode': process.returncode
    }
    
    # Write results to JSON file
    output_path = os.path.join(project_dir, 'tests\\feature_implementation_1.0\\test_result_requirements_txt.json')
    with open(output_path, 'w') as f:
        json.dump(results, f, indent=2)
    
    # Assert that the installation was successful
    assert process.returncode == 0, f"Installation failed with return code {process.returncode}"

if __name__ == '__main__':
    test_install_requirements()