%define game_name ufoai

Name:		ufoai-data
Version:	2.2.1
Release:	2
Summary:	UFO: Alien Invasion data files

Group:		Amusements/Games
License:	GPLv2+
URL:		http://ufoai.sourceforge.net/
Source:		http://downloads.sourceforge.net/%{game_name}/%{game_name}-%{version}-data.tar

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch


%description
UFO: ALIEN INVASION is a strategy game featuring tactical combat
against hostile alien forces which are about to infiltrate earth at
this very moment.

This package contains the data files needed to run the game.


%prep
%setup -c -q


%build
# this section left intentionally empty


%install
rm -rf %{buildroot}
mkdir -p -m 0755 %{buildroot}%{_datadir}/%{game_name}
cp -pr base %{buildroot}%{_datadir}/%{game_name}/


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{_datadir}/%{game_name}/


%changelog
* Sun Aug 03 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info - 2.2.1-2
- rebuild

* Mon Jun 09 2008 Karel Volny <kvolny@redhat.com> 2.2.1-1
- Version bump
- Fixes Livna bug #1931

* Sat Feb 16 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> 2.2-2
- remove disttag

* Tue Jan 22 2008 Karel Volny <kvolny@redhat.com> 2.2-1
- Version bump

* Mon Jan 07 2008 Karel Volny <kvolny@redhat.com> 2.1.1-3
- Removed "-n %%{name}-%%{version}" from %%setup

* Mon Dec 17 2007 Karel Volny <kvolny@redhat.com> 2.1.1-2
- added empty build section to better comply with rules

* Thu Dec 06 2007 Karel Volny <kvolny@redhat.com> 2.1.1-1
- Initial release for Fedora 8, split data from the ufoai package
