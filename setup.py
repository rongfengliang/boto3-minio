import setuptools
setuptools.setup(
    name="minioapp",
    version="0.0.1",
    author="dalongrong",
    author_email="1141591465@qq.com",
    description="minio app",
    install_requires=['boto3'],
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'minioapp=minioapp.app:main',
        ],
    }
)