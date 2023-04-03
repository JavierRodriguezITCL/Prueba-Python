from setuptools import setup

setup(
    name='Socket',
    version='1.0',
    description='Prueba con sockets para intercambio de datos cliente-servidor',
    author='Enrique Estebanez',
    author_email='quiquecomaneaj@gmail.com',
    url='https://github.com/JavierRodriguezITCL/Prueba-Python/blob/Enrique_Branch/Ficheros_Examen/Examen_ITCL_Antolin.ipynb',
    packages=['Socket'],
    install_requires=[
        'numpy',
        'pandas',
        'scikit-learn',
        'tensorflow',
        'joblib'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)