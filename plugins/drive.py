# Copyright (c) 2017 Marco Aceti <dev@marcoaceti.it>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


from config import *

from apiclient import discovery
from apiclient.http import MediaIoBaseDownload, MediaFileUpload
import os
import io
import httplib2

import botogram

import json

import random
import string

import sqlite3

conn = sqlite3.connect('users.sqlite')
c = conn.cursor()

MIME_TYPES = {

    # Special thanks to http://stackoverflow.com/a/33534156/6083563
    # From https://github.com/google/google-drive-proxy/blob/master/DriveProxy/API/MimeType.cs
    # LICENSE: https://github.com/google/google-drive-proxy/blob/master/LICENSE
    # Copyright 2014 Google Inc

    ".323": "text/h323",
    ".3g2": "video/3gpp2",
    ".3gp": "video/3gpp",
    ".3gp2": "video/3gpp2",
    ".3gpp": "video/3gpp",
    ".7z": "application/x-7z-compressed",
    ".aa": "audio/audible",
    ".AAC": "audio/aac",
    ".aaf": "application/octet-stream",
    ".aax": "audio/vnd.audible.aax",
    ".ac3": "audio/ac3",
    ".aca": "application/octet-stream",
    ".accda": "application/msaccess.addin",
    ".accdb": "application/msaccess",
    ".accdc": "application/msaccess.cab",
    ".accde": "application/msaccess",
    ".accdr": "application/msaccess.runtime",
    ".accdt": "application/msaccess",
    ".accdw": "application/msaccess.webapplication",
    ".accft": "application/msaccess.ftemplate",
    ".acx": "application/internet-property-stream",
    ".AddIn": "text/xml",
    ".ade": "application/msaccess",
    ".adobebridge": "application/x-bridge-url",
    ".adp": "application/msaccess",
    ".ADT": "audio/vnd.dlna.adts",
    ".ADTS": "audio/aac",
    ".afm": "application/octet-stream",
    ".ai": "application/postscript",
    ".aif": "audio/x-aiff",
    ".aifc": "audio/aiff",
    ".aiff": "audio/aiff",
    ".air": "application/vnd.adobe.air-application-installer-package+zip",
    ".amc": "application/x-mpeg",
    ".application": "application/x-ms-application",
    ".art": "image/x-jg",
    ".asa": "application/xml",
    ".asax": "application/xml",
    ".ascx": "application/xml",
    ".asd": "application/octet-stream",
    ".asf": "video/x-ms-asf",
    ".ashx": "application/xml",
    ".asi": "application/octet-stream",
    ".asm": "text/plain",
    ".asmx": "application/xml",
    ".aspx": "application/xml",
    ".asr": "video/x-ms-asf",
    ".asx": "video/x-ms-asf",
    ".atom": "application/atom+xml",
    ".au": "audio/basic",
    ".avi": "video/x-msvideo",
    ".axs": "application/olescript",
    ".bas": "text/plain",
    ".bcpio": "application/x-bcpio",
    ".bin": "application/octet-stream",
    ".bmp": "image/bmp",
    ".c": "text/plain",
    ".cab": "application/octet-stream",
    ".caf": "audio/x-caf",
    ".calx": "application/vnd.ms-office.calx",
    ".cat": "application/vnd.ms-pki.seccat",
    ".cc": "text/plain",
    ".cd": "text/plain",
    ".cdda": "audio/aiff",
    ".cdf": "application/x-cdf",
    ".cer": "application/x-x509-ca-cert",
    ".chm": "application/octet-stream",
    ".class": "application/x-java-applet",
    ".clp": "application/x-msclip",
    ".cmx": "image/x-cmx",
    ".cnf": "text/plain",
    ".cod": "image/cis-cod",
    ".config": "application/xml",
    ".contact": "text/x-ms-contact",
    ".coverage": "application/xml",
    ".cpio": "application/x-cpio",
    ".cpp": "text/plain",
    ".crd": "application/x-mscardfile",
    ".crl": "application/pkix-crl",
    ".crt": "application/x-x509-ca-cert",
    ".cs": "text/plain",
    ".csdproj": "text/plain",
    ".csh": "application/x-csh",
    ".csproj": "text/plain",
    ".css": "text/css",
    ".csv": "text/csv",
    ".cur": "application/octet-stream",
    ".cxx": "text/plain",
    ".dat": "application/octet-stream",
    ".datasource": "application/xml",
    ".dbproj": "text/plain",
    ".dcr": "application/x-director",
    ".def": "text/plain",
    ".deploy": "application/octet-stream",
    ".der": "application/x-x509-ca-cert",
    ".dgml": "application/xml",
    ".dib": "image/bmp",
    ".dif": "video/x-dv",
    ".dir": "application/x-director",
    ".disco": "text/xml",
    ".dll": "application/x-msdownload",
    ".dll.config": "text/xml",
    ".dlm": "text/dlm",
    ".doc": "application/msword",
    ".docm": "application/vnd.ms-word.document.macroEnabled.12",
    ".docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    ".dot": "application/msword",
    ".dotm": "application/vnd.ms-word.template.macroEnabled.12",
    ".dotx": "application/vnd.openxmlformats-officedocument.wordprocessingml.template",
    ".dsp": "application/octet-stream",
    ".dsw": "text/plain",
    ".dtd": "text/xml",
    ".dtsConfig": "text/xml",
    ".dv": "video/x-dv",
    ".dvi": "application/x-dvi",
    ".dwf": "drawing/x-dwf",
    ".dwp": "application/octet-stream",
    ".dxr": "application/x-director",
    ".eml": "message/rfc822",
    ".emz": "application/octet-stream",
    ".eot": "application/octet-stream",
    ".eps": "application/postscript",
    ".etl": "application/etl",
    ".etx": "text/x-setext",
    ".evy": "application/envoy",
    ".exe": "application/octet-stream",
    ".exe.config": "text/xml",
    ".fdf": "application/vnd.fdf",
    ".fif": "application/fractals",
    ".filters": "Application/xml",
    ".fla": "application/octet-stream",
    ".flr": "x-world/x-vrml",
    ".flv": "video/x-flv",
    ".fsscript": "application/fsharp-script",
    ".fsx": "application/fsharp-script",
    ".generictest": "application/xml",
    ".gif": "image/gif",
    ".group": "text/x-ms-group",
    ".gsm": "audio/x-gsm",
    ".gtar": "application/x-gtar",
    ".gz": "application/x-gzip",
    ".h": "text/plain",
    ".hdf": "application/x-hdf",
    ".hdml": "text/x-hdml",
    ".hhc": "application/x-oleobject",
    ".hhk": "application/octet-stream",
    ".hhp": "application/octet-stream",
    ".hlp": "application/winhlp",
    ".hpp": "text/plain",
    ".hqx": "application/mac-binhex40",
    ".hta": "application/hta",
    ".htc": "text/x-component",
    ".htm": "text/html",
    ".html": "text/html",
    ".htt": "text/webviewhtml",
    ".hxa": "application/xml",
    ".hxc": "application/xml",
    ".hxd": "application/octet-stream",
    ".hxe": "application/xml",
    ".hxf": "application/xml",
    ".hxh": "application/octet-stream",
    ".hxi": "application/octet-stream",
    ".hxk": "application/xml",
    ".hxq": "application/octet-stream",
    ".hxr": "application/octet-stream",
    ".hxs": "application/octet-stream",
    ".hxt": "text/html",
    ".hxv": "application/xml",
    ".hxw": "application/octet-stream",
    ".hxx": "text/plain",
    ".i": "text/plain",
    ".ico": "image/x-icon",
    ".ics": "application/octet-stream",
    ".idl": "text/plain",
    ".ief": "image/ief",
    ".iii": "application/x-iphone",
    ".inc": "text/plain",
    ".inf": "application/octet-stream",
    ".inl": "text/plain",
    ".ins": "application/x-internet-signup",
    ".ipa": "application/x-itunes-ipa",
    ".ipg": "application/x-itunes-ipg",
    ".ipproj": "text/plain",
    ".ipsw": "application/x-itunes-ipsw",
    ".iqy": "text/x-ms-iqy",
    ".isp": "application/x-internet-signup",
    ".ite": "application/x-itunes-ite",
    ".itlp": "application/x-itunes-itlp",
    ".itms": "application/x-itunes-itms",
    ".itpc": "application/x-itunes-itpc",
    ".IVF": "video/x-ivf",
    ".jar": "application/java-archive",
    ".java": "application/octet-stream",
    ".jck": "application/liquidmotion",
    ".jcz": "application/liquidmotion",
    ".jfif": "image/pjpeg",
    ".jnlp": "application/x-java-jnlp-file",
    ".jpb": "application/octet-stream",
    ".jpe": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".jpg": "image/jpeg",
    ".js": "application/x-javascript",
    ".jsx": "text/jscript",
    ".jsxbin": "text/plain",
    ".latex": "application/x-latex",
    ".library-ms": "application/windows-library+xml",
    ".lit": "application/x-ms-reader",
    ".loadtest": "application/xml",
    ".lpk": "application/octet-stream",
    ".lsf": "video/x-la-asf",
    ".lst": "text/plain",
    ".lsx": "video/x-la-asf",
    ".lzh": "application/octet-stream",
    ".m13": "application/x-msmediaview",
    ".m14": "application/x-msmediaview",
    ".m1v": "video/mpeg",
    ".m2t": "video/vnd.dlna.mpeg-tts",
    ".m2ts": "video/vnd.dlna.mpeg-tts",
    ".m2v": "video/mpeg",
    ".m3u": "audio/x-mpegurl",
    ".m3u8": "audio/x-mpegurl",
    ".m4a": "audio/m4a",
    ".m4b": "audio/m4b",
    ".m4p": "audio/m4p",
    ".m4r": "audio/x-m4r",
    ".m4v": "video/x-m4v",
    ".mac": "image/x-macpaint",
    ".mak": "text/plain",
    ".man": "application/x-troff-man",
    ".manifest": "application/x-ms-manifest",
    ".map": "text/plain",
    ".master": "application/xml",
    ".mda": "application/msaccess",
    ".mdb": "application/x-msaccess",
    ".mde": "application/msaccess",
    ".mdp": "application/octet-stream",
    ".me": "application/x-troff-me",
    ".mfp": "application/x-shockwave-flash",
    ".mht": "message/rfc822",
    ".mhtml": "message/rfc822",
    ".mid": "audio/mid",
    ".midi": "audio/mid",
    ".mix": "application/octet-stream",
    ".mk": "text/plain",
    ".mmf": "application/x-smaf",
    ".mno": "text/xml",
    ".mny": "application/x-msmoney",
    ".mod": "video/mpeg",
    ".mov": "video/quicktime",
    ".movie": "video/x-sgi-movie",
    ".mp2": "video/mpeg",
    ".mp2v": "video/mpeg",
    ".mp3": "audio/mpeg",
    ".mp4": "video/mp4",
    ".mp4v": "video/mp4",
    ".mpa": "video/mpeg",
    ".mpe": "video/mpeg",
    ".mpeg": "video/mpeg",
    ".mpf": "application/vnd.ms-mediapackage",
    ".mpg": "video/mpeg",
    ".mpp": "application/vnd.ms-project",
    ".mpv2": "video/mpeg",
    ".mqv": "video/quicktime",
    ".ms": "application/x-troff-ms",
    ".msi": "application/octet-stream",
    ".mso": "application/octet-stream",
    ".mts": "video/vnd.dlna.mpeg-tts",
    ".mtx": "application/xml",
    ".mvb": "application/x-msmediaview",
    ".mvc": "application/x-miva-compiled",
    ".mxp": "application/x-mmxp",
    ".nc": "application/x-netcdf",
    ".nsc": "video/x-ms-asf",
    ".nws": "message/rfc822",
    ".ocx": "application/octet-stream",
    ".oda": "application/oda",
    ".odc": "text/x-ms-odc",
    ".odh": "text/plain",
    ".odl": "text/plain",
    ".odp": "application/vnd.oasis.opendocument.presentation",
    ".ods": "application/oleobject",
    ".odt": "application/vnd.oasis.opendocument.text",
    ".one": "application/onenote",
    ".onea": "application/onenote",
    ".onepkg": "application/onenote",
    ".onetmp": "application/onenote",
    ".onetoc": "application/onenote",
    ".onetoc2": "application/onenote",
    ".orderedtest": "application/xml",
    ".osdx": "application/opensearchdescription+xml",
    ".p10": "application/pkcs10",
    ".p12": "application/x-pkcs12",
    ".p7b": "application/x-pkcs7-certificates",
    ".p7c": "application/pkcs7-mime",
    ".p7m": "application/pkcs7-mime",
    ".p7r": "application/x-pkcs7-certreqresp",
    ".p7s": "application/pkcs7-signature",
    ".pbm": "image/x-portable-bitmap",
    ".pcast": "application/x-podcast",
    ".pct": "image/pict",
    ".pcx": "application/octet-stream",
    ".pcz": "application/octet-stream",
    ".pdf": "application/pdf",
    ".pfb": "application/octet-stream",
    ".pfm": "application/octet-stream",
    ".pfx": "application/x-pkcs12",
    ".pgm": "image/x-portable-graymap",
    ".pic": "image/pict",
    ".pict": "image/pict",
    ".pkgdef": "text/plain",
    ".pkgundef": "text/plain",
    ".pko": "application/vnd.ms-pki.pko",
    ".pls": "audio/scpls",
    ".pma": "application/x-perfmon",
    ".pmc": "application/x-perfmon",
    ".pml": "application/x-perfmon",
    ".pmr": "application/x-perfmon",
    ".pmw": "application/x-perfmon",
    ".png": "image/png",
    ".pnm": "image/x-portable-anymap",
    ".pnt": "image/x-macpaint",
    ".pntg": "image/x-macpaint",
    ".pnz": "image/png",
    ".pot": "application/vnd.ms-powerpoint",
    ".potm": "application/vnd.ms-powerpoint.template.macroEnabled.12",
    ".potx": "application/vnd.openxmlformats-officedocument.presentationml.template",
    ".ppa": "application/vnd.ms-powerpoint",
    ".ppam": "application/vnd.ms-powerpoint.addin.macroEnabled.12",
    ".ppm": "image/x-portable-pixmap",
    ".pps": "application/vnd.ms-powerpoint",
    ".ppsm": "application/vnd.ms-powerpoint.slideshow.macroEnabled.12",
    ".ppsx": "application/vnd.openxmlformats-officedocument.presentationml.slideshow",
    ".ppt": "application/vnd.ms-powerpoint",
    ".pptm": "application/vnd.ms-powerpoint.presentation.macroEnabled.12",
    ".pptx": "application/vnd.openxmlformats-officedocument.presentationml.presentation",
    ".prf": "application/pics-rules",
    ".prm": "application/octet-stream",
    ".prx": "application/octet-stream",
    ".ps": "application/postscript",
    ".psc1": "application/PowerShell",
    ".psd": "application/octet-stream",
    ".psess": "application/xml",
    ".psm": "application/octet-stream",
    ".psp": "application/octet-stream",
    ".pub": "application/x-mspublisher",
    ".pwz": "application/vnd.ms-powerpoint",
    ".qht": "text/x-html-insertion",
    ".qhtm": "text/x-html-insertion",
    ".qt": "video/quicktime",
    ".qti": "image/x-quicktime",
    ".qtif": "image/x-quicktime",
    ".qtl": "application/x-quicktimeplayer",
    ".qxd": "application/octet-stream",
    ".ra": "audio/x-pn-realaudio",
    ".ram": "audio/x-pn-realaudio",
    ".rar": "application/octet-stream",
    ".ras": "image/x-cmu-raster",
    ".rat": "application/rat-file",
    ".rc": "text/plain",
    ".rc2": "text/plain",
    ".rct": "text/plain",
    ".rdlc": "application/xml",
    ".resx": "application/xml",
    ".rf": "image/vnd.rn-realflash",
    ".rgb": "image/x-rgb",
    ".rgs": "text/plain",
    ".rm": "application/vnd.rn-realmedia",
    ".rmi": "audio/mid",
    ".rmp": "application/vnd.rn-rn_music_package",
    ".roff": "application/x-troff",
    ".rpm": "audio/x-pn-realaudio-plugin",
    ".rqy": "text/x-ms-rqy",
    ".rtf": "application/rtf",
    ".rtx": "text/richtext",
    ".ruleset": "application/xml",
    ".s": "text/plain",
    ".safariextz": "application/x-safari-safariextz",
    ".scd": "application/x-msschedule",
    ".sct": "text/scriptlet",
    ".sd2": "audio/x-sd2",
    ".sdp": "application/sdp",
    ".sea": "application/octet-stream",
    ".searchConnector-ms": "application/windows-search-connector+xml",
    ".setpay": "application/set-payment-initiation",
    ".setreg": "application/set-registration-initiation",
    ".settings": "application/xml",
    ".sgimb": "application/x-sgimb",
    ".sgml": "text/sgml",
    ".sh": "application/x-sh",
    ".shar": "application/x-shar",
    ".shtml": "text/html",
    ".sit": "application/x-stuffit",
    ".sitemap": "application/xml",
    ".skin": "application/xml",
    ".sldm": "application/vnd.ms-powerpoint.slide.macroEnabled.12",
    ".sldx": "application/vnd.openxmlformats-officedocument.presentationml.slide",
    ".slk": "application/vnd.ms-excel",
    ".sln": "text/plain",
    ".slupkg-ms": "application/x-ms-license",
    ".smd": "audio/x-smd",
    ".smi": "application/octet-stream",
    ".smx": "audio/x-smd",
    ".smz": "audio/x-smd",
    ".snd": "audio/basic",
    ".snippet": "application/xml",
    ".snp": "application/octet-stream",
    ".sol": "text/plain",
    ".sor": "text/plain",
    ".spc": "application/x-pkcs7-certificates",
    ".spl": "application/futuresplash",
    ".src": "application/x-wais-source",
    ".srf": "text/plain",
    ".SSISDeploymentManifest": "text/xml",
    ".ssm": "application/streamingmedia",
    ".sst": "application/vnd.ms-pki.certstore",
    ".stl": "application/vnd.ms-pki.stl",
    ".sv4cpio": "application/x-sv4cpio",
    ".sv4crc": "application/x-sv4crc",
    ".svc": "application/xml",
    ".swf": "application/x-shockwave-flash",
    ".t": "application/x-troff",
    ".tar": "application/x-tar",
    ".tcl": "application/x-tcl",
    ".testrunconfig": "application/xml",
    ".testsettings": "application/xml",
    ".tex": "application/x-tex",
    ".texi": "application/x-texinfo",
    ".texinfo": "application/x-texinfo",
    ".tgz": "application/x-compressed",
    ".thmx": "application/vnd.ms-officetheme",
    ".thn": "application/octet-stream",
    ".tif": "image/tiff",
    ".tiff": "image/tiff",
    ".tlh": "text/plain",
    ".tli": "text/plain",
    ".toc": "application/octet-stream",
    ".tr": "application/x-troff",
    ".trm": "application/x-msterminal",
    ".trx": "application/xml",
    ".ts": "video/vnd.dlna.mpeg-tts",
    ".tsv": "text/tab-separated-values",
    ".ttf": "application/octet-stream",
    ".tts": "video/vnd.dlna.mpeg-tts",
    ".txt": "text/plain",
    ".u32": "application/octet-stream",
    ".uls": "text/iuls",
    ".user": "text/plain",
    ".ustar": "application/x-ustar",
    ".vb": "text/plain",
    ".vbdproj": "text/plain",
    ".vbk": "video/mpeg",
    ".vbproj": "text/plain",
    ".vbs": "text/vbscript",
    ".vcf": "text/x-vcard",
    ".vcproj": "Application/xml",
    ".vcs": "text/plain",
    ".vcxproj": "Application/xml",
    ".vddproj": "text/plain",
    ".vdp": "text/plain",
    ".vdproj": "text/plain",
    ".vdx": "application/vnd.ms-visio.viewer",
    ".vml": "text/xml",
    ".vscontent": "application/xml",
    ".vsct": "text/xml",
    ".vsd": "application/vnd.visio",
    ".vsi": "application/ms-vsi",
    ".vsix": "application/vsix",
    ".vsixlangpack": "text/xml",
    ".vsixmanifest": "text/xml",
    ".vsmdi": "application/xml",
    ".vspscc": "text/plain",
    ".vss": "application/vnd.visio",
    ".vsscc": "text/plain",
    ".vssettings": "text/xml",
    ".vssscc": "text/plain",
    ".vst": "application/vnd.visio",
    ".vstemplate": "text/xml",
    ".vsto": "application/x-ms-vsto",
    ".vsw": "application/vnd.visio",
    ".vsx": "application/vnd.visio",
    ".vtx": "application/vnd.visio",
    ".wav": "audio/wav",
    ".wave": "audio/wav",
    ".wax": "audio/x-ms-wax",
    ".wbk": "application/msword",
    ".wbmp": "image/vnd.wap.wbmp",
    ".wcm": "application/vnd.ms-works",
    ".wdb": "application/vnd.ms-works",
    ".wdp": "image/vnd.ms-photo",
    ".webarchive": "application/x-safari-webarchive",
    ".webtest": "application/xml",
    ".wiq": "application/xml",
    ".wiz": "application/msword",
    ".wks": "application/vnd.ms-works",
    ".WLMP": "application/wlmoviemaker",
    ".wlpginstall": "application/x-wlpg-detect",
    ".wlpginstall3": "application/x-wlpg3-detect",
    ".wm": "video/x-ms-wm",
    ".wma": "audio/x-ms-wma",
    ".wmd": "application/x-ms-wmd",
    ".wmf": "application/x-msmetafile",
    ".wml": "text/vnd.wap.wml",
    ".wmlc": "application/vnd.wap.wmlc",
    ".wmls": "text/vnd.wap.wmlscript",
    ".wmlsc": "application/vnd.wap.wmlscriptc",
    ".wmp": "video/x-ms-wmp",
    ".wmv": "video/x-ms-wmv",
    ".wmx": "video/x-ms-wmx",
    ".wmz": "application/x-ms-wmz",
    ".wpl": "application/vnd.ms-wpl",
    ".wps": "application/vnd.ms-works",
    ".wri": "application/x-mswrite",
    ".wrl": "x-world/x-vrml",
    ".wrz": "x-world/x-vrml",
    ".wsc": "text/scriptlet",
    ".wsdl": "text/xml",
    ".wvx": "video/x-ms-wvx",
    ".x": "application/directx",
    ".xaf": "x-world/x-vrml",
    ".xaml": "application/xaml+xml",
    ".xap": "application/x-silverlight-app",
    ".xbap": "application/x-ms-xbap",
    ".xbm": "image/x-xbitmap",
    ".xdr": "text/plain",
    ".xht": "application/xhtml+xml",
    ".xhtml": "application/xhtml+xml",
    ".xla": "application/vnd.ms-excel",
    ".xlam": "application/vnd.ms-excel.addin.macroEnabled.12",
    ".xlc": "application/vnd.ms-excel",
    ".xld": "application/vnd.ms-excel",
    ".xlk": "application/vnd.ms-excel",
    ".xll": "application/vnd.ms-excel",
    ".xlm": "application/vnd.ms-excel",
    ".xls": "application/vnd.ms-excel",
    ".xlsb": "application/vnd.ms-excel.sheet.binary.macroEnabled.12",
    ".xlsm": "application/vnd.ms-excel.sheet.macroEnabled.12",
    ".xlsx": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    ".xlt": "application/vnd.ms-excel",
    ".xltm": "application/vnd.ms-excel.template.macroEnabled.12",
    ".xltx": "application/vnd.openxmlformats-officedocument.spreadsheetml.template",
    ".xlw": "application/vnd.ms-excel",
    ".xml": "text/xml",
    ".xmta": "application/xml",
    ".xof": "x-world/x-vrml",
    ".XOML": "text/plain",
    ".xpm": "image/x-xpixmap",
    ".xps": "application/vnd.ms-xpsdocument",
    ".xrm-ms": "text/xml",
    ".xsc": "application/xml",
    ".xsd": "text/xml",
    ".xsf": "text/xml",
    ".xsl": "text/xml",
    ".xslt": "text/xml",
    ".xsn": "application/octet-stream",
    ".xss": "application/xml",
    ".xtp": "application/octet-stream",
    ".xwd": "image/x-xwindowdump",
    ".z": "application/x-compress",
    ".zip": "application/x-zip-compressed",
}


def login(user):
    credentials = user.credentials()
    http = credentials.authorize(httplib2.Http())
    return discovery.build('drive', 'v3', http=http)


def getfiles(user, pagetoken=None, parent=None):
    service = login(user)
    results = service.files().list(
        pageSize=10, orderBy='folder', pageToken=pagetoken,
        q='"{parent}" in parents and not trashed'.format(parent=parent) if parent is not None else 'not trashed') \
        .execute()
    items = results.get('files', [])

    if not items:
        # TODO: Custom error message for each folder

        return (user.getstr('drive_list_no_files'),
                json.dumps({'inline_keyboard': [[{'text': user.getstr('back_button'), 'callback_data': 'home'}]]}
                           ))

    text = user.getstr('drive_list_header')  # TODO: Custom header for each folder
    reply_markup = {"inline_keyboard": [[{"foo": "bar"}]]}
    for item in items:  # TODO: Better listing design
        if item.get('mimeType') == 'application/vnd.google-apps.folder':
            reply_markup["inline_keyboard"] += [[{"text": '➡️ 📂' + item.get('name'),
                                                  "callback_data": "drv@fldr@" + item.get('id')}]]
            text += '\n📂 <b>{name}</b>'.format(name=item.get('name'))
        else:
            url_dw = 'https://t.me/{u}?start=drv-file-{i}-download'.format(u=BOT_USERNAME, i=item.get('id'))
            url_dlt = 'https://t.me/{u}?start=drv-file-{i}-delete'.format(u=BOT_USERNAME, i=item.get('id'))

            text += '\n📃 <b>{name}</b> (<a href="{url_dw}">{dw}</a>, <a href="{url_dlt}">{dlt}</a>)' \
                .format(name=item.get('name'), url_dw=url_dw, dw=user.getstr('drive_download'),
                        url_dlt=url_dlt, dlt=user.getstr('drive_delete'))

    del reply_markup["inline_keyboard"][0]

    if results.get('nextPageToken') is not None:
        next_page_token = results.get('nextPageToken')
        short_token = ''.join(
            random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(10))
        c.execute('INSERT INTO cache_drive_page_tokens VALUES(?, ?)', (next_page_token, short_token))
        conn.commit()

        # TODO: First and previous page button

        reply_markup["inline_keyboard"] += \
            [[{"text": user.getstr('next_page'), "callback_data": "drv@fldr@" + parent + "@page@" + short_token}]]

    reply_markup["inline_keyboard"] += \
        [
            [{"text": user.getstr('drive_upload_button'),
              "callback_data": "drv@fldr@" + ('root' if parent is None else parent) + '@upld'}],
            [{"text": user.getstr('back_button'),
              "callback_data": "drive" if parent != 'root' else "home"}]
        ]

    # TODO: Go to upper folder by pressing back button

    return text, json.dumps(reply_markup)


def getfile(user, file_id):
    service = login(user)
    return service.files().get(fileId=file_id).execute()


def download(user, file, msg):
    def startdownload(_request):
        downloader = MediaIoBaseDownload(fh, _request)
        done = False
        while not done:
            status, done = downloader.next_chunk()
            try:
                msg.edit(user.getstr('drive_downloading_progress')
                         .format(p=int(status.progress() * 100)))
            except botogram.api.APIError:
                pass

    os.chdir('/tmp')  # Sorry Windows users
    fh = io.FileIO(file.get('name'), 'wb')

    service = login(user)
    try:
        request = service.files().get_media(fileId=file.get('id'))
        startdownload(request)
        return '/tmp/' + file.get('name')
    except:
        request = service.files().export_media(fileId=file.get('id'), mimeType='application/pdf')
        startdownload(request)
        os.rename('/tmp/' + file.get('name'), '/tmp/' + file.get('name') + '.pdf')
        return '/tmp/' + file.get('name') + '.pdf'


def upload(user, path, name, folder, msg):
    service = login(user)

    mimetype = MIME_TYPES.get('.' + path.split('.')[-1], 'text/plain')
    media = MediaFileUpload(path, mimetype=mimetype, resumable=True)
    request = service.files().create(media_body=media, body={'name': name, 'parents': [folder]})

    uploaded = False
    while not uploaded:
        status, uploaded = request.next_chunk()
        if uploaded:
            break
        msg.edit(user.getstr('drive_uploading_progress').format(p=int(status.progress() * 100)))

    msg.edit(user.getstr('drive_uploading_done'))  # TODO: Move in correct folder
    os.remove(path)


def delete(user, file_id):
    service = login(user)

    service.files().delete(fileId=file_id)


def process_callback(bot, cb, user):
    if 'drv@' in cb.query:
        if 'drv@fldr@' in cb.query:
            if '@upld' in cb.query:
                folder = cb.query.split('@')[2]

                bot.api.call('editMessageText', {
                    'chat_id': cb.chat.id, 'message_id': cb.message.message_id, 'text': user.getstr('drive_upload'),
                    'parse_mode': 'HTML', 'disable_web_page_preview': True, 'reply_markup':
                        json.dumps(
                            {"inline_keyboard": [
                                [{"text": user.getstr('back_button'), "callback_data": "drv@fldr@" + folder}]
                            ]}
                        )
                })

                user.state('drive_upload_' + folder)
                return

            if '@page' in cb.query:
                parent = cb.query.split('@')[2]
                short_token = cb.query.split('@')[4]

                c.execute('SELECT token FROM cache_drive_page_tokens WHERE short_token=?', (short_token,))
                next_page_token = c.fetchone()[0]

                c.execute('DELETE FROM cache_drive_page_tokens WHERE short_token=?', (short_token,))
                conn.commit()

                text, inline_keyboard = getfiles(user, pagetoken=next_page_token, parent=parent)
                bot.api.call('editMessageText', {
                    'chat_id': cb.chat.id, 'message_id': cb.message.message_id, 'text': text,
                    'parse_mode': 'HTML', 'disable_web_page_preview': True, 'reply_markup': inline_keyboard
                })
                return

            text, inline_keyboard = getfiles(user, pagetoken=None, parent=cb.query.split('@')[2])
            bot.api.call('editMessageText', {
                'chat_id': cb.chat.id, 'message_id': cb.message.message_id, 'text': text,
                'parse_mode': 'HTML', 'disable_web_page_preview': True, 'reply_markup': inline_keyboard
            })

        if 'drv@file' in cb.query:
            if '@delete' in cb.query:
                query = cb.query
                file = query.split('@')[2]
                delete(user, file)

                bot.api.call('editMessageText', {
                    'chat_id': cb.chat.id, 'message_id': cb.message.message_id,
                    'text': user.getstr('drive_delete_done'), 'parse_mode': 'HTML', 'reply_markup':
                        json.dumps(
                            {"inline_keyboard": [
                                [{"text": user.getstr('back_button'), "callback_data": "drive"}]
                            ]}
                        )
                })


def process_message(update):
    message = update.message
    user = update.user

    if user.state().startswith('drive_upload_'):
        if len(user.state().split('_')) >= 4:
            if message.text:
                folder = user.state().split('_')[2]
                file_id = '_'.join(user.state().split('_')[3:])
                path = '/tmp/' + file_id

                msg = message.reply(user.getstr('drive_uploading_progress').format(p=0))
                upload(user, path, message.text, folder, msg)
                return True

        if message.document is None:
            message.reply(user.getstr('drive_upload_no_file'))
            return True

        message.reply(user.getstr('drive_upload_ask_name'))
        message.document.save('/tmp/' + message.document.file_id + '.' + message.document.file_name.split('.')[-1])
        user.state(user.state() + '_' + message.document.file_id + '.' + message.document.file_name.split('.')[-1])
