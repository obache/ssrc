# $NetBSD: Makefile,v 1.71 2020/08/17 20:20:32 leot Exp $

PKGNAME=	${PYPKGPREFIX}-Tk-${PY_DISTVERSION}
PKGREVISION=	6
CATEGORIES=	x11 python

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://wiki.python.org/moin/TkInter
COMMENT=	Tkinter -- Python interface to Tcl/Tk
LICENSE=	python-software-foundation

USE_GCC_RUNTIME=	yes

PYDISTUTILSPKG=		yes
PY_SETUP_SUBST+=	BLPREFIX=${LOCALBASE}
PY_SETUP_SUBST+=	TCLRTPREFIX=${BUILDLINK_PREFIX.tcl}
PY_SETUP_SUBST+=	TKRTPREFIX=${BUILDLINK_PREFIX.tk}
PY_SETUP_SUBST+=	X11BASE=${X11BASE}

.include "../../mk/bsd.prefs.mk"

.if ${OPSYS} == "Darwin"
PY_SETUP_SUBST+=	X11LIB=
.else
.include "../../x11/libX11/buildlink3.mk"
PY_SETUP_SUBST+=	X11LIB=\'X11\'
.endif

.include "../../lang/python/srcdist.mk"
.include "../../lang/tcl/buildlink3.mk"
.include "../../x11/tk/buildlink3.mk"
.include "../../mk/bsd.pkg.mk"
