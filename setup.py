from setuptools import find_packages,setup

setup(
    name='mcqgenerator',
    version='0.0.1',
    author='Ashwini Dahiphale',
    author_email='dahiphaleashwini0710@gmail.com',
    install_requires=['huggingface','langchain','streamlit','python-dotenv','PyPDF2'],
    packages=find_packages()
)