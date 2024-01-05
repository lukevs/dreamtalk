from setuptools import setup, find_packages

dependencies = [
    'torch==2.1.2',
    'torchvision==0.16.2',
    'torchaudio==2.1.2',
    'urllib3==1.26.6',
    'transformers==4.28.1',
    'dlib==19.24.2',
    'yacs==0.1.8',
    'scipy==1.7.3',
    'scikit-image==0.19.3',
    'scikit-learn==1.0.2',
    'PyYAML==6.0',
    'Pillow==9.1.0',
    'numpy==1.21.5',
    'opencv-python',
    'imageio==2.18.0',
    'ffmpeg-python==0.2.0',
    'av==10.0.0',
]

setup(
    name='dreamtalk',
    version='0.1.0',
    description='DreamTalk: When Expressive Talking Head Generation Meets Diffusion Probabilistic Models',
    author='Ma, Yifeng and Zhang, Shiwei and Wang, Jiayu and Wang, Xiang and Zhang, Yingya and Deng, Zhidong',
    packages=find_packages(),
    install_requires=dependencies
)
