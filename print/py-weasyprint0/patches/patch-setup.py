$NetBSD: patch-setup.py,v 1.3 2021/04/29 13:15:32 joerg Exp $

Adjust script path to allow multiple Python version installs.

--- setup.py.orig	2017-12-22 23:26:45.000000000 +0000
+++ setup.py
@@ -83,7 +83,7 @@ setup(
         ':python_version >= "3.0"': ['CairoSVG >= 1.0.20']},
     entry_points={
         'console_scripts': [
-            'weasyprint = weasyprint.__main__:main',
+            'weasyprint%s = weasyprint.__main__:main' % sys.version[0:3],
         ],
     },
 )
