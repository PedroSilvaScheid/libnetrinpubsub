import setuptools


def readme():
    with open('README.md') as f:
        return f.read()


setuptools.setup(
    name='netrin_pubsub_redis_lib',
    version='0.0.1',
    description='Lib contendo o modelo de comunicação com redis através de pubsub',
    long_description=readme(),
    url='https://gitlab.meta.com.br/netrin/netrin-pubsub-redis-lib',
    author='Jean Leal Matheus Seidler e Pedro Scheid',
    author_email='jc.santos.leal@gmail.com',
    license='MIT',
    classifiers=['Development Status :: 1 - Beta'],
    keywords='redis, pubsub',
    setup_requires=['wheel'],
    packages=setuptools.find_packages(),
    install_requires=[
        'redis',
        'redis_om'
    ],
    include_package_data=True,
    zip_safe=False
)
