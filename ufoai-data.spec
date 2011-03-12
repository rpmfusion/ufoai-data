%define game_name ufoai

Name:		ufoai-data
Version:	2.3.1
Release:	1
Summary:	UFO: Alien Invasion data files

Group:		Amusements/Games
License:	GPLv2+
URL:		http://ufoai.sourceforge.net/
Source0:	http://downloads.sourceforge.net/%{game_name}/%{game_name}-%{version}-data.tar
# city maps hotfix
Source1:	http://mattn.ninex.info/1maps.pk3

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch

%package server
Summary:	UFO: Alien Invasion data files needed to run the server


%description
UFO: ALIEN INVASION is a strategy game featuring tactical combat
against hostile alien forces which are about to infiltrate earth at
this very moment.

This package contains the data files needed to run the game client.

%description server
UFO: ALIEN INVASION is a strategy game featuring tactical combat
against hostile alien forces which are about to infiltrate earth at
this very moment.

This package contains the data files needed to run the game server.


%prep
%setup -c -q


%build
# this section left intentionally empty


%install
rm -rf %{buildroot}
mkdir -p -m 0755 %{buildroot}%{_datadir}/%{game_name}
cp -pr base %{buildroot}%{_datadir}/%{game_name}/
# city maps hotfix
install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/%{game_name}/base/


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{_datadir}/%{game_name}/base/0media.pk3
%{_datadir}/%{game_name}/base/0materials.pk3
%{_datadir}/%{game_name}/base/0models.pk3
%{_datadir}/%{game_name}/base/0music.pk3
%{_datadir}/%{game_name}/base/0pics.pk3
%{_datadir}/%{game_name}/base/0snd.pk3
%{_datadir}/%{game_name}/base/0shaders.pk3


%files server
%defattr(-,root,root,-)
%dir %{_datadir}/%{game_name}
%dir %{_datadir}/%{game_name}/base
%{_datadir}/%{game_name}/base/0base.pk3
%{_datadir}/%{game_name}/base/0maps.pk3
%{_datadir}/%{game_name}/base/0ufos.pk3
# city maps hotfix
%{_datadir}/%{game_name}/base/1maps.pk3


%changelog
* Sat Mar 12 2011 Karel Volny <kvolny@redhat.com> 2.3.1-1
- Version bump
- Fixes RPMFusion bug #1546
- Added city maps hotfix, see http://ufoai.ninex.info/wiki/index.php/News/2010#Hotfix_for_2.3.1

* Tue Aug 17 2010 Karel Volny <kvolny@redhat.com> 2.3-1
- Version bump
- Split server subpackage

* Sun Mar 29 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 2.2.1-3
- rebuild for new F11 features

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
