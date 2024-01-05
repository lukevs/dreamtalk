from setuptools import setup, find_packages

dependencies = [
    'torch==2.1.2',
    'torchvision==0.16.2',
    'torchaudio==2.1.2',
    'urllib3==1.26.6',
    'transformers==4.28.1',
    'dlib==19.24.2',
]

setup(
    name='dreamtalk',
    version='0.1.0',
    description='DreamTalk: When Expressive Talking Head Generation Meets Diffusion Probabilistic Models',
    author='Ma, Yifeng and Zhang, Shiwei and Wang, Jiayu and Wang, Xiang and Zhang, Yingya and Deng, Zhidong',
    packages=find_packages(),
    install_requires=dependencies
)
