---
id: rsync
type: knowledge
owner: OA_Triage
---
# rsync
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
WHAT IS RSYNC?
--------------

Rsync is a fast and extraordinarily versatile file copying tool for
both remote and local files.

Rsync uses a delta-transfer algorithm which provides a very fast method
for bringing remote files into sync.  It does this by sending just the
differences in the files across the link, without requiring that both
sets of files are present at one of the ends of the link beforehand.  At
first glance this may seem impossible because the calculation of diffs
between two files normally requires local access to both files.

A technical report describing the rsync algorithm is included with this
package.


USAGE
-----

Basically you use rsync just like scp, but rsync has many additional
options.  To get a complete list of supported options type:

    rsync --help

See the [manpage][0] for more detailed information.

[0]: https://download.samba.org/pub/rsync/rsync.1

BUILDING AND INSTALLING
-----------------------

If you need to build rsync yourself, check out the [INSTALL][1] page for
information on what libraries and packages you can use to get the maximum
features in your build.

[1]: https://github.com/RsyncProject/rsync/blob/master/INSTALL.md

SETUP
-----

Rsync normally uses ssh or rsh for communication with remote systems.
It does not need to be setuid and requires no special privileges for
installation.  You must, however, have a working ssh or rsh system.
Using ssh is recommended for its security features.

Alternatively, rsync can run in `daemon' mode, listening on a socket.
This is generally used for public file distribution, although
authentication and access control are available.

To install rsync, first run the "configure" script.  This will create a
Makefile and config.h appropriate for your system.  Then type "make".

Note that on some systems you will have to force configure not to use
gcc because gcc may not support some features (such as 64 bit file
offsets) that your system may support.  Set the environment variable CC
to the name of your native compiler before running configure in this
case.

Once built put a copy of rsync in your search path on the local and
remote systems (or use "make install").  That's it!


RSYNC DAEMONS
-------------

Rsync can also talk to "rsync daemons" which can provide anonymous or
authenticated rsync.  See the rsyncd.conf(5) manpage for details on how
to setup an rsync daemon.  See the rsync(1) manpage for info on how to
connect to an rsync daemon.


WEB SITE
--------

For more information, visit the [main rsync web site][2].

[2]: https://rsync.samba.org/

You'll find a FAQ list, downloads, resources, HTML versions of the
manpages, etc.


MAILING LISTS
-------------

There is a mailing list for the discussion of rsync and its applications
that is open to anyone to join.  New releases are announced on this
list, and there is also an announcement-only mailing list for those that
want official announcements.  See the [mailing-list page][3] for full
details.

[3]: https://rsync.samba.org/lists.html


BUG REPORTS
-----------

The [bug-tracking web page][4] has full details on bug reporting.

[4]: https://rsync.samba.org/bug-tracking.html

That page contains links to the current bug list, and information on how to
do a good job when reporting a bug.  You might also like to try searching
the Internet for the error message you've received, or looking in the
[mailing list archives][5].

[5]: https://mail-archive.com/rsync@lists.samba.org/

To send a bug report, follow the instructions on the bug-tracking
page of the web site.

Alternately, email your bug report to <rsync@lists.samba.org>.

For security issues please email details of the issue to <rsync.project@gmail.com>.

GIT REPOSITORY
--------------

If you want to get the very latest version of rsync direct from the
source code repository, then you will need to use git.  The git repo
is hosted [on GitHub][6] and [on Samba's site][7].

[6]: https://github.com/RsyncProject/rsync
[7]: https://git.samba.org/?p=rsync.git;a=summary

See [the download page][8] for full details on all the ways to grab the
source.

[8]: https://rsync.samba.org/download.html


COPYRIGHT
---------

Rsync was originally written by Andrew Tridgell and Paul Mackerras.  Many
people from around the world have helped to maintain and improve it.

Rsync may be used, modified and redistributed only under the terms of
the GNU General Public License, found in the file [COPYING][9] in this
distribution, or at [the Free Software Foundation][10].

[9]: https://github.com/RsyncProject/rsync/blob/master/COPYING
[10]: https://www.fsf.org/licenses/gpl.html

```

### File: rsync\README.md
```md
WHAT IS RSYNC?
--------------

Rsync is a fast and extraordinarily versatile file copying tool for
both remote and local files.

Rsync uses a delta-transfer algorithm which provides a very fast method
for bringing remote files into sync.  It does this by sending just the
differences in the files across the link, without requiring that both
sets of files are present at one of the ends of the link beforehand.  At
first glance this may seem impossible because the calculation of diffs
between two files normally requires local access to both files.

A technical report describing the rsync algorithm is included with this
package.


USAGE
-----

Basically you use rsync just like scp, but rsync has many additional
options.  To get a complete list of supported options type:

    rsync --help

See the [manpage][0] for more detailed information.

[0]: https://download.samba.org/pub/rsync/rsync.1

BUILDING AND INSTALLING
-----------------------

If you need to build rsync yourself, check out the [INSTALL][1] page for
information on what libraries and packages you can use to get the maximum
features in your build.

[1]: https://github.com/RsyncProject/rsync/blob/master/INSTALL.md

SETUP
-----

Rsync normally uses ssh or rsh for communication with remote systems.
It does not need to be setuid and requires no special privileges for
installation.  You must, however, have a working ssh or rsh system.
Using ssh is recommended for its security features.

Alternatively, rsync can run in `daemon' mode, listening on a socket.
This is generally used for public file distribution, although
authentication and access control are available.

To install rsync, first run the "configure" script.  This will create a
Makefile and config.h appropriate for your system.  Then type "make".

Note that on some systems you will have to force configure not to use
gcc because gcc may not support some features (such as 64 bit file
offsets) that your system may support.  Set the environment variable CC
to the name of your native compiler before running configure in this
case.

Once built put a copy of rsync in your search path on the local and
remote systems (or use "make install").  That's it!


RSYNC DAEMONS
-------------

Rsync can also talk to "rsync daemons" which can provide anonymous or
authenticated rsync.  See the rsyncd.conf(5) manpage for details on how
to setup an rsync daemon.  See the rsync(1) manpage for info on how to
connect to an rsync daemon.


WEB SITE
--------

For more information, visit the [main rsync web site][2].

[2]: https://rsync.samba.org/

You'll find a FAQ list, downloads, resources, HTML versions of the
manpages, etc.


MAILING LISTS
-------------

There is a mailing list for the discussion of rsync and its applications
that is open to anyone to join.  New releases are announced on this
list, and there is also an announcement-only mailing list for those that
want official announcements.  See the [mailing-list page][3] for full
details.

[3]: https://rsync.samba.org/lists.html


BUG REPORTS
-----------

The [bug-tracking web page][4] has full details on bug reporting.

[4]: https://rsync.samba.org/bug-tracking.html

That page contains links to the current bug list, and information on how to
do a good job when reporting a bug.  You might also like to try searching
the Internet for the error message you've received, or looking in the
[mailing list archives][5].

[5]: https://mail-archive.com/rsync@lists.samba.org/

To send a bug report, follow the instructions on the bug-tracking
page of the web site.

Alternately, email your bug report to <rsync@lists.samba.org>.

For security issues please email details of the issue to <rsync.project@gmail.com>.

GIT REPOSITORY
--------------

If you want to get the very latest version of rsync direct from the
source code repository, then you will need to use git.  The git repo
is hosted [on GitHub][6] and [on Samba's site][7].

[6]: https://github.com/RsyncProject/rsync
[7]: https://git.samba.org/?p=rsync.git;a=summary

See [the download page][8] for full details on all the ways to grab the
source.

[8]: https://rsync.samba.org/download.html


COPYRIGHT
---------

Rsync was originally written by Andrew Tridgell and Paul Mackerras.  Many
people from around the world have helped to maintain and improve it.

Rsync may be used, modified and redistributed only under the terms of
the GNU General Public License, found in the file [COPYING][9] in this
distribution, or at [the Free Software Foundation][10].

[9]: https://github.com/RsyncProject/rsync/blob/master/COPYING
[10]: https://www.fsf.org/licenses/gpl.html

```

### File: access.c
```c
/*
 * Routines to authenticate access to a daemon (hosts allow/deny).
 *
 * Copyright (C) 1998 Andrew Tridgell
 * Copyright (C) 2004-2022 Wayne Davison
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License along
 * with this program; if not, visit the http://fsf.org website.
 */

#include "rsync.h"
#include "ifuncs.h"
#ifdef HAVE_NETGROUP_H
#include <netgroup.h>
#endif

static int allow_forward_dns;

extern const char undetermined_hostname[];

static int match_hostname(const char **host_ptr, const char *addr, const char *tok)
{
	struct hostent *hp;
	unsigned int i;
	const char *host = *host_ptr;

	if (!host || !*host)
		return 0;

#ifdef HAVE_INNETGR
	if (*tok == '@' && tok[1])
		return innetgr(tok + 1, host, NULL, NULL);
#endif

	/* First check if the reverse-DNS-determined hostname matches. */
	if (iwildmatch(tok, host))
		return 1;

	if (!allow_forward_dns)
		return 0;

	/* Fail quietly if tok is an address or wildcarded entry, not a simple hostname. */
	if (!tok[strspn(tok, ".0123456789")] || tok[strcspn(tok, ":/*?[")])
		return 0;

	/* Now try forward-DNS on the token (config-specified hostname) and see if the IP matches. */
	if (!(hp = gethostbyname(tok)))
		return 0;

	for (i = 0; hp->h_addr_list[i] != NULL; i++) {
		if (strcmp(addr, inet_ntoa(*(struct in_addr*)(hp->h_addr_list[i]))) == 0) {
			/* If reverse lookups are off, we'll use the conf-specified
			 * hostname in preference to UNDETERMINED. */
			if (host == undetermined_hostname)
				*host_ptr = strdup(tok);
			return 1;
		}
	}

	return 0;
}

static int match_binary(const char *b1, const char *b2, const char *mask, int addrlen)
{
	int i;

	for (i = 0; i < addrlen; i++) {
		if ((b1[i] ^ b2[i]) & mask[i])
			return 0;
	}

	return 1;
}

static void make_mask(char *mask, int plen, int addrlen)
{
	int w, b;

	w = plen >> 3;
	b = plen & 0x7;

	if (w)
		memset(mask, 0xff, w);
	if (w < addrlen)
		mask[w] = 0xff & (0xff<<(8-b));
	if (w+1 < addrlen)
		memset(mask+w+1, 0, addrlen-w-1);

	return;
}

static int match_address(const char *addr, const char *tok)
{
	char *p;
	struct addrinfo hints, *resa, *rest;
	int gai;
	int ret = 0;
	int addrlen = 0;
#ifdef HAVE_STRTOL
	long int bits;
#else
	int bits;
#endif
	char mask[16];
	char *a = NULL, *t = NULL;

	if (!addr || !*addr)
		return 0;

	p = strchr(tok,'/');
	if (p)
		*p = '\0';

	/* Fail quietly if tok is a hostname, not an address. */
	if (tok[strspn(tok, ".0123456789")] && strchr(tok, ':') == NULL) {
		if (p)
			*p = '/';
		return 0;
	}

	memset(&hints, 0, sizeof(hints));
	hints.ai_family = PF_UNSPEC;
	hints.ai_socktype = SOCK_STREAM;
#ifdef AI_NUMERICHOST
	hints.ai_flags = AI_NUMERICHOST;
#endif

	if (getaddrinfo(addr, NULL, &hints, &resa) != 0) {
		if (p)
			*p = '/';
		return 0;
	}

	gai = getaddrinfo(tok, NULL, &hints, &rest);
	if (p)
		*p++ = '/';
	if (gai != 0) {
		rprintf(FLOG, "error matching address %s: %s\n",
			tok, gai_strerror(gai));
		freeaddrinfo(resa);
		return 0;
	}

	if (rest->ai_family != resa->ai_family) {
		ret = 0;
		goto out;
	}

	switch(resa->ai_family) {
	case PF_INET:
		a = (char *)&((struct sockaddr_in *)resa->ai_addr)->sin_addr;
		t = (char *)&((struct sockaddr_in *)rest->ai_addr)->sin_addr;
		addrlen = 4;

		break;

#ifdef INET6
	case PF_INET6: {
		struct sockaddr_in6 *sin6a, *sin6t;

		sin6a = (struct sockaddr_in6 *)resa->ai_addr;
		sin6t = (struct sockaddr_in6 *)rest->ai_addr;

		a = (char *)&sin6a->sin6_addr;
		t = (char *)&sin6t->sin6_addr;

		addrlen = 16;

#ifdef HAVE_SOCKADDR_IN6_SCOPE_ID
		if (sin6t->sin6_scope_id && sin6a->sin6_scope_id != sin6t->sin6_scope_id) {
			ret = 0;
			goto out;
		}
#endif

		break;
	}
#endif
	default:
		rprintf(FLOG, "unknown family %u\n", rest->ai_family);
		ret = 0;
		goto out;
	}

	bits = -1;
	if (p) {
		if (inet_pton(resa->ai_addr->sa_family, p, mask) <= 0) {
#ifdef HAVE_STRTOL
			char *ep = NULL;
#else
			unsigned char *pp;
#endif

#ifdef HAVE_STRTOL
			bits = strtol(p, &ep, 10);
			if (!*p || *ep) {
				rprintf(FLOG, "malformed mask in %s\n", tok);
				ret = 0;
				goto out;
			}
#else
			for (pp = (unsigned char *)p; *pp; pp++) {
				if (!isascii(*pp) || !isdigit(*pp)) {
					rprintf(FLOG, "malformed mask in %s\n", tok);
					ret = 0;
					goto out;
				}
			}
			bits = atoi(p);
#endif
			if (bits == 0) {
				ret = 1;
				goto out;
			}
			if (bits < 0 || bits > (addrlen << 3)) {
				rprintf(FLOG, "malformed mask in %s\n", tok);
				ret = 0;
				goto out;
			}
		}
	} else {
		bits = 128;
	}

	if (bits >= 0)
		make_mask(mask, bits, addrlen);

	ret = match_binary(a, t, mask, addrlen);

  out:
	freeaddrinfo(resa);
	freeaddrinfo(rest);
	return ret;
}

static int access_match(const char *list, const char *addr, const char **host_ptr)
{
	char *tok;
	char *list2 = strdup(list);

	strlower(list2);

	for (tok = strtok(list2, " ,\t"); tok; tok = strtok(NULL, " ,\t")) {
		if (match_hostname(host_ptr, addr, tok) || match_address(addr, tok)) {
			free(list2);
			return 1;
		}
	}

	free(list2);
	return 0;
}

int allow_access(const char *addr, const char **host_ptr, int i)
{
	const char *allow_list = lp_hosts_allow(i);
	const char *deny_list = lp_hosts_deny(i);

	if (allow_list && !*allow_list)
		allow_list = NULL;
	if (deny_list && !*deny_list)
		deny_list = NULL;

	allow_forward_dns = lp_forward_lookup(i);

	/* If we match an allow-list item, we always allow access. */
	if (allow_list) {
		if (access_match(allow_list, addr, host_ptr))
			return 1;
		/* For an allow-list w/o a deny-list, disallow non-matches. */
		if (!deny_list)
			return 0;
	}

	/* If we match a deny-list item (and got past any allow-list
	 * items), we always disallow access. */
	if (deny_list && access_match(deny_list, addr, host_ptr))
		return 0;

	/* Allow all other access. */
	return 1;
}

```

### File: acls.c
```c
/*
 * Handle passing Access Control Lists between systems.
 *
 * Copyright (C) 1996 Andrew Tridgell
 * Copyright (C) 1996 Paul Mackerras
 * Copyright (C) 2006-2022 Wayne Davison
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License along
 * with this program; if not, visit the http://fsf.org website.
 */

#include "rsync.h"
#include "lib/sysacls.h"

#ifdef SUPPORT_ACLS

extern int dry_run;
extern int am_root;
extern int read_only;
extern int list_only;
extern mode_t orig_umask;
extern int numeric_ids;
extern int inc_recurse;
extern int preserve_devices;
extern int preserve_specials;

/* Flags used to indicate what items are being transmitted for an entry. */
#define XMIT_USER_OBJ (1<<0)
#define XMIT_GROUP_OBJ (1<<1)
#define XMIT_MASK_OBJ (1<<2)
#define XMIT_OTHER_OBJ (1<<3)
#define XMIT_NAME_LIST (1<<4)

#define NO_ENTRY ((uchar)0x80) /* Default value of a NON-name-list entry. */

#define NAME_IS_USER (1u<<31) /* Bit used only on a name-list entry. */

/* When we send the access bits over the wire, we shift them 2 bits to the
 * left and use the lower 2 bits as flags (relevant only to a name entry).
 * This makes the protocol more efficient than sending a value that would
 * be likely to have its highest bits set. */
#define XFLAG_NAME_FOLLOWS 0x0001u
#define XFLAG_NAME_IS_USER 0x0002u

/* === ACL structures === */

typedef struct {
	id_t id;
	uint32 access;
} id_access;

typedef struct {
	id_access *idas;
	int count;
} ida_entries;

typedef struct {
	char *name;
	uchar len;
} idname;

typedef struct rsync_acl {
	ida_entries names;
	/* These will be NO_ENTRY if there's no such entry. */
	uchar user_obj;
	uchar group_obj;
	uchar mask_obj;
	uchar other_obj;
} rsync_acl;

typedef struct {
	rsync_acl racl;
	SMB_ACL_T sacl;
} acl_duo;

static const rsync_acl empty_rsync_acl = {
	{NULL, 0}, NO_ENTRY, NO_ENTRY, NO_ENTRY, NO_ENTRY
};

static item_list access_acl_list = EMPTY_ITEM_LIST;
static item_list default_acl_list = EMPTY_ITEM_LIST;

static size_t prior_access_count = (size_t)-1;
static size_t prior_default_count = (size_t)-1;

/* === Calculations on ACL types === */

static const char *str_acl_type(SMB_ACL_TYPE_T type)
{
	switch (type) {
	case SMB_ACL_TYPE_ACCESS:
#ifdef HAVE_OSX_ACLS
		return "ACL_TYPE_EXTENDED";
#else
		return "ACL_TYPE_ACCESS";
#endif
	case SMB_ACL_TYPE_DEFAULT:
		return "ACL_TYPE_DEFAULT";
	default:
		break;
	}
	return "unknown ACL type!";
}

static int calc_sacl_entries(const rsync_acl *racl)
{
	/* A System ACL always gets user/group/other permission entries. */
	return racl->names.count
#ifdef ACLS_NEED_MASK
	     + 1
#else
	     + (racl->mask_obj != NO_ENTRY)
#endif
	     + 3;
}

/* Extracts and returns the permission bits from the ACL.  This cannot be
 * called on an rsync_acl that has NO_ENTRY in any spot but the mask. */
static int rsync_acl_get_perms(const rsync_acl *racl)
{
	return (racl->user_obj << 6)
	     + ((racl->mask_obj != NO_ENTRY ? racl->mask_obj : racl->group_obj) << 3)
	     + racl->other_obj;
}

/* Removes the permission-bit entries from the ACL because these
 * can be reconstructed from the file's mode. */
static void rsync_acl_strip_perms(stat_x *sxp)
{
	rsync_acl *racl = sxp->acc_acl;

	racl->user_obj = NO_ENTRY;
	if (racl->mask_obj == NO_ENTRY)
		racl->group_obj = NO_ENTRY;
	else {
		int group_perms = (sxp->st.st_mode >> 3) & 7;
		if (racl->group_obj == group_perms)
			racl->group_obj = NO_ENTRY;
#ifndef HAVE_SOLARIS_ACLS
		if (racl->names.count != 0 && racl->mask_obj == group_perms)
			racl->mask_obj = NO_ENTRY;
#endif
	}
	racl->other_obj = NO_ENTRY;
}

/* Given an empty rsync_acl, fake up the permission bits. */
static void rsync_acl_fake_perms(rsync_acl *racl, mode_t mode)
{
	racl->user_obj = (mode >> 6) & 7;
	racl->group_obj = (mode >> 3) & 7;
	racl->other_obj = mode & 7;
}

/* === Rsync ACL functions === */

static rsync_acl *create_racl(void)
{
	rsync_acl *racl = new(rsync_acl);

	*racl = empty_rsync_acl;

	return racl;
}

static BOOL ida_entries_equal(const ida_entries *ial1, const ida_entries *ial2)
{
	id_access *ida1, *ida2;
	int count = ial1->count;
	if (count != ial2->count)
		return False;
	ida1 = ial1->idas;
	ida2 = ial2->idas;
	for (; count--; ida1++, ida2++) {
		if (ida1->access != ida2->access || ida1->id != ida2->id)
			return False;
	}
	return True;
}

static BOOL rsync_acl_equal(const rsync_acl *racl1, const rsync_acl *racl2)
{
	return racl1->user_obj == racl2->user_obj
	    && racl1->group_obj == racl2->group_obj
	    && racl1->mask_obj == racl2->mask_obj
	    && racl1->other_obj == racl2->other_obj
	    && ida_entries_equal(&racl1->names, &racl2->names);
}

/* Are the extended (non-permission-bit) entries equal?  If so, the rest of
 * the ACL will be handled by the normal mode-preservation code.  This is
 * only meaningful for access ACLs!  Note: the 1st arg is a fully-populated
 * rsync_acl, but the 2nd parameter can be a condensed rsync_acl, which means
 * that it might have several of its permission objects set to NO_ENTRY. */
static BOOL rsync_acl_equal_enough(const rsync_acl *racl1,
				   const rsync_acl *racl2, mode_t m)
{
	if ((racl1->mask_obj ^ racl2->mask_obj) & NO_ENTRY)
		return False; /* One has a mask and the other doesn't */

	/* When there's a mask, the group_obj becomes an extended entry. */
	if (racl1->mask_obj != NO_ENTRY) {
		/* A condensed rsync_acl with a mask can only have no
		 * group_obj when it was identical to the mask.  This
		 * means that it was also identical to the group attrs
		 * from the mode. */
		if (racl2->group_obj == NO_ENTRY) {
			if (racl1->group_obj != ((m >> 3) & 7))
				return False;
		} else if (racl1->group_obj != racl2->group_obj)
			return False;
	}
	return ida_entries_equal(&racl1->names, &racl2->names);
}

static void rsync_acl_free(rsync_acl *racl)
{
	if (racl->names.idas)
		free(racl->names.idas);
	*racl = empty_rsync_acl;
}

void free_acl(stat_x *sxp)
{
	if (sxp->acc_acl) {
		rsync_acl_free(sxp->acc_acl);
		free(sxp->acc_acl);
		sxp->acc_acl = NULL;
	}
	if (sxp->def_acl) {
		rsync_acl_free(sxp->def_acl);
		free(sxp->def_acl);
		sxp->def_acl = NULL;
	}
}

#ifdef SMB_ACL_NEED_SORT
static int id_access_sorter(const void *r1, const void *r2)
{
	id_access *ida1 = (id_access *)r1;
	id_access *ida2 = (id_access *)r2;
	id_t rid1 = ida1->id, rid2 = ida2->id;
	if ((ida1->access ^ ida2->access) & NAME_IS_USER)
		return ida1->access & NAME_IS_USER ? -1 : 1;
	return rid1 == rid2 ? 0 : rid1 < rid2 ? -1 : 1;
}
#endif

/* === System ACLs === */

/* Unpack system ACL -> rsync ACL verbatim.  Return whether we succeeded. */
static BOOL unpack_smb_acl(SMB_ACL_T sacl, rsync_acl *racl)
{
	static item_list temp_ida_list = EMPTY_ITEM_LIST;
	SMB_ACL_ENTRY_T entry;
	const char *errfun;
	int rc;

	errfun = "sys_acl_get_entry";
	for (rc = sys_acl_get_entry(sacl, SMB_ACL_FIRST_ENTRY, &entry);
	     rc == 1;
	     rc = sys_acl_get_entry(sacl, SMB_ACL_NEXT_ENTRY, &entry)) {
		SMB_ACL_TAG_T tag_type;
		uint32 access;
		id_t g_u_id;
		id_access *ida;
		if ((rc = sys_acl_get_info(entry, &tag_type, &access, &g_u_id)) != 0) {
			errfun = "sys_acl_get_info";
			break;
		}
		/* continue == done with entry; break == store in temporary ida list */
		switch (tag_type) {
#ifndef HAVE_OSX_ACLS
		case SMB_ACL_USER_OBJ:
			if (racl->user_obj == NO_ENTRY)
				racl->user_obj = access;
			else
				rprintf(FINFO, "unpack_smb_acl: warning: duplicate USER_OBJ entry ignored\n");
			continue;
		case SMB_ACL_GROUP_OBJ:
			if (racl->group_obj == NO_ENTRY)
				racl->group_obj = access;
			else
				rprintf(FINFO, "unpack_smb_acl: warning: duplicate GROUP_OBJ entry ignored\n");
			continue;
		case SMB_ACL_MASK:
			if (racl->mask_obj == NO_ENTRY)
				racl->mask_obj = access;
			else
				rprintf(FINFO, "unpack_smb_acl: warning: duplicate MASK entry ignored\n");
			continue;
		case SMB_ACL_OTHER:
			if (racl->other_obj == NO_ENTRY)
				racl->other_obj = access;
			else
				rprintf(FINFO, "unpack_smb_acl: warning: duplicate OTHER entry ignored\n");
			continue;
#endif
		case SMB_ACL_USER:
			access |= NAME_IS_USER;
			break;
		case SMB_ACL_GROUP:
			break;
		default:
			rprintf(FINFO, "unpack_smb_acl: warning: entry with unrecognized tag type ignored\n");
			continue;
		}
		ida = EXPAND_ITEM_LIST(&temp_ida_list, id_access, -10);
		ida->id = g_u_id;
		ida->access = access;
	}
	if (rc) {
		rsyserr(FERROR_XFER, errno, "unpack_smb_acl: %s()", errfun);
		rsync_acl_free(racl);
		return False;
	}

	/* Transfer the count id_access items out of the temp_ida_list
	 * into the names ida_entries list in racl. */
	if (temp_ida_list.count) {
#ifdef SMB_ACL_NEED_SORT
		if (temp_ida_list.count > 1) {
			qsort(temp_ida_list.items, temp_ida_list.count, sizeof (id_access), id_access_sorter);
		}
#endif
		racl->names.idas = new_array(id_access, temp_ida_list.count);
		memcpy(racl->names.idas, temp_ida_list.items, temp_ida_list.count * sizeof (id_access));
	} else
		racl->names.idas = NULL;

	racl->names.count = temp_ida_list.count;

	/* Truncate the temporary list now that its idas have been saved. */
	temp_ida_list.count = 0;

	return True;
}

/* Synactic sugar for system calls */

#define CALL_OR_ERROR(func,args,str) \
	do { \
		if (func args) { \
			errfun = str; \
			goto error_exit; \
		} \
	} while (0)

#define COE(func,args) CALL_OR_ERROR(func,args,#func)
#define COE2(func,args) CALL_OR_ERROR(func,args,NULL)

#ifndef HAVE_OSX_ACLS
/* Store the permissions in the system ACL entry. */
static int store_access_in_entry(uint32 access, SMB_ACL_ENTRY_T entry)
{
	if (sys_acl_set_access_bits(entry, access)) {
		rsyserr(FERROR_XFER, errno, "store_access_in_entry sys_acl_set_access_bits()");
		return -1;
	}
	return 0;
}
#endif

/* Pack rsync ACL -> system ACL verbatim.  Return whether we succeeded. */
static BOOL pack_smb_acl(SMB_ACL_T *smb_acl, const rsync_acl *racl)
{
#ifdef ACLS_NEED_MASK
	uchar mask_bits;
#endif
	size_t count;
	id_access *ida;
	const char *errfun = NULL;
	SMB_ACL_ENTRY_T entry;

	if (!(*smb_acl = sys_acl_init(calc_sacl_entries(racl)))) {
		rsyserr(FERROR_XFER, errno, "pack_smb_acl: sys_acl_init()");
		return False;
	}

#ifndef HAVE_OSX_ACLS
	COE( sys_acl_create_entry,(smb_acl, &entry) );
	COE( sys_acl_set_info,(entry, SMB_ACL_USER_OBJ, racl->user_obj & ~NO_ENTRY, 0) );
#endif

	for (ida = racl->names.idas, count = racl->names.count; count; ida++, count--) {
#ifdef SMB_ACL_NEED_SORT
		if (!(ida->access & NAME_IS_USER))
			break;
#endif
		COE( sys_acl_create_entry,(smb_acl, &entry) );
		COE( sys_acl_set_info,
		    (entry,
		     ida->access & NAME_IS_USER ? SMB_ACL_USER : SMB_ACL_GROUP,
		     ida->access & ~NAME_IS_USER, ida->id) );
	}

#ifndef HAVE_OSX_ACLS
	COE( sys_acl_create_entry,(smb_acl, &entry) );
	COE( sys_acl_set_info,(entry, SMB_ACL_GROUP_OBJ, racl->group_obj & ~NO_ENTRY, 0) );

#ifdef SMB_ACL_NEED_SORT
	for ( ; count; ida++, count--) {
		COE( sys_acl_create_entry,(smb_acl, &entry) );
		COE( sys_acl_set_info,(entry, SMB_ACL_GROUP, ida->access, ida->id) );
	}
#endif

#ifdef ACLS_NEED_MASK
	mask_bits = racl->mask_obj == NO_ENTRY ? racl->group_obj & ~NO_ENTRY : racl->mask_obj;
	COE( sys_acl_create_entry,(smb_acl, &entry) );
	COE( sys_acl_set_info,(entry, SMB_ACL_MASK, mask_bits, 0) );
#else
	if (racl->mask_obj != NO_ENTRY) {
		COE( sys_acl_create_entry,(smb_acl, &entry) );
		COE( sys_acl_set_info,(entry, SMB_ACL_MASK, racl->mask_obj, 0) );
	}
#endif

	COE( sys_acl_create_entry,(smb_acl, &entry) );
	COE( sys_acl_set_info,(entry, SMB_ACL_OTHER, racl->other_obj & ~NO_ENTRY, 0) );
#endif

#ifdef DEBUG
	if (sys_acl_valid(*smb_acl) < 0)
		rprintf(FERROR_XFER, "pack_smb_acl: warning: system says the ACL I packed is invalid\n");
#endif

	return True;

  error_exit:
	if (errfun) {
		rsyserr(FERROR_XFER, errno, "pack_smb_acl %s()", errfun);
	}
	sys_acl_free_acl(*smb_acl);
	return False;
}

static int find_matching_rsync_acl(const rsync_acl *racl, SMB_ACL_TYPE_T type,
				   const item_list *racl_list)
{
	static int access_match = -1, default_match = -1;
	int *match = type == SMB_ACL_TYPE_ACCESS ? &access_match : &default_match;
	size_t count = racl_list->count;

	/* If this is the first time through or we didn't match the last
	 * time, then start at the end of the list, which should be the
	 * best place to start hunting. */
	if (*match == -1)
		*match = racl_list->count - 1;
	while (count--) {
		rsync_acl *base = racl_list->items;
		if (rsync_acl_equal(base + *match, racl))
			return *match;
		if (!(*match)--)
			*match = racl_list->count - 1;
	}

	*match = -1;
	return *match;
}

static int get_rsync_acl(const char *fname, rsync_acl *racl,
			 SMB_ACL_TYPE_T type, mode_t mode)
{
	SMB_ACL_T sacl;

#ifdef SUPPORT_XATTRS
	/* --fake-super support: load ACLs from an xattr. */
	if (am_root < 0) {
		char *buf;
		size_t len;
		int cnt;

		if ((buf = get_xattr_acl(fname, type == SMB_ACL_TYPE_ACCESS, &len)) == NULL)
			return 0;
		cnt = (len - 4*4) / (4+4);
		if (len < 4*4 || len != (size_t)cnt*(4+4) + 4*4) {
			free(buf);
			return -1;
		}

		racl->user_obj = IVAL(buf, 0);
		if (racl->user_obj == NO_ENTRY)
			racl->user_obj = (mode >> 6) & 7;
		racl->group_obj = IVAL(buf, 4);
		if (racl->group_obj == NO_ENTRY)
			racl->group_obj = (mode >> 3) & 7;
		racl->mask_obj = IVAL(buf, 8);
		racl->other_obj = IVAL(buf, 12);
		if (racl->other_obj == NO_ENTRY)
			racl->other_obj = mode & 7;

		if (cnt) {
			char *bp = buf + 4*4;
			id_access *ida = racl->names.idas = new_array(id_access, cnt);
			racl->names.count = cnt;
			for ( ; cnt--; ida++, bp += 4+4) {
				ida->id = IVAL(bp, 0);
				ida->access = IVAL(bp, 4);
			}
		}
		free(buf);
		return 0;
	}
#endif

	if ((sacl = sys_acl_get_file(fname, type)) != 0) {
		BOOL ok = unpack_smb_acl(sacl, racl);

		sys_acl_free_acl(sacl);
		if (!ok) {
			rsyserr(FERROR_XFER, errno, "get_acl: unpack_smb_acl(%s)", fname);
			return -1;
		}
	} else if (no_acl_syscall_error(errno)) {
		/* ACLs are not supported, so pretend we have a basic ACL. */
		if (type == SMB_ACL_TYPE_ACCESS)
			rsync_acl_fake_perms(racl, mode);
	} else {
		rsyserr(FERROR_XFER, errno, "get_acl: sys_acl_get_file(%s, %s)",
			fname, str_acl_type(type));
		return -1;
	}

	return 0;
}

/* Return the Access Control List for the given filename. */
int get_acl(const char *fname, stat_x *sxp)
{
	sxp->acc_acl = create_racl();

	if (S_ISREG(sxp->st.st_mode) || S_ISDIR(sxp->st.st_mode)) {
		/* Everyone supports this. */
	} else if (S_ISLNK(sxp->st.st_mode)) {
		return 0;
	} else if (IS_SPECIAL(sxp->st.st_mode)) {
#ifndef NO_SPECIAL_ACLS
		if (!preserve_specials)
#endif
		
... [TRUNCATED]
```

### File: authenticate.c
```c
/*
 * Support rsync daemon authentication.
 *
 * Copyright (C) 1998-2000 Andrew Tridgell
 * Copyright (C) 2002-2022 Wayne Davison
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License along
 * with this program; if not, visit the http://fsf.org website.
 */

#include "rsync.h"
#include "itypes.h"
#include "ifuncs.h"

extern int read_only;
extern char *password_file;
extern struct name_num_obj valid_auth_checksums;

/***************************************************************************
encode a buffer using base64 - simple and slow algorithm. null terminates
the result.
  ***************************************************************************/
void base64_encode(const char *buf, int len, char *out, int pad)
{
	char *b64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
	int bit_offset, byte_offset, idx, i;
	const uchar *d = (const uchar *)buf;
	int bytes = (len*8 + 5)/6;

	for (i = 0; i < bytes; i++) {
		byte_offset = (i*6)/8;
		bit_offset = (i*6)%8;
		if (bit_offset < 3) {
			idx = (d[byte_offset] >> (2-bit_offset)) & 0x3F;
		} else {
			idx = (d[byte_offset] << (bit_offset-2)) & 0x3F;
			if (byte_offset+1 < len) {
				idx |= (d[byte_offset+1] >> (8-(bit_offset-2)));
			}
		}
		out[i] = b64[idx];
	}

	while (pad && (i % 4))
		out[i++] = '=';

	out[i] = '\0';
}

/* Generate a challenge buffer and return it base64-encoded. */
static void gen_challenge(const char *addr, char *challenge)
{
	char input[32];
	char digest[MAX_DIGEST_LEN];
	struct timeval tv;
	int len;

	memset(input, 0, sizeof input);

	strlcpy(input, addr, 17);
	sys_gettimeofday(&tv);
	SIVAL(input, 16, tv.tv_sec);
	SIVAL(input, 20, tv.tv_usec);
	SIVAL(input, 24, getpid());

	len = sum_init(valid_auth_checksums.negotiated_nni, 0);
	sum_update(input, sizeof input);
	sum_end(digest);

	base64_encode(digest, len, challenge, 0);
}

/* Generate an MD4 hash created from the combination of the password
 * and the challenge string and return it base64-encoded. */
static void generate_hash(const char *in, const char *challenge, char *out)
{
	char buf[MAX_DIGEST_LEN];
	int len;

	len = sum_init(valid_auth_checksums.negotiated_nni, 0);
	sum_update(in, strlen(in));
	sum_update(challenge, strlen(challenge));
	sum_end(buf);

	base64_encode(buf, len, out, 0);
}

/* Return the secret for a user from the secret file, null terminated.
 * Maximum length is len (not counting the null). */
static const char *check_secret(int module, const char *user, const char *group,
				const char *challenge, const char *pass)
{
	char line[1024];
	char pass2[MAX_DIGEST_LEN*2];
	const char *fname = lp_secrets_file(module);
	STRUCT_STAT st;
	int ok = 1;
	int user_len = strlen(user);
	int group_len = group ? strlen(group) : 0;
	char *err;
	FILE *fh;

	if (!fname || !*fname || (fh = fopen(fname, "r")) == NULL)
		return "no secrets file";

	if (do_fstat(fileno(fh), &st) == -1) {
		rsyserr(FLOG, errno, "fstat(%s)", fname);
		ok = 0;
	} else if (lp_strict_modes(module)) {
		if ((st.st_mode & 06) != 0) {
			rprintf(FLOG, "secrets file must not be other-accessible (see strict modes option)\n");
			ok = 0;
		} else if (MY_UID() == ROOT_UID && st.st_uid != ROOT_UID) {
			rprintf(FLOG, "secrets file must be owned by root when running as root (see strict modes)\n");
			ok = 0;
		}
	}
	if (!ok) {
		fclose(fh);
		return "ignoring secrets file";
	}

	if (*user == '#') {
		/* Reject attempt to match a comment. */
		fclose(fh);
		return "invalid username";
	}

	/* Try to find a line that starts with the user (or @group) name and a ':'. */
	err = "secret not found";
	while ((user || group) && fgets(line, sizeof line, fh) != NULL) {
		const char **ptr, *s = strtok(line, "\n\r");
		int len;
		if (!s)
			continue;
		if (*s == '@') {
			ptr = &group;
			len = group_len;
			s++;
		} else {
			ptr = &user;
			len = user_len;
		}
		if (!*ptr || strncmp(s, *ptr, len) != 0 || s[len] != ':')
			continue;
		generate_hash(s+len+1, challenge, pass2);
		if (strcmp(pass, pass2) == 0) {
			err = NULL;
			break;
		}
		err = "password mismatch";
		*ptr = NULL; /* Don't look for name again. */
	}

	fclose(fh);

	force_memzero(line, sizeof line);
	force_memzero(pass2, sizeof pass2);

	return err;
}

static const char *getpassf(const char *filename)
{
	STRUCT_STAT st;
	char buffer[512], *p;
	int n;

	if (!filename)
		return NULL;

	if (strcmp(filename, "-") == 0) {
		n = fgets(buffer, sizeof buffer, stdin) == NULL ? -1 : (int)strlen(buffer);
	} else {
		int fd;

		if ((fd = open(filename,O_RDONLY)) < 0) {
			rsyserr(FERROR, errno, "could not open password file %s", filename);
			exit_cleanup(RERR_SYNTAX);
		}

		if (do_stat(filename, &st) == -1) {
			rsyserr(FERROR, errno, "stat(%s)", filename);
			exit_cleanup(RERR_SYNTAX);
		}
		if ((st.st_mode & 06) != 0) {
			rprintf(FERROR, "ERROR: password file must not be other-accessible\n");
			exit_cleanup(RERR_SYNTAX);
		}
		if (MY_UID() == ROOT_UID && st.st_uid != ROOT_UID) {
			rprintf(FERROR, "ERROR: password file must be owned by root when running as root\n");
			exit_cleanup(RERR_SYNTAX);
		}

		n = read(fd, buffer, sizeof buffer - 1);
		close(fd);
	}

	if (n > 0) {
		buffer[n] = '\0';
		if ((p = strtok(buffer, "\n\r")) != NULL)
			return strdup(p);
	}

	rprintf(FERROR, "ERROR: failed to read a password from %s\n", filename);
	exit_cleanup(RERR_SYNTAX);
}

/* Possibly negotiate authentication with the client.  Use "leader" to
 * start off the auth if necessary.
 *
 * Return NULL if authentication failed.  Return "" if anonymous access.
 * Otherwise return username.
 */
char *auth_server(int f_in, int f_out, int module, const char *host,
		  const char *addr, const char *leader)
{
	char *users = lp_auth_users(module);
	char challenge[MAX_DIGEST_LEN*2];
	char line[BIGPATHBUFLEN];
	const char **auth_uid_groups = NULL;
	int auth_uid_groups_cnt = -1;
	const char *err = NULL;
	int group_match = -1;
	char *tok, *pass;
	char opt_ch = '\0';

	/* if no auth list then allow anyone in! */
	if (!users || !*users)
		return "";

	negotiate_daemon_auth(f_out, 0);
	gen_challenge(addr, challenge);

	io_printf(f_out, "%s%s\n", leader, challenge);

	if (!read_line_old(f_in, line, sizeof line, 0)
	 || (pass = strchr(line, ' ')) == NULL) {
		rprintf(FLOG, "auth failed on module %s from %s (%s): "
			"invalid challenge response\n",
			lp_name(module), host, addr);
		return NULL;
	}
	*pass++ = '\0';

	users = strdup(users);

	for (tok = strtok(users, " ,\t"); tok; tok = strtok(NULL, " ,\t")) {
		char *opts;
		/* See if the user appended :deny, :ro, or :rw. */
		if ((opts = strchr(tok, ':')) != NULL) {
			*opts++ = '\0';
			opt_ch = isUpper(opts) ? toLower(opts) : *opts;
			if (opt_ch == 'r') { /* handle ro and rw */
				opt_ch = isUpper(opts+1) ? toLower(opts+1) : opts[1];
				if (opt_ch == 'o')
					opt_ch = 'r';
				else if (opt_ch != 'w')
					opt_ch = '\0';
			} else if (opt_ch != 'd') /* if it's not deny, ignore it */
				opt_ch = '\0';
		} else
			opt_ch = '\0';
		if (*tok != '@') {
			/* Match the username */
			if (wildmatch(tok, line))
				break;
		} else {
#ifdef HAVE_GETGROUPLIST
			int j;
			/* See if authorizing user is a real user, and if so, see
			 * if it is in a group that matches tok+1 wildmat. */
			if (auth_uid_groups_cnt < 0) {
				item_list gid_list = EMPTY_ITEM_LIST;
				uid_t auth_uid;
				if (!user_to_uid(line, &auth_uid, False)
				 || getallgroups(auth_uid, &gid_list) != NULL)
					auth_uid_groups_cnt = 0;
				else {
					gid_t *gid_array = gid_list.items;
					auth_uid_groups_cnt = gid_list.count;
					auth_uid_groups = new_array(const char *, auth_uid_groups_cnt);
					for (j = 0; j < auth_uid_groups_cnt; j++)
						auth_uid_groups[j] = gid_to_group(gid_array[j]);
				}
			}
			for (j = 0; j < auth_uid_groups_cnt; j++) {
				if (auth_uid_groups[j] && wildmatch(tok+1, auth_uid_groups[j])) {
					group_match = j;
					break;
				}
			}
			if (group_match >= 0)
				break;
#else
			rprintf(FLOG, "your computer doesn't support getgrouplist(), so no @group authorization is possible.\n");
#endif
		}
	}

	free(users);

	if (!tok)
		err = "no matching rule";
	else if (opt_ch == 'd')
		err = "denied by rule";
	else {
		const char *group = group_match >= 0 ? auth_uid_groups[group_match] : NULL;
		err = check_secret(module, line, group, challenge, pass);
	}

	force_memzero(challenge, sizeof challenge);
	force_memzero(pass, strlen(pass));

	if (auth_uid_groups) {
		int j;
		for (j = 0; j < auth_uid_groups_cnt; j++) {
			if (auth_uid_groups[j])
				free((char*)auth_uid_groups[j]);
		}
		free(auth_uid_groups);
	}

	if (err) {
		rprintf(FLOG, "auth failed on module %s from %s (%s) for %s: %s\n",
			lp_name(module), host, addr, line, err);
		return NULL;
	}

	if (opt_ch == 'r')
		read_only = 1;
	else if (opt_ch == 'w')
		read_only = 0;

	return strdup(line);
}

void auth_client(int fd, const char *user, const char *challenge)
{
	const char *pass;
	char pass2[MAX_DIGEST_LEN*2];

	if (!user || !*user)
		user = "nobody";
	negotiate_daemon_auth(-1, 1);

	if (!(pass = getpassf(password_file))
	 && !(pass = getenv("RSYNC_PASSWORD"))) {
		/* XXX: cyeoh says that getpass is deprecated, because
		 * it may return a truncated password on some systems,
		 * and it is not in the LSB.
		 *
		 * Andrew Klein says that getpassphrase() is present
		 * on Solaris and reads up to 256 characters.
		 *
		 * OpenBSD has a readpassphrase() that might be more suitable.
		 */
		pass = getpass("Password: ");
	}

	if (!pass)
		pass = "";

	generate_hash(pass, challenge, pass2);
	io_printf(fd, "%s %s\n", user, pass2);
}

```

### File: backup.c
```c
/*
 * Backup handling code.
 *
 * Copyright (C) 1999 Andrew Tridgell
 * Copyright (C) 2003-2022 Wayne Davison
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License along
 * with this program; if not, visit the http://fsf.org website.
 */

#include "rsync.h"
#include "ifuncs.h"

extern int am_root;
extern int preserve_acls;
extern int preserve_xattrs;
extern int preserve_devices;
extern int preserve_specials;
extern int preserve_links;
extern int safe_symlinks;
extern int backup_dir_len;
extern unsigned int backup_dir_remainder;
extern char backup_dir_buf[MAXPATHLEN];
extern char *backup_suffix;
extern char *backup_dir;

/* Returns -1 on error, 0 on missing dir, and 1 on present dir. */
static int validate_backup_dir(void)
{
	STRUCT_STAT st;

	if (do_lstat(backup_dir_buf, &st) < 0) {
		if (errno == ENOENT)
			return 0;
		rsyserr(FERROR, errno, "backup lstat %s failed", backup_dir_buf);
		return -1;
	}
	if (!S_ISDIR(st.st_mode)) {
		int flags = get_del_for_flag(st.st_mode) | DEL_FOR_BACKUP | DEL_RECURSE;
		if (delete_item(backup_dir_buf, st.st_mode, flags) == 0)
			return 0;
		return -1;
	}
	return 1;
}

/* Create a backup path from the given fname, putting the result into
 * backup_dir_buf.  Any new directories (compared to the prior backup
 * path) are ensured to exist as directories, replacing anything else
 * that may be in the way (e.g. a symlink). */
static BOOL copy_valid_path(const char *fname)
{
	const char *f;
	int val;
	BOOL ret = True;
	stat_x sx;
	char *b, *rel = backup_dir_buf + backup_dir_len, *name = rel;

	for (f = fname, b = rel; *f && *f == *b; f++, b++) {
		if (*b == '/')
			name = b + 1;
	}

	if (stringjoin(rel, backup_dir_remainder, fname, backup_suffix, NULL) >= backup_dir_remainder) {
		rprintf(FERROR, "backup filename too long\n");
		*name = '\0';
		return False;
	}

	for ( ; ; name = b + 1) {
		if ((b = strchr(name, '/')) == NULL)
			return True;
		*b = '\0';

		val = validate_backup_dir();
		if (val == 0)
			break;
		if (val < 0) {
			*name = '\0';
			return False;
		}

		*b = '/';
	}

	init_stat_x(&sx);

	for ( ; b; name = b + 1, b = strchr(name, '/')) {
		*b = '\0';

		while (do_mkdir(backup_dir_buf, ACCESSPERMS) < 0) {
			if (errno == EEXIST) {
				val = validate_backup_dir();
				if (val > 0)
					break;
				if (val == 0)
					continue;
			} else
				rsyserr(FERROR, errno, "backup mkdir %s failed", backup_dir_buf);
			*name = '\0';
			ret = False;
			goto cleanup;
		}

		/* Try to transfer the directory settings of the actual dir
		 * that the files are coming from. */
		if (x_stat(rel, &sx.st, NULL) < 0)
			rsyserr(FERROR, errno, "backup stat %s failed", full_fname(rel));
		else {
			struct file_struct *file;
			if (!(file = make_file(rel, NULL, NULL, 0, NO_FILTERS)))
				continue;
#ifdef SUPPORT_ACLS
			if (preserve_acls && !S_ISLNK(file->mode)) {
				get_acl(rel, &sx);
				cache_tmp_acl(file, &sx);
				free_acl(&sx);
			}
#endif
#ifdef SUPPORT_XATTRS
			if (preserve_xattrs) {
				get_xattr(rel, &sx);
				cache_tmp_xattr(file, &sx);
				free_xattr(&sx);
			}
#endif
			set_file_attrs(backup_dir_buf, file, NULL, NULL, 0);
			unmake_file(file);
		}

		*b = '/';
	}

  cleanup:

#ifdef SUPPORT_ACLS
	uncache_tmp_acls();
#endif
#ifdef SUPPORT_XATTRS
	uncache_tmp_xattrs();
#endif

	return ret;
}

/* Make a complete pathname for backup file and verify any new path elements. */
char *get_backup_name(const char *fname)
{
	if (backup_dir) {
		static int initialized = 0;
		if (!initialized) {
			int ret;
			if (backup_dir_len > 1)
				backup_dir_buf[backup_dir_len-1] = '\0';
			ret = make_path(backup_dir_buf, 0);
			if (backup_dir_len > 1)
				backup_dir_buf[backup_dir_len-1] = '/';
			if (ret < 0)
				return NULL;
			initialized = 1;
		}
		/* copy fname into backup_dir_buf while validating the dirs. */
		if (copy_valid_path(fname))
			return backup_dir_buf;
		/* copy_valid_path() has printed an error message. */
		return NULL;
	}

	if (stringjoin(backup_dir_buf, MAXPATHLEN, fname, backup_suffix, NULL) < MAXPATHLEN)
		return backup_dir_buf;

	rprintf(FERROR, "backup filename too long\n");
	return NULL;
}

/* Has same return codes as make_backup(). */
static inline int link_or_rename(const char *from, const char *to,
				 BOOL prefer_rename, STRUCT_STAT *stp)
{
#ifdef SUPPORT_HARD_LINKS
	if (!prefer_rename) {
#ifndef CAN_HARDLINK_SYMLINK
		if (S_ISLNK(stp->st_mode))
			return 0; /* Use copy code. */
#endif
#ifndef CAN_HARDLINK_SPECIAL
		if (IS_SPECIAL(stp->st_mode) || IS_DEVICE(stp->st_mode))
			return 0; /* Use copy code. */
#endif
		if (do_link(from, to) == 0) {
			if (DEBUG_GTE(BACKUP, 1))
				rprintf(FINFO, "make_backup: HLINK %s successful.\n", from);
			return 2;
		}
		/* We prefer to rename a regular file rather than copy it. */
		if (!S_ISREG(stp->st_mode) || errno == EEXIST || errno == EISDIR)
			return 0;
	}
#endif
	if (do_rename(from, to) == 0) {
		if (stp->st_nlink > 1 && !S_ISDIR(stp->st_mode)) {
			/* If someone has hard-linked the file into the backup
			 * dir, rename() might return success but do nothing! */
			robust_unlink(from); /* Just in case... */
		}
		if (DEBUG_GTE(BACKUP, 1))
			rprintf(FINFO, "make_backup: RENAME %s successful.\n", from);
		return 1;
	}
	return 0;
}

/* Hard-link, rename, or copy an item to the backup name.  Returns 0 for
 * failure, 1 if item was moved, 2 if item was duplicated or hard linked
 * into backup area, or 3 if item doesn't exist or isn't a regular file. */
int make_backup(const char *fname, BOOL prefer_rename)
{
	stat_x sx;
	struct file_struct *file;
	int save_preserve_xattrs;
	char *buf;
	int ret = 0;

	init_stat_x(&sx);
	/* Return success if no file to keep. */
	if (x_lstat(fname, &sx.st, NULL) < 0)
		return 3;

	if (!(buf = get_backup_name(fname)))
		return 0;

	/* Try a hard-link or a rename first.  Using rename is not atomic, but
	 * is more efficient than forcing a copy for larger files when no hard-
	 * linking is possible. */
	if ((ret = link_or_rename(fname, buf, prefer_rename, &sx.st)) != 0)
		goto success;
	if (errno == EEXIST || errno == EISDIR) {
		STRUCT_STAT bakst;
		if (do_lstat(buf, &bakst) == 0) {
			int flags = get_del_for_flag(bakst.st_mode) | DEL_FOR_BACKUP | DEL_RECURSE;
			if (delete_item(buf, bakst.st_mode, flags) != 0)
				return 0;
		}
		if ((ret = link_or_rename(fname, buf, prefer_rename, &sx.st)) != 0)
			goto success;
	}

	/* Fall back to making a copy. */
	if (!(file = make_file(fname, NULL, &sx.st, 0, NO_FILTERS)))
		return 3; /* the file could have disappeared */

#ifdef SUPPORT_ACLS
	if (preserve_acls && !S_ISLNK(file->mode)) {
		get_acl(fname, &sx);
		cache_tmp_acl(file, &sx);
		free_acl(&sx);
	}
#endif
#ifdef SUPPORT_XATTRS
	if (preserve_xattrs) {
		get_xattr(fname, &sx);
		cache_tmp_xattr(file, &sx);
		free_xattr(&sx);
	}
#endif

	/* Check to see if this is a device file, or link */
	if ((am_root && preserve_devices && IS_DEVICE(file->mode))
	 || (preserve_specials && IS_SPECIAL(file->mode))) {
		if (do_mknod(buf, file->mode, sx.st.st_rdev) < 0)
			rsyserr(FERROR, errno, "mknod %s failed", full_fname(buf));
		else if (DEBUG_GTE(BACKUP, 1))
			rprintf(FINFO, "make_backup: DEVICE %s successful.\n", fname);
		ret = 2;
	}

#ifdef SUPPORT_LINKS
	if (!ret && preserve_links && S_ISLNK(file->mode)) {
		const char *sl = F_SYMLINK(file);
		if (safe_symlinks && unsafe_symlink(sl, fname)) {
			if (INFO_GTE(SYMSAFE, 1)) {
				rprintf(FINFO, "not backing up unsafe symlink \"%s\" -> \"%s\"\n",
					fname, sl);
			}
			ret = 2;
		} else {
			if (do_symlink(sl, buf) < 0)
				rsyserr(FERROR, errno, "link %s -> \"%s\"", full_fname(buf), sl);
			else if (DEBUG_GTE(BACKUP, 1))
				rprintf(FINFO, "make_backup: SYMLINK %s successful.\n", fname);
			ret = 2;
		}
	}
#endif

	if (!ret && !S_ISREG(file->mode)) {
		if (INFO_GTE(NONREG, 1))
			rprintf(FINFO, "make_bak: skipping non-regular file %s\n", fname);
		unmake_file(file);
#ifdef SUPPORT_ACLS
		uncache_tmp_acls();
#endif
#ifdef SUPPORT_XATTRS
		uncache_tmp_xattrs();
#endif
		return 3;
	}

	/* Copy to backup tree if a file. */
	if (!ret) {
		if (copy_file(fname, buf, -1, file->mode) < 0) {
			rsyserr(FERROR, errno, "keep_backup failed: %s -> \"%s\"",
				full_fname(fname), buf);
			unmake_file(file);
#ifdef SUPPORT_ACLS
			uncache_tmp_acls();
#endif
#ifdef SUPPORT_XATTRS
			uncache_tmp_xattrs();
#endif
			return 0;
		}
		if (DEBUG_GTE(BACKUP, 1))
			rprintf(FINFO, "make_backup: COPY %s successful.\n", fname);
		ret = 2;
	}

	save_preserve_xattrs = preserve_xattrs;
	preserve_xattrs = 0;
	set_file_attrs(buf, file, NULL, fname, ATTRS_ACCURATE_TIME);
	preserve_xattrs = save_preserve_xattrs;

	unmake_file(file);
#ifdef SUPPORT_ACLS
	uncache_tmp_acls();
#endif
#ifdef SUPPORT_XATTRS
	uncache_tmp_xattrs();
#endif

  success:
	if (INFO_GTE(BACKUP, 1))
		rprintf(FINFO, "backed up %s to %s\n", fname, buf);
	return ret;
}

```

### File: batch.c
```c
/*
 * Support for the batch-file options.
 *
 * Copyright (C) 1999 Weiss
 * Copyright (C) 2004 Chris Shoemaker
 * Copyright (C) 2004-2022 Wayne Davison
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License along
 * with this program; if not, visit the http://fsf.org website.
 */

#include "rsync.h"
#include <zlib.h>
#include <time.h>

extern int eol_nulls;
extern int recurse;
extern int xfer_dirs;
extern int preserve_links;
extern int preserve_hard_links;
extern int preserve_devices;
extern int preserve_uid;
extern int preserve_gid;
extern int preserve_acls;
extern int preserve_xattrs;
extern int always_checksum;
extern int do_compression;
extern int inplace;
extern int append_mode;
extern int write_batch;
extern int protocol_version;
extern int raw_argc, cooked_argc;
extern char **raw_argv, **cooked_argv;
extern char *batch_name;
#ifdef ICONV_OPTION
extern char *iconv_opt;
#endif

extern filter_rule_list filter_list;

int batch_fd = -1;
int batch_sh_fd = -1;
int batch_stream_flags;

static int tweaked_append;
static int tweaked_append_verify;
static int tweaked_iconv;

static int *flag_ptr[] = {
	&recurse,		/* 0 */
	&preserve_uid,		/* 1 */
	&preserve_gid,		/* 2 */
	&preserve_links,	/* 3 */
	&preserve_devices,	/* 4 */
	&preserve_hard_links,	/* 5 */
	&always_checksum,	/* 6 */
	&xfer_dirs,		/* 7 (protocol 29) */
	&do_compression,	/* 8 (protocol 29) */
	&tweaked_iconv,		/* 9  (protocol 30) */
	&preserve_acls,		/* 10 (protocol 30) */
	&preserve_xattrs,	/* 11 (protocol 30) */
	&inplace,		/* 12 (protocol 30) */
	&tweaked_append,	/* 13 (protocol 30) */
	&tweaked_append_verify,	/* 14 (protocol 30) */
	NULL
};

static const char *const flag_name[] = {
	"--recurse (-r)",
	"--owner (-o)",
	"--group (-g)",
	"--links (-l)",
	"--devices (-D)",
	"--hard-links (-H)",
	"--checksum (-c)",
	"--dirs (-d)",
	"--compress (-z)",
	"--iconv",
	"--acls (-A)",
	"--xattrs (-X)",
	"--inplace",
	"--append",
	"--append-verify",
	NULL
};

void write_stream_flags(int fd)
{
	int i, flags;

	tweaked_append = append_mode == 1;
	tweaked_append_verify = append_mode == 2;
#ifdef ICONV_OPTION
	tweaked_iconv = iconv_opt != NULL;
#endif

	/* Start the batch file with a bitmap of data-stream-affecting
	 * flags. */
	for (i = 0, flags = 0; flag_ptr[i]; i++) {
		if (*flag_ptr[i])
			flags |= 1 << i;
	}
	write_int(fd, flags);
}

void read_stream_flags(int fd)
{
	batch_stream_flags = read_int(fd);
}

void check_batch_flags(void)
{
	int i;

	if (protocol_version < 29)
		flag_ptr[7] = NULL;
	else if (protocol_version < 30)
		flag_ptr[9] = NULL;
	tweaked_append = append_mode == 1;
	tweaked_append_verify = append_mode == 2;
#ifdef ICONV_OPTION
	tweaked_iconv = iconv_opt != NULL;
#endif
	for (i = 0; flag_ptr[i]; i++) {
		int set = batch_stream_flags & (1 << i) ? 1 : 0;
		if (*flag_ptr[i] != set) {
			if (i == 9) {
				rprintf(FERROR,
					"%s specify the --iconv option to use this batch file.\n",
					set ? "Please" : "Do not");
				exit_cleanup(RERR_SYNTAX);
			}
			if (INFO_GTE(MISC, 1)) {
				rprintf(FINFO,
					"%sing the %s option to match the batchfile.\n",
					set ? "Sett" : "Clear", flag_name[i]);
			}
			*flag_ptr[i] = set;
		}
	}
	if (protocol_version < 29) {
		if (recurse)
			xfer_dirs |= 1;
		else if (xfer_dirs < 2)
			xfer_dirs = 0;
	}

	if (tweaked_append)
		append_mode = 1;
	else if (tweaked_append_verify)
		append_mode = 2;
}

static int write_arg(const char *arg)
{
	const char *x, *s;
	int len, err = 0;

	if (*arg == '-' && (x = strchr(arg, '=')) != NULL) {
		err |= write(batch_sh_fd, arg, x - arg + 1) != x - arg + 1;
		arg += x - arg + 1;
	}

	if (strpbrk(arg, " \"'&;|[]()$#!*?^\\") != NULL) {
		err |= write(batch_sh_fd, "'", 1) != 1;
		for (s = arg; (x = strchr(s, '\'')) != NULL; s = x + 1) {
			err |= write(batch_sh_fd, s, x - s + 1) != x - s + 1;
			err |= write(batch_sh_fd, "'", 1) != 1;
		}
		len = strlen(s);
		err |= write(batch_sh_fd, s, len) != len;
		err |= write(batch_sh_fd, "'", 1) != 1;
		return err;
	}

	len = strlen(arg);
	err |= write(batch_sh_fd, arg, len) != len;

	return err;
}

/* Writes out a space and then an option (or other string) with an optional "=" + arg suffix. */
static int write_opt(const char *opt, const char *arg)
{
	int len = strlen(opt);
	int err = write(batch_sh_fd, " ", 1) != 1;
	err = write(batch_sh_fd, opt, len) != len ? 1 : 0;
	if (arg) {
		err |= write(batch_sh_fd, "=", 1) != 1;
		err |= write_arg(arg);
	}
	return err;
}

static void write_filter_rules(int fd)
{
	filter_rule *ent;

	write_sbuf(fd, " <<'#E#'\n");
	for (ent = filter_list.head; ent; ent = ent->next) {
		unsigned int plen;
		char *p = get_rule_prefix(ent, "- ", 0, &plen);
		write_buf(fd, p, plen);
		write_sbuf(fd, ent->pattern);
		if (ent->rflags & FILTRULE_DIRECTORY)
			write_byte(fd, '/');
		write_byte(fd, eol_nulls ? 0 : '\n');
	}
	if (eol_nulls)
		write_sbuf(fd, ";\n");
	write_sbuf(fd, "#E#");
}

/* This sets batch_fd and (for --write-batch) batch_sh_fd. */
void open_batch_files(void)
{
	if (write_batch) {
		char filename[MAXPATHLEN];

		stringjoin(filename, sizeof filename, batch_name, ".sh", NULL);

		batch_sh_fd = do_open(filename, O_WRONLY | O_CREAT | O_TRUNC, S_IRUSR | S_IWUSR | S_IXUSR);
		if (batch_sh_fd < 0) {
			rsyserr(FERROR, errno, "Batch file %s open error", full_fname(filename));
			exit_cleanup(RERR_FILESELECT);
		}

		batch_fd = do_open(batch_name, O_WRONLY | O_CREAT | O_TRUNC, S_IRUSR | S_IWUSR);
	} else if (strcmp(batch_name, "-") == 0)
		batch_fd = STDIN_FILENO;
	else
		batch_fd = do_open(batch_name, O_RDONLY, S_IRUSR | S_IWUSR);

	if (batch_fd < 0) {
		rsyserr(FERROR, errno, "Batch file %s open error", full_fname(batch_name));
		exit_cleanup(RERR_FILEIO);
	}
}

/* This routine tries to write out an equivalent --read-batch command
 * given the user's --write-batch args.  However, it doesn't really
 * understand most of the options, so it uses some overly simple
 * heuristics to munge the command line into something that will
 * (hopefully) work. */
void write_batch_shell_file(void)
{
	int i, j, len, err = 0;
	char *p, *p2;

	/* Write argvs info to BATCH.sh file */
	err |= write_arg(raw_argv[0]);
	if (filter_list.head) {
		if (protocol_version >= 29)
			err |= write_opt("--filter", "._-");
		else
			err |= write_opt("--exclude-from", "-");
	}

	/* Elide the filename args from the option list, but scan for them in reverse. */
	for (i = raw_argc-1, j = cooked_argc-1; i > 0 && j >= 0; i--) {
		if (strcmp(raw_argv[i], cooked_argv[j]) == 0) {
			raw_argv[i] = NULL;
			j--;
		}
	}

	for (i = 1; i < raw_argc; i++) {
		if (!(p = raw_argv[i]))
			continue;
		if (strncmp(p, "--files-from", 12) == 0
		 || strncmp(p, "--filter", 8) == 0
		 || strncmp(p, "--include", 9) == 0
		 || strncmp(p, "--exclude", 9) == 0) {
			if (strchr(p, '=') == NULL)
				i++;
			continue;
		}
		if (strcmp(p, "-f") == 0) {
			i++;
			continue;
		}
		if (strncmp(p, "--write-batch", len = 13) == 0
		 || strncmp(p, "--only-write-batch", len = 18) == 0)
			err |= write_opt("--read-batch", p[len] == '=' ? p + len + 1 : NULL);
		else {
			err |= write(batch_sh_fd, " ", 1) != 1;
			err |= write_arg(p);
		}
	}
	if (!(p = check_for_hostspec(cooked_argv[cooked_argc - 1], &p2, &i)))
		p = cooked_argv[cooked_argc - 1];
	err |= write_opt("${1:-", NULL);
	err |= write_arg(p);
	err |= write(batch_sh_fd, "}", 1) != 1;
	if (filter_list.head)
		write_filter_rules(batch_sh_fd);
	if (write(batch_sh_fd, "\n", 1) != 1 || close(batch_sh_fd) < 0 || err) {
		rsyserr(FERROR, errno, "Batch file %s.sh write error", batch_name);
		exit_cleanup(RERR_FILEIO);
	}
	batch_sh_fd = -1;
}

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
