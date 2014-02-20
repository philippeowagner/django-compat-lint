#!/usr/bin/env python

from optparse import OptionParser
import os

from djangocompatlint import get_rules, initialize


usage = 'usage: %prog OPTIONS file1 file2 ...'

MESSAGE_TEMPLATE = '%s:%s:%s:%s'


def format_messages(messages, line, filename, level):
    return [MESSAGE_TEMPLATE % (level, filename, line, message) for \
            message in messages]


def check_file(filename, enabled_rules, options):
    messages = []
    lines = open(os.path.abspath(filename)).readlines()
    for i, line in enumerate(lines):
        for rule in enabled_rules:
            warnings, errors, info = rule(line, filename, options)
            if options.level in ('warnings', 'all'):
                messages += format_messages(warnings, i + 1, filename, 'WARNING')
            if options.level in ('errors', 'all'):
                messages += format_messages(errors, i + 1, filename, 'ERROR')
            if options.level in ('info', 'all'):
                messages += format_messages(info, i + 1, filename, 'INFO')
    return messages


if __name__ == '__main__':
    initialize()

    parser = OptionParser(usage)
    parser.add_option('-l', '--level', dest='level',
                      action='store',
                      type='string',
                      default='errors',
                      help="Level of messages to display. 'errors', 'warnings', 'info' or 'all'. Default 'errors'.")

    parser.add_option('--verbose', dest='verbose',
                      action='store_true',
                      help="Verbosity level")

    for rule in get_rules():
        parser.add_option(rule['long_option'],
                          dest=rule['dest'], action=rule['action'],
                          help=rule['help'])

    options, args = parser.parse_args()

    enabled_rules = []
    for rule in get_rules():
        if rule['enabled'](options):
            enabled_rules.append(rule['callback'])

    files = []
    if not args:
        args = [os.getcwd()]

    for path in args:
        if os.path.isdir(os.path.abspath(path)):
            subdir = os.path.abspath(path)
            files += [os.path.join(subdir, f) for f in os.listdir(subdir) if \
                      (os.path.isfile(os.path.join(subdir, f)) and '.pyc' not in f)]
        else:
            files.append(path)

    messages = []
    for filename in files:
        if options.verbose:
            print '>>> Chcking {0}'.format(filename)
        try:
            messages += check_file(filename, enabled_rules, options)
        except IOError as exc:
            if options.verbose:
                print '>>> Skipping {0}: {1}'.format(filename, exc)

    for message in messages:
        print message

    print 'Checked {0} files.'.format(len(files))
