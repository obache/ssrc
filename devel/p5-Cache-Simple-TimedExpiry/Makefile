# $NetBSD: Makefile,v 1.27 2021/05/24 19:50:12 wiz Exp $

DISTNAME=	Cache-Simple-TimedExpiry-0.27
PKGNAME=	p5-${DISTNAME}
PKGREVISION=	13
CATEGORIES=	devel perl5
MASTER_SITES=	${MASTER_SITE_PERL_CPAN:=Cache/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://metacpan.org/release/Cache-Simple-TimedExpiry
COMMENT=	Perl module providing a lightweight cache with timed expiration
LICENSE=	${PERL5_LICENSE}

PERL5_PACKLIST=		auto/Cache/Simple/TimedExpiry/.packlist

.include "../../lang/perl5/module.mk"
.include "../../mk/bsd.pkg.mk"
