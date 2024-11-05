from setuptools import setup, find_packages

setup(
    name="math_quiz",                      # Name of your package
    version="0.1",                         # Initial version
    packages=find_packages(),              # Automatically find packages in the directory
    install_requires=[                     # Dependencies (if any)
        # Add dependencies here, e.g., "numpy", "requests"
    ],
    entry_points={
        "console_scripts": [
            "math_quiz=math_quiz.math_quiz:math_quiz"  # Command-line executable (optional)
        ]
    },
    author="NITHISH",
    author_email="nithish17389@gmail.com",
    description="A simple math quiz game",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Nithish17389/Nitheaswarran-Saravanan-Komathi.git",  # Link to your repository
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
