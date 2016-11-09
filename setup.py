from setuptools import setup

setup(
    name='jenkins-job-builder-stash-pr',
    version='0.0.1',
    description='Jenkins Job Builder Stash Pullrequest builder',
    url='https://github.com/bookwar/jenkins-job-builder-stash-pr',
    author='Aleksandra Fedorova',
    author_email='alpha@bookwar.info',
    license='MIT license',
    install_requires=[],
    entry_points={
        'jenkins_jobs.triggers': [
            'stash = jenkins_jobs_stash_pr.stash:stash_pr_trigger']},
    packages=['jenkins_jobs_stash_pr'],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3'])
