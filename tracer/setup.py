from setuptools import setup, find_packages

setup(
    name='ai-tracer',
    version='0.1.0',
    author='Barun Halder',
    author_email='barunhalder@example.com',
    description='A tracing library designed for Large Language Model (LLM) applications.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/bhalder/ai-tracer',
    packages=find_packages(),
    install_requires=[
        'fastapi==0.75.0',
        'pydantic==1.9.0',
        'uvicorn==0.17.6',
        'duckdb==0.3.2',
        # Include any other dependencies your library needs here
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    keywords='tracing llm ai analytics',
    python_requires='>=3.7',
    extras_require={
        'dev': [
            'pytest>=6.0',
            # Include any other development dependencies here
        ],
    },
)
