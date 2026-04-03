---
id: github.com-midudev-tailwind-animations-ed6ff24e-kn
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:27:58.886144
---

# KNOWLEDGE EXTRACT: github.com_midudev_tailwind-animations_ed6ff24e
> **Extracted on:** 2026-04-01 15:32:37
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007524582/github.com_midudev_tailwind-animations_ed6ff24e

---

## File: `HEAD`
```
ref: refs/heads/main
```

## File: `config`
```
[core]
	repositoryformatversion = 0
	filemode = false
	bare = false
	logallrefupdates = true
	symlinks = false
	ignorecase = true
[remote "origin"]
	url = https://github.com/midudev/tailwind-animations
	fetch = +refs/heads/main:refs/remotes/origin/main
[branch "main"]
	remote = origin
	merge = refs/heads/main
```

## File: `description`
```
Unnamed repository; edit this file 'description' to name the repository.
```

## File: `packed-refs`
```
# pack-refs with: peeled fully-peeled sorted 
ceed187044dc02f2cde392b0be503b5972d42c95 refs/remotes/origin/main
```

## File: `shallow`
```
ceed187044dc02f2cde392b0be503b5972d42c95
```

## File: `hooks/applypatch-msg.sample`
```
#!/bin/sh
#
# An example hook script to check the commit log message taken by
# applypatch from an e-mail message.
#
# The hook should exit with non-zero status after issuing an
# appropriate message if it wants to stop the commit.  The hook is
# allowed to edit the commit message file.
#
# To enable this hook, rename this file to "applypatch-msg".

. git-sh-setup
commitmsg="$(git rev-parse --git-path hooks/commit-msg)"
test -x "$commitmsg" && exec "$commitmsg" ${1+"$@"}
:
```

## File: `hooks/commit-msg.sample`
```
#!/bin/sh
#
# An example hook script to check the commit log message.
# Called by "git commit" with one argument, the name of the file
# that has the commit message.  The hook should exit with non-zero
# status after issuing an appropriate message if it wants to stop the
# commit.  The hook is allowed to edit the commit message file.
#
# To enable this hook, rename this file to "commit-msg".

# Uncomment the below to add a Signed-off-by line to the message.
# Doing this in a hook is a bad idea in general, but the prepare-commit-msg
# hook is more suited to it.
#
# SOB=$(git var GIT_AUTHOR_IDENT | sed -n 's/^\(.*>\).*$/Signed-off-by: \1/p')
# grep -qs "^$SOB" "$1" || echo "$SOB" >> "$1"

# This example catches duplicate Signed-off-by lines.

test "" = "$(grep '^Signed-off-by: ' "$1" |
	 sort | uniq -c | sed -e '/^[ 	]*1[ 	]/d')" || {
	echo >&2 Duplicate Signed-off-by lines.
	exit 1
}
```

## File: `hooks/fsmonitor-watchman.sample`
```
#!/usr/bin/perl

use strict;
use warnings;
use IPC::Open2;

# An example hook script to integrate Watchman
# (https://facebook.github.io/watchman/) with git to speed up detecting
# new and modified files.
#
# The hook is passed a version (currently 2) and last update token
# formatted as a string and outputs to stdout a new update token and
# all files that have been modified since the update token. Paths must
# be relative to the root of the working tree and separated by a single NUL.
#
# To enable this hook, rename this file to "query-watchman" and set
# 'git config core.fsmonitor .git/hooks/query-watchman'
#
my ($version, $last_update_token) = @ARGV;

# Uncomment for debugging
# print STDERR "$0 $version $last_update_token\n";

# Check the hook interface version
if ($version ne 2) {
	die "Unsupported query-fsmonitor hook version '$version'.\n" .
	    "Falling back to scanning...\n";
}

my $git_work_tree = get_working_dir();

my $retry = 1;

my $json_pkg;
eval {
	require JSON::XS;
	$json_pkg = "JSON::XS";
	1;
} or do {
	require JSON::PP;
	$json_pkg = "JSON::PP";
};

launch_watchman();

sub launch_watchman {
	my $o = watchman_query();
	if (is_work_tree_watched($o)) {
		output_result($o->{clock}, @{$o->{files}});
	}
}

sub output_result {
	my ($clockid, @files) = @_;

	# Uncomment for debugging watchman output
	# open (my $fh, ">", ".git/watchman-output.out");
	# binmode $fh, ":utf8";
	# print $fh "$clockid\n@files\n";
	# close $fh;

	binmode STDOUT, ":utf8";
	print $clockid;
	print "\0";
	local $, = "\0";
	print @files;
}

sub watchman_clock {
	my $response = qx/watchman clock "$git_work_tree"/;
	die "Failed to get clock id on '$git_work_tree'.\n" .
		"Falling back to scanning...\n" if $? != 0;

	return $json_pkg->new->utf8->decode($response);
}

sub watchman_query {
	my $pid = open2(\*CHLD_OUT, \*CHLD_IN, 'watchman -j --no-pretty')
	or die "open2() failed: $!\n" .
	"Falling back to scanning...\n";

	# In the query expression below we're asking for names of files that
	# changed since $last_update_token but not from the .git folder.
	#
	# To accomplish this, we're using the "since" generator to use the
	# recency index to select candidate nodes and "fields" to limit the
	# output to file names only. Then we're using the "expression" term to
	# further constrain the results.
	my $last_update_line = "";
	if (substr($last_update_token, 0, 1) eq "c") {
		$last_update_token = "\"$last_update_token\"";
		$last_update_line = qq[\n"since": $last_update_token,];
	}
	my $query = <<"	END";
		["query", "$git_work_tree", {$last_update_line
			"fields": ["name"],
			"expression": ["not", ["dirname", ".git"]]
		}]
	END

	# Uncomment for debugging the watchman query
	# open (my $fh, ">", ".git/watchman-query.json");
	# print $fh $query;
	# close $fh;

	print CHLD_IN $query;
	close CHLD_IN;
	my $response = do {local $/; <CHLD_OUT>};

	# Uncomment for debugging the watch response
	# open ($fh, ">", ".git/watchman-response.json");
	# print $fh $response;
	# close $fh;

	die "Watchman: command returned no output.\n" .
	"Falling back to scanning...\n" if $response eq "";
	die "Watchman: command returned invalid output: $response\n" .
	"Falling back to scanning...\n" unless $response =~ /^\{/;

	return $json_pkg->new->utf8->decode($response);
}

sub is_work_tree_watched {
	my ($output) = @_;
	my $error = $output->{error};
	if ($retry > 0 and $error and $error =~ m/unable to resolve root .* directory (.*) is not watched/) {
		$retry--;
		my $response = qx/watchman watch "$git_work_tree"/;
		die "Failed to make watchman watch '$git_work_tree'.\n" .
		    "Falling back to scanning...\n" if $? != 0;
		$output = $json_pkg->new->utf8->decode($response);
		$error = $output->{error};
		die "Watchman: $error.\n" .
		"Falling back to scanning...\n" if $error;

		# Uncomment for debugging watchman output
		# open (my $fh, ">", ".git/watchman-output.out");
		# close $fh;

		# Watchman will always return all files on the first query so
		# return the fast "everything is dirty" flag to git and do the
		# Watchman query just to get it over with now so we won't pay
		# the cost in git to look up each individual file.
		my $o = watchman_clock();
		$error = $output->{error};

		die "Watchman: $error.\n" .
		"Falling back to scanning...\n" if $error;

		output_result($o->{clock}, ("/"));
		$last_update_token = $o->{clock};

		eval { launch_watchman() };
		return 0;
	}

	die "Watchman: $error.\n" .
	"Falling back to scanning...\n" if $error;

	return 1;
}

sub get_working_dir {
	my $working_dir;
	if ($^O =~ 'msys' || $^O =~ 'cygwin') {
		$working_dir = Win32::GetCwd();
		$working_dir =~ tr/\\/\//;
	} else {
		require Cwd;
		$working_dir = Cwd::cwd();
	}

	return $working_dir;
}
```

## File: `hooks/post-update.sample`
```
#!/bin/sh
#
# An example hook script to prepare a packed repository for use over
# dumb transports.
#
# To enable this hook, rename this file to "post-update".

exec git update-server-info
```

## File: `hooks/pre-applypatch.sample`
```
#!/bin/sh
#
# An example hook script to verify what is about to be committed
# by applypatch from an e-mail message.
#
# The hook should exit with non-zero status after issuing an
# appropriate message if it wants to stop the commit.
#
# To enable this hook, rename this file to "pre-applypatch".

. git-sh-setup
precommit="$(git rev-parse --git-path hooks/pre-commit)"
test -x "$precommit" && exec "$precommit" ${1+"$@"}
:
```

## File: `hooks/pre-commit.sample`
```
#!/bin/sh
#
# An example hook script to verify what is about to be committed.
# Called by "git commit" with no arguments.  The hook should
# exit with non-zero status after issuing an appropriate message if
# it wants to stop the commit.
#
# To enable this hook, rename this file to "pre-commit".

if git rev-parse --verify HEAD >/dev/null 2>&1
then
	against=HEAD
else
	# Initial commit: diff against an empty tree object
	against=$(git hash-object -t tree /dev/null)
fi

# If you want to allow non-ASCII filenames set this variable to true.
allownonascii=$(git config --type=bool hooks.allownonascii)

# Redirect output to stderr.
exec 1>&2

# Cross platform projects tend to avoid non-ASCII filenames; prevent
# them from being added to the repository. We exploit the fact that the
# printable range starts at the space character and ends with tilde.
if [ "$allownonascii" != "true" ] &&
	# Note that the use of brackets around a tr range is ok here, (it's
	# even required, for portability to Solaris 10's /usr/bin/tr), since
	# the square bracket bytes happen to fall in the designated range.
	test $(git diff-index --cached --name-only --diff-filter=A -z $against |
	  LC_ALL=C tr -d '[ -~]\0' | wc -c) != 0
then
	cat <<\EOF
Error: Attempt to add a non-ASCII file name.

This can cause problems if you want to work with people on other platforms.

To be portable it is advisable to rename the file.

If you know what you are doing you can disable this check using:

  git config hooks.allownonascii true
EOF
	exit 1
fi

# If there are whitespace errors, print the offending file names and fail.
exec git diff-index --check --cached $against --
```

## File: `hooks/pre-merge-commit.sample`
```
#!/bin/sh
#
# An example hook script to verify what is about to be committed.
# Called by "git merge" with no arguments.  The hook should
# exit with non-zero status after issuing an appropriate message to
# stderr if it wants to stop the merge commit.
#
# To enable this hook, rename this file to "pre-merge-commit".

. git-sh-setup
test -x "$GIT_DIR/hooks/pre-commit" &&
        exec "$GIT_DIR/hooks/pre-commit"
:
```

## File: `hooks/pre-push.sample`
```
#!/bin/sh

# An example hook script to verify what is about to be pushed.  Called by "git
# push" after it has checked the remote status, but before anything has been
# pushed.  If this script exits with a non-zero status nothing will be pushed.
#
# This hook is called with the following parameters:
#
# $1 -- Name of the remote to which the push is being done
# $2 -- URL to which the push is being done
#
# If pushing without using a named remote those arguments will be equal.
#
# Information about the commits which are being pushed is supplied as lines to
# the standard input in the form:
#
#   <local ref> <local oid> <remote ref> <remote oid>
#
# This sample shows how to prevent push of commits where the log message starts
# with "WIP" (work in progress).

remote="$1"
url="$2"

zero=$(git hash-object --stdin </dev/null | tr '[0-9a-f]' '0')

while read local_ref local_oid remote_ref remote_oid
do
	if test "$local_oid" = "$zero"
	then
		# Handle delete
		:
	else
		if test "$remote_oid" = "$zero"
		then
			# New branch, examine all commits
			range="$local_oid"
		else
			# Update to existing branch, examine new commits
			range="$remote_oid..$local_oid"
		fi

		# Check for WIP commit
		commit=$(git rev-list -n 1 --grep '^WIP' "$range")
		if test -n "$commit"
		then
			echo >&2 "Found WIP commit in $local_ref, not pushing"
			exit 1
		fi
	fi
done

exit 0
```

## File: `hooks/pre-rebase.sample`
```
#!/bin/sh
#
# Copyright (c) 2006, 2008 Junio C Hamano
#
# The "pre-rebase" hook is run just before "git rebase" starts doing
# its job, and can prevent the command from running by exiting with
# non-zero status.
#
# The hook is called with the following parameters:
#
# $1 -- the upstream the series was forked from.
# $2 -- the branch being rebased (or empty when rebasing the current branch).
#
# This sample shows how to prevent topic branches that are already
# merged to 'next' branch from getting rebased, because allowing it
# would result in rebasing already published history.

publish=next
basebranch="$1"
if test "$#" = 2
then
	topic="refs/heads/$2"
else
	topic=`git symbolic-ref HEAD` ||
	exit 0 ;# we do not interrupt rebasing detached HEAD
fi

case "$topic" in
refs/heads/??/*)
	;;
*)
	exit 0 ;# we do not interrupt others.
	;;
esac

# Now we are dealing with a topic branch being rebased
# on top of master.  Is it OK to rebase it?

# Does the topic really exist?
git show-ref -q "$topic" || {
	echo >&2 "No such branch $topic"
	exit 1
}

# Is topic fully merged to master?
not_in_master=`git rev-list --pretty=oneline ^master "$topic"`
if test -z "$not_in_master"
then
	echo >&2 "$topic is fully merged to master; better remove it."
	exit 1 ;# we could allow it, but there is no point.
fi

# Is topic ever merged to next?  If so you should not be rebasing it.
only_next_1=`git rev-list ^master "^$topic" ${publish} | sort`
only_next_2=`git rev-list ^master           ${publish} | sort`
if test "$only_next_1" = "$only_next_2"
then
	not_in_topic=`git rev-list "^$topic" master`
	if test -z "$not_in_topic"
	then
		echo >&2 "$topic is already up to date with master"
		exit 1 ;# we could allow it, but there is no point.
	else
		exit 0
	fi
else
	not_in_next=`git rev-list --pretty=oneline ^${publish} "$topic"`
	/usr/bin/perl -e '
		my $topic = $ARGV[0];
		my $msg = "* $topic has commits already merged to public branch:\n";
		my (%not_in_next) = map {
			/^([0-9a-f]+) /;
			($1 => 1);
		} split(/\n/, $ARGV[1]);
		for my $elem (map {
				/^([0-9a-f]+) (.*)$/;
				[$1 => $2];
			} split(/\n/, $ARGV[2])) {
			if (!exists $not_in_next{$elem->[0]}) {
				if ($msg) {
					print STDERR $msg;
					undef $msg;
				}
				print STDERR " $elem->[1]\n";
			}
		}
	' "$topic" "$not_in_next" "$not_in_master"
	exit 1
fi

<<\DOC_END

This sample hook safeguards topic branches that have been
published from being rewound.

The workflow assumed here is:

 * Once a topic branch forks from "master", "master" is never
   merged into it again (either directly or indirectly).

 * Once a topic branch is fully cooked and merged into "master",
   it is deleted.  If you need to build on top of it to correct
   earlier mistakes, a new topic branch is created by forking at
   the tip of the "master".  This is not strictly necessary, but
   it makes it easier to keep your history simple.

 * Whenever you need to test or publish your changes to topic
   branches, merge them into "next" branch.

The script, being an example, hardcodes the publish branch name
to be "next", but it is trivial to make it configurable via
$GIT_DIR/config mechanism.

With this workflow, you would want to know:

(1) ... if a topic branch has ever been merged to "next".  Young
    topic branches can have stupid mistakes you would rather
    clean up before publishing, and things that have not been
    merged into other branches can be easily rebased without
    affecting other people.  But once it is published, you would
    not want to rewind it.

(2) ... if a topic branch has been fully merged to "master".
    Then you can delete it.  More importantly, you should not
    build on top of it -- other people may already want to
    change things related to the topic as patches against your
    "master", so if you need further changes, it is better to
    fork the topic (perhaps with the same name) afresh from the
    tip of "master".

Let's look at this example:

		   o---o---o---o---o---o---o---o---o---o "next"
		  /       /           /           /
		 /   a---a---b A     /           /
		/   /               /           /
	       /   /   c---c---c---c B         /
	      /   /   /             \         /
	     /   /   /   b---b C     \       /
	    /   /   /   /             \     /
    ---o---o---o---o---o---o---o---o---o---o---o "master"


A, B and C are topic branches.

 * A has one fix since it was merged up to "next".

 * B has finished.  It has been fully merged up to "master" and "next",
   and is ready to be deleted.

 * C has not merged to "next" at all.

We would want to allow C to be rebased, refuse A, and encourage
B to be deleted.

To compute (1):

	git rev-list ^master ^topic next
	git rev-list ^master        next

	if these match, topic has not merged in next at all.

To compute (2):

	git rev-list master..topic

	if this is empty, it is fully merged to "master".

DOC_END
```

## File: `hooks/pre-receive.sample`
```
#!/bin/sh
#
# An example hook script to make use of push options.
# The example simply echoes all push options that start with 'echoback='
# and rejects all pushes when the "reject" push option is used.
#
# To enable this hook, rename this file to "pre-receive".

if test -n "$GIT_PUSH_OPTION_COUNT"
then
	i=0
	while test "$i" -lt "$GIT_PUSH_OPTION_COUNT"
	do
		eval "value=\$GIT_PUSH_OPTION_$i"
		case "$value" in
		echoback=*)
			echo "echo from the pre-receive-hook: ${value#*=}" >&2
			;;
		reject)
			exit 1
		esac
		i=$((i + 1))
	done
fi
```

## File: `hooks/prepare-commit-msg.sample`
```
#!/bin/sh
#
# An example hook script to prepare the commit log message.
# Called by "git commit" with the name of the file that has the
# commit message, followed by the description of the commit
# message's source.  The hook's purpose is to edit the commit
# message file.  If the hook fails with a non-zero status,
# the commit is aborted.
#
# To enable this hook, rename this file to "prepare-commit-msg".

# This hook includes three examples. The first one removes the
# "# Please enter the commit message..." help message.
#
# The second includes the output of "git diff --name-status -r"
# into the message, just before the "git status" output.  It is
# commented because it doesn't cope with --amend or with squashed
# commits.
#
# The third example adds a Signed-off-by line to the message, that can
# still be edited.  This is rarely a good idea.

COMMIT_MSG_FILE=$1
COMMIT_SOURCE=$2
SHA1=$3

/usr/bin/perl -i.bak -ne 'print unless(m/^. Please enter the commit message/..m/^#$/)' "$COMMIT_MSG_FILE"

# case "$COMMIT_SOURCE,$SHA1" in
#  ,|template,)
#    /usr/bin/perl -i.bak -pe '
#       print "\n" . `git diff --cached --name-status -r`
# 	 if /^#/ && $first++ == 0' "$COMMIT_MSG_FILE" ;;
#  *) ;;
# esac

# SOB=$(git var GIT_COMMITTER_IDENT | sed -n 's/^\(.*>\).*$/Signed-off-by: \1/p')
# git interpret-trailers --in-place --trailer "$SOB" "$COMMIT_MSG_FILE"
# if test -z "$COMMIT_SOURCE"
# then
#   /usr/bin/perl -i.bak -pe 'print "\n" if !$first_line++' "$COMMIT_MSG_FILE"
# fi
```

## File: `hooks/push-to-checkout.sample`
```
#!/bin/sh

# An example hook script to update a checked-out tree on a git push.
#
# This hook is invoked by git-receive-pack(1) when it reacts to git
# push and updates reference(s) in its repository, and when the push
# tries to update the branch that is currently checked out and the
# receive.denyCurrentBranch configuration variable is set to
# updateInstead.
#
# By default, such a push is refused if the working tree and the index
# of the remote repository has any difference from the currently
# checked out commit; when both the working tree and the index match
# the current commit, they are updated to match the newly pushed tip
# of the branch. This hook is to be used to override the default
# behaviour; however the code below reimplements the default behaviour
# as a starting point for convenient modification.
#
# The hook receives the commit with which the tip of the current
# branch is going to be updated:
commit=$1

# It can exit with a non-zero status to refuse the push (when it does
# so, it must not modify the index or the working tree).
die () {
	echo >&2 "$*"
	exit 1
}

# Or it can make any necessary changes to the working tree and to the
# index to bring them to the desired state when the tip of the current
# branch is updated to the new commit, and exit with a zero status.
#
# For example, the hook can simply run git read-tree -u -m HEAD "$1"
# in order to emulate git fetch that is run in the reverse direction
# with git push, as the two-tree form of git read-tree -u -m is
# essentially the same as git switch or git checkout that switches
# branches while keeping the local changes in the working tree that do
# not interfere with the difference between the branches.

# The below is a more-or-less exact translation to shell of the C code
# for the default behaviour for git's push-to-checkout hook defined in
# the push_to_deploy() function in builtin/receive-pack.c.
#
# Note that the hook will be executed from the repository directory,
# not from the working tree, so if you want to perform operations on
# the working tree, you will have to adapt your code accordingly, e.g.
# by adding "cd .." or using relative paths.

if ! git update-index -q --ignore-submodules --refresh
then
	die "Up-to-date check failed"
fi

if ! git diff-files --quiet --ignore-submodules --
then
	die "Working directory has unstaged changes"
fi

# This is a rough translation of:
#
#   head_has_history() ? "HEAD" : EMPTY_TREE_SHA1_HEX
if git cat-file -e HEAD 2>/dev/null
then
	head=HEAD
else
	head=$(git hash-object -t tree --stdin </dev/null)
fi

if ! git diff-index --quiet --cached --ignore-submodules $head --
then
	die "Working directory has staged changes"
fi

if ! git read-tree -u -m "$commit"
then
	die "Could not update working tree to new HEAD"
fi
```

## File: `hooks/sendemail-validate.sample`
```
#!/bin/sh

# An example hook script to validate a patch (and/or patch series) before
# sending it via email.
#
# The hook should exit with non-zero status after issuing an appropriate
# message if it wants to prevent the email(s) from being sent.
#
# To enable this hook, rename this file to "sendemail-validate".
#
# By default, it will only check that the patch(es) can be applied on top of
# the default upstream branch without conflicts in a secondary worktree. After
# validation (successful or not) of the last patch of a series, the worktree
# will be deleted.
#
# The following config variables can be set to change the default remote and
# remote ref that are used to apply the patches against:
#
#   sendemail.validateRemote (default: origin)
#   sendemail.validateRemoteRef (default: HEAD)
#
# Replace the TODO placeholders with appropriate checks according to your
# needs.

validate_cover_letter () {
	file="$1"
	# TODO: Replace with appropriate checks (e.g. spell checking).
	true
}

validate_patch () {
	file="$1"
	# Ensure that the patch applies without conflicts.
	git am -3 "$file" || return
	# TODO: Replace with appropriate checks for this patch
	# (e.g. checkpatch.pl).
	true
}

validate_series () {
	# TODO: Replace with appropriate checks for the whole series
	# (e.g. quick build, coding style checks, etc.).
	true
}

# main -------------------------------------------------------------------------

if test "$GIT_SENDEMAIL_FILE_COUNTER" = 1
then
	remote=$(git config --default origin --get sendemail.validateRemote) &&
	ref=$(git config --default HEAD --get sendemail.validateRemoteRef) &&
	worktree=$(mktemp --tmpdir -d sendemail-validate.XXXXXXX) &&
	git worktree add -fd --checkout "$worktree" "refs/remotes/$remote/$ref" &&
	git config --replace-all sendemail.validateWorktree "$worktree"
else
	worktree=$(git config --get sendemail.validateWorktree)
fi || {
	echo "sendemail-validate: error: failed to prepare worktree" >&2
	exit 1
}

unset GIT_DIR GIT_WORK_TREE
cd "$worktree" &&

if grep -q "^diff --git " "$1"
then
	validate_patch "$1"
else
	validate_cover_letter "$1"
fi &&

if test "$GIT_SENDEMAIL_FILE_COUNTER" = "$GIT_SENDEMAIL_FILE_TOTAL"
then
	git config --unset-all sendemail.validateWorktree &&
	trap 'git worktree remove -ff "$worktree"' EXIT &&
	validate_series
fi
```

## File: `hooks/update.sample`
```
#!/bin/sh
#
# An example hook script to block unannotated tags from entering.
# Called by "git receive-pack" with arguments: refname sha1-old sha1-new
#
# To enable this hook, rename this file to "update".
#
# Config
# ------
# hooks.allowunannotated
#   This boolean sets whether unannotated tags will be allowed into the
#   repository.  By default they won't be.
# hooks.allowdeletetag
#   This boolean sets whether deleting tags will be allowed in the
#   repository.  By default they won't be.
# hooks.allowmodifytag
#   This boolean sets whether a tag may be modified after creation. By default
#   it won't be.
# hooks.allowdeletebranch
#   This boolean sets whether deleting branches will be allowed in the
#   repository.  By default they won't be.
# hooks.denycreatebranch
#   This boolean sets whether remotely creating branches will be denied
#   in the repository.  By default this is allowed.
#

# --- Command line
refname="$1"
oldrev="$2"
newrev="$3"

# --- Safety check
if [ -z "$GIT_DIR" ]; then
	echo "Don't run this script from the command line." >&2
	echo " (if you want, you could supply GIT_DIR then run" >&2
	echo "  $0 <ref> <oldrev> <newrev>)" >&2
	exit 1
fi

if [ -z "$refname" -o -z "$oldrev" -o -z "$newrev" ]; then
	echo "usage: $0 <ref> <oldrev> <newrev>" >&2
	exit 1
fi

# --- Config
allowunannotated=$(git config --type=bool hooks.allowunannotated)
allowdeletebranch=$(git config --type=bool hooks.allowdeletebranch)
denycreatebranch=$(git config --type=bool hooks.denycreatebranch)
allowdeletetag=$(git config --type=bool hooks.allowdeletetag)
allowmodifytag=$(git config --type=bool hooks.allowmodifytag)

# check for no description
projectdesc=$(sed -e '1q' "$GIT_DIR/description")
case "$projectdesc" in
"Unnamed repository"* | "")
	echo "*** Project description file hasn't been set" >&2
	exit 1
	;;
esac

# --- Check types
# if $newrev is 0000...0000, it's a commit to delete a ref.
zero=$(git hash-object --stdin </dev/null | tr '[0-9a-f]' '0')
if [ "$newrev" = "$zero" ]; then
	newrev_type=delete
else
	newrev_type=$(git cat-file -t $newrev)
fi

case "$refname","$newrev_type" in
	refs/tags/*,commit)
		# un-annotated tag
		short_refname=${refname##refs/tags/}
		if [ "$allowunannotated" != "true" ]; then
			echo "*** The un-annotated tag, $short_refname, is not allowed in this repository" >&2
			echo "*** Use 'git tag [ -a | -s ]' for tags you want to propagate." >&2
			exit 1
		fi
		;;
	refs/tags/*,delete)
		# delete tag
		if [ "$allowdeletetag" != "true" ]; then
			echo "*** Deleting a tag is not allowed in this repository" >&2
			exit 1
		fi
		;;
	refs/tags/*,tag)
		# annotated tag
		if [ "$allowmodifytag" != "true" ] && git rev-parse $refname > /dev/null 2>&1
		then
			echo "*** Tag '$refname' already exists." >&2
			echo "*** Modifying a tag is not allowed in this repository." >&2
			exit 1
		fi
		;;
	refs/heads/*,commit)
		# branch
		if [ "$oldrev" = "$zero" -a "$denycreatebranch" = "true" ]; then
			echo "*** Creating a branch is not allowed in this repository" >&2
			exit 1
		fi
		;;
	refs/heads/*,delete)
		# delete branch
		if [ "$allowdeletebranch" != "true" ]; then
			echo "*** Deleting a branch is not allowed in this repository" >&2
			exit 1
		fi
		;;
	refs/remotes/*,commit)
		# tracking branch
		;;
	refs/remotes/*,delete)
		# delete tracking branch
		if [ "$allowdeletebranch" != "true" ]; then
			echo "*** Deleting a tracking branch is not allowed in this repository" >&2
			exit 1
		fi
		;;
	*)
		# Anything else (is there anything else?)
		echo "*** Update hook: unknown type of update to ref $refname of type $newrev_type" >&2
		exit 1
		;;
esac

# --- Finished
exit 0
```

## File: `info/exclude`
```
# git ls-files --others --exclude-from=.git/info/exclude
# Lines that start with '#' are comments.
# For a project mostly in C, the following would be a good set of
# exclude patterns (uncomment them if you want to use them):
# *.[oa]
# *~
```

## File: `logs/HEAD`
```
0000000000000000000000000000000000000000 ceed187044dc02f2cde392b0be503b5972d42c95 MaiKhue <R9000P 2021@MaiKhue.(none)> 1775032356 +0700	clone: from https://github.com/midudev/tailwind-animations
```

## File: `logs/refs/heads/main`
```
0000000000000000000000000000000000000000 ceed187044dc02f2cde392b0be503b5972d42c95 MaiKhue <R9000P 2021@MaiKhue.(none)> 1775032356 +0700	clone: from https://github.com/midudev/tailwind-animations
```

## File: `logs/refs/remotes/origin/HEAD`
```
0000000000000000000000000000000000000000 ceed187044dc02f2cde392b0be503b5972d42c95 MaiKhue <R9000P 2021@MaiKhue.(none)> 1775032356 +0700	clone: from https://github.com/midudev/tailwind-animations
```

## File: `midudev-tailwind-animations-ceed187/.gitignore`
```
**/node_modules
pnpm-lock.yaml
bun.lockb
package-lock.json
.DS_Store
```

## File: `midudev-tailwind-animations-ceed187/.npmignore`
```
.github/*
test/*
web/*
web/README.md
lib/imgs/web.jpg
pnpm-workspace.yaml
README.es.md
README.md
```

## File: `midudev-tailwind-animations-ceed187/CHANGELOG.md`
```markdown
# Changelog

Todos los cambios notables en este proyecto serán documentados en este archivo.

## [1.0.0] - 2026-01-12

### Añadido
- Soporte nativo para **Tailwind CSS v4**.

### Cambiado
- **Renombre del Paquete**: El paquete ha sido renombrado de `@midudev/tailwind-animations` a `tailwind-animations`.
- **Implementación CSS-only**: El plugin ahora es puramente CSS, eliminando la dependencia de lógica en JavaScript para registrar las animaciones.
- **Estructura del Proyecto**: Los datos de las animaciones para la documentación se han movido a la carpeta de la web (`web/src/data/theme.js`) para mantener el plugin lo más limpio posible.
- **Exportaciones del Paquete**: Se ha actualizado el `package.json` para exportar directamente el archivo CSS.
- **Documentación**: README actualizado con las nuevas instrucciones de uso exclusivas para la v4.

### Eliminado
- **Soporte para Tailwind CSS v3**: Se ha eliminado la compatibilidad con versiones anteriores de Tailwind para simplificar la arquitectura del plugin.
- **Plugin de JavaScript**: Se ha eliminado el archivo `src/theme.js` y la lógica de plugin basada en JS (`src/index.js`), ya que ahora se utiliza la directiva `@plugin` directamente sobre el archivo CSS.

---

## [0.2.0] - Versión anterior estable
- Versión compatible con Tailwind CSS v3 basada en plugins de JavaScript.
```

## File: `midudev-tailwind-animations-ceed187/DEPLOY.md`
```markdown
# Guía de ejecución y despliegue del proyecto

## Información importante

Este proyecto utiliza **pnpm** como gestor de paquetes y está basado en **Astro**. Se recomienda seguir los pasos en el orden indicado para evitar errores.

Antes de ejecutar el proyecto, asegúrate de contar con:

- Node.js (versión recomendada: 18 o superior)
- pnpm instalado globalmente

---

## Pasos previos (Ramas) (*Recomendación)

Antes de correr el proyecto si necesitas hacer cambios grandes en la estructura del proyecto, es recomendable, crear una nueva rama y hacer los cambios en dicha rama git:

``` bash
git checkout -b [nombre-rama]
```

Si se daña algo de la web, se puede eliminar la rama y la rama principal estará en buen estado:

``` bash
git branch -d [nombre-rama]
````

> Si no conoces bien los comandos git, información extra del funcionamiento/comandos de git investigar.

---

## Pasos para ejecutar el proyecto en desarrollo

1. Instalar dependencias:

``` bash
pnpm install
```

2. Ejecutar el proyecto (paquete `web`):

``` bash
pnpm --filter web dev
```

3. Agregar Tailwind CSS (solo si no está instalado):

``` bash
npx astro add tailwind
```

---

## Notas adicionales

- Si Tailwind ya está configurado, **no es necesario ejecutar el paso 3**.

- El servidor de desarrollo mostrará la URL local en la terminal.

- Ante errores, verifica que las dependencias estén correctamente instaladas.

- Si llegas a crear algún tipo de documentación, Markdownlint para una buena sintaxis de documentación (.md) y ltex para corrección de faltas ortográficas.
```

## File: `midudev-tailwind-animations-ceed187/LICENSE`
```
MIT License

Copyright (c) 2024 Miguel Ángel Durán

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## File: `midudev-tailwind-animations-ceed187/LLM.txt`
```
# Tailwind Animations - LLM Context File

## Project Overview

**tailwind-animations** is a Tailwind CSS v4 plugin that provides a comprehensive and exhaustive set of ready-to-use CSS animations through utility classes. Created and maintained by Miguel Ángel Durán (@midudev) in collaboration with his active community.

**Repository**: [GitHub - midudev/tailwind-animations](https://github.com/midudev/tailwind-animations)
**License**: MIT
**Current Version**: 1.0.1
**Website**: https://tailwind-animations.com/

***

## Installation and Configuration

### Package Installation

```bash
# NPM
npm install tailwind-animations

# PNPM (recommended for monorepos)
pnpm install tailwind-animations

# Yarn
yarn add tailwind-animations
```

### Setup in Tailwind CSS v4

The plugin is configured directly in your global CSS file:

```css
/* globals.css or main.css */
@import "tailwindcss";
@import 'tailwind-animations';
```

### Requirements

- **Tailwind CSS**: v4.0.0 or higher
- For Tailwind CSS v3 support: use `@midudev/tailwind-animations@0.2.0` (deprecated legacy version)

***

## Main Features

### 1. **70+ Predefined Animations**
Exhaustive set of ready-to-use animations without needing custom CSS code.

### 2. **Granular Control through Utility Classes**
Modify duration, delays, iterations, and behavior of any animation:
- `animate-delay-*` (0ms to 1000ms)
- `animate-duration-*` (faster, fast, normal, slow, slower + numeric values)
- `animate-iteration-count-*` (once, twice, thrice, infinite)
- `animate-direction-*` (normal, reverse, alternate, alternate-reverse)
- `animate-fill-mode-*` (forwards, backwards, both)
- `animate-play-*` (running, paused)

### 3. **Advanced Easing Functions**
- **Standard Timing Functions**: ease, ease-in, ease-out, ease-in-out, linear
- **Predefined Cubic Bezier Curves**: 
  - Sine, Quad, Cubic, Quart, Quint, Expo (with -in, -out, -in-out variants)
  - Circ, Back (with variants)

### 4. **View Timeline Support**
Animations synchronized with element position in the viewport:

```html
<div class="animate-zoom-in view-animate-[--entrance] animate-range-[entry_10%_contain_25%]">
  Animates when entering the viewport
</div>
```

### 5. **Scroll Timeline Support**

Animations linked to user scrolling:

```html
<div class="timeline-scroll animate-rotate-360">
  Rotates while you scroll
</div>
```

### 6. **Steps and Retro Animations**
Support for pixel/retro-style animations with defined steps:
- retro (8 steps), normal (16 steps), modern (24 steps)

***

## Complete Animation Catalog

### 🎨 Fade Animations
| Animation | Description |
|-----------|-------------|
| `fade-in` | Smooth appearance |
| `fade-out` | Smooth fade out |
| `blurred-fade-in` | Progressive blurred entry |
| `fade-in-up`, `fade-in-down` | Entry with vertical movement |
| `fade-in-left`, `fade-in-right` | Entry with horizontal movement |
| `fade-out-*` | Exit variants |
| `pulse-fade-in` | Entry with pulse effect |

### 🎯 Slide Animations
| Animation | Description |
|-----------|-------------|
| `slide-in-top`, `slide-in-bottom` | Entry from/to top/bottom |
| `slide-in-left`, `slide-in-right` | Entry from/to sides |
| `slide-out-*` | Exit variants |
| `slide-up-fade` | Upward slide with fade |
| `slide-rotate-in`, `slide-rotate-out` | Slide with simultaneous rotation |

### 🔍 Zoom & Scale Animations
| Animation | Description |
|-----------|-------------|
| `zoom-in` | Zoom in with appearance |
| `zoom-out` | Zoom out with fade |
| `scale` | Simple scaling |
| `pop` | Soft "explosion" effect |
| `expand-horizontally`, `contract-horizontally` | Horizontal expand/contract |
| `expand-vertically`, `contract-vertically` | Vertical expand/contract |

### 🔄 Rotation Animations
| Animation | Description |
|-----------|-------------|
| `rotate-90`, `rotate-180`, `rotate-360` | Defined rotations |
| `spin-clockwise`, `spin-counter-clockwise` | Continuous rotation |
| `rotate-in`, `rotate-out` | Entry/exit with rotation |
| `impulse-rotation-right`, `impulse-rotation-left` | Impulse rotation with direction |
| `rotational-wave` | Continuous rotational wave |

### 🔀 Flip Animations
| Animation | Description |
|-----------|-------------|
| `flip-horizontal`, `flip-vertical` | 3D flip (Y/X axis) |
| `flip-x`, `flip-y` | Mirror on X/Y axes |
| `flip-in-x`, `flip-in-y` | Entry with 3D flip |
| `flip-out-x`, `flip-out-y` | Exit with 3D flip |

### 💫 Movement & Motion Animations
| Animation | Description |
|-----------|-------------|
| `bouncing` | Simple vertical bounce |
| `bounce-fade-in` | Bounce with appearance |
| `vertical-bounce`, `horizontal-bounce` | Directional bounces |
| `swing` | Pendulum movement |
| `sway` | Soft swaying |
| `wobble` | Irregular oscillation |
| `jiggle` | Quick shaking |
| `tilt` | 3D tilt |
| `squeeze` | Compression and expansion |
| `jump` | Vertical jump |
| `hang` | Hanging effect |
| `roll-in`, `roll-out` | Rolling with rotation |
| `float` | Soft floating |
| `sink` | Soft sinking |
| `shake` | Tremor |
| `blink` | Blinking |

### ⭐ Interactive & Fun Animations
| Animation | Description |
|-----------|-------------|
| `tada` | Celebration effect WOW.js style |
| `heartbeat` | Heartbeat |
| `pulse`, `pulsing` | Opacity/scale pulsing |
| `rubber-band` | Rubber band effect |
| `flash` | Quick flash |
| `horizontal-vibration` | Horizontal vibration |
| `dancing` | Dance movement |
| `jelly` | Jelly effect |

### 🎪 Composite & Advanced Animations
| Animation | Description |
|-----------|-------------|
| `swing-drop-in` | Entry with swing and drop |
| `skew`, `skew-right` | Skew/tilt |

***

## CSS Configuration Variables

### Delays

```
0ms | 100ms | 150ms | 200ms | 250ms | 300ms | 400ms | 500ms | 700ms | 800ms | 900ms | 1000ms
```

### Durations
**Semantic names**:
- `faster`: 100ms
- `fast`: 200ms
- `normal`: 300ms
- `slow`: 400ms
- `slower`: 500ms

**Numeric values**: 0ms to 1000ms

### Iteration Counts
- `once`: 1 time
- `twice`: 2 times
- `thrice`: 3 times
- `infinite`: Infinite

### Fill Modes
- `forwards`: Maintains final state
- `backwards`: Uses initial state before starting
- `both`: Combines forwards and backwards

### Animation Steps (For retro effect)
- `retro`: 8 steps
- `normal`: 16 steps
- `modern`: 24 steps

### Animation Ranges (Scroll/View Timeline)
- `cover`: Full range
- `contain`: Within viewport
- `entry`: Entry to viewport
- `exit`: Exit from viewport
- `gradual`, `moderate`, `brisk`, `rapid`: Predefined ranges with percentages

***

## Complete Technology Stack

| Tool | Version | Purpose |
|------|---------|---------|
| **Tailwind CSS** | 4.1.18 | Main CSS framework |
| **PostCSS** | 8.5.6 | CSS processor |
| **Astro** | 4.3.3 | Website build tool |
| **Vitest** | 4.0.16 | Testing framework |
| **ESLint** | 9.39.2 | JS code linting |
| **Neostandard** | 0.12.2 | ESLint configuration |
| **Prettier** | 3.7.4 | Code formatter |
| **TypeScript Parser** | 8.52.0 | TypeScript support |

***

## Project Structure

```
tailwind-animations/
├── CHANGELOG.md                     # Version history and changes
├── LICENSE                          # MIT License file
├── LLM.txt                          # LLM context file (this file)
├── README.es.md                     # Spanish documentation
├── README.md                        # English documentation
├── eslint.config.js                 # ESLint configuration
├── lib/
│   └── imgs/
│       └── web.jpg                  # Project visual assets
├── package.json                     # Main package configuration
├── packages/
│   └── scoped/                      # @midudev/tailwind-animations (deprecated)
│       ├── README.md
│       ├── package.json
│       └── src/
│           └── index.css            # Synced CSS for scoped package
├── pnpm-workspace.yaml              # Monorepo workspace config
├── scripts/
│   ├── deprecate-scoped.mjs         # Script to deprecate scoped package
│   ├── publish-both.mjs             # Publish automation for both packages
│   └── sync-scoped-package.mjs      # Sync code between packages
├── src/
│   └── index.css                    # Main file with all animations
├── test/
│   ├── index.test.js                # Test suite with Vitest
│   └── utils.js                     # Test utilities
└── web/                             # Demo website (Astro)
    ├── README.md
    ├── astro.config.mjs             # Astro configuration
    ├── package.json
    ├── public/
    │   ├── favicon.svg
    │   ├── fonts/
    │   │   ├── Figtree.ttf
    │   │   └── GeistMono.ttf
    │   └── og.jpg                   # Open Graph image
    ├── src/
    │   ├── components/
    │   │   ├── Footer.astro
    │   │   ├── Logo.astro
    │   │   ├── ToggleTheme.astro
    │   │   └── icons/
    │   │       ├── copy.astro
    │   │       ├── github.astro
    │   │       ├── moon.astro
    │   │       ├── sun.astro
    │   │       └── system.astro
    │   ├── data/
    │   │   └── theme.js             # Theme configuration
    │   ├── env.d.ts                 # TypeScript environment types
    │   ├── layouts/
    │   │   └── Layout.astro         # Main layout component
    │   ├── pages/
    │   │   └── index.astro          # Homepage
    │   └── styles/
    │       └── index.css            # Website styles
    └── tsconfig.json                # TypeScript configuration

Directories: 18 | Files: 39
```

***

## Available Scripts and Commands

| Command | Function |
|---------|----------|
| `npm run lint` | Check code with ESLint |
| `npm run lint:fix` | Auto-fix ESLint issues |
| `npm run test` | Run tests with Vitest |
| `npm run test:ci` | Tests in CI mode (single run) |
| `npm run publish:official` | Publish official package to NPM |
| `npm run publish:scoped` | Publish scoped @midudev/ package (deprecated) |
| `npm run publish:both` | Publish both versions |
| `npm run sync:scoped` | Sync code between packages |
| `npm run deprecate:scoped` | Mark scoped package as deprecated |

***

## Dependencies and Compatibility

### Peer Dependencies
- `tailwindcss`: ^4.0.0 (required)

### Main Dev Dependencies
- @tailwindcss/postcss: 4.1.18
- @csstools/postcss-minify: 2.0.5
- postcss: 8.5.6
- tailwindcss: 4.1.18
- vitest: 4.0.16
- eslint: 9.39.2

### Installed Tools
- prettier and prettier-plugin-tailwindcss
- eslint-plugin-astro (for web/ linting)
- TypeScript ESLint Parser

***

## Usage Examples

### Basic Usage

```html
<!-- Simple fade in -->
<div class="animate-fade-in">
  Content that appears smoothly
</div>

<!-- Slide with customization -->
<div class="animate-slide-in-bottom animate-delay-300 animate-duration-slow">
  Slides from bottom after 300ms (duration: 400ms)
</div>
```

### Advanced Combinations

```html
<!-- Zoom entry that pauses on hover -->
<div class="animate-zoom-in hover:animate-play-paused animate-duration-fast">
  Fast zoom that pauses on hover
</div>

<!-- Animation linked to scroll -->
<div class="animate-rotate-360 timeline-scroll animate-duration-slower">
  Rotates while you scroll (very slowly)
</div>

<!-- View Timeline: animates when entering viewport -->
<div class="w-72 h-52 bg-gradient-to-r from-blue-500 to-purple-500
            animate-pop view-animate-[--entrance] 
            animate-range-[entry_10%_contain_25%]">
  Pop when entering viewport
</div>
```

### Advanced Easing Usage

```html
<!-- With custom cubic easing curve -->
<div class="animate-fade-in-up animate-bezier-cubic-out animate-duration-normal">
  Smooth entry with cubic easing
</div>

<!-- Step by step (retro pixel style) -->
<div class="animate-rotate-360 animate-steps-retro animate-duration-slower animate-iteration-count-infinite">
  Pixel/retro style rotation
</div>
```

***

## Important Information

### ⚠️ Deprecation
- The **`@midudev/tailwind-animations`** package is **completely deprecated**
- Maintained only for backward compatibility
- **All new projects should use `tailwind-animations`**

### 📦 Older Versions
For projects using **Tailwind CSS v3**, use:

```bash
npm install @midudev/tailwind-animations@0.2.0
```

### 🏗️ Technical Features
- **CSS-only**: No JavaScript dependencies
- **Tree-shakeable**: Only used animations are included in your build
- **Performance optimized**: Uses CSS variables for maximum efficiency
- **Monorepo**: Uses pnpm workspaces to manage multiple packages

### 🤝 Community and Contributions
- Actively maintained project
- Accepts PRs and community suggestions
- Contributors graph: https://contrib.rocks/image?repo=midudev/tailwind-animations
- Last updates in June 2024

***

## Recent History

### Main Updates
- **Jun 2024**: Multiple UX/UI improvements and new animations
- **May 2024**: Feature pull requests integration
- **Mar 2024**: Version update and ESLint configuration
- **Feb 2024**: Accessibility improvements and dark mode

### Recent Development Areas
- ESLint standard migrations
- New animations (jelly, skew, etc.)
- Scroll-driven animations
- Dark mode improvements
- Demo website UX optimizations

***

## Quick Reference

### Animation Class Anatomy

```
animate-[name] animate-delay-[ms] animate-duration-[time]
animate-iteration-count-[repetitions] animate-direction-[direction]
animate-fill-mode-[mode] animate-bezier-[easing]
```

### Complete Example

```html
<button class="animate-tada 
               animate-delay-200 
               animate-duration-slow 
               animate-iteration-count-infinite 
               animate-direction-alternate
               hover:animate-play-paused">
  Click me!
</button>
```

***

## Resources

- **Official Website**: https://tailwind-animations.com/
- **GitHub Repository**: https://github.com/midudev/tailwind-animations
- **NPM Package**: https://www.npmjs.com/package/tailwind-animations
- **Documentation**: README.md (EN) and README.es.md (ES)
- **Issues & Discussions**: GitHub Issues and Discussions
```

## File: `midudev-tailwind-animations-ceed187/README.es.md`
```markdown
<div align="center">

# Awesome Tailwind Animations

[![en](https://img.shields.io/badge/lang-en-red.svg)](./README.md)
[![es](https://img.shields.io/badge/lang-es-yellow.svg)](./README.es.md)

![GitHub stars](https://img.shields.io/github/stars/midudev/tailwind-animations)
![GitHub Forks](https://img.shields.io/github/forks/midudev/tailwind-animations)
![GitHub PRs](https://img.shields.io/github/issues-pr/midudev/tailwind-animations)
![GitHub issues](https://img.shields.io/github/issues/midudev/tailwind-animations)
![GitHub Contributors](https://img.shields.io/github/contributors/midudev/tailwind-animations)

![web](./lib/imgs/web.jpg)

![Tailwind
CSS](https://img.shields.io/badge/Tailwind%20CSS-3.4.1-blue?style=for-the-badge&logo=tailwind-css)
![Astro](https://img.shields.io/badge/Astro-4.3.3-orange?style=for-the-badge&logo=astro)

Obten animaciones de CSS con una sola clase de Tailwind!

Visita la [web](https://tailwindcss-animations.vercel.app/) para obtener más
información.

</div>

## Instalación

> Nota: este proyecto antes se publicaba como `@midudev/tailwind-animations`. Ese paquete se mantiene solo como **compatibilidad** y está **deprecado**.

> ¿Necesitas soporte para **Tailwind CSS v3**? Usa la última versión compatible: `@midudev/tailwind-animations@0.2.0`.

Instala el paquete con tu gestor de paquetes favorito:

```sh
$ npm install tailwind-animations
$ pnpm add tailwind-animations
$ yarn add tailwind-animations
```

Usa el plugin en tu configuración de Tailwind:

```css
@import 'tailwindcss';
@import 'tailwind-animations';
```

## Uso

Este plugin trae varias clases de utilidad así como varias animaciones CSS listas para usar. Aquí tienes algunos ejemplos simples:

```html
<div class="animate-fade-in">
  Fade in box
</div>

<div class="animate-slide-in-bottom animate-delay-300 animate-duration-slow">
  Slow animation after 300ms to slide in from bottom
</div>
```

### Animates Timeline

Este plugin también trae una clase de utilidad para animar elementos basados en su posición en la ventana. Puedes usar la clase `view-animate-single` o `view-animate-[animation]` para poder generar cualquier nombre a tu timeline.

```html
<div class="w-3/4 max-w-[800px] m-[0_auto]">
<h1>Content</h1>

<p>
  Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
  tempor incididunt ut labore et dolore magna aliqua. Risus quis varius quam
  quisque id. Et ligula ullamcorper malesuada proin libero nunc consequat
  interdum varius. Elit ullamcorper dignissim cras tincidunt lobortis feugiat
  vivamus at augue.
</p>

<p>
  Dolor sed viverra ipsum nunc aliquet. Sed sed risus pretium quam vulputate
  dignissim. Tortor aliquam nulla facilisi cras. A erat nam at lectus urna
  duis convallis convallis. Nibh ipsum consequat nisl vel pretium lectus.
  Sagittis aliquam malesuada bibendum arcu vitae elementum. Malesuada bibendum
  arcu vitae elementum curabitur vitae nunc sed velit.
</p>

<div
  class="w-72 h-52 m-[0_auto] bg-[deeppink] view-animate-[--subjectReveal] animate-zoom-in animate-range-[entry_10%_contain_25%]">
</div>

<p>
  Adipiscing enim eu turpis egestas pretium aenean pharetra magna ac. Arcu
  cursus vitae congue mauris rhoncus aenean vel. Sit amet cursus sit amet
  dictum. Augue neque gravida in fermentum et. Gravida rutrum quisque non
  tellus orci ac auctor augue mauris. Risus quis varius quam quisque id diam
  vel quam elementum. Nibh praesent tristique magna sit amet purus gravida
  quis. Duis ultricies lacus sed turpis tincidunt id aliquet. In egestas erat
  imperdiet sed euismod nisi. Eget egestas purus viverra accumsan in nisl nisi
  scelerisque. Netus et malesuada fames ac.
</p>
</div>
```
> Ejemplo extraido de [MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/view-timeline)

## Contribuidores

<a href="https://github.com/midudev/tailwind-animations/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=midudev/tailwind-animations" />
</a>
```

## File: `midudev-tailwind-animations-ceed187/README.md`
```markdown
<div align="center">

# Awesome Tailwind Animations

[![en](https://img.shields.io/badge/lang-en-red.svg)](./README.md)
[![es](https://img.shields.io/badge/lang-es-yellow.svg)](./README.es.md)

![GitHub stars](https://img.shields.io/github/stars/midudev/tailwind-animations)
![GitHub Forks](https://img.shields.io/github/forks/midudev/tailwind-animations)
![GitHub PRs](https://img.shields.io/github/issues-pr/midudev/tailwind-animations)
![GitHub issues](https://img.shields.io/github/issues/midudev/tailwind-animations)
![GitHub Contributors](https://img.shields.io/github/contributors/midudev/tailwind-animations)

![CleanShot 2026-01-12 at 21 27 57@2x](https://github.com/user-attachments/assets/e2d42595-c049-4c21-a208-770d56291483)

![Tailwind
CSS](https://img.shields.io/badge/Tailwind%20CSS-3.4.1-blue?style=for-the-badge&logo=tailwind-css)
![Astro](https://img.shields.io/badge/Astro-4.3.3-orange?style=for-the-badge&logo=astro)

Get your animations easily done with only Tailwind CSS classes.

Visit the [website](https://tailwindcss-animations.vercel.app/) to get more information.
</div>
  
## Installation :book:

> Note: this project used to be published as `@midudev/tailwind-animations`. That package remains available only as a **deprecated compatibility shim**.

> Need **Tailwind CSS v3** support? Use the last v3-compatible release: `@midudev/tailwind-animations@0.2.0`.

#### Package install

> Install the package with your favorite package manager:

- npm
```bash
npm install tailwind-animations
```
- pnpm
```bash
pnpm install tailwind-animations
```
- yarn
```bash
yarn add tailwind-animations
```

#### Plugin Implementation
> Use the plugin in your Tailwind CSS project:

```css
/* globals.css (for Tailwind CSS 4.*) */
@import 'tailwindcss';
@import 'tailwind-animations';
```

## Usage :gear:

#### Example

> Here are some simple examples of how to use this plugin and its animations:

```html
<div class="animate-fade-in">
  Fade in box
</div>

<div class="animate-slide-in-bottom animate-delay-300 animate-duration-slow">
  Slow animation after 300ms to slide in from bottom
</div>
```

### Animates Timeline

This plugin also brings a utility class to animate elements based on their position in the window. You can use the class `view-animate-single` or `view-animate-[animation]` to generate any name for your timeline.

```html
<div class="w-3/4 max-w-[800px] m-[0_auto]">
<h1>Content</h1>

<p>
  Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
  tempor incididunt ut labore et dolore magna aliqua. Risus quis varius quam
  quisque id. Et ligula ullamcorper malesuada proin libero nunc consequat
  interdum varius. Elit ullamcorper dignissim cras tincidunt lobortis feugiat
  vivamus at augue.
</p>

<p>
  Dolor sed viverra ipsum nunc aliquet. Sed sed risus pretium quam vulputate
  dignissim. Tortor aliquam nulla facilisi cras. A erat nam at lectus urna
  duis convallis convallis. Nibh ipsum consequat nisl vel pretium lectus.
  Sagittis aliquam malesuada bibendum arcu vitae elementum. Malesuada bibendum
  arcu vitae elementum curabitur vitae nunc sed velit.
</p>

<div
  class="w-72 h-52 m-[0_auto] bg-[deeppink] view-animate-[--subjectReveal] animate-zoom-in animate-range-[entry_10%_contain_25%]">
</div>

<p>
  Adipiscing enim eu turpis egestas pretium aenean pharetra magna ac. Arcu
  cursus vitae congue mauris rhoncus aenean vel. Sit amet cursus sit amet
  dictum. Augue neque gravida in fermentum et. Gravida rutrum quisque non
  tellus orci ac auctor augue mauris. Risus quis varius quam quisque id diam
  vel quam elementum. Nibh praesent tristique magna sit amet purus gravida
  quis. Duis ultricies lacus sed turpis tincidunt id aliquet. In egestas erat
  imperdiet sed euismod nisi. Eget egestas purus viverra accumsan in nisl nisi
  scelerisque. Netus et malesuada fames ac.
</p>
</div>
```

> Example extracted from [MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/view-timeline)

## Contributors 👑
  
<a href="https://github.com/midudev/tailwind-animations/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=midudev/tailwind-animations" />
</a>
```

## File: `midudev-tailwind-animations-ceed187/eslint.config.js`
```javascript
import neostandard from 'neostandard'

export default [
  ...neostandard({}),
  {
    ignores: [
      'web/.astro/**',
      'web/.vscode/**',
      'web/dist/**',
      'web/node_modules/**',
    ],
  },
]
```

## File: `midudev-tailwind-animations-ceed187/package.json`
```json
{
  "name": "tailwind-animations",
  "version": "1.0.1",
  "description": "Tailwind CSS plugin to add animations to your website",
  "style": "./src/index.css",
  "exports": {
    ".": "./src/index.css",
    "./index.css": "./src/index.css"
  },
  "type": "module",
  "scripts": {
    "lint": "eslint .",
    "lint:fix": "eslint --fix .",
    "test": "vitest",
    "test:ci": "vitest run",
    "sync:scoped": "node ./scripts/sync-scoped-package.mjs",
    "publish:official": "pnpm publish --access public --no-git-checks",
    "publish:scoped": "pnpm --dir ./packages/scoped publish --access public --no-git-checks",
    "deprecate:scoped": "node ./scripts/deprecate-scoped.mjs",
    "publish:both": "node ./scripts/publish-both.mjs"
  },
  "keywords": ["tailwind", "css", "animations", "plugin"],
  "author": "Miguel Ángel Durán (@midudev) & su maravillosa comunidad",
  "license": "MIT",
  "peerDependencies": {
    "tailwindcss": "^4.0.0"
  },
  "devDependencies": {
    "@tailwindcss/postcss": "4.1.18",
    "@csstools/postcss-minify": "2.0.5",
    "eslint": "9.39.2",
    "neostandard": "0.12.2",
    "postcss": "8.5.6",
    "tailwindcss": "4.1.18",
    "vitest": "4.0.16",
    "@typescript-eslint/parser": "8.52.0",
    "eslint-config-prettier": "10.1.8",
    "eslint-plugin-astro": "1.5.0",
    "eslint-plugin-jsx-a11y": "6.10.2",
    "prettier": "3.7.4",
    "prettier-config-standard": "7.0.0",
    "prettier-plugin-astro": "0.14.1",
    "prettier-plugin-tailwindcss": "0.7.2"
  }
}
```

## File: `midudev-tailwind-animations-ceed187/pnpm-workspace.yaml`
```yaml
packages:
  - .
  - packages/**
  - web/**

onlyBuiltDependencies:
  - '@tailwindcss/oxide'
```

## File: `midudev-tailwind-animations-ceed187/packages/scoped/README.md`
```markdown
# @midudev/tailwind-animations (deprecated)

This package is **deprecated**.

Use the correct package instead:

```bash
npm install tailwind-animations
```

If you still depend on this package, it re-exports the CSS from `tailwind-animations`.
```

## File: `midudev-tailwind-animations-ceed187/packages/scoped/package.json`
```json
{
  "name": "@midudev/tailwind-animations",
  "version": "1.0.1",
  "description": "Deprecated: use tailwind-animations instead",
  "style": "./src/index.css",
  "exports": {
    ".": "./src/index.css",
    "./index.css": "./src/index.css"
  },
  "type": "module",
  "files": [
    "src"
  ],
  "keywords": [
    "tailwind",
    "css",
    "animations",
    "plugin"
  ],
  "author": "Miguel Ángel Durán (@midudev) & su maravillosa comunidad",
  "license": "MIT",
  "repository": {
    "type": "git",
    "url": "https://github.com/midudev/tailwind-animations.git"
  },
  "bugs": {
    "url": "https://github.com/midudev/tailwind-animations/issues"
  },
  "homepage": "https://github.com/midudev/tailwind-animations#readme",
  "dependencies": {
    "tailwind-animations": "1.0.1"
  },
  "peerDependencies": {
    "tailwindcss": "^4.0.0"
  }
}
```

## File: `midudev-tailwind-animations-ceed187/packages/scoped/src/index.css`
```css
/*
  Deprecated package shim.
  Use `tailwind-animations` instead.
*/

@import "tailwind-animations";
```

## File: `midudev-tailwind-animations-ceed187/scripts/deprecate-scoped.mjs`
```
import { execFileSync } from 'node:child_process'
import fs from 'node:fs'
import path from 'node:path'

const repoRoot = path.resolve(new URL('..', import.meta.url).pathname)
const rootPkg = JSON.parse(fs.readFileSync(path.join(repoRoot, 'package.json'), 'utf8'))

const version = rootPkg.version
if (!version) throw new Error('Root package.json is missing "version"')

const spec = `@midudev/tailwind-animations@${version}`
const message = 'Deprecated: use tailwind-animations instead.'

execFileSync('npm', ['deprecate', spec, message], { stdio: 'inherit' })
```

## File: `midudev-tailwind-animations-ceed187/scripts/publish-both.mjs`
```
import { execFileSync } from 'node:child_process'

const run = (cmd, args) => execFileSync(cmd, args, { stdio: 'inherit' })

// 1) keep versions aligned
run('node', ['./scripts/sync-scoped-package.mjs'])

// 2) publish official package (unscoped)
run('pnpm', ['publish', '--access', 'public', '--no-git-checks'])

// 3) publish deprecated scoped shim
run('pnpm', ['--dir', './packages/scoped', 'publish', '--access', 'public', '--no-git-checks'])

// 4) mark the scoped shim as deprecated for this version
run('node', ['./scripts/deprecate-scoped.mjs'])
```

## File: `midudev-tailwind-animations-ceed187/scripts/sync-scoped-package.mjs`
```
import fs from 'node:fs/promises'
import path from 'node:path'

const repoRoot = path.resolve(new URL('..', import.meta.url).pathname)

const rootPackagePath = path.join(repoRoot, 'package.json')
const scopedPackagePath = path.join(repoRoot, 'packages', 'scoped', 'package.json')

const [rootPkgRaw, scopedPkgRaw] = await Promise.all([
  fs.readFile(rootPackagePath, 'utf8'),
  fs.readFile(scopedPackagePath, 'utf8')
])

const rootPkg = JSON.parse(rootPkgRaw)
const scopedPkg = JSON.parse(scopedPkgRaw)

if (!rootPkg?.version) throw new Error('Root package.json is missing "version"')

scopedPkg.version = rootPkg.version
scopedPkg.dependencies ||= {}
scopedPkg.dependencies['tailwind-animations'] = rootPkg.version

await fs.writeFile(scopedPackagePath, JSON.stringify(scopedPkg, null, 2) + '\n', 'utf8')

console.log(`Synced @midudev/tailwind-animations to version ${rootPkg.version}`)
```

## File: `midudev-tailwind-animations-ceed187/src/index.css`
```css
/**
 * tailwind-animations
 * Tailwind CSS v4 Plugin - CSS-only implementation
 * 
 * @author Miguel Ángel Durán (@midudev) & su maravillosa comunidad
 * @license MIT
 */

/* ============================================
   Theme Configuration
   ============================================ */

@theme inline {
  /* Animation Delay Values - using tw-anim- prefix to avoid conflicts */
  --tw-anim-delay-none: 0ms;
  --tw-anim-delay-0: 0ms;
  --tw-anim-delay-100: 100ms;
  --tw-anim-delay-150: 150ms;
  --tw-anim-delay-200: 200ms;
  --tw-anim-delay-250: 250ms;
  --tw-anim-delay-300: 300ms;
  --tw-anim-delay-400: 400ms;
  --tw-anim-delay-500: 500ms;
  --tw-anim-delay-700: 700ms;
  --tw-anim-delay-800: 800ms;
  --tw-anim-delay-900: 900ms;
  --tw-anim-delay-1000: 1000ms;

  /* Animation Duration Values */
  --tw-anim-duration-none: 0ms;
  --tw-anim-duration-slower: 500ms;
  --tw-anim-duration-slow: 400ms;
  --tw-anim-duration-normal: 300ms;
  --tw-anim-duration-fast: 200ms;
  --tw-anim-duration-faster: 100ms;
  --tw-anim-duration-0: 0ms;
  --tw-anim-duration-100: 100ms;
  --tw-anim-duration-150: 150ms;
  --tw-anim-duration-200: 200ms;
  --tw-anim-duration-250: 250ms;
  --tw-anim-duration-300: 300ms;
  --tw-anim-duration-400: 400ms;
  --tw-anim-duration-500: 500ms;
  --tw-anim-duration-700: 700ms;
  --tw-anim-duration-800: 800ms;
  --tw-anim-duration-900: 900ms;
  --tw-anim-duration-1000: 1000ms;

  /* Animation Iteration Count Values */
  --tw-anim-iteration-count-none: 0;
  --tw-anim-iteration-count-once: 1;
  --tw-anim-iteration-count-twice: 2;
  --tw-anim-iteration-count-thrice: 3;
  --tw-anim-iteration-count-infinite: infinite;

  /* Animation Fill Mode Values */
  --tw-anim-fill-mode-none: none;
  --tw-anim-fill-mode-forwards: forwards;
  --tw-anim-fill-mode-backwards: backwards;
  --tw-anim-fill-mode-both: both;

  /* Animation Steps Values */
  --tw-anim-steps-none: 0;
  --tw-anim-steps-retro: 8;
  --tw-anim-steps-normal: 16;
  --tw-anim-steps-modern: 24;

  /* Animation Cubic Bezier Values */
  --tw-anim-bezier-sine-in: cubic-bezier(0.12, 0, 0.39, 0);
  --tw-anim-bezier-sine-out: cubic-bezier(0.39, 0.575, 0.565, 1);
  --tw-anim-bezier-sine-in-out: cubic-bezier(0.445, 0.05, 0.55, 0.95);
  --tw-anim-bezier-quad-in: cubic-bezier(0.55, 0.085, 0.68, 0.53);
  --tw-anim-bezier-quad-out: cubic-bezier(0.25, 0.46, 0.45, 0.94);
  --tw-anim-bezier-quad-in-out: cubic-bezier(0.455, 0.03, 0.515, 0.955);
  --tw-anim-bezier-cubic-in: cubic-bezier(0.55, 0.055, 0.675, 0.19);
  --tw-anim-bezier-cubic-out: cubic-bezier(0.215, 0.61, 0.355, 1);
  --tw-anim-bezier-cubic-in-out: cubic-bezier(0.645, 0.045, 0.355, 1);
  --tw-anim-bezier-quart-in: cubic-bezier(0.895, 0.03, 0.685, 0.22);
  --tw-anim-bezier-quart-out: cubic-bezier(0.165, 0.84, 0.44, 1);
  --tw-anim-bezier-quart-in-out: cubic-bezier(0.77, 0, 0.175, 1);
  --tw-anim-bezier-quint-in: cubic-bezier(0.755, 0.05, 0.855, 0.06);
  --tw-anim-bezier-quint-out: cubic-bezier(0.23, 1, 0.32, 1);
  --tw-anim-bezier-quint-in-out: cubic-bezier(0.86, 0, 0.07, 1);
  --tw-anim-bezier-expo-in: cubic-bezier(0.95, 0.05, 0.795, 0.035);
  --tw-anim-bezier-expo-out: cubic-bezier(0.19, 1, 0.22, 1);
  --tw-anim-bezier-expo-in-out: cubic-bezier(1, 0, 0, 1);
  --tw-anim-bezier-circ-in: cubic-bezier(0.6, 0.04, 0.98, 0.335);
  --tw-anim-bezier-circ-out: cubic-bezier(0.075, 0.82, 0.165, 1);
  --tw-anim-bezier-circ-in-out: cubic-bezier(0.785, 0.135, 0.15, 0.86);
  --tw-anim-bezier-back-in: cubic-bezier(0.6, -0.28, 0.735, 0.045);
  --tw-anim-bezier-back-out: cubic-bezier(0.175, 0.885, 0.32, 1.275);
  --tw-anim-bezier-back-in-out: cubic-bezier(0.68, -0.55, 0.265, 1.55);

  /* Animation Range Values */
  --tw-anim-range-normal: normal;
  --tw-anim-range-cover: cover;
  --tw-anim-range-contain: contain;
  --tw-anim-range-entry: entry;
  --tw-anim-range-exit: exit;
  --tw-anim-range-gradual: 10% 90%;
  --tw-anim-range-moderate: 20% 80%;
  --tw-anim-range-brisk: 30% 70%;
  --tw-anim-range-rapid: 40% 60%;

  /* Timeline Values */
  --tw-timeline-none: none;
  --tw-timeline-auto: auto;
  --tw-timeline-scroll: scroll();
  --tw-timeline-scroll-x: scroll(x);
  --tw-timeline-scroll-y: scroll(y);
  --tw-timeline-scroll-block: scroll(block);
  --tw-timeline-scroll-inline: scroll(inline);
  --tw-timeline-view: view();
  --tw-timeline-view-x: view(x);
  --tw-timeline-view-y: view(y);
  --tw-timeline-view-block: view(block);
  --tw-timeline-view-inline: view(inline);

  /* Scroll/View Timeline Axis Values */
  --tw-scroll-timeline-axis-block: block;
  --tw-scroll-timeline-axis-inline: inline;
  --tw-scroll-timeline-axis-x: x;
  --tw-scroll-timeline-axis-y: y;
  --tw-view-timeline-axis-block: block;
  --tw-view-timeline-axis-inline: inline;
  --tw-view-timeline-axis-x: x;
  --tw-view-timeline-axis-y: y;

  /* ============================================
     Predefined Animations
     ============================================ */

  --animate-blurred-fade-in: blurred-fade-in 0.9s ease-in-out both;
  --animate-fade-in: fade-in 0.6s ease-in both;
  --animate-fade-out: fade-out 0.6s ease-out both;
  --animate-slide-in-top: slide-in-top 0.6s ease-out both;
  --animate-slide-in-bottom: slide-in-bottom 0.6s ease-out both;
  --animate-slide-out-top: slide-out-top 0.6s ease-out both;
  --animate-slide-out-bottom: slide-out-bottom 0.6s ease-out both;
  --animate-zoom-in: zoom-in 0.6s ease-out both;
  --animate-zoom-out: zoom-out 0.6s ease-out both;
  --animate-rotate-90: rotate-90 1s ease-in-out both;
  --animate-rotate-180: rotate-180 1s ease-in-out both;
  --animate-rotate-360: rotate-360 1s linear both;
  --animate-flip-horizontal: flip-horizontal 1s ease-in-out both;
  --animate-flip-vertical: flip-vertical 1s ease-in-out both;
  --animate-bouncing: bouncing 1s ease-in-out both;
  --animate-swing: swing 1s ease-in-out both;
  --animate-wobble: wobble 1s ease-in-out both;
  --animate-pulsing: pulsing 1s ease-in-out both;
  --animate-shake: shake 0.5s ease-in-out both;
  --animate-tada: tada 1s ease-in-out both;
  --animate-jump: jump 1s ease-in-out both;
  --animate-hang: hang 1s ease-in-out both;
  --animate-roll-in: roll-in 1s ease-in-out both;
  --animate-roll-out: roll-out 1s ease-in-out both;
  --animate-float: float 1s ease-in-out both;
  --animate-sink: sink 1s ease-in-out both;
  --animate-flash: flash 1s ease-in-out both;
  --animate-jiggle: jiggle 0.5s ease-in-out both;
  --animate-rubber-band: rubber-band 1s ease-in-out both;
  --animate-scale: scale 0.6s ease-out both;
  --animate-slide-in-left: slide-in-left 0.6s ease-out both;
  --animate-slide-in-right: slide-in-right 0.6s ease-out both;
  --animate-slide-out-left: slide-out-left 0.6s ease-out both;
  --animate-slide-out-right: slide-out-right 0.6s ease-out both;
  --animate-spin-clockwise: spin-clockwise 0.6s linear both;
  --animate-spin-counter-clockwise: spin-counter-clockwise 0.6s linear both;
  --animate-flip-x: flip-x 0.6s ease-out both;
  --animate-flip-y: flip-y 0.6s ease-out both;
  --animate-blink: blink 0.5s both;
  --animate-pop: pop 0.6s ease-out both;
  --animate-expand-horizontally: expand-horizontally 0.6s ease-out both;
  --animate-contract-horizontally: contract-horizontally 0.6s ease-out both;
  --animate-expand-vertically: expand-vertically 0.6s ease-out both;
  --animate-contract-vertically: contract-vertically 0.6s ease-out both;
  --animate-fade-in-up: fade-in-up 0.6s ease-in-out both;
  --animate-fade-in-down: fade-in-down 0.6s ease-in-out both;
  --animate-fade-in-left: fade-in-left 0.6s ease-in-out both;
  --animate-fade-in-right: fade-in-right 0.6s ease-in-out both;
  --animate-fade-out-up: fade-out-up 0.6s ease-out both;
  --animate-fade-out-down: fade-out-down 0.6s ease-out both;
  --animate-fade-out-left: fade-out-left 0.6s ease-out both;
  --animate-fade-out-right: fade-out-right 0.6s ease-out both;
  --animate-sway: sway 0.6s ease-out both;
  --animate-flip-in-x: flip-in-x 0.6s ease-out both;
  --animate-flip-in-y: flip-in-y 0.6s ease-out both;
  --animate-flip-out-x: flip-out-x 0.6s ease-out both;
  --animate-flip-out-y: flip-out-y 0.6s ease-out both;
  --animate-rotate-in: rotate-in 0.6s ease-out both;
  --animate-rotate-out: rotate-out 0.6s ease-out both;
  --animate-slide-rotate-in: slide-rotate-in 0.6s ease-out both;
  --animate-slide-rotate-out: slide-rotate-out 0.6s ease-out both;
  --animate-heartbeat: heartbeat 0.6s ease-out both;
  --animate-horizontal-vibration: horizontal-vibration 0.3s linear infinite both;
  --animate-rotational-wave: rotational-wave 2s ease-in-out infinite both;
  --animate-skew: skew 0.5s ease-in-out both;
  --animate-skew-right: skew-right 0.5s ease-in-out both;
  --animate-vertical-bounce: vertical-bounce 0.6s ease-in-out both;
  --animate-horizontal-bounce: horizontal-bounce 0.6s ease-in-out both;
  --animate-tilt: tilt 0.6s ease-in-out both;
  --animate-squeeze: squeeze 0.6s ease-in-out both;
  --animate-slide-up-fade: slide-up-fade 0.6s ease-out both;
  --animate-bounce-fade-in: bounce-fade-in 0.6s ease-out both;
  --animate-swing-drop-in: swing-drop-in 0.6s ease-out both;
  --animate-pulse-fade-in: pulse-fade-in 0.6s ease-out both;
  --animate-impulse-rotation-right: impulse-rotation-right 1s ease-in-out both;
  --animate-impulse-rotation-left: impulse-rotation-left 1s ease-in-out both;
  --animate-dancing: dancing 1s ease-in-out both;
  --animate-pulse: pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
  --animate-jelly: jelly 1s ease-out forwards;

  /* ============================================
     Keyframes
     ============================================ */

  @keyframes fade-in {
    0% { opacity: 0; }
    100% { opacity: 1; }
  }

  @keyframes fade-out {
    0% { opacity: 1; }
    100% { opacity: 0; }
  }

  @keyframes slide-in-top {
    0% { transform: translateY(-20px); }
    100% { transform: translateY(0); }
  }

  @keyframes slide-in-bottom {
    0% { transform: translateY(20px); }
    100% { transform: translateY(0); }
  }

  @keyframes slide-out-top {
    0% { transform: translateY(0); }
    100% { transform: translateY(-20px); }
  }

  @keyframes slide-out-bottom {
    0% { transform: translateY(0); }
    100% { transform: translateY(20px); }
  }

  @keyframes zoom-in {
    0% { opacity: 0; transform: scale(.5); }
    100% { opacity: 1; transform: scale(1); }
  }

  @keyframes zoom-out {
    0% { opacity: 1; transform: scale(1); }
    100% { opacity: 0; transform: scale(.5); }
  }

  @keyframes rotate-90 {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(90deg); }
  }

  @keyframes rotate-180 {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(180deg); }
  }

  @keyframes rotate-360 {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
  }

  @keyframes flip-horizontal {
    0% { transform: rotateY(0deg); }
    100% { transform: rotateY(180deg); }
  }

  @keyframes flip-vertical {
    0% { transform: rotateX(0deg); }
    100% { transform: rotateX(180deg); }
  }

  @keyframes bouncing {
    0% { transform: translateY(0); }
    50% { transform: translateY(-10px); }
    100% { transform: translateY(0); }
  }

  @keyframes swing {
    0% { transform: rotate(0deg); }
    50% { transform: rotate(15deg); }
    100% { transform: rotate(0deg); }
  }

  @keyframes wobble {
    0% { transform: translateX(0); }
    15% { transform: translateX(-20px); }
    30% { transform: translateX(20%); }
    45% { transform: translateX(-15%); }
    60% { transform: translateX(20px); }
    75% { transform: translateX(-5%); }
    100% { transform: translateX(0); }
  }

  @keyframes pulse {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.5; }
  }

  @keyframes pulsing {
    0% { transform: scale(1); }
    50% { transform: scale(1.1); }
    100% { transform: scale(1); }
  }

  @keyframes shake {
    0% { transform: translateX(0); }
    25% { transform: translateX(-10px); }
    50% { transform: translateX(10px); }
    75% { transform: translateX(-10px); }
    100% { transform: translateX(0); }
  }

  @keyframes tada {
    0% { transform: scale(1); }
    10% { transform: scale(0.9) rotate(-3deg); }
    20% { transform: scale(0.9) rotate(-3deg); }
    30% { transform: scale(1.1) rotate(3deg); }
    40% { transform: scale(1.1) rotate(-3deg); }
    50% { transform: scale(1.1) rotate(3deg); }
    60% { transform: scale(1.1) rotate(-3deg); }
    70% { transform: scale(1.1) rotate(3deg); }
    80% { transform: scale(1.1) rotate(3deg); }
    90% { transform: scale(1.1) rotate(3deg); }
    100% { transform: scale(1) rotate(0); }
  }

  @keyframes jump {
    0% { transform: translateY(0); }
    50% { transform: translateY(-20px); }
    100% { transform: translateY(0); }
  }

  @keyframes hang {
    0% { transform: translateY(-20px); }
    50% { transform: translateY(0); }
    100% { transform: translateY(-20px); }
  }

  @keyframes roll-in {
    0% { transform: translateX(-20px) rotate(-120deg); }
    100% { transform: translateX(0) rotate(0); }
  }

  @keyframes roll-out {
    0% { transform: translateX(0) rotate(0); }
    100% { transform: translateX(20px) rotate(120deg); }
  }

  @keyframes float {
    0% { transform: translateY(0); }
    50% { transform: translateY(-10px); }
    100% { transform: translateY(0); }
  }

  @keyframes sink {
    0% { transform: translateY(-10px); }
    50% { transform: translateY(0); }
    100% { transform: translateY(-10px); }
  }

  @keyframes flash {
    0% { opacity: 1; }
    50% { opacity: 0; }
    100% { opacity: 1; }
  }

  @keyframes jiggle {
    0% { transform: rotate(-3deg); }
    50% { transform: rotate(3deg); }
    100% { transform: rotate(-3deg); }
  }

  @keyframes rubber-band {
    0% { transform: scale(1); }
    30% { transform: scale(1.25); }
    40% { transform: scale(0.75); }
    50% { transform: scale(1.15); }
    65% { transform: scale(0.95); }
    75% { transform: scale(1.05); }
    100% { transform: scale(1); }
  }

  @keyframes scale {
    0% { transform: scale(1); }
    100% { transform: scale(1.10); }
  }

  @keyframes slide-in-left {
    0% { transform: translateX(-20px); }
    100% { transform: translateX(0); }
  }

  @keyframes slide-in-right {
    0% { transform: translateX(20px); }
    100% { transform: translateX(0); }
  }

  @keyframes slide-out-left {
    0% { transform: translateX(0); }
    100% { transform: translateX(-20px); }
  }

  @keyframes slide-out-right {
    0% { transform: translateX(0); }
    100% { transform: translateX(20px); }
  }

  @keyframes spin-clockwise {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
  }

  @keyframes spin-counter-clockwise {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(-360deg); }
  }

  @keyframes flip-x {
    0% { transform: scaleX(1); }
    50% { transform: scaleX(-1); }
    100% { transform: scaleX(1); }
  }

  @keyframes flip-y {
    0% { transform: scaleY(1); }
    50% { transform: scaleY(-1); }
    100% { transform: scaleY(1); }
  }

  @keyframes blink {
    0% { opacity: 0; }
    100% { opacity: 1; }
  }

  @keyframes pop {
    0% { transform: scale(1); }
    50% { transform: scale(1.1); }
    100% { transform: scale(1); }
  }

  @keyframes expand-horizontally {
    0% { transform: scaleX(0); }
    100% { transform: scaleX(1); }
  }

  @keyframes contract-horizontally {
    0% { transform: scaleX(1); }
    100% { transform: scaleX(0); }
  }

  @keyframes expand-vertically {
    0% { transform: scaleY(0); }
    100% { transform: scaleY(1); }
  }

  @keyframes contract-vertically {
    0% { transform: scaleY(1); }
    100% { transform: scaleY(0); }
  }

  @keyframes fade-in-up {
    0% { opacity: 0; transform: translateY(20px); }
    100% { opacity: 1; transform: translateY(0); }
  }

  @keyframes fade-in-down {
    0% { opacity: 0; transform: translateY(-20px); }
    100% { opacity: 1; transform: translateY(0); }
  }

  @keyframes fade-in-left {
    0% { opacity: 0; transform: translateX(20px); }
    100% { opacity: 1; transform: translateX(0); }
  }

  @keyframes fade-in-right {
    0% { opacity: 0; transform: translateX(-20px); }
    100% { opacity: 1; transform: translateX(0); }
  }

  @keyframes fade-out-up {
    0% { opacity: 1; transform: translateY(0); }
    100% { opacity: 0; transform: translateY(-20px); }
  }

  @keyframes fade-out-down {
    0% { opacity: 1; transform: translateY(0); }
    100% { opacity: 0; transform: translateY(20px); }
  }

  @keyframes fade-out-left {
    0% { opacity: 1; transform: translateX(0); }
    100% { opacity: 0; transform: translateX(-20px); }
  }

  @keyframes fade-out-right {
    0% { opacity: 1; transform: translateX(0); }
    100% { opacity: 0; transform: translateX(20px); }
  }

  @keyframes sway {
    0% { transform: rotate(0deg); }
    50% { transform: rotate(15deg); }
    100% { transform: rotate(0deg); }
  }

  @keyframes flip-in-x {
    0% { opacity: 0; transform: rotateY(90deg); }
    100% { opacity: 1; transform: rotateY(0deg); }
  }

  @keyframes flip-in-y {
    0% { opacity: 0; transform: rotateX(90deg); }
    100% { opacity: 1; transform: rotateX(0deg); }
  }

  @keyframes flip-out-x {
    0% { opacity: 1; transform: rotateY(0deg); }
    100% { opacity: 0; transform: rotateY(90deg); }
  }

  @keyframes flip-out-y {
    0% { opacity: 1; transform: rotateX(0deg); }
    100% { opacity: 0; transform: rotateX(90deg); }
  }

  @keyframes rotate-in {
    0% { opacity: 0; transform: rotate(-90deg); }
    100% { opacity: 1; transform: rotate(0deg); }
  }

  @keyframes rotate-out {
    0% { opacity: 1; transform: rotate(0deg); }
    100% { opacity: 0; transform: rotate(90deg); }
  }

  @keyframes slide-rotate-in {
    0% { opacity: 0; transform: translateX(-20px) rotate(-90deg); }
    100% { opacity: 1; transform: translateX(0) rotate(0deg); }
  }

  @keyframes slide-rotate-out {
    0% { opacity: 1; transform: translateX(0) rotate(0deg); }
    100% { opacity: 0; transform: translateX(20px) rotate(90deg); }
  }

  @keyframes heartbeat {
    0% { transform: scale(1); }
    25% { transform: scale(1.1); }
    50% { transform: scale(1); }
    75% { transform: scale(0.9); }
    100% { transform: scale(1); }
  }

  @keyframes blurred-fade-in {
    0% { filter: blur(5px); opacity: 0; }
    100% { filter: blur(0); opacity: 1; }
  }

  @keyframes horizontal-vibration {
    0% { transform: translateX(0); }
    25% { transform: translateX(5px); }
    50% { transform: translateX(-5px); }
    75% { transform: translateX(5px); }
    100% { transform: translateX(0); }
  }

  @keyframes rotational-wave {
    0% { transform: rotate(0deg); }
    25% { transform: rotate(10deg); }
    50% { transform: rotate(-10deg); }
    75% { transform: rotate(10deg); }
    100% { transform: rotate(0deg); }
  }

  @keyframes skew {
    0% { transform: skew(0deg); }
    100% { transform: skew(20deg); }
  }

  @keyframes skew-right {
    0% { transform: skew(0deg); }
    100% { transform: skew(-20deg); }
  }

  @keyframes vertical-bounce {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-20px); }
  }

  @keyframes horizontal-bounce {
    0%, 100% { transform: translateX(0); }
    50% { transform: translateX(20px); }
  }

  @keyframes tilt {
    0% { transform: rotateY(0deg); }
    50% { transform: rotateY(20deg); }
    100% { transform: rotateY(0deg); }
  }

  @keyframes squeeze {
    0%, 100% { transform: scale(1, 1); }
    50% { transform: scale(1.1, 0.9); }
  }

  @keyframes slide-up-fade {
    0% { opacity: 0; transform: translateY(50px); }
    100% { opacity: 1; transform: translateY(0); }
  }

  @keyframes bounce-fade-in {
    0% { transform: scale(0.5); opacity: 0; }
    100% { transform: scale(1); opacity: 1; }
  }

  @keyframes swing-drop-in {
    0% { transform: rotate(-30deg) translateY(-50px); opacity: 0; }
    100% { transform: rotate(0deg) translateY(0); opacity: 1; }
  }

  @keyframes pulse-fade-in {
    0% { transform: scale(0.9); opacity: 0; }
    50% { transform: scale(1.05); opacity: 0.5; }
    100% { transform: scale(1); opacity: 1; }
  }

  @keyframes impulse-rotation-right {
    0% { transform: rotate(0deg); }
    50% { transform: rotate(-40deg); }
    100% { transform: rotate(360deg); }
  }

  @keyframes impulse-rotation-left {
    0% { transform: rotate(0deg); }
    50% { transform: rotate(40deg); }
    100% { transform: rotate(-360deg); }
  }

  @keyframes dancing {
    0% { transform: skew(0deg); }
    25% { transform: skew(-40deg); }
    50% { transform: skew(40deg); }
    75% { transform: skew(-40deg); }
    100% { transform: skew(0deg); }
  }

  @keyframes jelly {
    0% { transform: scale(1, 1); }
    20% { transform: scale(1.25, 0.75); }
    40% { transform: scale(0.75, 1.25); }
    60% { transform: scale(1.15, 0.85); }
    75% { transform: scale(0.95, 1.05); }
    85% { transform: scale(1.05, 0.95); }
    92% { transform: scale(1, 1.02); }
    100% { transform: scale(1, 1); }
  }
}

/* ============================================
   Utility Classes - Animation Delay
   ============================================ */

@utility animate-delay-* {
  animation-delay: calc(--value(integer) * 1ms);
  animation-delay: --value(--tw-anim-delay-*, [duration], [*]);
}

/* ============================================
   Utility Classes - Animation Duration
   ============================================ */

@utility animate-duration-* {
  animation-duration: calc(--value(integer) * 1ms);
  animation-duration: --value(--tw-anim-duration-*, [duration], [*]);
}

/* ============================================
   Utility Classes - Animation Iteration Count
   ============================================ */

@utility animate-iteration-count-* {
  animation-iteration-count: --value(--tw-anim-iteration-count-*, number, [number], [*]);
}

/* ============================================
   Utility Classes - Animation Fill Mode
   ============================================ */

@utility animate-fill-mode-* {
  animation-fill-mode: --value(--tw-anim-fill-mode-*, [*]);
}

/* ============================================
   Utility Classes - Animation Steps
   ============================================ */

@utility animate-steps-* {
  animation-timing-function: steps(--value(--tw-anim-steps-*, integer, [integer]));
}

/* ============================================
   Utility Classes - Animation Timing Functions
   ============================================ */

@utility animate-ease {
  animation-timing-function: ease;
}

@utility animate-ease-in {
  animation-timing-function: ease-in;
}

@utility animate-ease-out {
  animation-timing-function: ease-out;
}

@utility animate-ease-in-out {
  animation-timing-function: ease-in-out;
}

@utility animate-linear {
  animation-timing-function: linear;
}

/* ============================================
   Utility Classes - Animation Bezier Curves
   ============================================ */

@utility animate-bezier-* {
  animation-timing-function: --value(--tw-anim-bezier-*, [*]);
}

/* ============================================
   Utility Classes - Animation Direction
   ============================================ */

@utility animate-direction-normal {
  animation-direction: normal;
}

@utility animate-direction-reverse {
  animation-direction: reverse;
}

@utility animate-direction-alternate {
  animation-direction: alternate;
}

@utility animate-direction-alternate-reverse {
  animation-direction: alternate-reverse;
}

/* ============================================
   Utility Classes - Animation Play State
   ============================================ */

@utility animate-play-running {
  animation-play-state: running;
}

@utility animate-play-paused {
  animation-play-state: paused;
}

/* ============================================
   Utility Classes - Animation Timeline
   ============================================ */

@utility timeline-* {
  animation-timeline: --value(--tw-timeline-*, [ident], [*]) !important;
}

/* ============================================
   Utility Classes - Scroll Timeline Axis
   ============================================ */

@utility scroll-timeline-axis-* {
  scroll-timeline-axis: --value(--tw-scroll-timeline-axis-*, [ident], [*]);
}

/* ============================================
   Utility Classes - View Timeline Axis
   ============================================ */

@utility view-timeline-axis-* {
  view-timeline-axis: --value(--tw-view-timeline-axis-*, [ident], [*]);
}

/* ============================================
   Utility Classes - Animation Range
   ============================================ */

@utility animate-range-* {
  animation-range: --value(--tw-anim-range-*, [*]);
}

```

## File: `midudev-tailwind-animations-ceed187/test/index.test.js`
```javascript
import { generatePluginCSS } from './utils.js'
import { describe, it, expect } from 'vitest'

describe('tailwindcss-animations plugins', () => {
  it('use a predefined animation', async () => {
    const css = await generatePluginCSS({
      content: '<div class="animate-zoom-in">Hello</div>'
    })
    expect(css).toContain('.animate-zoom-in{animation:zoom-in 0.6s ease-out both}')
    expect(css).toContain('@keyframes zoom-in{0%{opacity:0;transform:scale(.5)}100%{opacity:1;transform:scale(1)}}')
  })

  it('use fade in up animation', async () => {
    const css = await generatePluginCSS({
      content: '<div class="animate-fade-in-up">Hello</div>'
    })
    expect(css).toContain('.animate-fade-in-up{animation:fade-in-up 0.6s ease-in-out both}')
    expect(css).toContain('@keyframes fade-in-up{0%{opacity:0;transform:translateY(20px)}100%{opacity:1;transform:translateY(0)}}')
  })

  it('use a predefined animation delay', async () => {
    const css = await generatePluginCSS({
      content: '<div class="animate-delay-100">Hello</div>'
    })

    expect(css).toContain('animation-delay:100ms')
  })

  it('use a custom animation delay', async () => {
    const css = await generatePluginCSS({
      content: '<div class="animate-delay-[777ms]">Hello</div>'
    })

    expect(css).toContain('.animate-delay-\\[777ms\\]{animation-delay:777ms}')
  })

  it('use a predefined animation duration', async () => {
    const css = await generatePluginCSS({
      content: '<div class="animate-duration-100">Hello</div>'
    })

    expect(css).toContain('animation-duration:100ms')
  })

  it('use a predefined named animation duration', async () => {
    const css = await generatePluginCSS({
      content: '<div class="animate-duration-faster">Hello</div>'
    })

    expect(css).toContain('.animate-duration-faster{animation-duration:100ms}')
  })

  it('use a custom animation duration', async () => {
    const css = await generatePluginCSS({
      content: '<div class="animate-duration-[777ms]">Hello</div>'
    })

    expect(css).toContain('.animate-duration-\\[777ms\\]{animation-duration:777ms}')
  })

  it('use a timing function animation', async () => {
    const css = await generatePluginCSS({
      content: '<div class="animate-linear">Hello</div>'
    })

    expect(css).toContain('.animate-linear{animation-timing-function:linear}')
  })

  it('use a bezier curve as a timing function animation', async () => {
    const css = await generatePluginCSS({
      content: '<div class="animate-bezier-sine-in">Hello</div>'
    })

    expect(css).toContain('.animate-bezier-sine-in{animation-timing-function:cubic-bezier(0.12, 0, 0.39, 0)}')
  })

  it('use a custom bezier curve as a timing function animation', async () => {
    const css = await generatePluginCSS({
      content: '<div class="animate-bezier-[cubic-bezier(0,0,0,0)]">Hello</div>'
    })

    expect(css).toContain(
      '.animate-bezier-\\[cubic-bezier\\(0\\,0\\,0\\,0\\)\\]{animation-timing-function:cubic-bezier(0,0,0,0)}'
    )
  })

  it('use a custom animation iteration count', async () => {
    const css = await generatePluginCSS({
      content: '<div class="animate-iteration-count-twice">Hello</div>'
    })

    expect(css).toContain('.animate-iteration-count-twice{animation-iteration-count:2}')
  })

  it('use a custom animation iteration count with an arbitrary value', async () => {
    const css = await generatePluginCSS({
      content: '<div class="animate-iteration-count-[10]">Hello</div>'
    })

    expect(css).toContain('.animate-iteration-count-\\[10\\]{animation-iteration-count:10}')
  })

  it('use a custom animation direction', async () => {
    const css = await generatePluginCSS({
      content: '<div class="animate-direction-reverse">Hello</div>'
    })

    expect(css).toContain('.animate-direction-reverse{animation-direction:reverse}')
  })

  it('use a fill mode animation', async () => {
    const css = await generatePluginCSS({
      content: '<div class="animate-fill-mode-forwards">Hello</div>'
    })

    expect(css).toContain('.animate-fill-mode-forwards{animation-fill-mode:forwards}')
  })

  it('use not custom animation steps', async () => {
    const css = await generatePluginCSS({
      content: '<div class="animate-steps-retro">Hello</div>'
    })

    expect(css).toContain('.animate-steps-retro{animation-timing-function:steps(8)}')
  })
  it('use a custom animation steps', async () => {
    const css = await generatePluginCSS({
      content: '<div class="animate-steps-[33]">Hello</div>'
    })

    expect(css).toContain('.animate-steps-\\[33\\]{animation-timing-function:steps(33)}')
  })

  it('use a play state animation play', async () => {
    const css = await generatePluginCSS({
      content: '<div class="animate-play-paused">Hello</div>'
    })

    expect(css).toContain('.animate-play-paused{animation-play-state:paused}')
  })

  it('use a animation timeline none or auto', async () => {
    const css = await generatePluginCSS({
      content: '<div class="timeline-none">Hello</div>'
    })

    expect(css).toContain('.timeline-none{animation-timeline:none!important}')
  })

  it('use a animation timeline scroll', async () => {
    const css = await generatePluginCSS({
      content: '<div class="timeline-scroll">Hello</div>'
    })

    expect(css).toContain('.timeline-scroll{animation-timeline:scroll()!important}')
  })

  it('use a animation timeline scroll-x', async () => {
    const css = await generatePluginCSS({
      content: '<div class="timeline-scroll-x">Hello</div>'
    })

    expect(css).toContain('.timeline-scroll-x{animation-timeline:scroll(x)!important}')
  })

  it('use a animation timeline scroll-y', async () => {
    const css = await generatePluginCSS({
      content: '<div class="timeline-scroll-y">Hello</div>'
    })

    expect(css).toContain('.timeline-scroll-y{animation-timeline:scroll(y)!important}')
  })

  it('use a animation timeline scroll-block', async () => {
    const css = await generatePluginCSS({
      content: '<div class="timeline-scroll-block">Hello</div>'
    })

    expect(css).toContain('.timeline-scroll-block{animation-timeline:scroll(block)!important}')
  })

  it('use a animation timeline scroll-inline', async () => {
    const css = await generatePluginCSS({
      content: '<div class="timeline-scroll-inline">Hello</div>'
    })

    expect(css).toContain('.timeline-scroll-inline{animation-timeline:scroll(inline)!important}')
  })

  it('use a animation timeline view-x', async () => {
    const css = await generatePluginCSS({
      content: '<div class="timeline-view-x">Hello</div>'
    })

    expect(css).toContain('.timeline-view-x{animation-timeline:view(x)!important}')
  })

  it('use a animation timeline view-inline', async () => {
    const css = await generatePluginCSS({
      content: '<div class="timeline-view-inline">Hello</div>'
    })

    expect(css).toContain('.timeline-view-inline{animation-timeline:view(inline)!important}')
  })

  it('use a animation timeline scroll custom', async () => {
    const css = await generatePluginCSS({
      content: '<div class="timeline-[scroll(20%)]">Hello</div>'
    })

    expect(css).toContain('.timeline-\\[scroll\\(20\\%\\)\\]{animation-timeline:scroll(20%)!important}')
  })

  it('use a animation timeline scroll custom with spaces', async () => {
    const css = await generatePluginCSS({
      content: '<div class="timeline-[scroll(x_root)]">Hello</div>'
    })

    expect(css).toContain('.timeline-\\[scroll\\(x_root\\)\\]{animation-timeline:scroll(x root)!important}')
  })

  it('use a animation timeline view custom with multiple values', async () => {
    const css = await generatePluginCSS({
      content: '<div class="timeline-[view(x_200px_auto)]">Hello</div>'
    })

    expect(css).toContain('.timeline-\\[view\\(x_200px_auto\\)\\]{animation-timeline:view(x 200px auto)!important}')
  })

  it('use a animation timeline custom name', async () => {
    const css = await generatePluginCSS({
      content: '<div class="timeline-[--test]">Hello</div>'
    })

    expect(css).toContain('.timeline-\\[--test\\]{animation-timeline:--test!important}')
  })

  it('use a timeline range', async () => {
    const css = await generatePluginCSS({
      content: '<div class="animate-range-cover">Hello</div>'
    })

    expect(css).toContain('.animate-range-cover{animation-range:cover}')
  })

  it('use a timeline range porcentual', async () => {
    const css = await generatePluginCSS({
      content: '<div class="animate-range-moderate">Hello</div>'
    })

    expect(css).toContain('.animate-range-moderate{animation-range:20% 80%}')
  })

  it('use a timeline range custom', async () => {
    const css = await generatePluginCSS({
      content: '<div class="animate-range-[12%_65%]">Hello</div>'
    })

    expect(css).toContain('.animate-range-\\[12\\%_65\\%\\]{animation-range:12% 65%}')
  })

  it('use a scroll timeline axis', async () => {
    const css = await generatePluginCSS({
      content: '<div class="scroll-timeline-axis-block">Hello</div>'
    })

    expect(css).toContain('.scroll-timeline-axis-block{scroll-timeline-axis:block}')
  })

  it('use a view timeline axis', async () => {
    const css = await generatePluginCSS({
      content: '<div class="view-timeline-axis-y">Hello</div>'
    })

    expect(css).toContain('.view-timeline-axis-y{view-timeline-axis:y}')
  })
})
```

## File: `midudev-tailwind-animations-ceed187/test/utils.js`
```javascript
import tailwindcss from '@tailwindcss/postcss'
import postcss from 'postcss'
import minify from '@csstools/postcss-minify'
import { join } from 'path'

const TAILWIND_BASE = '@import "tailwindcss";'
const PLUGIN_IMPORT = `@import "${join(process.cwd(), 'src/index.css')}";`

export function generatePluginCSS (options = {}) {
  const { inline = '', content = '' } = options

  return postcss([
    tailwindcss(),
    minify()
  ])
    .process(`${TAILWIND_BASE}\n${PLUGIN_IMPORT}\n${inline}`, {
      from: join(process.cwd(), 'test/index.test.js'),
      content: [{ raw: content, extension: 'html' }]
    })
    .then(result => result.css)
}
```

## File: `midudev-tailwind-animations-ceed187/web/.eslintrc.cjs`
```
/** @type {import("eslint").Linter.Config} */
module.exports = {
  extends: ['plugin:astro/recommended', 'prettier'],
  parser: '@typescript-eslint/parser',
  parserOptions: {
    tsconfigRootDir: __dirname,
    sourceType: 'module',
    ecmaVersion: 'latest'
  },
  overrides: [
    {
      files: ['*.astro'],
      parser: 'astro-eslint-parser',
      parserOptions: {
        parser: '@typescript-eslint/parser',
        extraFileExtensions: ['.astro']
      }
    }
  ]
}
```

## File: `midudev-tailwind-animations-ceed187/web/.gitignore`
```
# build output
dist/

# generated types
.astro/

# dependencies
node_modules/

# logs
npm-debug.log*
yarn-debug.log*
yarn-error.log*
pnpm-debug.log*
bun.lockb*

# environment variables
.env
.env.production

# macOS-specific files
.DS_Store
```

## File: `midudev-tailwind-animations-ceed187/web/.prettierrc.cjs`
```
/** @type {import("prettier").Config} */
module.exports = {
  ...require('prettier-config-standard'),
  plugins: [
    require.resolve('prettier-plugin-astro'),
    'prettier-plugin-tailwindcss'
  ],
  overrides: [
    {
      files: '*.astro',
      options: {
        parser: 'astro'
      }
    }
  ]
}
```

## File: `midudev-tailwind-animations-ceed187/web/README.md`
```markdown
# Web de `tailwind-animations`
```

## File: `midudev-tailwind-animations-ceed187/web/astro.config.mjs`
```
import { defineConfig } from 'astro/config'
import tailwindcss from '@tailwindcss/vite'
import sitemap from '@astrojs/sitemap'

export default defineConfig({
  site: 'https://tailwind-animations.com',
  integrations: [sitemap()],
  vite: {
    plugins: [tailwindcss()]
  }
})
```

## File: `midudev-tailwind-animations-ceed187/web/package.json`
```json
{
  "name": "web",
  "type": "module",
  "version": "0.0.1",
  "scripts": {
    "dev": "astro dev",
    "start": "astro dev",
    "build": "astro check && astro build",
    "preview": "astro preview",
    "astro": "astro",
    "lint": "prettier --write \"**/*.{js,jsx,ts,tsx,md,mdx,astro}\" && eslint --fix \"src/**/*.{js,ts,jsx,tsx,astro}\""
  },
  "dependencies": {
    "@astrojs/check": "0.9.6",
    "@astrojs/sitemap": "^3.7.0",
    "@fontsource-variable/geist-mono": "5.2.7",
    "@tailwindcss/vite": "4.1.18",
    "astro": "5.16.8",
    "tailwind-animations": "workspace:*",
    "tailwindcss": "4.1.18",
    "typescript": "5.9.3",
    "wc-toast": "1.3.1"
  }
}
```

## File: `midudev-tailwind-animations-ceed187/web/tsconfig.json`
```json
{
  "extends": "astro/tsconfigs/strict",
  "compilerOptions": {
    "baseUrl": ".",
    "paths": {
      "@components/*": [
        "src/components/*"
      ],
      "@layouts/*": [
        "src/layouts/*"
      ]
    },
  }
}
```

## File: `midudev-tailwind-animations-ceed187/web/public/robots.txt`
```
User-agent: *
Allow: /

Sitemap: https://tailwind-animations.com/sitemap-index.xml
```

## File: `midudev-tailwind-animations-ceed187/web/src/env.d.ts`
```typescript
/// <reference path="../.astro/types.d.ts" />
/// <reference types="astro/client" />
```

## File: `midudev-tailwind-animations-ceed187/web/src/components/icons/copy.astro`
```
<svg width='16' height='16' stroke-width='1.5' viewBox='0 0 24 24' fill='none' aria-hidden='true'
  ><path
    d='M19.4 20H9.6C9.26863 20 9 19.7314 9 19.4V9.6C9 9.26863 9.26863 9 9.6 9H19.4C19.7314 9 20 9.26863 20 9.6V19.4C20 19.7314 19.7314 20 19.4 20Z'
    stroke='currentColor'
    stroke-linecap='round'
    stroke-linejoin='round'></path><path
    d='M15 9V4.6C15 4.26863 14.7314 4 14.4 4H4.6C4.26863 4 4 4.26863 4 4.6V14.4C4 14.7314 4.26863 15 4.6 15H9'
    stroke='currentColor'
    stroke-linecap='round'
    stroke-linejoin='round'></path></svg
>
```

## File: `midudev-tailwind-animations-ceed187/web/src/components/icons/github.astro`
```
---
const props = Astro.props
---

<svg
  xmlns='http://www.w3.org/2000/svg'
  width='24'
  height='24'
  viewBox='0 0 24 24'
  fill='none'
  stroke='currentColor'
  stroke-width='1.6'
  stroke-linecap='round'
  stroke-linejoin='round'
  aria-hidden='true'
  {...props}
  ><path stroke='none' d='M0 0h24v24H0z' fill='none'></path><path
    d='M9 19c-4.3 1.4 -4.3 -2.5 -6 -3m12 5v-3.5c0 -1 .1 -1.4 -.5 -2c2.8 -.3 5.5 -1.4 5.5 -6a4.6 4.6 0 0 0 -1.3 -3.2a4.2 4.2 0 0 0 -.1 -3.2s-1.1 -.3 -3.5 1.3a12.3 12.3 0 0 0 -6.2 0c-2.4 -1.6 -3.5 -1.3 -3.5 -1.3a4.2 4.2 0 0 0 -.1 3.2a4.6 4.6 0 0 0 -1.3 3.2c0 4.6 2.7 5.7 5.5 6c-.6 .6 -.6 1.2 -.5 2v3.5'
  ></path></svg
>
```

## File: `midudev-tailwind-animations-ceed187/web/src/components/icons/menu.astro`
```
---
const props = Astro.props
---

<!-- Nuevo icono para cuando el header sea movil -->

<svg
  xmlns='http://www.w3.org/2000/svg'
  width='24'
  height='24'
  viewBox='0 0 640 640'
  fill='currentColor'
  {...props}
>
  <path
    d='M96 160C96 142.3 110.3 128 128 128L512 128C529.7 128 544 142.3 544 160C544 177.7 529.7 192 512 192L128 192C110.3 192 96 177.7 96 160zM96 320C96 302.3 110.3 288 128 288L512 288C529.7 288 544 302.3 544 320C544 337.7 529.7 352 512 352L128 352C110.3 352 96 337.7 96 320zM544 480C544 497.7 529.7 512 512 512L128 512C110.3 512 96 497.7 96 480C96 462.3 110.3 448 128 448L512 448C529.7 448 544 462.3 544 480z'
  ></path>
</svg>
```

## File: `midudev-tailwind-animations-ceed187/web/src/components/icons/moon.astro`
```
<svg
  {...Astro.props}
  width='24'
  height='24'
  viewBox='0 0 24 24'
  stroke-width='1.6'
  stroke='currentColor'
  fill='none'
  stroke-linecap='round'
  stroke-linejoin='round'
>
  <path stroke='none' d='M0 0h24v24H0z' fill='none'></path>
  <path
    d='M12 3c.132 0 .263 0 .393 0a7.5 7.5 0 0 0 7.92 12.446a9 9 0 1 1 -8.313 -12.454z'
  ></path>
</svg>
```

## File: `midudev-tailwind-animations-ceed187/web/src/components/icons/sun.astro`
```
<svg
  {...Astro.props}
  width='24'
  height='24'
  viewBox='0 0 24 24'
  stroke-width='1.6'
  stroke='currentColor'
  fill='none'
  stroke-linecap='round'
  stroke-linejoin='round'
>
  <path stroke='none' d='M0 0h24v24H0z' fill='none'></path>
  <path d='M12 12m-4 0a4 4 0 1 0 8 0a4 4 0 1 0 -8 0'></path>
  <path
    d='M3 12h1m8 -9v1m8 8h1m-9 8v1m-6.4 -15.4l.7 .7m12.1 -.7l-.7 .7m0 11.4l.7 .7m-12.1 -.7l-.7 .7'
  ></path>
</svg>
```

## File: `midudev-tailwind-animations-ceed187/web/src/components/icons/system.astro`
```
<svg
  {...Astro.props}
  width='24'
  height='24'
  viewBox='0 0 24 24'
  stroke-width='1.6'
  stroke='currentColor'
  fill='none'
  stroke-linecap='round'
  stroke-linejoin='round'
>
  <path stroke='none' d='M0 0h24v24H0z' fill='none'></path>
  <path
    d='M3 5a1 1 0 0 1 1 -1h16a1 1 0 0 1 1 1v10a1 1 0 0 1 -1 1h-16a1 1 0 0 1 -1 -1v-10z'
  ></path>
  <path d='M7 20h10'></path>
  <path d='M9 16v4'></path>
  <path d='M15 16v4'></path>
</svg>
```

## File: `midudev-tailwind-animations-ceed187/web/src/components/layout/Footer.astro`
```
---
// se agrega "../" a las rutas porque se movio de ubicacion a la carpeta layout el footer 
import Github from '../icons/github.astro'
import Logo from '../ui/Logo.astro'

const currentYear = new Date().getFullYear()

const FOOTER_LINKS = [
  {
    title: 'Documentation',
    links: [
      { name: 'Installation', href: '#install-command' },
      { name: 'Usage', href: '#option-inputs' },
      {
        name: 'Utility Classes',
        href: 'https://github.com/midudev/tailwind-animations#utility-classes'
      },
      {
        name: 'Customizing',
        href: 'https://github.com/midudev/tailwind-animations#customization'
      }
    ]
  },
  {
    title: 'Community',
    links: [
      {
        name: 'Contributors',
        href: 'https://github.com/midudev/tailwind-animations/graphs/contributors'
      },
      {
        name: 'GitHub Issues',
        href: 'https://github.com/midudev/tailwind-animations/issues'
      },
      {
        name: 'Discussions',
        href: 'https://github.com/midudev/tailwind-animations/discussions'
      },
      { name: 'Discord', href: 'https://discord.gg/midudev' }
    ]
  },
  {
    title: 'Links',
    links: [
      {
        name: 'npm Package',
        href: 'https://npm.im/tailwind-animations'
      },
      { name: 'Midu.dev', href: 'https://midu.dev' },
      { name: 'Twitch', href: 'https://twitch.tv/midudev' },
      { name: 'YouTube', href: 'https://youtube.com/midudev' }
    ]
  }
]
---

<footer
  class='relative mt-32 overflow-hidden border-t border-slate-200 bg-slate-50/50 pt-20 pb-10 dark:border-slate-800 dark:bg-[#080808]/50'
>
  <div
    class='absolute top-0 left-1/2 h-px w-full -translate-x-1/2 bg-linear-to-r from-transparent via-blue-500/20 to-transparent dark:via-blue-500/10'
  >
  </div>
  <div
    class='absolute -top-24 left-1/4 size-64 rounded-full bg-blue-500/5 blur-[100px] dark:bg-blue-600/5'
  >
  </div>
  <div
    class='absolute right-1/4 -bottom-24 size-64 rounded-full bg-blue-500/5 blur-[100px] dark:bg-blue-600/5'
  >
  </div>

  <div class='relative mx-auto max-w-6xl px-4 lg:px-8'>
    <div class='grid grid-cols-1 gap-12 lg:grid-cols-12'>
      <!-- Brand & Info -->
      <div class='group flex flex-col gap-6 lg:col-span-5'>
        <div class='flex items-center gap-3'>
          <Logo
            class='size-10 group-hover:scale-110 group-hover:rotate-3 group-hover:shadow-blue-500/40'
            iconClass='size-6 animate-float-subtle group-hover:animate-pulse'
          />
          <span
            class='text-2xl font-bold tracking-tight text-slate-900 transition-colors group-hover:text-blue-600 dark:text-white dark:group-hover:text-blue-400'
          >
            Tailwind <span class='text-blue-500'>Animations</span>
          </span>
        </div>

        <p
          class='max-w-sm text-base leading-relaxed text-slate-600 dark:text-slate-400'
        >
          Elevate your user experience with high-performance animations. Open
          source, community-driven, and designed for Tailwind CSS.
        </p>

        <div class='flex items-center gap-5'>
          <a
            href='https://github.com/midudev/tailwind-animations'
            target='_blank'
            rel='noopener noreferrer'
            aria-label='GitHub'
            class='group flex items-center justify-center rounded-full bg-white p-2.5 text-slate-400 shadow-sm ring-1 ring-slate-200 transition-all hover:text-slate-900 hover:ring-slate-300 dark:bg-slate-900 dark:text-slate-500 dark:ring-slate-800 dark:hover:text-white dark:hover:ring-slate-700'
          >
            <Github class='size-5' />
          </a>
          <a
            href='https://x.com/midudev'
            target='_blank'
            rel='noopener noreferrer'
            aria-label='X (Twitter)'
            class='group flex items-center justify-center rounded-full bg-white p-2.5 text-slate-400 shadow-sm ring-1 ring-slate-200 transition-all hover:text-slate-900 hover:ring-slate-300 dark:bg-slate-900 dark:text-slate-500 dark:ring-slate-800 dark:hover:text-white dark:hover:ring-slate-700'
          >
            <svg viewBox='0 0 24 24' class='size-5' fill='currentColor'>
              <path
                d='M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z'
              ></path>
            </svg>
          </a>
        </div>
      </div>

      <!-- Links Grid -->
      <div class='grid grid-cols-2 gap-8 sm:grid-cols-3 lg:col-span-7'>
        {
          FOOTER_LINKS.map((section) => (
            <div class='flex flex-col gap-4'>
              <h3 class='text-xs font-bold tracking-[0.2em] whitespace-nowrap text-slate-900 uppercase dark:text-white'>
                {section.title}
              </h3>
              <ul class='flex flex-col gap-3'>
                {section.links.map((link) => {
                  const isExternal = link.href.startsWith('http')
                  return (
                    <li>
                      <a
                        href={link.href}
                        class='text-sm text-slate-500 transition-colors hover:text-blue-500 dark:text-slate-400 dark:hover:text-white'
                        {...(isExternal ? { target: '_blank', rel: 'noopener noreferrer' } : {})}
                      >
                        {link.name}
                        {isExternal && (
                          <span class='sr-only'> (opens in a new tab)</span>
                        )}
                      </a>
                    </li>
                  )
                })}
              </ul>
            </div>
          ))
        }
      </div>
    </div>

    <!-- Bottom Section -->
    <div
      class='mt-20 flex flex-col items-center justify-between gap-6 border-t border-dashed border-slate-200 pt-10 md:flex-row dark:border-slate-800'
    >
      <a
        href='https://discord.gg/midudev'
        target='_blank'
        rel='noopener noreferrer'
        class='group/community flex flex-col items-center gap-2 md:items-start'
      >
        <p
          class='text-sm font-bold text-slate-900 transition-colors group-hover/community:text-blue-500 dark:text-white dark:group-hover/community:text-blue-400'
        >
          Join our community!
        </p>
        <p
          class='max-w-[200px] text-center text-xs text-slate-500 md:text-left'
        >
          Contributing animations or fixing bugs is the best way to support the
          project.
        </p>
      </a>

      <div class='flex flex-col items-center gap-4 md:items-end'>
        <div class='flex items-center gap-2 text-sm text-slate-500'>
          <span>Created with</span>
          <span class='animate-pulse text-red-500'>❤️</span>
          <span>by</span>
          <a
            href='https://x.com/midudev'
            target='_blank'
            rel='noopener noreferrer'
            class='font-bold text-slate-900 transition-all hover:scale-105 hover:text-blue-500 dark:text-white'
          >
            midudev
          </a>
          <span>and friends</span>
        </div>
        <p
          class='text-[10px] tracking-widest whitespace-nowrap text-slate-400 uppercase'
        >
          © {currentYear} Tailwind Animations • MIT License
        </p>
      </div>
    </div>
  </div>
</footer>
```

## File: `midudev-tailwind-animations-ceed187/web/src/components/layout/Header.astro`
```
---
import Logo from '@components/ui/Logo.astro'
import Github from '@components/icons/github.astro'
import ToggleTheme from '@components/ui/ToggleTheme.astro'
import Menu from '@components/icons/menu.astro'
import Enlace from '@components/ui/Enlace.astro'
---

<!-- Todo el header completo el componente y sus configuraciones -->

<style>
  .header-scroll {
    --header-opacity: 0;
    background: rgb(255 255 255 / calc(var(--header-opacity) * 0.8));
    border-color: rgb(226 232 240 / var(--header-opacity));
    backdrop-filter: blur(calc(var(--header-opacity) * 4px));
  }

  :global(.dark) .header-scroll {
    background: rgb(15 23 42 / calc(var(--header-opacity) * 0.8));
    border-color: rgb(51 65 85 / var(--header-opacity));
  }

  .logo-scroll {
    --logo-opacity: 0;
    opacity: var(--logo-opacity);
    transform: translateY(calc((1 - var(--logo-opacity)) * 20px));
  }
</style>

<script>
  const btn = document.getElementById('menu-btn')
  const menu = document.getElementById('menu')

  if (btn && menu) {
    btn.addEventListener('click', () => {
      const menuOpen = menu.classList.toggle('hidden')
      btn.setAttribute('aria-expanded', String(!menuOpen))
    })

    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && !menu.classList.contains('hidden')) {
        menu.classList.add('hidden')
        btn.setAttribute('aria-expanded', 'false')
        btn.focus()
      }
    })
  }

  // Logo and header scroll visibility
  const logoContainer = document.getElementById('logo-container')
  const header = document.getElementById('header')

  const handleScroll = () => {
    const scrollY = window.scrollY

    // Progressive opacity based on scroll (0 to 100px)
    const progress = Math.min(scrollY / 100, 1)
    header?.style.setProperty('--header-opacity', String(progress))
    logoContainer?.style.setProperty('--logo-opacity', String(progress))
  }

  window.addEventListener('scroll', handleScroll)
</script>

<a
  href='#main-content'
  class='sr-only focus:not-sr-only focus:fixed focus:top-4 focus:left-4 focus:z-50 focus:rounded-lg focus:bg-blue-500 focus:px-4 focus:py-2 focus:text-white focus:outline-none'
>
  Skip to content
</a>

<header
  id='header'
  class='fixed z-20 w-screen border-b px-3 py-5 header-scroll'
  role='banner'
>
  <div class='mx-auto grid w-full max-w-6xl grid-cols-2 grid-cols-[auto_auto]'>
    <!-- Title of Web -->
    <div
      id='logo-container'
      class='flex items-center gap-1 sm:gap-2 logo-scroll'
    >
      <Logo
        class='aspect-square size-7 shrink-0 sm:size-9'
        iconClass='size-4 sm:size-6 animate-float-subtle'
      />
      <span
        class='text-2xl font-bold tracking-tight text-slate-900 sm:text-3xl dark:text-white'
        aria-hidden='true'
      >
        Tailwind <span class='text-blue-500'>Animations</span>
      </span>
    </div>

    <button
      id='menu-btn'
      aria-label='Abrir menú'
      aria-expanded='false'
      class='flex justify-end text-2xl lg:hidden'
    >
      <Menu class='size-7 self-end sm:size-8' />
    </button>

    <div
      id='menu'
      class='col-span-2 hidden h-fit gap-5 lg:col-span-1 lg:grid lg:grid-cols-[auto_auto]'
    >
      <!-- main navigation -->
      <nav
        class='my-3 flex flex-col gap-5 max-lg:text-center lg:flex-row lg:items-center lg:gap-6'
      >
        <div
          class='h-[2px] bg-gradient-to-r from-transparent via-slate-300 to-transparent dark:via-slate-800'
        >
        </div>
        <Enlace href='#animation-collection'>Animation Collection</Enlace>
        <Enlace href='#scroll-animations'>Scroll Animations</Enlace>
        <Enlace href='#scroll-view-timelines'>Scroll View Timelines</Enlace>
      </nav>

      <!-- Color Theme / GitHub -->
      <div
        id='menu-icons'
        class='mt-3 flex flex-row justify-center gap-4 lg:flex'
      >
        <ToggleTheme />

        <a
          aria-label='View website repository on GitHub'
          href='https://github.com/midudev/tailwind-animations'
          target='_blank'
          rel='noopener noreferrer'
          class='text-slate-400 transition-colors hover:text-slate-600 dark:hover:text-slate-200'
        >
          <Github class='size-7' />
        </a>
      </div>
    </div>
  </div>
</header>
```

## File: `midudev-tailwind-animations-ceed187/web/src/components/ui/Enlace.astro`
```
---
const { href, target = '_self', className = '' } = Astro.props
---

<!-- Este es un componente que utiliza el header para navegar fluidamente con sus enlaces -->

<a
  href={href}
  target={target}
  draggable='false'
  class='text-slate-600 transition-colors select-none hover:text-slate-900 dark:text-slate-400 dark:hover:text-slate-200'
  data-enlace
>
  <slot />
</a>

<script>
  document.addEventListener('click', (e) => {
    if (!e.target) return
    const link = (e.target as Element).closest('a[data-enlace]')
    if (!link) return

    const href = link.getAttribute('href')

    // If it's an in-page anchor like #temario, scroll to the element instead
    if (href && href.startsWith('#')) {
      e.preventDefault()
      const id = href.slice(1)
      const el =
        document.getElementById(id) || document.getElementsByName(id)[0]

      if (el) {
        // try to account for a fixed header
        const header = document.querySelector('header')
        const offset = header ? header.offsetHeight + 8 : 8
        const y = el.getBoundingClientRect().top + window.pageYOffset - offset

        window.scrollTo({ top: y, behavior: 'smooth' })
      } else {
        console.warn('Anchor target not found:', href)
      }
    }
    // External or normal links are handled by the browser
  })
</script>
```

## File: `midudev-tailwind-animations-ceed187/web/src/components/ui/Logo.astro`
```
---
interface Props {
  class?: string
  iconClass?: string
}

const { class: className, iconClass } = Astro.props
---

<div
  class:list={[
    'flex items-center justify-center rounded-xl bg-blue-500 shadow-lg shadow-blue-500/20 transition-all duration-300',
    className
  ]}
>
  <svg
    class:list={[
      'text-white drop-shadow-[0_1px_2px_rgba(30,58,138,0.5)]',
      iconClass
    ]}
    viewBox='0 0 24 24'
    fill='currentColor'
    aria-hidden='true'
  >
    <path d='M13 2L3 14h9l-1 8 10-10h-9l1-8z'></path>
  </svg>
</div>

<style is:global>
  @keyframes float-subtle {
    0%,
    100% {
      transform: translateY(0) scale(1);
      opacity: 0.95;
    }
    50% {
      transform: translateY(-2px) scale(1.02);
      opacity: 1;
    }
  }

  .animate-float-subtle {
    animation: float-subtle 4s ease-in-out infinite;
  }
</style>
```

## File: `midudev-tailwind-animations-ceed187/web/src/components/ui/ToggleTheme.astro`
```
---
import SunIcon from '../icons/sun.astro'
import MoonIcon from '../icons/moon.astro'
---

<button
  id='theme-toggle'
  class='inline-flex cursor-pointer text-slate-400 transition-colors hover:text-slate-600 dark:hover:text-slate-200'
  aria-label='Toggle theme'
>
  <SunIcon id='sun-icon' class='hidden size-6 dark:block' />
  <MoonIcon id='moon-icon' class='block size-6 dark:hidden' />
</button>

<script>
  const handleToggleClick = () => {
    const element = document.documentElement
    element.classList.toggle('dark')

    const isDark = element.classList.contains('dark')
    localStorage.setItem('theme', isDark ? 'dark' : 'light')
  }

  const $toggle = document.getElementById('theme-toggle')

  if ($toggle) {
    $toggle.addEventListener('click', handleToggleClick)
  }
</script>
```

## File: `midudev-tailwind-animations-ceed187/web/src/data/theme.js`
```javascript
export const theme = {
  animation: {
    'blurred-fade-in': 'blurred-fade-in 0.9s ease-in-out both',
    'fade-in': 'fade-in 0.6s ease-in both',
    'fade-out': 'fade-out 0.6s ease-out both',
    'slide-in-top': 'slide-in-top 0.6s ease-out both',
    'slide-in-bottom': 'slide-in-bottom 0.6s ease-out both',
    'slide-out-top': 'slide-out-top 0.6s ease-out both',
    'slide-out-bottom': 'slide-out-bottom 0.6s ease-out both',
    'zoom-in': 'zoom-in 0.6s ease-out both',
    'zoom-out': 'zoom-out 0.6s ease-out both',
    'rotate-90': 'rotate-90 1s ease-in-out both',
    'rotate-180': 'rotate-180 1s ease-in-out both',
    'rotate-360': 'rotate-360 1s linear both',
    'flip-horizontal': 'flip-horizontal 1s ease-in-out both',
    'flip-vertical': 'flip-vertical 1s ease-in-out both',
    bouncing: 'bouncing 1s ease-in-out both',
    swing: 'swing 1s ease-in-out both',
    wobble: 'wobble 1s ease-in-out both',
    pulsing: 'pulsing 1s ease-in-out both',
    shake: 'shake 0.5s ease-in-out both',
    tada: 'tada 1s ease-in-out both',
    jump: 'jump 1s ease-in-out both',
    hang: 'hang 1s ease-in-out both',
    'roll-in': 'roll-in 1s ease-in-out both',
    'roll-out': 'roll-out 1s ease-in-out both',
    float: 'float 1s ease-in-out both',
    sink: 'sink 1s ease-in-out both',
    flash: 'flash 1s ease-in-out both',
    jiggle: 'jiggle 0.5s ease-in-out both',
    'rubber-band': 'rubber-band 1s ease-in-out both',
    scale: 'scale 0.6s ease-out both',
    'slide-in-left': 'slide-in-left 0.6s ease-out both',
    'slide-in-right': 'slide-in-right 0.6s ease-out both',
    'slide-out-left': 'slide-out-left 0.6s ease-out both',
    'slide-out-right': 'slide-out-right 0.6s ease-out both',
    'spin-clockwise': 'spin-clockwise 0.6s linear both',
    'spin-counter-clockwise': 'spin-counter-clockwise 0.6s linear both',
    'flip-x': 'flip-x 0.6s ease-out both',
    'flip-y': 'flip-y 0.6s ease-out both',
    blink: 'blink 0.5s both',
    pop: 'pop 0.6s ease-out both',
    'expand-horizontally': 'expand-horizontally 0.6s ease-out both',
    'contract-horizontally': 'contract-horizontally 0.6s ease-out both',
    'expand-vertically': 'expand-vertically 0.6s ease-out both',
    'contract-vertically': 'contract-vertically 0.6s ease-out both',
    'fade-in-up': 'fade-in-up 0.6s ease-in-out both',
    'fade-in-down': 'fade-in-down 0.6s ease-in-out both',
    'fade-in-left': 'fade-in-left 0.6s ease-in-out both',
    'fade-in-right': 'fade-in-right 0.6s ease-in-out both',
    'fade-out-up': 'fade-out-up 0.6s ease-out both',
    'fade-out-down': 'fade-out-down 0.6s ease-out both',
    'fade-out-left': 'fade-out-left 0.6s ease-out both',
    'fade-out-right': 'fade-out-right 0.6s ease-out both',
    sway: 'sway 0.6s ease-out both',
    'flip-in-x': 'flip-in-x 0.6s ease-out both',
    'flip-in-y': 'flip-in-y 0.6s ease-out both',
    'flip-out-x': 'flip-out-x 0.6s ease-out both',
    'flip-out-y': 'flip-out-y 0.6s ease-out both',
    'rotate-in': 'rotate-in 0.6s ease-out both',
    'rotate-out': 'rotate-out 0.6s ease-out both',
    'slide-rotate-in': 'slide-rotate-in 0.6s ease-out both',
    'slide-rotate-out': 'slide-rotate-out 0.6s ease-out both',
    heartbeat: 'heartbeat 0.6s ease-out both',
    'horizontal-vibration': 'horizontal-vibration 0.3s linear infinite both',
    'rotational-wave': 'rotational-wave 2s ease-in-out infinite both',
    skew: 'skew 0.5s ease-in-out both',
    'skew-right': 'skew-right 0.5s ease-in-out both',
    'vertical-bounce': 'vertical-bounce 0.6s ease-in-out both',
    'horizontal-bounce': 'horizontal-bounce 0.6s ease-in-out both',
    tilt: 'tilt 0.6s ease-in-out both',
    squeeze: 'squeeze 0.6s ease-in-out both',
    'slide-up-fade': 'slide-up-fade 0.6s ease-out both',
    'bounce-fade-in': 'bounce-fade-in 0.6s ease-out both',
    'swing-drop-in': 'swing-drop-in 0.6s ease-out both',
    'pulse-fade-in': 'pulse-fade-in 0.6s ease-out both',
    'impulse-rotation-right': 'impulse-rotation-right 1s ease-in-out both',
    'impulse-rotation-left': 'impulse-rotation-left 1s ease-in-out both',
    dancing: 'dancing 1s ease-in-out both',
    pulse: 'pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite',
    jelly: 'jelly 1s ease-out forwards'
  },
  keyframes: {
    'fade-in': {
      '0%': { opacity: '0' },
      '100%': { opacity: '1' }
    },
    'fade-out': {
      '0%': { opacity: '1' },
      '100%': { opacity: '0' }
    },
    'slide-in-top': {
      '0%': { transform: 'translateY(-20px)' },
      '100%': { transform: 'translateY(0)' }
    },
    'slide-in-bottom': {
      '0%': { transform: 'translateY(20px)' },
      '100%': { transform: 'translateY(0)' }
    },
    'slide-out-top': {
      '0%': { transform: 'translateY(0)' },
      '100%': { transform: 'translateY(-20px)' }
    },
    'slide-out-bottom': {
      '0%': { transform: 'translateY(0)' },
      '100%': { transform: 'translateY(20px)' }
    },
    'zoom-in': {
      '0%': { opacity: '0', transform: 'scale(.5)' },
      '100%': { opacity: '1', transform: 'scale(1)' }
    },
    'zoom-out': {
      '0%': { opacity: '1', transform: 'scale(1)' },
      '100%': { opacity: '0', transform: 'scale(.5)' }
    },
    'rotate-90': {
      '0%': { transform: 'rotate(0deg)' },
      '100%': { transform: 'rotate(90deg)' }
    },
    'rotate-180': {
      '0%': { transform: 'rotate(0deg)' },
      '100%': { transform: 'rotate(180deg)' }
    },
    'rotate-360': {
      '0%': { transform: 'rotate(0deg)' },
      '100%': { transform: 'rotate(360deg)' }
    },
    'flip-horizontal': {
      '0%': { transform: 'rotateY(0deg)' },
      '100%': { transform: 'rotateY(180deg)' }
    },
    'flip-vertical': {
      '0%': { transform: 'rotateX(0deg)' },
      '100%': { transform: 'rotateX(180deg)' }
    },
    bouncing: {
      '0%': { transform: 'translateY(0)' },
      '50%': { transform: 'translateY(-10px)' },
      '100%': { transform: 'translateY(0)' }
    },
    swing: {
      '0%': { transform: 'rotate(0deg)' },
      '50%': { transform: 'rotate(15deg)' },
      '100%': { transform: 'rotate(0deg)' }
    },
    wobble: {
      '0%': { transform: 'translateX(0)' },
      '15%': { transform: 'translateX(-20px)' },
      '30%': { transform: 'translateX(20%)' },
      '45%': { transform: 'translateX(-15%)' },
      '60%': { transform: 'translateX(20px)' },
      '75%': { transform: 'translateX(-5%)' },
      '100%': { transform: 'translateX(0)' }
    },
    pulse: {
      '0%, 100%': { opacity: '1' },
      '50%': { opacity: '0.5' }
    },
    pulsing: {
      '0%': { transform: 'scale(1)' },
      '50%': { transform: 'scale(1.1)' },
      '100%': { transform: 'scale(1)' }
    },
    shake: {
      '0%': { transform: 'translateX(0)' },
      '25%': { transform: 'translateX(-10px)' },
      '50%': { transform: 'translateX(10px)' },
      '75%': { transform: 'translateX(-10px)' },
      '100%': { transform: 'translateX(0)' }
    },
    tada: {
      '0%': { transform: 'scale(1)' },
      '10%': { transform: 'scale(0.9) rotate(-3deg)' },
      '20%': { transform: 'scale(0.9) rotate(-3deg)' },
      '30%': { transform: 'scale(1.1) rotate(3deg)' },
      '40%': { transform: 'scale(1.1) rotate(-3deg)' },
      '50%': { transform: 'scale(1.1) rotate(3deg)' },
      '60%': { transform: 'scale(1.1) rotate(-3deg)' },
      '70%': { transform: 'scale(1.1) rotate(3deg)' },
      '80%': { transform: 'scale(1.1) rotate(-3deg)' },
      '90%': { transform: 'scale(1.1) rotate(3deg)' },
      '100%': { transform: 'scale(1) rotate(0)' }
    },
    jump: {
      '0%': { transform: 'translateY(0)' },
      '50%': { transform: 'translateY(-20px)' },
      '100%': { transform: 'translateY(0)' }
    },
    hang: {
      '0%': { transform: 'translateY(-20px)' },
      '50%': { transform: 'translateY(0)' },
      '100%': { transform: 'translateY(-20px)' }
    },
    'roll-in': {
      '0%': { transform: 'translateX(-20px) rotate(-120deg)' },
      '100%': { transform: 'translateX(0) rotate(0)' }
    },
    'roll-out': {
      '0%': { transform: 'translateX(0) rotate(0)' },
      '100%': { transform: 'translateX(20px) rotate(120deg)' }
    },
    float: {
      '0%': { transform: 'translateY(0)' },
      '50%': { transform: 'translateY(-10px)' },
      '100%': { transform: 'translateY(0)' }
    },
    sink: {
      '0%': { transform: 'translateY(-10px)' },
      '50%': { transform: 'translateY(0)' },
      '100%': { transform: 'translateY(-10px)' }
    },
    flash: {
      '0%': { opacity: '1' },
      '50%': { opacity: '0' },
      '100%': { opacity: '1' }
    },
    jiggle: {
      '0%': { transform: 'rotate(-3deg)' },
      '50%': { transform: 'rotate(3deg)' },
      '100%': { transform: 'rotate(-3deg)' }
    },
    'rubber-band': {
      '0%': { transform: 'scale(1)' },
      '30%': { transform: 'scale(1.25)' },
      '40%': { transform: 'scale(0.75)' },
      '50%': { transform: 'scale(1.15)' },
      '65%': { transform: 'scale(0.95)' },
      '75%': { transform: 'scale(1.05)' },
      '100%': { transform: 'scale(1)' }
    },
    scale: {
      '0%': { transform: 'scale(1)' },
      '100%': { transform: 'scale(1.10)' }
    },
    'slide-in-left': {
      '0%': { transform: 'translateX(-20px)' },
      '100%': { transform: 'translateX(0)' }
    },
    'slide-in-right': {
      '0%': { transform: 'translateX(20px)' },
      '100%': { transform: 'translateX(0)' }
    },
    'slide-out-left': {
      '0%': { transform: 'translateX(0)' },
      '100%': { transform: 'translateX(-20px)' }
    },
    'slide-out-right': {
      '0%': { transform: 'translateX(0)' },
      '100%': { transform: 'translateX(20px)' }
    },
    'spin-clockwise': {
      '0%': { transform: 'rotate(0deg)' },
      '100%': { transform: 'rotate(360deg)' }
    },
    'spin-counter-clockwise': {
      '0%': { transform: 'rotate(0deg)' },
      '100%': { transform: 'rotate(-360deg)' }
    },
    'flip-x': {
      '0%': { transform: 'scaleX(1)' },
      '50%': { transform: 'scaleX(-1)' },
      '100%': { transform: 'scaleX(1)' }
    },
    'flip-y': {
      '0%': { transform: 'scaleY(1)' },
      '50%': { transform: 'scaleY(-1)' },
      '100%': { transform: 'scaleY(1)' }
    },
    blink: {
      '0%': { opacity: '0' },
      '100%': { opacity: '1' }
    },
    pop: {
      '0%': { transform: 'scale(1)' },
      '50%': { transform: 'scale(1.1)' },
      '100%': { transform: 'scale(1)' }
    },
    'expand-horizontally': {
      '0%': { transform: 'scaleX(0)' },
      '100%': { transform: 'scaleX(1)' }
    },
    'contract-horizontally': {
      '0%': { transform: 'scaleX(1)' },
      '100%': { transform: 'scaleX(0)' }
    },
    'expand-vertically': {
      '0%': { transform: 'scaleY(0)' },
      '100%': { transform: 'scaleY(1)' }
    },
    'contract-vertically': {
      '0%': { transform: 'scaleY(1)' },
      '100%': { transform: 'scaleY(0)' }
    },
    'fade-in-up': {
      '0%': { opacity: '0', transform: 'translateY(20px)' },
      '100%': { opacity: '1', transform: 'translateY(0)' }
    },
    'fade-in-down': {
      '0%': { opacity: '0', transform: 'translateY(-20px)' },
      '100%': { opacity: '1', transform: 'translateY(0)' }
    },
    'fade-in-left': {
      '0%': { opacity: '0', transform: 'translateX(20px)' },
      '100%': { opacity: '1', transform: 'translateX(0)' }
    },
    'fade-in-right': {
      '0%': { opacity: '0', transform: 'translateX(-20px)' },
      '100%': { opacity: '1', transform: 'translateX(0)' }
    },
    'fade-out-up': {
      '0%': { opacity: '1', transform: 'translateY(0)' },
      '100%': { opacity: '0', transform: 'translateY(-20px)' }
    },
    'fade-out-down': {
      '0%': { opacity: '1', transform: 'translateY(0)' },
      '100%': { opacity: '0', transform: 'translateY(20px)' }
    },
    'fade-out-left': {
      '0%': { opacity: '1', transform: 'translateX(0)' },
      '100%': { opacity: '0', transform: 'translateX(-20px)' }
    },
    'fade-out-right': {
      '0%': { opacity: '1', transform: 'translateX(0)' },
      '100%': { opacity: '0', transform: 'translateX(20px)' }
    },
    sway: {
      '0%': { transform: 'rotate(0deg)' },
      '50%': { transform: 'rotate(15deg)' },
      '100%': { transform: 'rotate(0deg)' }
    },
    'flip-in-x': {
      '0%': { opacity: '0', transform: 'rotateY(90deg)' },
      '100%': { opacity: '1', transform: 'rotateY(0deg)' }
    },
    'flip-in-y': {
      '0%': { opacity: '0', transform: 'rotateX(90deg)' },
      '100%': { opacity: '1', transform: 'rotateX(0deg)' }
    },
    'flip-out-x': {
      '0%': { opacity: '1', transform: 'rotateY(0deg)' },
      '100%': { opacity: '0', transform: 'rotateY(90deg)' }
    },
    'flip-out-y': {
      '0%': { opacity: '1', transform: 'rotateX(0deg)' },
      '100%': { opacity: '0', transform: 'rotateX(90deg)' }
    },
    'rotate-in': {
      '0%': { opacity: '0', transform: 'rotate(-90deg)' },
      '100%': { opacity: '1', transform: 'rotate(0deg)' }
    },
    'rotate-out': {
      '0%': { opacity: '1', transform: 'rotate(0deg)' },
      '100%': { opacity: '0', transform: 'rotate(90deg)' }
    },
    'slide-rotate-in': {
      '0%': { opacity: '0', transform: 'translateX(-20px) rotate(-90deg)' },
      '100%': { opacity: '1', transform: 'translateX(0) rotate(0deg)' }
    },
    'slide-rotate-out': {
      '0%': { opacity: '1', transform: 'translateX(0) rotate(0deg)' },
      '100%': { opacity: '0', transform: 'translateX(20px) rotate(90deg)' }
    },
    heartbeat: {
      '0%': { transform: 'scale(1)' },
      '25%': { transform: 'scale(1.1)' },
      '50%': { transform: 'scale(1)' },
      '75%': { transform: 'scale(0.9)' },
      '100%': { transform: 'scale(1)' }
    },
    'blurred-fade-in': {
      '0%': { filter: 'blur(5px)', opacity: '0' },
      '100%': { filter: 'blur(0)', opacity: '1' }
    },
    'horizontal-vibration': {
      '0%': { transform: 'translateX(0)' },
      '25%': { transform: 'translateX(5px)' },
      '50%': { transform: 'translateX(-5px)' },
      '75%': { transform: 'translateX(5px)' },
      '100%': { transform: 'translateX(0)' }
    },
    'rotational-wave': {
      '0%': { transform: 'rotate(0deg)' },
      '25%': { transform: 'rotate(10deg)' },
      '50%': { transform: 'rotate(-10deg)' },
      '75%': { transform: 'rotate(10deg)' },
      '100%': { transform: 'rotate(0deg)' }
    },
    skew: {
      '0%': { transform: 'skew(0deg)' },
      '100%': { transform: 'skew(20deg)' }
    },
    'skew-right': {
      '0%': { transform: 'skew(0deg)' },
      '100%': { transform: 'skew(-20deg)' }
    },
    'vertical-bounce': {
      '0%, 100%': { transform: 'translateY(0)' },
      '50%': { transform: 'translateY(-20px)' }
    },
    'horizontal-bounce': {
      '0%, 100%': { transform: 'translateX(0)' },
      '50%': { transform: 'translateX(20px)' }
    },
    tilt: {
      '0%': { transform: 'rotateY(0deg)' },
      '50%': { transform: 'rotateY(20deg)' },
      '100%': { transform: 'rotateY(0deg)' }
    },
    squeeze: {
      '0%, 100%': { transform: 'scale(1, 1)' },
      '50%': { transform: 'scale(1.1, 0.9)' }
    },
    'slide-up-fade': {
      '0%': { opacity: '0', transform: 'translateY(50px)' },
      '100%': { opacity: '1', transform: 'translateY(0)' }
    },
    'bounce-fade-in': {
      '0%': { transform: 'scale(0.5)', opacity: '0' },
      '100%': { transform: 'scale(1)', opacity: '1' }
    },
    'swing-drop-in': {
      '0%': { transform: 'rotate(-30deg) translateY(-50px)', opacity: '0' },
      '100%': { transform: 'rotate(0deg) translateY(0)', opacity: '1' }
    },
    'pulse-fade-in': {
      '0%': { transform: 'scale(0.9)', opacity: '0' },
      '50%': { transform: 'scale(1.05)', opacity: '0.5' },
      '100%': { transform: 'scale(1)', opacity: '1' }
    },
    'impulse-rotation-right': {
      '0%': { transform: 'rotate(0deg)' },
      '50%': { transform: 'rotate(-40deg)' },
      '100%': { transform: 'rotate(360deg)' }
    },
    'impulse-rotation-left': {
      '0%': { transform: 'rotate(0deg)' },
      '50%': { transform: 'rotate(40deg)' },
      '100%': { transform: 'rotate(-360deg)' }
    },
    dancing: {
      '0%': { transform: 'skew(0deg)' },
      '25%': { transform: 'skew(-40deg)' },
      '50%': { transform: 'skew(40deg)' },
      '75%': { transform: 'skew(-40deg)' },
      '100%': { transform: 'skew(0deg)' }
    },
    jelly: {
      '0%': { transform: 'scale(1, 1)' },
      '20%': { transform: 'scale(1.25, 0.75)' },
      '40%': { transform: 'scale(0.75, 1.25)' },
      '60%': { transform: 'scale(1.15, 0.85)' },
      '75%': { transform: 'scale(0.95, 1.05)' },
      '85%': { transform: 'scale(1.05, 0.95)' },
      '92%': { transform: 'scale(1, 1.02)' },
      '100%': { transform: 'scale(1, 1)' }
    }
  },
  animationDelay: {
    none: '0ms',
    0: '0ms',
    100: '100ms',
    150: '150ms',
    200: '200ms',
    250: '250ms',
    300: '300ms',
    400: '400ms',
    500: '500ms',
    700: '700ms',
    800: '800ms',
    900: '900ms',
    1000: '1000ms'
  },
  animationDuration: {
    none: '0ms',
    slower: '500ms',
    slow: '400ms',
    normal: '300ms',
    fast: '200ms',
    faster: '100ms',
    0: '0ms',
    100: '100ms',
    150: '150ms',
    200: '200ms',
    250: '250ms',
    300: '300ms',
    400: '400ms',
    500: '500ms',
    700: '700ms',
    800: '800ms',
    900: '900ms',
    1000: '1000ms'
  },
  animationSteps: {
    none: '0',
    retro: '8',
    normal: '16',
    modern: '24'
  },
  animationIterationCount: {
    none: '0',
    once: '1',
    twice: '2',
    thrice: '3',
    infinite: 'infinite'
  },
  animationFillMode: {
    none: 'none',
    forwards: 'forwards',
    backwards: 'backwards',
    both: 'both'
  },
  animationCubicBezier: {
    'sine-in': 'cubic-bezier(0.12,0,0.39,0)',
    'sine-out': 'cubic-bezier(0.39,0.575,0.565,1)',
    'sine-in-out': 'cubic-bezier(0.445,0.05,0.55,0.95)',
    'quad-in': 'cubic-bezier(0.55,0.085,0.68,0.53)',
    'quad-out': 'cubic-bezier(0.25,0.46,0.45,0.94)',
    'quad-in-out': 'cubic-bezier(0.455,0.03,0.515,0.955)',
    'cubic-in': 'cubic-bezier(0.55,0.055,0.675,0.19)',
    'cubic-out': 'cubic-bezier(0.215,0.61,0.355,1)',
    'cubic-in-out': 'cubic-bezier(0.645,0.045,0.355,1)',
    'quart-in': 'cubic-bezier(0.895,0.03,0.685,0.22)',
    'quart-out': 'cubic-bezier(0.165,0.84,0.44,1)',
    'quart-in-out': 'cubic-bezier(0.77,0,0.175,1)',
    'quint-in': 'cubic-bezier(0.755,0.05,0.855,0.06)',
    'quint-out': 'cubic-bezier(0.23,1,0.32,1)',
    'quint-in-out': 'cubic-bezier(0.86,0,0.07,1)',
    'expo-in': 'cubic-bezier(0.95,0.05,0.795,0.035)',
    'expo-out': 'cubic-bezier(0.19,1,0.22,1)',
    'expo-in-out': 'cubic-bezier(1,0,0,1)',
    'circ-in': 'cubic-bezier(0.6,0.04,0.98,0.335)',
    'circ-out': 'cubic-bezier(0.075,0.82,0.165,1)',
    'circ-in-out': 'cubic-bezier(0.785,0.135,0.15,0.86)',
    'back-in': 'cubic-bezier(0.6,-0.28,0.735,0.045)',
    'back-out': 'cubic-bezier(0.175,0.885,0.32,1.275)',
    'back-in-out': 'cubic-bezier(0.68,-0.55,0.265,1.55)'
  },
  animationRange: {
    normal: 'normal',
    cover: 'cover',
    contain: 'contain',
    entry: 'entry',
    exit: 'exit',
    gradual: '10% 90%',
    moderate: '20% 80%',
    brisk: '30% 70%',
    rapid: '40% 60%'
  },
  timeline: {
    none: 'none',
    auto: 'auto',
    single: '--single-timeline',
    scroll: 'scroll()',
    'scroll-x': 'scroll(x)',
    'scroll-y': 'scroll(y)',
    'scroll-block': 'scroll(block)',
    'scroll-inline': 'scroll(inline)',
    view: 'view()',
    'view-x': 'view(x)',
    'view-y': 'view(y)',
    'view-block': 'view(block)',
    'view-inline': 'view(inline)'
  },
  scrollTimeline: {
    single: '--single-timeline'
  },
  viewTimeline: {
    single: '--single-timeline'
  },
  scrollTimelineAxis: {
    block: 'block',
    inline: 'inline',
    x: 'x',
    y: 'y'
  },
  viewTimelineAxis: {
    block: 'block',
    inline: 'inline',
    x: 'x',
    y: 'y'
  },
  scrollAnimation: {
    single: '--single-timeline'
  },
  viewAnimation: {
    single: '--single-timeline'
  }
}
```

## File: `midudev-tailwind-animations-ceed187/web/src/layouts/Layout.astro`
```
---
import '@fontsource-variable/geist-mono'
import '../styles/index.css'

interface Props {
  title: string
}

const { title } = Astro.props
const description =
  'Tailwind CSS plugin to add stunning animations to your website. Zero configuration, pure performance.'
const siteUrl = 'https://tailwind-animations.com'
const ogImage = `${siteUrl}/og.jpg`
---

<!doctype html>
<html lang='en'>
  <head>
    <meta charset='UTF-8' />
    <meta name='description' content={description} />
    <meta name='viewport' content='width=device-width' />
    <link rel='icon' type='image/svg+xml' href='/favicon.svg' />
    <link rel='canonical' href={siteUrl} />
    <meta name='theme-color' content='#0099ff' />

    <!-- Open Graph -->
    <meta property='og:type' content='website' />
    <meta property='og:url' content={siteUrl} />
    <meta property='og:title' content={title} />
    <meta property='og:description' content={description} />
    <meta property='og:image' content={ogImage} />

    <!-- Twitter -->
    <meta name='twitter:card' content='summary_large_image' />
    <meta name='twitter:title' content={title} />
    <meta name='twitter:description' content={description} />
    <meta name='twitter:image' content={ogImage} />

    <title>{title}</title>

    <script is:inline>
      const getThemePreference = () => {
        if (
          typeof localStorage !== 'undefined' &&
          localStorage.getItem('theme')
        ) {
          return localStorage.getItem('theme')
        }
        return 'dark'
      }

      const isDark = getThemePreference() === 'dark'
      document.documentElement.classList.toggle('dark', isDark)
    </script>
  </head>
  <body
    class='relative h-fit w-full bg-white text-slate-900 transition-colors duration-300 dark:bg-[#050505] dark:text-slate-50'
  >
    <slot />
  </body>
</html>

<style is:global>
  @media (prefers-reduced-motion: reduce) {
    *,
    *::before,
    *::after {
      animation-duration: 0.01ms !important;
      animation-iteration-count: 1 !important;
      transition-duration: 0.01ms !important;
      scroll-behavior: auto !important;
    }
  }
</style>
```

## File: `midudev-tailwind-animations-ceed187/web/src/pages/index.astro`
```
---
import Layout from '@layouts/Layout.astro'

import pkg from '../../../package.json'
import { theme } from '../data/theme.js'

/*  
Las importaciones, se han organizado de la siguiente forma: 
1. importacion de code.
2. importaciones de iconos.
3. importaciones de componentes UI.
4. importaciones de layout.
*/

import { Code } from 'astro:components'
import CopyIcon from '@components/icons/copy.astro'
import Github from '@components/icons/github.astro'

import Logo from '@components/ui/Logo.astro'
import ToggleTheme from '@components/ui/ToggleTheme.astro'

// Importacion de componentes de layout
import Footer from '@components/layout/Footer.astro'
import Header from '@components/layout/Header.astro'

const { animation, animationDuration, animationSteps, animationDelay } = theme
const { version } = pkg

const POPULAR_ANIMATIONS = [
  'fade-in',
  'blurred-fade-in',
  'zoom-in',
  'slide-in-top',
  'bouncing',
  'pulsing',
  'shake',
  'tada',
  'jelly',
  'flip-horizontal',
  'swing',
  'wobble',
  'rotate-360',
  'fade-in-up',
  'slide-in-left',
  'zoom-out',
  'fade-in-down',
  'slide-in-bottom',
  'slide-in-right'
]

const sortedAnimations = Object.keys(animation).sort((a, b) => {
  const indexA = POPULAR_ANIMATIONS.indexOf(a)
  const indexB = POPULAR_ANIMATIONS.indexOf(b)

  if (indexA === -1 && indexB === -1) return a.localeCompare(b)
  if (indexA === -1) return 1
  if (indexB === -1) return -1
  return indexA - indexB
})

const packageManagers = [
  {
    name: 'npm',
    icon: `<svg xmlns='http://www.w3.org/2000/svg' width='1em' height='1em' viewBox='0 0 32 32'><path fill='#c12127' d='M2 2h28v28H2'/><path fill='#fff' d='M7.25 7.25h17.5v17.5h-3.5v-14H16v14H7.25'/></svg>`,
    command: 'npm install tailwind-animations'
  },
  {
    name: 'pnpm',
    icon: `<svg xmlns='http://www.w3.org/2000/svg' width='1em' height='1em' viewBox='0 0 32 32'><path fill='#f9ad00' d='M30 10.75h-8.749V2H30Zm-9.626 0h-8.75V2h8.75Zm-9.625 0H2V2h8.749ZM30 20.375h-8.749v-8.75H30Z'/><path fill='#4e4e4e' d='M20.374 20.375h-8.75v-8.75h8.75Zm0 9.625h-8.75v-8.75h8.75ZM30 30h-8.749v-8.75H30Zm-19.251 0H2v-8.75h8.749Z'/></svg>`,
    command: 'pnpm add tailwind-animations'
  },
  {
    name: 'yarn',
    icon: `<svg xmlns='http://www.w3.org/2000/svg' width='1em' height='1em' viewBox='0 0 32 32'><path fill='#2188b6' d='M28.208 24.409a10.5 10.5 0 0 0-3.959 1.822a23.7 23.7 0 0 1-5.835 2.642a1.63 1.63 0 0 1-.983.55a62 62 0 0 1-6.447.577c-1.163.009-1.876-.3-2.074-.776a1.573 1.573 0 0 1 .866-2.074a4 4 0 0 1-.514-.379c-.171-.171-.352-.514-.406-.388c-.225.55-.343 1.894-.947 2.5c-.83.839-2.4.559-3.328.072c-1.019-.541.072-1.813.072-1.813a.73.73 0 0 1-.992-.343a4.85 4.85 0 0 1-.667-2.949a5.37 5.37 0 0 1 1.749-2.895a9.3 9.3 0 0 1 .658-4.4a10.45 10.45 0 0 1 3.165-3.661S6.628 10.747 7.35 8.817c.469-1.262.658-1.253.812-1.308a3.6 3.6 0 0 0 1.452-.857a5.27 5.27 0 0 1 4.41-1.7S15.2 1.4 16.277 2.09a18.4 18.4 0 0 1 1.533 2.886s1.281-.748 1.425-.469a11.33 11.33 0 0 1 .523 6.132a14 14 0 0 1-2.6 5.411c-.135.225 1.551.938 2.615 3.887c.983 2.7.108 4.96.262 5.212c.027.045.036.063.036.063s1.127.09 3.391-1.308a8.5 8.5 0 0 1 4.277-1.604a1.081 1.081 0 0 1 .469 2.11Z'/></svg>`,
    command: 'yarn add tailwind-animations'
  },
  {
    name: 'bun',
    icon: `<svg xmlns='http://www.w3.org/2000/svg' width='1em' height='1em' viewBox='0 0 32 32'><path fill='#fbf0df' d='M29 17c0 5.65-5.82 10.23-13 10.23S3 22.61 3 17c0-3.5 2.24-6.6 5.66-8.44S14.21 4.81 16 4.81s3.32 1.54 7.34 3.71C26.76 10.36 29 13.46 29 17'/><path fill='none' stroke='#000' d='M16 27.65c7.32 0 13.46-4.65 13.46-10.65c0-3.72-2.37-7-5.89-8.85c-1.39-.75-2.46-1.41-3.37-2l-1.13-.69A6.14 6.14 0 0 0 16 4.35a6.9 6.9 0 0 0-3.3 1.23c-.42.24-.86.51-1.32.8c-.87.54-1.83 1.13-3 1.73C4.91 10 2.54 13.24 2.54 17c0 6 6.14 10.65 13.46 10.65Z'/><ellipse cx='21.65' cy='18.62' fill='#febbd0' rx='2.17' ry='1.28'/><ellipse cx='10.41' cy='18.62' fill='#febbd0' rx='2.17' ry='1.28'/><path fill-rule='evenodd' d='M11.43 18.11a2 2 0 1 0-2-2.05a2.05 2.05 0 0 0 2 2.05m9.2 0a2 2 0 1 0-2-2.05a2 2 0 0 0 2 2.05'/><path fill='#fff' fill-rule='evenodd' d='M10.79 16.19a.77.77 0 1 0-.76-.77a.76.76 0 0 0 .76.77m9.2 0a.77.77 0 1 0 0-1.53a.77.77 0 0 0 0 1.53'/><path fill='#b71422' stroke='#000' stroke-width='.75' d='M18.62 19.67a3.3 3.3 0 0 1-1.09 1.75a2.48 2.48 0 0 1-1.5.69a2.53 2.53 0 0 1-1.5-.69a3.28 3.28 0 0 1-1.08-1.75a.26.26 0 0 1 .29-.3h4.58a.27.27 0 0 1 .3.3Z'/><path fill='#ccbea7' fill-rule='evenodd' d='M14.93 5.75a6.1 6.1 0 0 1-2.09 4.62c-.1.09 0 .27.11.22c1.25-.49 2.94-1.94 2.23-4.88c-.03-.15-.25-.11-.25.04m.85 0a6 6 0 0 1 .57 5c0 .13.12.24.21.13c.83-1 1.54-3.11-.59-5.31c-.1-.11-.27.04-.19.17Zm1-.06a6.1 6.1 0 0 1 2.53 4.38c0 .14.21.17.24 0c.34-1.3.15-3.51-2.66-4.66c-.12-.02-.21.18-.09.27ZM9.94 9.55a6.27 6.27 0 0 0 3.89-3.33c.07-.13.28-.08.25.07c-.64 3-2.79 3.59-4.13 3.51c-.14-.01-.14-.21-.01-.25'/></svg>`,
    command: 'bun add tailwind-animations'
  },
  {
    name: 'deno',
    icon: `<svg xmlns='http://www.w3.org/2000/svg' width='1em' height='1em' viewBox='0 0 32 32'><path fill-rule='evenodd' d='M4.45 21.34A12.5 12.5 0 0 1 3.27 16a12 12 0 0 1 .09-1.46a11 11 0 0 1 .24-1.42a12.75 12.75 0 0 1 9.73-9.57A13 13 0 0 1 16 3.27h1a12.73 12.73 0 0 1 11.57 10.5a13 13 0 0 1 .16 2.23v1a12.6 12.6 0 0 1-3.3 7.61a6.62 6.62 0 0 1-4.7 2.06a4.68 4.68 0 0 1-2.88-1.09a4.58 4.58 0 0 1-1.63-3.09a5.5 5.5 0 0 1 .14-1.61a3.4 3.4 0 0 1 .8-1.53a5 5 0 0 1-1.3-.88a.15.15 0 0 1 0-.19a.16.16 0 0 1 .18-.06a10 10 0 0 0 1.46.37a20 20 0 0 0 2.45.31c2.13.1 4.38-.9 5.05-2.81s.43-3.83-2.08-5s-3.66-2.5-5.69-3.32a5 5 0 0 0-4.3.62c-4.08 2.25-7.72 9.35-6 15.94a.21.21 0 0 1-.1.23a.2.2 0 0 1-.23 0a13 13 0 0 1-1.33-1.73a13 13 0 0 1-.82-1.49'/><path fill='#f5f5f5' fill-rule='evenodd' d='M16.65 2A14 14 0 1 1 2 15.35A14 14 0 0 1 16.65 2m3.27 16.85a20 20 0 0 1-2.45-.31a8.6 8.6 0 0 1-1.47-.35a.16.16 0 0 0-.18.06a.15.15 0 0 0 0 .19a5 5 0 0 0 1.3.88a3.4 3.4 0 0 0-.8 1.53a5.5 5.5 0 0 0-.14 1.61a4.58 4.58 0 0 0 1.63 3.09a4.68 4.68 0 0 0 2.88 1.09a6.62 6.62 0 0 0 4.72-2.07a12.73 12.73 0 1 0-18.84 0a.21.21 0 0 0 .35-.19c-1.68-6.59 2-13.69 6-15.94a5 5 0 0 1 4.3-.62c2 .82 3.18 2.18 5.69 3.32s2.78 3 2.08 5s-2.91 2.86-5.07 2.73ZM15.54 8.69c-.82.06-1.36 1.08-1.43 1.73s.25 1.73 1.32 1.71c1.25 0 1.64-1.09 1.5-2.13a1.39 1.39 0 0 0-1.39-1.31'/><path fill-rule='evenodd' d='M15.54 8.68A1.4 1.4 0 0 1 16.93 10c.14 1-.24 2.12-1.49 2.14c-1.07 0-1.4-1.06-1.33-1.71s.61-1.68 1.43-1.75'/></svg>`,
    command: 'deno add tailwind-animations'
  }
]
---

<Layout
  title='Tailwind CSS Animations Plugin: Community-Powered Animation Magic'
>
  <wc-toast class='pointer-events-none fixed inset-0 z-50'></wc-toast>
  <!-- se agrega el componente header -->
  <Header />

  <main id='main-content' class='mx-auto w-full max-w-6xl pt-16'>
    <header
      id='preview'
      class='relative z-10 mx-auto mb-20 max-w-6xl px-4 lg:px-8'
    >
      <!-- Version badge -->
      <div class='animate-fade-in-up mb-8'>
        <span
          class='inline-flex items-center rounded-full bg-blue-50 px-2 py-1 text-xs font-medium text-blue-700 ring-1 ring-blue-700/10 ring-inset dark:bg-blue-400/10 dark:text-blue-400 dark:ring-blue-400/30'
        >
          v{version}
        </span>
      </div>

      <!-- Main Hero: Two columns layout -->
      <div class='grid items-end gap-12 lg:grid-cols-2 lg:gap-16'>
        <!-- Left Column: Content -->
        <div class='text-left'>
          <div
            class='animate-fade-in-up animate-delay-100 mb-6 flex items-center gap-2 sm:gap-5'
          >
            <Logo
              class='aspect-square size-10 shrink-0 sm:size-14'
              iconClass='size-7 animate-float-subtle'
            />
            <h1
              class='text-3xl font-bold tracking-tight text-slate-900 sm:text-5xl dark:text-white'
            >
              Tailwind <span class='text-blue-500'>Animations</span>
            </h1>
          </div>
          <p
            class='animate-fade-in-up animate-delay-200 mb-10 max-w-md text-base leading-7 text-slate-600 sm:text-lg dark:text-slate-400'
          >
            The easiest way to add stunning animations to your Tailwind CSS
            projects. Zero configuration, pure performance.
          </p>

          <!-- Install Command Box -->
          <div class='animate-fade-in-up animate-delay-300 flex flex-col gap-5'>
            <div
              class='overflow-hidden rounded-xl border border-slate-200 bg-white/50 p-1 shadow-xl shadow-slate-200/50 backdrop-blur-sm dark:border-white/10 dark:bg-black/40 dark:shadow-none'
            >
              <div
                class='flex items-center justify-between border-b border-slate-200 px-1 sm:px-4 dark:border-white/10'
              >
                <div
                  class='scrollbar-hide flex items-center gap-1 overflow-x-auto py-2 max-sm:grid max-sm:grid-flow-col max-sm:grid-rows-2 max-sm:overflow-x-auto'
                  role='group'
                  aria-label='Package manager'
                >
                  {
                    packageManagers.map((pm, index) => (
                      <button
                        class={`package-manager-btn flex items-center gap-2 rounded-full px-2 py-1 text-xs font-bold transition-all ${index === 0 ? 'bg-black/10 text-slate-900 dark:bg-white/5 dark:text-white' : 'text-slate-500 hover:text-slate-700 dark:text-slate-400 dark:hover:text-slate-200'}`}
                        data-pm={pm.name}
                        data-command={pm.command}
                        aria-pressed={index === 0 ? 'true' : 'false'}
                      >
                        <span
                          class='flex size-4 items-center justify-center'
                          aria-hidden='true'
                          set:html={pm.icon}
                        />
                        <span>{pm.name}</span>
                      </button>
                    ))
                  }
                </div>
                <button
                  id='copyNpmInstall'
                  class='group flex shrink-0 items-center gap-2 text-xs font-semibold text-slate-500 transition-colors hover:text-blue-500'
                  aria-label='Copy install command to clipboard'
                >
                  <CopyIcon class='size-4 group-active:scale-90' />
                </button>
              </div>
              <div class='flex items-center gap-4 p-4'>
                <div class='scrollbar-hide flex-1 overflow-x-auto text-left'>
                  <code
                    class='font-mono text-sm text-slate-800 dark:text-slate-200'
                  >
                    <span class='text-blue-500 select-none'>$ </span><span
                      id='install-command'>{packageManagers[0].command}</span
                    >
                  </code>
                </div>
              </div>
            </div>

            <div
              class='overflow-hidden rounded-xl border border-slate-200 bg-white/50 p-1 backdrop-blur-sm dark:border-white/10 dark:bg-black/40'
            >
              <div
                class='flex items-center justify-between border-b border-slate-200 px-4 py-2 dark:border-white/10'
              >
                <div class='flex gap-1' role='tablist' aria-label='Tailwind version'>
                  <button
                    class='version-tab rounded-full bg-black/10 px-3 py-1 text-[10px] font-bold tracking-widest text-slate-900 uppercase transition-all dark:bg-white/5 dark:text-white'
                    data-version='v4'
                    role='tab'
                    aria-selected='true'
                    aria-controls='code-v4'
                    id='tab-v4'
                  >
                    Tailwind v4
                  </button>
                  <button
                    class='version-tab rounded-full px-3 py-1 text-[10px] font-bold tracking-widest text-slate-500 uppercase transition-all hover:text-slate-700 dark:text-slate-400 dark:hover:text-slate-200'
                    data-version='v3'
                    role='tab'
                    aria-selected='false'
                    aria-controls='code-v3'
                    id='tab-v3'
                  >
                    Tailwind v3
                  </button>
                </div>
                <div class='flex items-center gap-4'>
                  <div
                    class='text-[10px] font-bold tracking-widest text-slate-400 uppercase'
                  >
                    How to use
                  </div>
                  <button
                    id='copyCode'
                    class='group flex shrink-0 items-center gap-2 text-xs font-semibold text-slate-500 transition-colors hover:text-blue-500'
                    aria-label='Copy code to clipboard'
                  >
                    <CopyIcon class='size-4 group-active:scale-90' />
                  </button>
                </div>
              </div>
              <div class='overflow-x-auto p-4 text-left dark:border-none'>
                <div id='code-v4' class='version-code' role='tabpanel' aria-labelledby='tab-v4'>
                  <Code
                    class='text-sm'
                    wrap={true}
                    lang='postcss'
                    theme='synthwave-84'
                    code={`@import 'tailwindcss';
@import 'tailwind-animations';`}
                  />
                </div>
                <div id='code-v3' class='version-code hidden' role='tabpanel' aria-labelledby='tab-v3'>
                  <Code
                    class='text-sm'
                    wrap={true}
                    theme='synthwave-84'
                    lang='javascript'
                    code={`// install package '@midudev/tailwind-animations@0.2.0'
// npm install @midudev/tailwind-animations@0.2.0
                    
// tailwind.config.mjs
import animations from 'tailwind-animations'

export default {
  plugins: [
    animations
  ],
}`}
                  />
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Right Column: Interactive Demo -->
        <div class='animate-fade-in-up animate-delay-500 relative'>
          <!-- Demo Window -->
          <div
            class='relative overflow-hidden rounded-2xl border border-slate-200 bg-slate-50 shadow-2xl shadow-blue-500/10 dark:border-slate-700/50 dark:bg-slate-900'
          >
            <!-- Window Header -->
            <div
              class='flex items-center justify-between border-b border-slate-200 bg-slate-100 px-4 py-3 dark:border-slate-700/50 dark:bg-slate-800/50'
            >
              <div class='flex items-center gap-2'>
                <div class='size-3 rounded-full bg-red-500'></div>
                <div class='size-3 rounded-full bg-yellow-500'></div>
                <div class='size-3 rounded-full bg-green-500'></div>
              </div>
              <span class='font-mono text-xs text-slate-500'
                >demo_preview.html</span
              >
              <div class='w-12'></div>
            </div>

            <!-- Preview Area -->
            <div
              class='relative flex min-h-[280px] items-center justify-center overflow-hidden bg-linear-to-br from-slate-50 via-white to-slate-50 p-8 dark:from-slate-900 dark:via-slate-800 dark:to-slate-900'
            >
              <!-- Grid Pattern Background -->
              <div
                class='pointer-events-none absolute inset-0 opacity-30 dark:opacity-30'
                style='background-image: linear-gradient(rgba(99, 102, 241, 0.1) 1px, transparent 1px), linear-gradient(90deg, rgba(99, 102, 241, 0.1) 1px, transparent 1px); background-size: 40px 40px;'
              >
              </div>

              <!-- Animated Box -->
              <div
                id='hero-demo-box'
                class='relative size-28 rounded-2xl bg-linear-to-br from-violet-500 via-purple-500 to-pink-500 shadow-2xl shadow-purple-500/40'
              >
                <!-- Glow effect -->
                <div
                  class='absolute -inset-1 -z-10 rounded-2xl bg-linear-to-br from-violet-500 via-purple-500 to-pink-500 opacity-50 blur-xl'
                >
                </div>
              </div>
            </div>

            <!-- Code Display Area -->
            <div
              class='border-t border-slate-200 bg-white p-5 dark:border-slate-700/50 dark:bg-slate-900/80'
            >
              <div class='font-mono text-sm'>
                <span class='text-slate-500'>&lt;</span><span
                  class='text-pink-600 dark:text-pink-400'>div</span
                >
                <span class='text-slate-500'> class="</span><span
                  id='hero-demo-classes'
                  class='text-cyan-600 dark:text-cyan-400'></span><span
                  class='text-slate-500'>"&gt;</span
                >
              </div>
              <div
                class='pl-4 font-mono text-sm text-slate-400 dark:text-slate-600'
              >
                &lt;!-- Applied animation --&gt;
              </div>
              <div class='font-mono text-sm'>
                <span class='text-slate-500'>&lt;/</span><span
                  class='text-pink-600 dark:text-pink-400'>div</span
                ><span class='text-slate-500'>&gt;</span>
              </div>
            </div>
          </div>

          <!-- Decorative elements -->
          <div
            class='pointer-events-none absolute top-0 right-0 size-40 -translate-x-20 -translate-y-20 rounded-full bg-blue-500/20 blur-3xl'
          >
          </div>

          <div
            class='pointer-events-none absolute -bottom-20 -left-20 size-40 rounded-full bg-purple-500/20 blur-3xl'
          >
          </div>
        </div>
      </div>
    </header>

    <section id='animation-collection' class='mt-32 mb-24'>
      <div class='mb-16 flex flex-col items-center'>
        <h2
          class='animate-fade-in-up animate-delay-[600ms] mb-4 text-2xl font-bold tracking-tight text-slate-900 sm:text-4xl dark:text-white'
        >
          Animation Collection
        </h2>
        <p
          class='animate-fade-in-up animate-delay-700 max-w-2xl text-center text-lg text-balance text-slate-600 dark:text-slate-400'
        >
          Explore our comprehensive library of ready-to-use animations.
          Customize duration, delay, and timing to fit your needs with zero
          configuration.
        </p>
      </div>

      <div class='relative'>
        <!-- Antes era sticky se le quito para que no tenga problemas con el header que es sticky -->
        <section
          class='top-4 z-50 mb-12 flex items-center justify-center px-4'
          id='option-inputs'
        >
          <div
            class='animate-fade-in-up animate-delay-800 flex flex-wrap items-center justify-center gap-4 rounded-2xl border border-slate-200 bg-white/70 p-4 shadow-2xl backdrop-blur-xl dark:border-white/10 dark:bg-black/60'
          >
            <div class='flex flex-col gap-1'>
              <label
                for='duration'
                class='text-[10px] font-bold tracking-wider text-slate-400 uppercase'
                >Duration</label
              >
              <select
                name='duration'
                id='duration'
                class='min-w-32 rounded-lg border border-slate-200 bg-slate-50/50 px-2 py-1 text-sm font-medium transition-colors outline-none hover:border-blue-500 dark:border-white/5 dark:bg-white/5'
              >
                {
                  Object.entries(animationDuration).map(([key, value]) => (
                    <option
                      value={value}
                      selected={key === '1000'}
                      class='dark:bg-slate-900'
                    >
                      {key}
                    </option>
                  ))
                }
              </select>
            </div>

            <div class='flex flex-col gap-1'>
              <label
                for='delay'
                class='text-[10px] font-bold tracking-wider text-slate-400 uppercase'
                >Delay</label
              >
              <select
                name='delay'
                id='delay'
                class='min-w-32 rounded-lg border border-slate-200 bg-slate-50/50 px-2 py-1 text-sm font-medium transition-colors outline-none hover:border-blue-500 dark:border-white/5 dark:bg-white/5'
              >
                {
                  Object.entries(animationDelay).map(([key, value]) => (
                    <option value={value} class='dark:bg-slate-900'>
                      {key}
                    </option>
                  ))
                }
              </select>
            </div>

            <div class='flex flex-col gap-1'>
              <label
                for='steps'
                class='text-[10px] font-bold tracking-wider text-slate-400 uppercase'
                >Steps</label
              >
              <select
                name='steps'
                id='steps'
                class='min-w-32 rounded-lg border border-slate-200 bg-slate-50/50 px-2 py-1 text-sm font-medium transition-colors outline-none hover:border-blue-500 dark:border-white/5 dark:bg-white/5'
              >
                {
                  Object.entries(animationSteps).map(([key, value]) => (
                    <option value={value} class='dark:bg-slate-900'>
                      {key}
                    </option>
                  ))
                }
              </select>
            </div>

            <div
              class='hidden h-8 w-px bg-slate-200 sm:block dark:bg-slate-800'
            >
            </div>

            <label class='group flex cursor-pointer items-center gap-3'>
              <span
                class='text-sm font-medium text-slate-600 transition-colors group-hover:text-blue-500 dark:text-slate-400'
                >Animate all</span
              >
              <div class='relative inline-flex h-6 w-11 items-center'>
                <input class='peer sr-only' id='animate' type='checkbox' />
                <div
                  class='h-6 w-11 rounded-full bg-slate-200 transition-colors peer-checked:bg-blue-500 dark:bg-slate-800'
                >
                </div>
                <div
                  class='absolute left-1 h-4 w-4 rounded-full bg-white shadow-sm transition-all peer-checked:translate-x-5'
                >
                </div>
              </div>
            </label>
          </div>
        </section>

        <section
          class='relative mx-auto grid max-w-6xl grid-cols-2 gap-6 px-4 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 lg:px-8'
        >
          {
            sortedAnimations.map((animationKey, index) => (
              <article
                class={`group animate-fade-in-up relative flex cursor-pointer flex-col items-center gap-4 rounded-2xl border border-slate-200 bg-white p-6 shadow-sm transition-all hover:-translate-y-1 hover:border-blue-500 hover:shadow-xl hover:shadow-blue-500/10 focus-visible:ring-2 focus-visible:ring-blue-500 focus-visible:outline-none dark:border-slate-800 dark:bg-slate-900/50 dark:hover:border-blue-500/50 ${index >= 15 ? 'hidden' : ''}`}
                data-class={animationKey}
                style={`animation-delay: ${1000 + index * 50}ms; animation-fill-mode: both;`}
                tabindex='0'
                role='button'
                aria-label={`Copy animate-${animationKey} class. Hover to preview.`}
              >
                <div class='flex w-full items-center justify-between'>
                  <span class='truncate pr-2 text-xs font-semibold text-slate-600 transition-colors group-hover:text-slate-900 dark:text-slate-400 dark:group-hover:text-white'>
                    {animationKey}
                  </span>
                  <span
                    aria-hidden='true'
                    class='text-slate-300 transition-colors hover:text-blue-500'
                  >
                    <CopyIcon class='size-4' />
                  </span>
                </div>

                <div class='flex flex-1 items-center justify-center py-8'>
                  <div
                    id={`preview-${animationKey}`}
                    class='size-16 rounded-xl bg-linear-to-br from-blue-500 to-blue-600 shadow-lg shadow-blue-500/30 transition-all duration-300 dark:from-blue-400 dark:to-blue-500 dark:shadow-blue-500/20'
                  />
                </div>
              </article>
            ))
          }
        </section>

        {
          sortedAnimations.length > 15 && (
            <div class='flex justify-center py-12'>
              <button
                id='load-more'
                class='animate-fade-in animate-delay-[1500ms] group flex cursor-pointer items-center gap-3 rounded-xl border border-slate-200 bg-white/50 px-10 py-3 text-sm font-bold text-slate-700 shadow-sm backdrop-blur-sm transition-all hover:border-blue-500 hover:text-blue-500 hover:shadow-md active:scale-95 dark:border-white/10 dark:bg-black/40 dark:text-slate-300 dark:hover:border-blue-500/50 dark:hover:text-blue-400'
              >
                <span>View all animations</span>
                <svg
                  xmlns='http://www.w3.org/2000/svg'
                  width='20'
                  height='20'
                  viewBox='0 0 24 24'
                  fill='none'
                  stroke='currentColor'
                  stroke-width='2.5'
                  stroke-linecap='round'
                  stroke-linejoin='round'
                  class='transition-transform group-hover:rotate-90'
                >
                  <path d='M12 5v14' />
                  <path d='M5 12h14' />
                </svg>
              </button>
            </div>
          )
        }
      </div>

      <section id='scroll-animations' class='relative mt-32 mb-24'>
        <div class='mb-16 flex flex-col items-center'>
          <h2
            class='mb-4 text-2xl font-bold tracking-tight text-slate-900 sm:text-4xl dark:text-white'
          >
            Scroll Animations
          </h2>
          <p
            class='max-w-2xl text-center text-lg text-balance text-slate-600 dark:text-slate-400'
          >
            Animate elements based on their position in the viewport using the <code
              class='text-blue-500'>timeline-view</code
            > utility.
          </p>
        </div>

        <div
          class='mx-auto max-w-[800px] rounded-3xl border border-slate-200 bg-slate-50/50 p-8 backdrop-blur-sm sm:p-12 dark:border-slate-800 dark:bg-slate-900/50'
        >
          <div class='max-w-none'>
            <h3 class='mb-6 text-center text-xl font-semibold dark:text-white'>
              Scroll down to see the magic
            </h3>

            <p class='mb-6 text-slate-600 dark:text-slate-400'>
              To animate elements on scroll, we use the <code
                class='text-blue-500'>timeline-view</code
              > utility. This property creates a View Timeline that allows you to
              synchronize the animation with the element's displacement within the
              viewport.
            </p>

            <p class='mb-12 text-slate-600 dark:text-slate-400'>
              The animation is automatically linked to the element's visibility
              in the viewport. Use <code class='text-blue-500'
                >animate-range</code
              > to control when the animation starts and ends relative to the element's
              visibility.
            </p>

            <div
              class='timeline-view animate-zoom-in animate-range-cover flex h-64 w-full flex-col items-center justify-center gap-4 rounded-2xl bg-pink-500 p-4 text-center font-bold text-white shadow-2xl'
            >
              <span class='text-2xl'>I reveal on scroll</span>
              <code
                class='rounded-lg bg-black/20 px-3 py-1 font-mono text-xs backdrop-blur-sm'
              >
                timeline-view animate-zoom-in animate-range-cover
              </code>
            </div>

            <p class='mt-12 mb-12 text-slate-600 dark:text-slate-400'>
              The <code class='text-blue-500'>animate-range</code> property is essential
              for defining when the animation starts and ends relative to the element's
              visibility. You can use predefined ranges like <code
                class='text-blue-500'>gradual</code
              >, <code class='text-blue-500'>moderate</code>, <code
                class='text-blue-500'>brisk</code
              >, or <code class='text-blue-500'>rapid</code> to easily control the
              animation's pace.
            </p>

            <div class='grid grid-cols-1 gap-6 sm:grid-cols-2'>
              <div
                class='timeline-view animate-fade-in animate-range-gradual flex h-32 w-full flex-col items-center justify-center gap-2 rounded-xl bg-slate-200 p-4 text-center font-bold text-slate-800 shadow-lg dark:bg-slate-800 dark:text-slate-200'
              >
                <span class='text-sm'>Gradual (10% - 90%)</span>
                <code
                  class='rounded-lg bg-black/10 px-2 py-1 font-mono text-[10px] dark:bg-white/10'
                >
                  animate-range-gradual
                </code>
              </div>
              <div
                class='timeline-view animate-fade-in animate-range-moderate flex h-32 w-full flex-col items-center justify-center gap-2 rounded-xl bg-slate-200 p-4 text-center font-bold text-slate-800 shadow-lg dark:bg-slate-800 dark:text-slate-200'
              >
                <span class='text-sm'>Moderate (20% - 80%)</span>
                <code
                  class='rounded-lg bg-black/10 px-2 py-1 font-mono text-[10px] dark:bg-white/10'
                >
                  animate-range-moderate
                </code>
              </div>
              <div
                class='timeline-view animate-fade-in animate-range-brisk flex h-32 w-full flex-col items-center justify-center gap-2 rounded-xl bg-slate-200 p-4 text-center font-bold text-slate-800 shadow-lg dark:bg-slate-800 dark:text-slate-200'
              >
                <span class='text-sm'>Brisk (30% - 70%)</span>
                <code
                  class='rounded-lg bg-black/10 px-2 py-1 font-mono text-[10px] dark:bg-white/10'
                >
                  animate-range-brisk
                </code>
              </div>
              <div
                class='timeline-view animate-fade-in animate-range-rapid flex h-32 w-full flex-col items-center justify-center gap-2 rounded-xl bg-slate-200 p-4 text-center font-bold text-slate-800 shadow-lg dark:bg-slate-800 dark:text-slate-200'
              >
                <span class='text-sm'>Rapid (40% - 60%)</span>
                <code
                  class='rounded-lg bg-black/10 px-2 py-1 font-mono text-[10px] dark:bg-white/10'
                >
                  animate-range-rapid
                </code>
              </div>
            </div>

            <p class='mt-12 mb-12 text-slate-600 dark:text-slate-400'>
              Of course, you can also use custom values for more precision. By
              specifying values like <code class='text-blue-500'>entry 10%</code
              > or <code class='text-blue-500'>contain 25%</code>, you can
              perfectly time the reveal effect to match your design's flow.
            </p>

            <div
              class='timeline-view animate-fade-in-left animate-range-[entry_5%_contain_20%] flex h-48 w-full flex-col items-center justify-center gap-4 rounded-2xl bg-blue-500 p-4 text-center font-bold text-white shadow-2xl'
            >
              <span class='text-2xl'>I fade in from the left</span>
              <code
                class='rounded-lg bg-black/20 px-3 py-1 font-mono text-xs backdrop-blur-sm'
              >
                timeline-view animate-slide-in-left
                animate-range-[entry_5%_contain_20%]
              </code>
            </div>

            <p class='mt-12 mb-12 text-slate-600 dark:text-slate-400'>
              You can combine different directions and effects. Using <code
                class='text-blue-500'>animate-slide-in-left</code
              > with a scroll timeline makes the element gracefully slide into place
              while adjusting its opacity, synchronized with the user's scrolling
              speed for a more interactive feel.
            </p>

            <div
              class='timeline-view animate-blurred-fade-in animate-range-[entry_10%_contain_30%] flex h-48 w-full flex-col items-center justify-center gap-4 rounded-2xl bg-purple-500 p-4 text-center font-bold text-white shadow-2xl'
            >
              <span class='text-2xl'>I fade in with blur</span>
              <code
                class='rounded-lg bg-black/20 px-3 py-1 font-mono text-xs backdrop-blur-sm'
              >
                timeline-view animate-blurred-fade-in
                animate-range-[entry_10%_contain_30%]
              </code>
            </div>

            <p class='mt-12 text-slate-600 dark:text-slate-400'>
              Blurred transitions like <code class='text-blue-500'
                >animate-blurred-fade-in</code
              > add a layer of polish. By linking it to a scroll timeline, you create
              a depth-of-field effect that naturally draws attention to the content
              as it becomes clear and focused.
            </p>
          </div>
        </div>
      </section>

      <section id='scroll-view-timelines' class='relative mt-32 mb-24'>
        <div class='mb-16 flex flex-col items-center'>
          <h2
            class='mb-4 text-2xl font-bold tracking-tight text-slate-900 sm:text-4xl dark:text-white'
          >
            Scroll & View Timelines
          </h2>
          <p
            class='max-w-2xl text-center text-lg text-balance text-slate-600 dark:text-slate-400'
          >
            Link animations to scroll progress or element visibility using
            powerful timeline utilities.
          </p>
        </div>

        <div
          class='mx-auto max-w-[800px] rounded-3xl border border-slate-200 bg-slate-50/50 p-8 backdrop-blur-sm sm:p-12 dark:border-slate-800 dark:bg-slate-900/50'
        >
          <div class='grid grid-cols-1 gap-16'>
            <!-- Example 1: Vertical Scroll Progress -->
            <div class='flex flex-col gap-6'>
              <h3 class='text-xl font-semibold dark:text-white'>
                Vertical Scroll Progress
              </h3>
              <p class='text-slate-600 dark:text-slate-400'>
                Use <code class='text-blue-500'>timeline-scroll</code> to link an
                animation to the scroll container's progress. The animation advances
                as you scroll.
              </p>
              <div
                class='relative h-64 overflow-y-auto rounded-2xl border border-slate-200 bg-white dark:border-slate-800 dark:bg-slate-950'
              >
                <div
                  class='timeline-scroll animate-expand-horizontally sticky top-0 h-2 w-full origin-left bg-gradient-to-r from-green-400 to-emerald-600'
                >
                </div>
                <div class='h-[800px] p-6'>
                  <p class='text-sm text-slate-500 dark:text-slate-400'>
                    ↓ Scroll down to see the progress bar fill
                  </p>
                  <div class='mt-6 space-y-4'>
                    {
                      [1, 2, 3].map(() => (
                        <div class='h-28 rounded-xl bg-slate-100 dark:bg-slate-900' />
                      ))
                    }
                  </div>
                </div>
              </div>
              <code
                class='self-center rounded-lg bg-slate-900 px-3 py-2 font-mono text-xs text-green-400'
              >
                timeline-scroll animate-expand-horizontally
              </code>
            </div>

            <!-- Example 2: Horizontal Scroll Progress -->
            <div class='flex flex-col gap-6'>
              <h3 class='text-xl font-semibold dark:text-white'>
                Horizontal Scroll Progress
              </h3>
              <p class='text-slate-600 dark:text-slate-400'>
                Use <code class='text-blue-500'>timeline-[scroll(inline)]</code>
                for horizontal scroll containers. The progress bar follows your horizontal
                scrolling.
              </p>
              <div
                class='relative h-48 overflow-x-auto overflow-y-hidden rounded-2xl border border-slate-200 bg-white dark:border-slate-800 dark:bg-slate-950'
              >
                <div
                  class='timeline-[scroll(inline)] animate-expand-horizontally sticky top-0 left-0 z-10 h-2 w-full origin-left bg-gradient-to-r from-purple-400 to-pink-600'
                >
                </div>
                <div
                  class='flex h-full w-full max-w-[1500px] items-center gap-4 p-6'
                >
                  {
                    ['🚀', '⭐', '💎', '🎯', '🔥', '✨', '🎨', '💡'].map(
                      (emoji) => (
                        <div class='flex h-28 w-40 flex-shrink-0 items-center justify-center rounded-xl bg-slate-100 text-4xl dark:bg-slate-900'>
                          {emoji}
                        </div>
                      )
                    )
                  }
                </div>
              </div>
              <code
                class='self-center rounded-lg bg-slate-900 px-3 py-2 font-mono text-xs text-purple-400'
              >
                timeline-[scroll(inline)] animate-expand-horizontally
              </code>
            </div>

            <!-- Example 3: Entry vs Exit Ranges -->
            <div class='flex flex-col gap-6'>
              <h3 class='text-xl font-semibold dark:text-white'>
                Entry & Exit Animation Ranges
              </h3>
              <p class='text-slate-600 dark:text-slate-400'>
                Control when animations play with <code class='text-blue-500'
                  >animate-range-entry</code
                > (entering viewport) and <code class='text-blue-500'
                  >animate-range-exit</code
                > (leaving viewport).
              </p>
              <div
                class='relative h-80 overflow-y-auto rounded-2xl border border-slate-200 bg-white dark:border-slate-800 dark:bg-slate-950'
              >
                <div class='flex h-[1100px] flex-col items-center gap-8 p-8'>
                  <p class='text-sm text-slate-500 dark:text-slate-400'>
                    ↓ Scroll to see entry/exit animations
                  </p>
                  <div class='h-48'></div>
                  <div
                    class='timeline-view animate-slide-in-left animate-range-entry flex w-64 items-center justify-center rounded-xl bg-cyan-500 p-6 font-bold text-white shadow-lg'
                  >
                    <span class='text-center'
                      >Entry Animation<br /><span
                        class='text-xs font-normal opacity-80'
                        >Plays when entering</span
                      ></span
                    >
                  </div>
                  <div class='h-32'></div>
                  <div
                    class='timeline-view animate-slide-out-right animate-range-exit flex w-64 items-center justify-center rounded-xl bg-rose-500 p-6 font-bold text-white shadow-lg'
                  >
                    <span class='text-center'
                      >Exit Animation<br /><span
                        class='text-xs font-normal opacity-80'
                        >Plays when leaving</span
                      ></span
                    >
                  </div>
                  <div class='h-48'></div>
                </div>
              </div>
              <div class='flex flex-wrap justify-center gap-2'>
                <code
                  class='rounded-lg bg-slate-900 px-3 py-2 font-mono text-xs text-cyan-400'
                >
                  animate-range-entry
                </code>
                <code
                  class='rounded-lg bg-slate-900 px-3 py-2 font-mono text-xs text-rose-400'
                >
                  animate-range-exit
                </code>
              </div>
            </div>

            <!-- Example 4: Staggered Reveal -->
            <div class='flex flex-col gap-6'>
              <h3 class='text-xl font-semibold dark:text-white'>
                Staggered Reveal Effect
              </h3>
              <p class='text-slate-600 dark:text-slate-400'>
                Combine <code class='text-blue-500'>timeline-view</code> with different
                <code class='text-blue-500'>animate-range</code>
                values to create a staggered reveal effect.
              </p>
              <div
                class='relative h-96 overflow-y-auto rounded-2xl border border-slate-200 bg-white dark:border-slate-800 dark:bg-slate-950'
              >
                <div class='flex h-[1100px] flex-col items-center gap-6 p-8'>
                  <p class='text-sm text-slate-500 dark:text-slate-400'>
                    ↓ Scroll to reveal cards in sequence
                  </p>
                  <div class='h-64'></div>
                  <div class='grid grid-cols-2 gap-4'>
                    <div
                      class='timeline-view animate-fade-in-up animate-range-[entry_0%_cover_35%] flex h-24 w-28 items-center justify-center rounded-xl bg-amber-500 font-bold text-white shadow-lg'
                    >
                      First
                    </div>
                    <div
                      class='timeline-view animate-fade-in-up animate-range-[entry_10%_cover_45%] flex h-24 w-28 items-center justify-center rounded-xl bg-orange-500 font-bold text-white shadow-lg'
                    >
                      Second
                    </div>
                    <div
                      class='timeline-view animate-fade-in-up animate-range-[entry_20%_cover_55%] flex h-24 w-28 items-center justify-center rounded-xl bg-red-500 font-bold text-white shadow-lg'
                    >
                      Third
                    </div>
                    <div
                      class='timeline-view animate-fade-in-up animate-range-[entry_30%_cover_65%] flex h-24 w-28 items-center justify-center rounded-xl bg-pink-500 font-bold text-white shadow-lg'
                    >
                      Fourth
                    </div>
                  </div>
                  <div class='h-96'></div>
                </div>
              </div>
              <code
                class='self-center rounded-lg bg-slate-900 px-3 py-2 font-mono text-xs text-amber-400'
              >
                animate-range-[entry_0%_cover_30%] → [entry_10%_cover_40%] → ...
              </code>
            </div>

            <!-- Example 5: View Timeline with Rotation -->
            <div class='flex flex-col gap-6'>
              <h3 class='text-xl font-semibold dark:text-white'>
                Rotation on Scroll
              </h3>
              <p class='text-slate-600 dark:text-slate-400'>
                Use <code class='text-blue-500'>animate-rotate-360</code> with
                <code class='text-blue-500'>animate-range-cover</code> to rotate elements
                as they pass through the viewport.
              </p>
              <div
                class='relative h-72 overflow-y-auto rounded-2xl border border-slate-200 bg-white dark:border-slate-800 dark:bg-slate-950'
              >
                <div class='flex h-[800px] flex-col items-center gap-8 p-8'>
                  <p class='text-sm text-slate-500 dark:text-slate-400'>
                    ↓ Scroll to spin the shapes
                  </p>
                  <div class='h-40'></div>
                  <div class='flex gap-6'>
                    <div
                      class='timeline-view animate-rotate-360 animate-range-cover h-20 w-20 rounded-xl bg-gradient-to-br from-indigo-500 to-purple-600 shadow-lg'
                    >
                    </div>
                    <div
                      class='timeline-view animate-spin-clockwise animate-range-cover h-20 w-20 rounded-full bg-gradient-to-br from-teal-500 to-cyan-600 shadow-lg'
                    >
                    </div>
                    <div
                      class='timeline-view animate-flip-x animate-range-cover flex h-20 w-20 items-center justify-center rounded-xl bg-gradient-to-br from-fuchsia-500 to-pink-600 text-3xl shadow-lg'
                    >
                      🎲
                    </div>
                  </div>
                  <div class='h-96'></div>
                </div>
              </div>
              <div class='flex flex-wrap justify-center gap-2'>
                <code
                  class='rounded-lg bg-slate-900 px-3 py-2 font-mono text-xs text-indigo-400'
                >
                  animate-rotate-360
                </code>
                <code
                  class='rounded-lg bg-slate-900 px-3 py-2 font-mono text-xs text-teal-400'
                >
                  animate-spin-clockwise
                </code>
                <code
                  class='rounded-lg bg-slate-900 px-3 py-2 font-mono text-xs text-fuchsia-400'
                >
                  animate-flip-x
                </code>
              </div>
            </div>

            <!-- Example 6: Timeline Axis Variants -->
            <div class='flex flex-col gap-6'>
              <h3 class='text-xl font-semibold dark:text-white'>
                Timeline Utilities Reference
              </h3>
              <p class='text-slate-600 dark:text-slate-400'>
                Available timeline utilities and how to use them:
              </p>
              <div class='grid grid-cols-1 gap-3 sm:grid-cols-2'>
                <div
                  class='flex flex-col gap-1 rounded-xl border border-slate-200 p-4 dark:border-slate-800'
                >
                  <span
                    class='text-xs font-bold tracking-wide text-slate-400 uppercase'
                    >Scroll Timelines</span
                  >
                  <code class='text-xs text-blue-500'>timeline-scroll</code>
                  <code class='text-xs text-blue-500'>timeline-[scroll(x)]</code
                  >
                  <code class='text-xs text-blue-500'>timeline-[scroll(y)]</code
                  >
                  <code class='text-xs text-blue-500'
                    >timeline-[scroll(block)]</code
                  >
                  <code class='text-xs text-blue-500'
                    >timeline-[scroll(inline)]</code
                  >
                </div>
                <div
                  class='flex flex-col gap-1 rounded-xl border border-slate-200 p-4 dark:border-slate-800'
                >
                  <span
                    class='text-xs font-bold tracking-wide text-slate-400 uppercase'
                    >View Timelines</span
                  >
                  <code class='text-xs text-emerald-500'>timeline-view</code>
                  <code class='text-xs text-emerald-500'
                    >timeline-[view(x)]</code
                  >
                  <code class='text-xs text-emerald-500'
                    >timeline-[view(y)]</code
                  >
                  <code class='text-xs text-emerald-500'
                    >timeline-[view(block)]</code
                  >
                  <code class='text-xs text-emerald-500'
                    >timeline-[view(inline)]</code
                  >
                </div>
                <div
                  class='flex flex-col gap-1 rounded-xl border border-slate-200 p-4 dark:border-slate-800'
                >
                  <span
                    class='text-xs font-bold tracking-wide text-slate-400 uppercase'
                    >Animation Ranges</span
                  >
                  <code class='text-xs text-amber-500'>animate-range-cover</code
                  >
                  <code class='text-xs text-amber-500'
                    >animate-range-contain</code
                  >
                  <code class='text-xs text-amber-500'>animate-range-entry</code
                  >
                  <code class='text-xs text-amber-500'>animate-range-exit</code>
                </div>
                <div
                  class='flex flex-col gap-1 rounded-xl border border-slate-200 p-4 dark:border-slate-800'
                >
                  <span
                    class='text-xs font-bold tracking-wide text-slate-400 uppercase'
                    >Preset Ranges</span
                  >
                  <code class='text-xs text-purple-500'
                    >animate-range-gradual <span class='text-slate-500'
                      >(10%-90%)</span
                    ></code
                  >
                  <code class='text-xs text-purple-500'
                    >animate-range-moderate <span class='text-slate-500'
                      >(20%-80%)</span
                    ></code
                  >
                  <code class='text-xs text-purple-500'
                    >animate-range-brisk <span class='text-slate-500'
                      >(30%-70%)</span
                    ></code
                  >
                  <code class='text-xs text-purple-500'
                    >animate-range-rapid <span class='text-slate-500'
                      >(40%-60%)</span
                    ></code
                  >
                </div>
              </div>
            </div>

            <!-- Example 7: Arbitrary Values -->
            <div class='flex flex-col gap-6'>
              <h3 class='text-xl font-semibold dark:text-white'>
                Arbitrary Values
              </h3>
              <p class='text-slate-600 dark:text-slate-400'>
                Use brackets for custom values. Use underscores <code
                  class='text-blue-500'>_</code
                > instead of spaces.
              </p>
              <div class='grid grid-cols-1 gap-3 sm:grid-cols-2'>
                <div
                  class='flex flex-col gap-2 rounded-xl border border-slate-200 bg-slate-50 p-4 dark:border-slate-800 dark:bg-slate-900'
                >
                  <span
                    class='text-xs font-bold tracking-wide text-slate-400 uppercase'
                    >Scroll with axis</span
                  >
                  <code class='text-xs text-blue-400'
                    >timeline-[scroll(x_root)]</code
                  >
                  <code class='text-xs text-blue-400'
                    >timeline-[scroll(y_nearest)]</code
                  >
                </div>
                <div
                  class='flex flex-col gap-2 rounded-xl border border-slate-200 bg-slate-50 p-4 dark:border-slate-800 dark:bg-slate-900'
                >
                  <span
                    class='text-xs font-bold tracking-wide text-slate-400 uppercase'
                    >View with inset</span
                  >
                  <code class='text-xs text-emerald-400'
                    >timeline-[view(block)]</code
                  >
                  <code class='text-xs text-emerald-400'
                    >timeline-[view(x_200px_auto)]</code
                  >
                </div>
                <div
                  class='col-span-full flex flex-col gap-2 rounded-xl border border-slate-200 bg-slate-50 p-4 dark:border-slate-800 dark:bg-slate-900'
                >
                  <span
                    class='text-xs font-bold tracking-wide text-slate-400 uppercase'
                    >Custom animation ranges</span
                  >
                  <code class='text-xs text-amber-400'
                    >animate-range-[entry_0%_cover_50%]</code
                  >
                  <code class='text-xs text-amber-400'
                    >animate-range-[cover_25%_cover_75%]</code
                  >
                  <code class='text-xs text-amber-400'
                    >animate-range-[exit_-10%_exit_100%]</code
                  >
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <Footer />
    </section>
  </main>

  <script>
    import { toast } from 'wc-toast'

    const $articles = document.querySelectorAll('article')
    const $animateAll: HTMLInputElement = document.querySelector('#animate')!
    const $duration: HTMLSelectElement = document.querySelector('#duration')!
    const $steps: HTMLSelectElement = document.querySelector('#steps')!
    const $delay: HTMLSelectElement = document.querySelector('#delay')!

    const $pmButtons = document.querySelectorAll('.package-manager-btn')
    const $installCommand = document.getElementById('install-command')!
    const $copyBtn = document.getElementById('copyNpmInstall')!
    const $copyCodeBtn = document.getElementById('copyCode')!

    const $versionTabs = document.querySelectorAll('.version-tab')
    const $versionCodes = document.querySelectorAll('.version-code')

    const $loadMore = document.getElementById('load-more')

    if ($loadMore) {
      $loadMore.addEventListener('click', () => {
        const $hiddenArticles = document.querySelectorAll('article.hidden')
        $hiddenArticles.forEach(($article, index) => {
          $article.classList.remove('hidden')
          // @ts-ignore
          $article.style.animationDelay = `${index * 50}ms`
        })
        $loadMore.parentElement?.remove()
      })
    }

    // Initial duration setup (if any logic depends on it)
    $duration.value = '1000ms'

    // Version Tab Switcher
    $versionTabs.forEach(($tab) => {
      $tab.addEventListener('click', () => {
        const version = $tab.getAttribute('data-version')!

        $versionTabs.forEach(($t) => {
          $t.classList.remove(
            'bg-black/10',
            'text-slate-900',
            'dark:bg-white/5',
            'dark:text-white'
          )
          $t.classList.add(
            'text-slate-500',
            'dark:text-slate-400',
            'hover:text-slate-700',
            'dark:hover:text-slate-200'
          )
          $t.setAttribute('aria-selected', 'false')
        })

        $tab.classList.add(
          'bg-black/10',
          'text-slate-900',
          'dark:bg-white/5',
          'dark:text-white'
        )
        $tab.classList.remove(
          'text-slate-500',
          'dark:text-slate-400',
          'hover:text-slate-700',
          'dark:hover:text-slate-200'
        )
        $tab.setAttribute('aria-selected', 'true')

        $versionCodes.forEach(($code) => {
          if ($code.id === `code-${version}`) {
            $code.classList.remove('hidden')
          } else {
            $code.classList.add('hidden')
          }
        })
      })
    })

    $copyCodeBtn.addEventListener('click', () => {
      const $visibleCode = document.querySelector(
        '.version-code:not(.hidden) pre'
      )
      if ($visibleCode) {
        const text = $visibleCode.textContent!
        navigator.clipboard.writeText(text)
        toast('Configuration copied to clipboard!', {
          icon: { type: 'success' },
          theme: {
            type: document.documentElement.classList.contains('dark')
              ? 'dark'
              : 'light'
          }
        })
      }
    })

    // Package Manager Switcher
    $pmButtons.forEach(($btn) => {
      $btn.addEventListener('click', () => {
        const command = $btn.getAttribute('data-command')!
        $installCommand.textContent = command

        $pmButtons.forEach(($b) => {
          $b.classList.remove(
            'bg-black/10',
            'text-slate-900',
            'dark:bg-white/5',
            'dark:text-white'
          )
          $b.classList.add(
            'text-slate-500',
            'dark:text-slate-400',
            'hover:text-slate-700',
            'dark:hover:text-slate-200'
          )
          $b.setAttribute('aria-pressed', 'false')
        })

        $btn.classList.add(
          'bg-black/10',
          'text-slate-900',
          'dark:bg-white/5',
          'dark:text-white'
        )
        $btn.classList.remove(
          'text-slate-500',
          'dark:text-slate-400',
          'hover:text-slate-700',
          'dark:hover:text-slate-200'
        )
        $btn.setAttribute('aria-pressed', 'true')
      })
    })

    $copyBtn.addEventListener('click', () => {
      const text = $installCommand.textContent!
      navigator.clipboard.writeText(text)
      toast('Command copied to clipboard!', {
        icon: { type: 'success' },
        theme: {
          type: document.documentElement.classList.contains('dark')
            ? 'dark'
            : 'light'
        }
      })
    })

    function handleMouseEnter(this: HTMLElement) {
      const animationKey = this.getAttribute('data-class')
      const animationClass = `animate-${animationKey}`
      const $box = this.querySelector('div[id^="preview-"]') as HTMLElement
      if ($box) {
        $box.classList.add(animationClass)
        // Apply current styles
        $box.style.animationDuration = $duration.value
        $box.style.animationDelay = $delay.value
        $box.style.animationTimingFunction =
          $steps.value !== 'none' ? `steps(${$steps.value})` : ''
      }
    }

    function handleMouseLeave(this: HTMLElement): void {
      const animationKey = this.getAttribute('data-class')
      const animationClass = `animate-${animationKey}`
      const $box = this.querySelector('div[id^="preview-"]')
      if ($box) $box.classList.remove(animationClass)
    }

    function updateArticlesListeners() {
      $articles.forEach(($article) => {
        if ($animateAll.checked) {
          $article.removeEventListener('mouseenter', handleMouseEnter)
          $article.removeEventListener('mouseleave', handleMouseLeave)
        } else {
          $article.addEventListener('mouseenter', handleMouseEnter)
          $article.addEventListener('mouseleave', handleMouseLeave)
        }
      })
    }

    $animateAll.addEventListener('change', () => {
      $articles.forEach(($article) => {
        const animationKey = $article.getAttribute('data-class')!
        const animationClass = `animate-${animationKey}`
        const $box = $article.querySelector(
          'div[id^="preview-"]'
        ) as HTMLElement

        if ($box) {
          if ($animateAll.checked) {
            $box.classList.add(animationClass)
            $box.style.animationIterationCount = 'infinite'
            $box.style.animationDuration = $duration.value
            $box.style.animationDelay = $delay.value
            $box.style.animationTimingFunction =
              $steps.value !== 'none' ? `steps(${$steps.value})` : ''
          } else {
            $box.classList.remove(animationClass)
            $box.style.animationIterationCount = 'unset'
          }
        }
      })
      updateArticlesListeners()
    })

    $duration.addEventListener('change', (event) => {
      const target = event.target as HTMLSelectElement
      $articles.forEach(($article) => {
        const $box = $article.querySelector(
          'div[id^="preview-"]'
        ) as HTMLElement
        if ($box) $box.style.animationDuration = target.value
      })
    })

    $steps.addEventListener('change', (event) => {
      const target = event.target as HTMLSelectElement
      $articles.forEach(($article) => {
        const $box = $article.querySelector(
          'div[id^="preview-"]'
        ) as HTMLElement
        if ($box)
          $box.style.animationTimingFunction =
            target.value !== 'none' ? `steps(${target.value})` : ''
      })
    })

    $delay.addEventListener('change', (event) => {
      const target = event.target as HTMLSelectElement
      $articles.forEach(($article) => {
        const $box = $article.querySelector(
          'div[id^="preview-"]'
        ) as HTMLElement
        if ($box) $box.style.animationDelay = target.value
      })
    })

    $articles.forEach(($article) => {
      const animationKey = $article.getAttribute('data-class')!
      const animationClass = `animate-${animationKey}`

      $article.addEventListener('mouseenter', handleMouseEnter)
      $article.addEventListener('mouseleave', handleMouseLeave)

      function copyAnimation() {
        navigator.clipboard.writeText(animationClass)
        toast(`Copied "animate-${animationKey}"`, {
          icon: { type: 'success' },
          theme: {
            type: document.documentElement.classList.contains('dark')
              ? 'dark'
              : 'light'
          }
        })
      }

      $article.addEventListener('click', copyAnimation)
      $article.addEventListener('keydown', (e: KeyboardEvent) => {
        if (e.key === 'Enter' || e.key === ' ') {
          e.preventDefault()
          copyAnimation()
        }
      })
    })

    // ==========================================
    // Hero Demo Animation - Interactive Typewriter
    // ==========================================
    const $heroDemoBox = document.getElementById('hero-demo-box')
    const $heroDemoClasses = document.getElementById('hero-demo-classes')

    if ($heroDemoBox && $heroDemoClasses) {
      // Different animation configurations to showcase
      const demoAnimations = [
        { animation: 'animate-fade-in-up', extras: '' },
        { animation: 'animate-bounce', extras: 'animate-duration-700' },
        { animation: 'animate-shake', extras: 'animate-delay-100' },
        { animation: 'animate-pulse', extras: 'animate-duration-slow' },
        { animation: 'animate-swing', extras: 'animate-delay-[25ms]' },
        { animation: 'animate-wobble', extras: 'animate-duration-[777ms]' },
        { animation: 'animate-float', extras: 'animate-delay-300' },
        { animation: 'animate-zoom-in', extras: 'animate-duration-500' },
        { animation: 'animate-flip-x', extras: 'animate-duration-fast' },
        { animation: 'animate-bouncing', extras: 'animate-delay-[50ms]' },
        { animation: 'animate-heartbeat', extras: 'animate-duration-1000' },
        { animation: 'animate-jelly', extras: 'animate-delay-150' },
        {
          animation: 'animate-rubber-band',
          extras: 'animate-duration-[500ms]'
        },
        { animation: 'animate-tada', extras: 'animate-delay-200' }
      ]

      let currentDemoIndex = 0
      let isTyping = false

      // Typewriter effect function
      async function typeText(text: string): Promise<void> {
        $heroDemoClasses!.textContent = ''
        for (let i = 0; i <= text.length; i++) {
          $heroDemoClasses!.textContent = text.substring(0, i)
          await new Promise((resolve) =>
            setTimeout(resolve, 35 + Math.random() * 25)
          )
        }
      }

      // Clear text with backspace effect
      async function clearText(): Promise<void> {
        const currentText = $heroDemoClasses!.textContent || ''
        for (let i = currentText.length; i >= 0; i--) {
          $heroDemoClasses!.textContent = currentText.substring(0, i)
          await new Promise((resolve) => setTimeout(resolve, 20))
        }
      }

      // Main demo loop
      async function runDemoAnimation(): Promise<void> {
        if (isTyping) return
        isTyping = true

        const demo = demoAnimations[currentDemoIndex]
        const fullClass = demo.extras
          ? `${demo.animation} ${demo.extras}`
          : demo.animation

        // Clear previous animation class
        demoAnimations.forEach((d) => {
          const animClass = d.animation
          $heroDemoBox!.classList.remove(animClass)
        })
        $heroDemoBox!.style.animation = 'none'
        $heroDemoBox!.offsetHeight // Trigger reflow
        $heroDemoBox!.style.animation = ''

        // Type the new class
        await typeText(fullClass)

        // Apply the animation
        const animClass = demo.animation
        $heroDemoBox!.classList.add(animClass)

        // Apply extras via inline styles
        if (demo.extras.includes('duration')) {
          const match = demo.extras.match(/animate-duration-(\[?\w+ms?\]?|\w+)/)
          if (match) {
            const value = match[1]
            if (value.startsWith('[') && value.endsWith(']')) {
              $heroDemoBox!.style.animationDuration = value.slice(1, -1)
            } else if (value === 'slow') {
              $heroDemoBox!.style.animationDuration = '1500ms'
            } else if (value === 'fast') {
              $heroDemoBox!.style.animationDuration = '300ms'
            } else {
              $heroDemoBox!.style.animationDuration = value + 'ms'
            }
          }
        } else {
          $heroDemoBox!.style.animationDuration = ''
        }

        if (demo.extras.includes('delay')) {
          const match = demo.extras.match(/animate-delay-(\[?\w+ms?\]?|\w+)/)
          if (match) {
            const value = match[1]
            if (value.startsWith('[') && value.endsWith(']')) {
              $heroDemoBox!.style.animationDelay = value.slice(1, -1)
            } else {
              $heroDemoBox!.style.animationDelay = value + 'ms'
            }
          }
        } else {
          $heroDemoBox!.style.animationDelay = ''
        }

        // Wait for animation to play
        await new Promise((resolve) => setTimeout(resolve, 2500))

        // Clear and move to next
        await clearText()

        currentDemoIndex = (currentDemoIndex + 1) % demoAnimations.length
        isTyping = false

        // Continue the loop
        setTimeout(runDemoAnimation, 300)
      }

      // Start the demo
      setTimeout(runDemoAnimation, 800)
    }
  </script>

  <style>
    .scrollbar-hide::-webkit-scrollbar {
      display: none;
    }
    .scrollbar-hide {
      -ms-overflow-style: none;
      scrollbar-width: none;
    }
    pre.astro-code {
      padding: 0 !important;
      margin: 0 !important;
    }
  </style>
</Layout>
```

## File: `midudev-tailwind-animations-ceed187/web/src/styles/global.css`
```css
@import "tailwindcss";
```

## File: `midudev-tailwind-animations-ceed187/web/src/styles/index.css`
```css
@import 'tailwindcss';
@import '../../../src/index.css';

@custom-variant dark (&:where(.dark, .dark *));
/* prettier-ignore */
@source inline('animate-{blurred-fade-in,fade-in,fade-out,slide-in-top,slide-in-bottom,slide-out-top,slide-out-bottom,zoom-in,zoom-out,rotate-90,rotate-180,rotate-360,rotate-3d,flip-horizontal,flip-vertical,bouncing,swing,wobble,pulsing,shake,tada,jump,hang,roll-in,roll-out,float,sink,flash,jiggle,rubber-band,scale,slide-in-left,slide-in-right,slide-out-left,slide-out-right,spin-clockwise,spin-counter-clockwise,flip-x,flip-y,blink,pop,expand-horizontally,contract-horizontally,expand-vertically,contract-vertically,fade-in-up,fade-in-down,fade-in-left,fade-in-right,fade-out-up,fade-out-down,fade-out-left,fade-out-right,sway,flip-in-x,flip-in-y,flip-out-x,flip-out-y,rotate-in,rotate-out,slide-rotate-in,slide-rotate-out,heartbeat,horizontal-vibration,rotational-wave,skew,skew-right,vertical-bounce,horizontal-bounce,tilt,squeeze,slide-up-fade,bounce-fade-in,swing-drop-in,pulse-fade-in,impulse-rotation-right,impulse-rotation-left,dancing,pulse,jelly}');
/* prettier-ignore */
@source inline('animate-duration-{none,slower,slow,normal,fast,faster,0,100,150,200,250,300,400,500,700,800,900,1000}');
/* prettier-ignore */
@source inline('animate-delay-{none,0,100,150,200,250,300,400,500,700,800,900,1000}');
@source inline('animate-steps-{none,retro,normal,modern}');
/* prettier-ignore */
@source inline('timeline-{scroll,view}');
/* prettier-ignore */
@source inline('animate-range-{cover,contain,entry,exit,gradual,moderate,brisk,rapid}');

:root {
  --font-sans:
    'Geist Mono', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto,
    'Helvetica Neue', Arial, sans-serif;
  --font-mono:
    'Geist Mono', ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas,
    'Liberation Mono', 'Courier New', monospace;
}

body {
  font-family: var(--font-sans);
}

pre {
  background: transparent !important;
}

/* Smooth selection */
::selection {
  background: rgba(0, 153, 255, 0.1);
  color: #0099ff;
}

.dark ::selection {
  background: rgba(0, 153, 255, 0.2);
  color: #0099ff;
}

/* Custom Utilities */
.glass {
  background: rgba(255, 255, 255, 0.7);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.2);
}

.dark .glass {
  background: rgba(0, 0, 0, 0.7);
  border: 1px solid rgba(255, 255, 255, 0.1);
}
```

## File: `refs/heads/main`
```
ceed187044dc02f2cde392b0be503b5972d42c95
```

## File: `refs/remotes/origin/HEAD`
```
ref: refs/remotes/origin/main
```

