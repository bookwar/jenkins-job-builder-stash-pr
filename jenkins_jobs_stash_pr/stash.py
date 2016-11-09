import xml.etree.ElementTree as XML
import jenkins_jobs.modules.base
from jenkins_jobs.errors import JenkinsJobsException
import logging


REQUIRED = [
    # (yaml tag, xml tag)
    ('stash_host', 'stashHost'),
    ('project_code', 'projectCode'),
    ('repository_name', 'repositoryName'),
]

OPTIONAL = [
    # ( yaml tag, xml tag, default value )
    ('spec', 'spec', ''),
    ('cron', 'cron', ''),
    ('credentials_id','credentialsId', ''),
    ('ci_skip_phrases', 'ciSkipPhrases', 'NO TEST'),
    ('ci_build_phrases', 'ciBuildPhrases', 'test this please'),
    ('target_branches_to_build', 'targetBranchesToBuild',''),
    ('ignore_ssl', 'ignoreSsl', 'true'),
    ('check_destination_commit','checkDestinationCommit','false'),
    ('check_mergeable', 'checkMergeable', 'false'),
    ('merge_on_success', 'mergeOnSuccess', 'false'),
    ('check_not_conflicted', 'checkNotConflicted', 'false'),
    ('only_build_on_comment', 'onlyBuildOnComment', 'false'),
    ('delete_previous_build_finish_comments', 'deletePreviousBuildFinishComments', 'false'),
    ('cancel_outdated_jobs_enabled', 'cancelOutdatedJobsEnabled', 'true'),
]

def stash_pr_trigger(parser, xml_parent, data):
    """ Setup trigger for Stash Pull Request plugin

    """

    logger = logging.getLogger("%s:stash_pr_trigger" % __name__)

    if data is None:
        data = dict()

    trigger = XML.SubElement(
        xml_parent,
        'stashpullrequestbuilder.stashpullrequestbuilder.StashBuildTrigger',
    )

    trigger.set('plugin', 'stash-pullrequest-builder@1.7.0')

    for (yaml_tag, xml_tag) in REQUIRED:
        XML.SubElement(trigger, xml_tag).text = data.get(yaml_tag)

    for (yaml_tag, xml_tag, default) in OPTIONAL:
        XML.SubElement(trigger, xml_tag).text = data.get(yaml_tag, default)
