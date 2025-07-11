
from setuptools import setup, find_packages

setup(
    name="highrise-bot-egyptian",
    version="3.0.0",
    description="بوت Highrise المصري المتطور مع ذكاء اصطناعي",
    author="فريق EDX",
    packages=find_packages(),
    install_requires=[
        "highrise-bot-sdk==24.1.0",
        "aiohttp>=3.8.0",
        "google-generativeai>=0.8.5",
        "openai>=1.0.0",
        "flask>=3.0.0",
        "python-dotenv>=1.0.0",
        "revchatgpt>=6.8.6",
        "pychatgpt>=0.4.3.3",
        "requests>=2.28.0",
    ],
    python_requires=">=3.10",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.10",
    ],
)
