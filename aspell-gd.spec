%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define src_ver 0.1.1-1
%define fname aspell5-%{languagecode}
%define aspell_ver 0.60
%define languageenglazy Scottish
%define languagecode gd
%define lc_ctype gd_GB

Summary:       %{languageenglazy} files for aspell
Name:          aspell-%{languagecode}
Version:       0.1.1.1
Release:       %mkrel 8
Epoch:         1
Group:         System/Internationalization
Source:        http://ftp.gnu.org/gnu/aspell/dict/%{languagecode}/%{fname}-%{src_ver}.tar.bz2
URL:           http://aspell.net/
License:	   GPL
BuildRoot:     %{_tmppath}/%{name}-%{version}-root
Provides:	   spell-%{languagecode}
# old ispell is repalced with aspell
Obsoletes:	   ispell-%{languagecode}
Obsoletes:	   igaelic


BuildRequires: aspell >= %{aspell_ver}
BuildRequires: make
Requires:      aspell >= %{aspell_ver}

# Mandriva Stuff
Requires:      locales-%{languagecode}
# aspell = 1, myspell = 2, lang-specific = 3
Provides:      enchant-dictionary = 1
Provides:      aspell-dictionary
Provides:	   aspell-%{lc_ctype}

Autoreqprov:   no

%description
A %{languageenglazy} dictionary for use with aspell, a spelling checker.

%prep
%setup -q -n %{fname}-%{src_ver}

%build

# don't use configure macro
./configure

%make

%install
rm -fr $RPM_BUILD_ROOT

%makeinstall_std

mv -f README README.%{languagecode}
chmod 644 Copyright README.%{languagecode} doc/*

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README.%{languagecode} Copyright 
%doc doc/*
%{_libdir}/aspell-%{aspell_ver}/*


